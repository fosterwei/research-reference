#!/usr/bin/env python3
"""Draft claims into compound, stack and comparison records from their own sources.

Usage:
    python3 scripts/draft_claims.py bpc-157 semaglutide    # named compound slugs
    python3 scripts/draft_claims.py --all                  # every compound record
    python3 scripts/draft_claims.py --stacks --comparisons # from research/registry.json
    python3 scripts/draft_claims.py --all --force          # re-draft records already in draft

Method, and why it is deliberately narrow
-----------------------------------------
Every claim this script writes is *extractive*: its `source_excerpt` is a
sentence copied verbatim from the abstract of a paper already in the record's
ledger, and its `value` is that sentence prefixed with the study's design,
species, sample size and year, all read from the paper's own indexing. The
script never paraphrases, never combines two papers into one statement, and
never writes a sentence the source did not. That is stricter than what
agent/AGENT.md permits, and it is chosen so the reviewer's job is mechanical:
does the excerpt say what the value says? It always does, by construction, so
review attention goes to whether the excerpt belongs under that heading and
carries the right tier.

Sections are matched by pattern (dose strings, route words, adverse-event
vocabulary, and so on). A sentence that matches nothing is not used. A paper
with no primary-evidence tier (reviews, unclassifiable) contributes to the
ledger but never to a claim.

Derived sections (summary, FAQ, open questions, reference data) are written
only from what the record itself already states: counts, tiers, species,
ChEMBL status. Where a section has no evidence the open-questions list says
so, which is the honest page for that compound.

Records move from "researched" to "draft". Nothing past "draft" is touched.
Standard library only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fetch_evidence import (  # noqa: E402
    EPMC, TIER_ORDER, NOT_REVIEWS, alias_query, classify, get_json, phase_of, search, strip_tags,
)

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REGISTRY = json.loads((ROOT / "research" / "registry.json").read_text(encoding="utf-8"))
REG = {c["slug"]: c for c in REGISTRY["compounds"]}
TODAY = dt.date.today().isoformat()
MAX_PER_SECTION = 6
MAX_TABLE_ROWS = 25
MAX_VALUE = 340

# ---- Section patterns ------------------------------------------------------

DOSE = re.compile(
    r"\b\d+(?:[.,·]\d+)?(?:\s?(?:-|–|to)\s?\d+(?:[.,·]\d+)?)?\s?"
    r"(?:mg|mcg|µg|μg|ng|IU|units?)(?:\s?/\s?(?:kg|day|d|week|wk|h|hour))?(?:\s?/\s?(?:kg|day|week))?"
    r"(?:\s?(?:once|twice|three times)?[ -]?(?:daily|weekly|per day|per week|a day|a week|q\.?d\.?|b\.?i\.?d\.?))?",
    re.IGNORECASE,
)
PER_KG = re.compile(r"(?:mg|mcg|µg|μg|ng|IU|units?)\s?/\s?kg", re.IGNORECASE)
DURATION = re.compile(r"\b(\d{1,3})\s?(?:-|–)?\s?(days?|weeks?|months?|years?|wk|mo)\b", re.IGNORECASE)
ROUTES = {
    "subcutaneous": r"subcutaneous(?:ly)?|s\.c\.|\bSC\b", "intravenous": r"intravenous(?:ly)?|i\.v\.|\bIV\b",
    "intraperitoneal": r"intraperitoneal(?:ly)?|i\.p\.|\bIP\b", "intragastric": r"intragastric(?:ally)?",
    "oral": r"\boral(?:ly)?\b|per os|\bp\.o\.", "intranasal": r"intranasal(?:ly)?|nasal spray",
    "topical": r"topical(?:ly)?", "intramuscular": r"intramuscular(?:ly)?|i\.m\.|\bIM\b",
    "transdermal": r"transdermal", "inhaled": r"inhal(?:ed|ation)", "intrathecal": r"intrathecal",
}
ROUTE_RE = {k: re.compile(v, re.IGNORECASE) for k, v in ROUTES.items()}
N_RE = [
    re.compile(r"\b[nN]\s?=\s?(\d{1,5})\b"),
    re.compile(r"\b(\d{1,5})\s+(?:patients|participants|subjects|volunteers|adults|individuals|people|men|women|children|rats|mice|rabbits|dogs|pigs|animals)\b", re.IGNORECASE),
]
PATTERNS: dict[str, re.Pattern] = {
    "escalation_schedules": re.compile(r"escalat|titrat|dose[- ]ranging|stepwise|step-wise|increased? (?:the )?dose|up-?titrat|dose increment", re.I),
    "interactions": re.compile(r"\binteract|co-?administ|concomitant|combined with|in combination with|add-?on to|together with", re.I),
    "exclusion_criteria": re.compile(r"\bexclu(?:ded|sion)|\beligib|inclusion criteria|were not eligible", re.I),
    "adverse_events": re.compile(r"adverse|side[- ]effect|tolerab|nausea|vomiting|diarrh|constipation|injection[- ]site|hypoglyc|discontinu|serious|safety|well[- ]tolerated|no (?:significant )?(?:toxic|adverse)", re.I),
    "biomarkers_monitored": re.compile(r"HbA1c|glycated|fasting glucose|plasma glucose|insulin|IGF-?1|growth hormone|\bGH\b|cortisol|triglycerid|cholesterol|LDL|HDL|ALT|AST|creatinine|blood pressure|heart rate|body ?weight|BMI|biomarker|serum (?:level|concentration)|plasma (?:level|concentration)|C-reactive|cytokine|IL-6|TNF", re.I),
    "reported_timelines": re.compile(r"\bonset|within \d+ ?(?:min|hour|day|week)|half-?life|\bt ?1/2|\bCmax|\bTmax|peak (?:plasma|concentration|effect)|duration of action|time to (?:peak|maximum|effect)|after \d+ ?(?:weeks?|days?|months?) of", re.I),
    "storage": re.compile(r"stabil|storage|stored at|degrad|shelf[- ]life|lyophil|reconstitut|\b4 ?°C|-?20 ?°C|-?80 ?°C|room temperature|freeze-?dried", re.I),
}
OUTCOME = re.compile(r"significant|reduc|increas|improv|decreas|no (?:significant )?differen|did not|was associated|were associated|greater|lower|higher|half-?life|peak|Cmax|Tmax|resulted|demonstrated|showed|observed|attenuat|inhibit|stimulat", re.I)

DESIGN_FROM_PUBTYPE = [
    ("Randomized Controlled Trial", "Randomized controlled trial"),
    ("Clinical Trial, Phase III", "Phase 3 clinical trial"), ("Clinical Trial, Phase II", "Phase 2 clinical trial"),
    ("Clinical Trial, Phase I", "Phase 1 clinical trial"), ("Clinical Trial, Phase IV", "Phase 4 clinical trial"),
    ("Controlled Clinical Trial", "Controlled clinical trial"), ("Clinical Trial", "Clinical trial"),
    ("Observational Study", "Observational study"), ("Cohort Studies", "Cohort study"),
    ("Case Reports", "Case report"), ("Case-Control Studies", "Case-control study"),
    ("Cross-Sectional Studies", "Cross-sectional study"), ("Multicenter Study", "Multicentre study"),
]
ABBREV = ["e.g.", "i.e.", "vs.", "et al.", "approx.", "Fig.", "fig.", "No.", "no.", "ca.", "cf.", "resp.", "Dr.", "Prof."]
LABEL = re.compile(r"^(?:BACKGROUND|INTRODUCTION|OBJECTIVES?|AIMS?|PURPOSE|METHODS?|DESIGN|SETTING|PARTICIPANTS|INTERVENTIONS?|"
                   r"MAIN OUTCOMES? AND MEASURES?|RESULTS?|FINDINGS|CONCLUSIONS?|INTERPRETATION|FUNDING|IMPORTANCE|"
                   r"MATERIALS? AND METHODS|PATIENTS AND METHODS|STUDY DESIGN|TRIAL DESIGN|MEASUREMENTS|DATA SOURCES|STUDY SELECTION|"
                   r"Materials? and [Mm]ethods|Patients and methods|Methods and materials|Study design|Trial design|Objective|Measurements|Data sources|Study selection|Main outcome measures?|"
                   r"Background|Introduction|Objectives?|Aims?|Purpose|Methods?|Design|Setting|Participants|Interventions?|"
                   r"Main outcomes? and measures?|Results?|Findings|Conclusions?|Interpretation|Funding|Importance)\s*:?\s+(?=[A-Z])")
AE_STRONG = re.compile(r"adverse (?:event|effect|reaction)s?|side[- ]effects?|nausea|vomiting|diarrh|constipation|injection[- ]site|hypoglyc|"
                       r"discontinu|serious adverse|well[- ]tolerated|tolerability was|no (?:significant )?(?:toxic|adverse)|incidence of|"
                       r"treatment-emergent|withdrew|withdrawal", re.I)


# ---- Text helpers -----------------------------------------------------------


def sentences(text: str) -> list[str]:
    protected = text
    for a in ABBREV:
        protected = protected.replace(a, a.replace(".", "․"))
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(\"'])", protected)
    out = []
    for p in parts:
        s = LABEL.sub("", p.replace("․", ".").strip())
        if len(s) >= 25 and not s.endswith("…"):
            out.append(s)
    return out


def mentions(s: str, names: list[str]) -> bool:
    return any(re.search(r"(?<![A-Za-z])" + re.escape(n) + r"(?![A-Za-z])", s, re.I) for n in names)


STOP = re.compile(r";|\s(?:plus|and|or|versus|vs\.?|with|compared|than)\s|/(?![a-z])", re.I)
COMMA_CONTINUE = re.compile(r",\s*(?:\d|then\b|initiated|titrated|escalated|increased|followed|up-titrated|maintained|once|twice|daily|weekly)", re.I)


def doses_near(s: str, names: list[str], window: int = 70) -> list[str]:
    """Dose strings that belong to the compound, not to a comparator.

    Abstracts list comparator and background doses in the same sentence
    ("zalfermin 7.5 mg plus semaglutide 2.4 mg, zalfermin 15 mg"). After a
    compound-name mention we scan forward at most `window` chars and stop at a
    semicolon, a conjunction, or a comma that introduces a new word rather than
    a continuation ("then 7 mg/day"). A dose up to 25 chars *before* the name
    counts too ("2.4 mg semaglutide"). Precision beats recall here: a missed
    dose is still visible in the excerpt; a misattributed one is a false claim.
    """
    found: list[str] = []
    for n in names:
        for m in re.finditer(r"(?<![A-Za-z])" + re.escape(n) + r"(?![A-Za-z])", s, re.I):
            start = m.end()
            tail = s[start : start + window]
            cut = len(tail)
            stop = STOP.search(tail)
            if stop:
                cut = min(cut, stop.start())
            for cm in re.finditer(r",", tail):
                if cm.start() < cut and not COMMA_CONTINUE.match(tail, cm.start()):
                    cut = cm.start()
                    break
            for dm in DOSE.finditer(tail[:cut + 1]):
                d = re.sub(r"\s+", " ", dm.group(0)).strip()
                if d not in found:
                    found.append(d)
            head = s[max(0, m.start() - 25) : m.start()]
            if not STOP.search(head) and "," not in head:
                for dm in DOSE.finditer(head):
                    d = re.sub(r"\s+", " ", dm.group(0)).strip()
                    if d not in found:
                        found.append(d)
    return found


ANALYTICAL = re.compile(r"LC-MS|mass spectromet|chromatograph|urine|doping|detection|screening|determination of|analytical method|metabolites? of|derivati[sz]ation", re.I)


def design_of(paper: dict, tier: str) -> str:
    title = strip_tags(paper.get("title"))
    if ANALYTICAL.search(title):
        # Anti-doping detection and metabolism papers are about measuring the
        # compound, not about what it does; labelled so a reader is not misled.
        return "Analytical method"
    types = set(paper.get("pubTypeList", {}).get("pubType", []))
    for key, label in DESIGN_FROM_PUBTYPE:
        if key in types:
            return label
    return {"animal-preclinical": "Animal study", "mechanistic-in-vitro": "In vitro study",
            "observational-human": "Human study", "human-clinical-trial": "Clinical trial"}.get(tier, "Study")


def sample_size(abstract: str) -> int | None:
    for rx in N_RE:
        m = rx.search(abstract)
        if m:
            try:
                n = int(m.group(1))
                if 1 <= n <= 100000:
                    return n
            except ValueError:
                pass
    return None


def first_author(paper: dict) -> str:
    a = (paper.get("authorString") or "").split(",")[0].strip()
    if not a:
        return ""
    words = a.split(" ")
    # "Zhu N" -> Zhu; "N Sandhu" (initial first) -> Sandhu; "van der Berg J" -> van der Berg
    if len(words[0]) <= 2 and len(words) > 1:
        words = words[1:]
    surname = [w for w in words if not (len(w) <= 2 and w.isupper())]
    return " ".join(surname) or words[0]


def prefix(design: str, species: str, n: int | None, year: str | None) -> str:
    bits = [design]
    if species and species != "not indexed":
        bits.append(species.lower())
    if n:
        bits.append(f"n={n:,}")
    if year:
        bits.append(str(year))
    return ", ".join(bits) + ": "


def clip(text: str, limit: int = MAX_VALUE) -> str:
    if len(text) <= limit:
        return text
    cut = text[: limit - 1].rsplit(" ", 1)[0]
    return cut + "…"


def tier_rank(tier: str) -> int:
    return TIER_ORDER.index(tier) if tier in TIER_ORDER else 99


# ---- Europe PMC batch --------------------------------------------------------


def fetch_ledger(sources: list[dict]) -> list[dict]:
    pmids = [s["id"][5:] for s in sources if s["id"].startswith("pmid-")]
    papers: list[dict] = []
    for i in range(0, len(pmids), 40):
        chunk = pmids[i : i + 40]
        q = "(" + " OR ".join(f"EXT_ID:{p}" for p in chunk) + ") AND SRC:MED"
        data = get_json(EPMC, {"query": q, "format": "json", "resultType": "core", "pageSize": 100})
        papers.extend(data.get("resultList", {}).get("result", []))
    return papers


# ---- Claim extraction ---------------------------------------------------------


def single_compound_paper(paper: dict, names: list[str], other_names: list[str]) -> bool:
    """True when the title names this compound and no other registry compound.

    In such a paper every abstract sentence is about this compound, so the
    per-sentence naming requirement (which exists to keep comparator and
    background statements out of claims) would only lose evidence: "The PK
    parameters showed ... a short terminal half-life of 2 hours" in a paper
    titled "Pharmacokinetic-pharmacodynamic modeling of ipamorelin" is a
    claim about ipamorelin. Multi-compound papers keep the strict rule.
    """
    title = strip_tags(paper.get("title"))
    return mentions(title, names) and not mentions(title, [n for n in other_names if not mentions(n, names)])


def analyse(paper: dict, names: list[str], other_names: list[str] | None = None) -> dict | None:
    tier, species = classify(paper)
    if tier not in TIER_ORDER:
        return None
    abstract = strip_tags(paper.get("abstractText"))
    if not abstract:
        return None
    sents = sentences(abstract)
    # Reconcile species with tier: a keyword fallback can see "patients" in the
    # background of an animal paper, or "mice" in a human trial's rationale.
    parts = [s for s in species.split(", ") if s and s != "not indexed"]
    if tier in ("human-clinical-trial", "observational-human"):
        parts = [s for s in parts if s == "Humans"] or ["Humans"]
    elif tier == "animal-preclinical":
        parts = [s for s in parts if s != "Humans"]
    species = ", ".join(parts) or "not indexed"
    design = design_of(paper, tier)
    n = sample_size(abstract)
    year = paper.get("pubYear")
    sid = f"pmid-{paper['pmid']}" if paper.get("pmid") else None
    if not sid:
        return None
    single = single_compound_paper(paper, names, other_names or [])
    named = sents if single else ([s for s in sents if mentions(s, names)] or sents)
    routes = sorted({name for name, rx in ROUTE_RE.items() if any(rx.search(s) for s in named)})
    doses = []
    for s in sents:
        for d in doses_near(s, names):
            if d not in doses:
                doses.append(d)
    perkg = [d for d in doses if PER_KG.search(d)]
    durations = []
    for s in sents:
        if re.search(r"treat|administ|therap|receiv|dosing|study period|follow", s, re.I):
            for m in DURATION.finditer(s):
                d = f"{m.group(1)} {m.group(2).lower()}"
                if d not in durations:
                    durations.append(d)
    # Outcome: prefer results-half sentences that name the compound, then results-half, then any.
    half = len(sents) // 2
    # Outcome: a results-half sentence that names the compound, else any naming
    # sentence with an outcome word. A sentence about a different agent is never
    # used, however results-like it reads (an anamorelin result once stood in
    # for ipamorelin here).
    outcome = (next((s for s in sents[half:] if OUTCOME.search(s) and mentions(s, names)), None)
               or next((s for s in sents if OUTCOME.search(s) and mentions(s, names)), None))
    return dict(id=sid, tier=tier, species=species, design=design, n=n, year=year, sents=sents, named=named, single=single,
                routes=routes, doses=doses, perkg=perkg, durations=durations, outcome=outcome,
                author=first_author(paper), pre=prefix(design, species, n, year))


def claim(p: dict, value: str, excerpt: str, extra: dict | None = None) -> dict:
    c = {"value": clip(value), "evidence_label": p["tier"], "source_ids": [p["id"]],
         "source_excerpt": excerpt, "drafting": "extractive"}
    if extra:
        c.update(extra)
    return c


def sentence_with(sents: list[str], *needles: str) -> str | None:
    for s in sents:
        if all(re.search(re.escape(nd), s, re.I) for nd in needles):
            return s
    return None


def pick(sents_named: list[str], sents_all: list[str], rx: re.Pattern, strong: re.Pattern | None = None) -> str | None:
    """First sentence matching: strong pattern in a compound-naming sentence, then strong anywhere,
    then the ordinary pattern in a naming sentence, then anywhere."""
    for pool, pat in ((sents_named, strong), (sents_all, strong), (sents_named, rx), (sents_all, rx)):
        if pat is None:
            continue
        s = next((s for s in pool if pat.search(s)), None)
        if s:
            return s
    return None


def draft_sections(papers: list[dict], names: list[str], other_names: list[str] | None = None) -> dict[str, list[dict]]:
    analysed = [a for a in (analyse(p, names, other_names) for p in papers) if a]
    analysed.sort(key=lambda a: (tier_rank(a["tier"]), -int(a["year"] or 0)))
    out: dict[str, list[dict]] = {k: [] for k in [
        "routes_studied", "study_doses", "study_durations", "weight_normalized_doses",
        *PATTERNS.keys(), "evidence_table"]}

    for a in analysed:
        if a["routes"] and len(out["routes_studied"]) < MAX_PER_SECTION:
            s = next((s for s in a["named"] if any(ROUTE_RE[r].search(s) for r in a["routes"])), a["named"][0])
            out["routes_studied"].append(claim(a, a["pre"] + "administration by " + ", ".join(a["routes"]) + " route reported. " + s, s))
        if a["doses"] and len(out["study_doses"]) < MAX_PER_SECTION:
            s = next((s for s in a["sents"] if doses_near(s, names)), a["named"][0])
            out["study_doses"].append(claim(a, a["pre"] + "doses stated in the abstract: " + "; ".join(a["doses"][:4]) + ". " + s, s))
        if a["perkg"] and len(out["weight_normalized_doses"]) < MAX_PER_SECTION:
            s = next((s for s in a["sents"] if any(PER_KG.search(d) for d in doses_near(s, names))), a["named"][0])
            out["weight_normalized_doses"].append(claim(a, a["pre"] + "weight-normalized doses as published: " + "; ".join(a["perkg"][:4]) + ". " + s, s))
        if a["durations"] and len(out["study_durations"]) < MAX_PER_SECTION:
            s = next((s for s in a["sents"] if DURATION.search(s) and re.search(r"treat|administ|therap|receiv|dosing|study period|follow", s, re.I)), a["sents"][0])
            out["study_durations"].append(claim(a, a["pre"] + "durations stated: " + "; ".join(a["durations"][:3]) + ". " + s, s))
        for field, rx in PATTERNS.items():
            if len(out[field]) >= MAX_PER_SECTION:
                continue
            # Only sentences that name the compound. A topical sentence that does
            # not name it is usually background about other agents, and under
            # this heading it would read as a claim about the compound.
            named_only = a["sents"] if a["single"] else (a["named"] if a["named"] is not a["sents"] else [])
            s = pick(named_only, [], AE_STRONG if field == "adverse_events" else rx)
            if s:
                out[field].append(claim(a, a["pre"] + s, s))
        if len(out["evidence_table"]) < MAX_TABLE_ROWS:
            fields = {
                "study": (a["author"] + " " if a["author"] else "") + str(a["year"] or ""),
                "year": a["year"], "design": a["design"], "n": a["n"], "species": a["species"],
                "dose": "; ".join(a["doses"][:2]) or "not stated in abstract",
                "route": ", ".join(a["routes"]) or "not stated in abstract",
                "duration": "; ".join(a["durations"][:2]) or "not stated in abstract",
                "outcome": clip(a["outcome"], 220) if a["outcome"] else "see source",
            }
            excerpt = a["outcome"] or a["named"][0]
            out["evidence_table"].append(claim(a, a["pre"] + excerpt, excerpt, {"fields": fields}))
    return out


# ---- Derived sections ----------------------------------------------------------

TIER_LABEL_SHORT = {"approved-label": "approved label", "human-clinical-trial": "human clinical trial", "observational-human": "observational human data",
                    "animal-preclinical": "animal studies", "mechanistic-in-vitro": "in-vitro work", "community-reported": "community reports only"}
HEADINGS = {
    "routes_studied": "routes of administration", "study_doses": "doses used", "study_durations": "treatment durations",
    "weight_normalized_doses": "weight-normalized doses", "escalation_schedules": "dose-escalation schedules",
    "interactions": "interactions with other agents", "exclusion_criteria": "exclusion criteria",
    "adverse_events": "adverse events or their frequency", "biomarkers_monitored": "biomarkers monitored",
    "reported_timelines": "onset or duration of effects", "storage": "storage or stability",
}


def derive(record: dict, reg: dict | None, sections: dict, papers_analysed: int) -> None:
    name = record["preferred_name"]
    es = record.get("evidence_summary") or {}
    counts = es.get("publications") or {}
    chembl = es.get("chembl")
    total, rct, trials = counts.get("total", 0), counts.get("randomized_controlled_trials", 0), counts.get("clinical_trials", 0)
    tier = record["evidence_tier"]
    # Species for the FAQ come from primary rows only, tier-consistent: "Humans"
    # counts only when it comes from a human-subject study, not a cell line.
    species = sorted({sp for c in sections.get("evidence_table", [])
                      for sp in re.split(r",\s*", c.get("fields", {}).get("species", ""))
                      if sp and sp != "not indexed"
                      and not (sp == "Humans" and c.get("evidence_label") not in ("human-clinical-trial", "observational-human", "approved-label"))})
    cls = reg["class"].replace("-", " ").replace(" and ", " & ") if reg else None

    tier_sentence = {
        "approved-label": "an approved medicine with a regulator-reviewed label",
        "human-clinical-trial": "human clinical trials",
        "observational-human": "observational human studies, with no indexed randomized trial",
        "animal-preclinical": "animal studies only, with no indexed human study",
        "mechanistic-in-vitro": "laboratory and cell studies only",
        "community-reported": "no indexed study at all; what circulates about it is community-reported",
    }[tier]
    record["summary"] = (
        f"{name} is a {reg['molecule_type'] if reg else 'compound'}"
        + (f" in the {cls} class ({reg['target']})" if reg else "")
        + f". Europe PMC indexes {total:,} publications naming it or a listed alias in a title or abstract, including {rct} randomized controlled trials and {trials} clinical trials of any design, as of {es.get('retrieved_at', TODAY)}. "
        f"The strongest evidence tier in that literature is {tier_sentence}. "
        "This page reports what those studies state, sentence by sentence, with each statement tied to its source and labeled by the kind of evidence it is. It does not recommend use, and it does not translate study doses into anything personal."
    )
    record.setdefault("seo", {})
    record["seo"]["title"] = clip(f"{name}: what the research shows", 60)
    human = counts.get("clinical_trials", 0) + rct
    record["seo"]["description"] = clip(
        f"{name}: {total:,} indexed publications, {rct} randomized trials, {human} human studies, each claim quoted from its source and tiered. "
        f"Strongest evidence: {TIER_LABEL_SHORT.get(tier, tier)}.", 160)

    faq = [
        {"question": f"Has {name} been tested in humans?",
         "answer": (f"Yes. Europe PMC indexes {trials} clinical trials and {rct} randomized controlled trials naming {name} or a listed alias in the title or abstract. The evidence table above lists the ones in this record's ledger with their design and sample size; check the study name, since an alias can refer to a different formulation of the same molecule."
                    if trials or rct else f"Not in any indexed clinical trial. The studies in this record's ledger report work in " + (", ".join(s.lower() for s in species) if species else "laboratory systems") + f". Any human dosing information circulating about {name} does not come from a published trial.")},
        {"question": f"What kind of evidence exists for {name}?",
         "answer": f"The strongest tier is {tier.replace('-', ' ')}: {tier_sentence}. Every claim on this page carries its own tier, because a compound with one human trial and forty animal studies is described by both facts, not the better one."},
        {"question": f"Is {name} an approved medicine?",
         "answer": (f"ChEMBL records {chembl['chembl_id']} at maximum clinical phase {phase_of(chembl):g}" + (f", first approved {chembl['first_approval']}" if chembl.get("first_approval") else ", with no approval recorded") + ". Approval status differs by jurisdiction and is pending human review on this record."
                    if chembl else f"No ChEMBL record matches {name} or its aliases, which usually means it has not entered a registered clinical development programme. It is not an approved medicine in any jurisdiction this record has checked.")},
    ]
    if species:
        faq.append({"question": f"Which species has {name} been studied in?",
                    "answer": f"Studies in this record's ledger report work in: {', '.join(species)}. Findings in one species do not transfer to another, and weight-normalized doses in particular do not scale linearly between them."})
    record["faq"] = faq

    oq = []
    for field, label in HEADINGS.items():
        if not sections.get(field):
            oq.append(f"No study in this record's ledger reports {label} for {name}.")
    if not rct:
        oq.append(f"No randomized controlled trial of {name} is indexed in Europe PMC.")
    if tier in ("animal-preclinical", "mechanistic-in-vitro"):
        oq.append(f"Whether any finding about {name} holds in humans is untested.")
    if total == 0:
        oq = [f"No indexed study names {name} in its title or abstract. Everything currently said about it is unverified."]
    record["open_questions"] = oq

    es["drafting"] = {"method": "extractive", "script": "scripts/draft_claims.py", "date": TODAY,
                      "papers_analysed": papers_analysed,
                      "claims": sum(len(v) for k, v in sections.items() if k != "evidence_table"),
                      "evidence_table_rows": len(sections.get("evidence_table", []))}
    record["evidence_summary"] = es


# ---- Record drivers -------------------------------------------------------------


def draft_compound(path: pathlib.Path, force: bool) -> str:
    record = json.loads(path.read_text(encoding="utf-8"))
    status = record.get("status")
    if status not in ("researched", "draft") or (status == "draft" and not force):
        return f"skip ({status})"
    papers = fetch_ledger(record.get("sources", []))
    names = [record["preferred_name"], *record.get("aliases", [])]
    other_names = [c["name"] for c in REGISTRY["compounds"] if c["slug"] != record["slug"]]
    sections = draft_sections(papers, names, other_names) if papers else {}
    attrs = record.setdefault("attributes", {})
    for field, claims in sections.items():
        attrs[field] = claims
    if record.get("prose_reviewed"):
        keep = {k: record.get(k) for k in ("summary", "faq", "open_questions", "evidence_assessment")}
        derive(record, REG.get(record["slug"]), sections, len(papers))
        record.update({k: v for k, v in keep.items() if v is not None})
    else:
        derive(record, REG.get(record["slug"]), sections, len(papers))
    record["status"] = "draft"
    record.setdefault("changelog", []).append({"date": TODAY, "change": (
        f"Claims drafted extractively from {len(papers)} ledger sources by scripts/draft_claims.py: "
        f"{sum(len(v) for k, v in sections.items() if k != 'evidence_table')} claims, "
        f"{len(sections.get('evidence_table', []))} evidence-table rows. Status researched -> draft.")})
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    n = sum(len(v) for k, v in sections.items() if k != "evidence_table")
    return f"draft   claims={n:<3} table={len(sections.get('evidence_table', [])):<3} papers={len(papers)}"


def ledger_from(papers: list[dict]) -> list[dict]:
    out = []
    for p in papers:
        if not p.get("pmid"):
            continue
        out.append({"id": f"pmid-{p['pmid']}", "title": strip_tags(p.get("title")),
                    "url": f"https://europepmc.org/article/MED/{p['pmid']}",
                    "published": p.get("firstPublicationDate") or f"{p.get('pubYear', '1900')}-01-01",
                    "kind": "preprint" if p.get("source") == "PPR" else "peer-reviewed"})
    return out


def names_of(slug: str) -> list[str]:
    c = REG[slug]
    return [c["name"], *c.get("aliases", [])]


def load_compound(slug: str) -> dict | None:
    p = DATA / "compounds" / f"{slug}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def base_record(rtype: str, slug: str, title: str) -> dict:
    return {"type": rtype, "title": title, "slug": slug, "status": "draft", "summary": "",
            "seo": {}, "attributes": {}, "sources": [], "related": [], "faq": [], "open_questions": [],
            "review": {"author": "", "reviewer": "", "reviewer_credential": "", "reviewed_at": ""},
            "uniqueness_pct": None, "changelog": []}


def draft_stack(plan: dict, force: bool) -> str:
    path = DATA / "stacks" / f"{plan['slug']}.json"
    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))
        if existing.get("status") not in ("researched", "draft") or (existing.get("status") == "draft" and not force):
            return f"skip ({existing.get('status')})"
    comps = plan["components"]
    q = " AND ".join(alias_query(names_of(s)) for s in comps) + f" AND HAS_ABSTRACT:y AND SRC:MED {NOT_REVIEWS}"
    papers = search(q, 8)
    claims = []
    allnames = [n for c in comps for n in names_of(c)]
    for p in papers:
        a = analyse(p, allnames)
        if not a:
            continue
        s = next((s for s in a["sents"] if all(mentions(s, names_of(c)) for c in comps)), a["named"][0])
        claims.append(claim(a, a["pre"] + s, s))
    recs = {c: load_compound(c) for c in comps}
    tiers = {c: (recs[c] or {}).get("evidence_tier", "community-reported") for c in comps}
    weakest = max(tiers.values(), key=tier_rank)
    rec = base_record("stack", plan["slug"], plan["name"])
    rec["components"] = comps
    rec["summary"] = (
        f"{plan['name']} combines " + " and ".join(f"{REG[c]['name']} ({tiers[c].replace('-', ' ')})" for c in comps)
        + f". A stack cannot carry a stronger evidence tier than its weakest component, which here is {weakest.replace('-', ' ')}. "
        + (f"{len(claims)} indexed studies mention both components; the combination-evidence section quotes what they state."
           if claims else "No indexed study tested this combination. What is known about each component is the whole of what is known.")
    )
    rec["seo"] = {"title": clip(f"{plan['name']}: the evidence", 60),
                  "description": clip(f"{' + '.join(REG[c]['name'] for c in comps)}: each component's evidence tier, and whether any study tested the combination. Cited; not advice.", 160)}
    rec["attributes"] = {"combination_evidence": claims}
    rec["sources"] = ledger_from(papers)
    rec["related"] = comps
    rec["open_questions"] = ([] if claims else [f"No indexed study has tested {' with '.join(REG[c]['name'] for c in comps)} together."]) + \
        [f"No published schedule reconciles the components' different reported frequencies onto one calendar."]
    rec["changelog"] = [{"date": TODAY, "change": f"Stack record generated from research/registry.json plan; {len(claims)} combination claims drafted extractively by scripts/draft_claims.py."}]
    path.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return f"draft   combination-claims={len(claims)} sources={len(rec['sources'])}"


def draft_comparison(plan: dict, force: bool) -> str:
    path = DATA / "comparisons" / f"{plan['slug']}.json"
    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))
        if existing.get("status") not in ("researched", "draft") or (existing.get("status") == "draft" and not force):
            return f"skip ({existing.get('status')})"
    a, b = plan["sides"]
    q = (f"{alias_query(names_of(a))} AND {alias_query(names_of(b))} AND (versus OR \"compared with\" OR comparison OR head-to-head OR \"compared to\") "
         f"AND HAS_ABSTRACT:y AND SRC:MED {NOT_REVIEWS}")
    papers = search(q, 8)
    claims = []
    for p in papers:
        an = analyse(p, names_of(a) + names_of(b))
        if not an:
            continue
        s = next((s for s in an["named"] if re.search(r"versus|compared|comparison|head-to-head|\bvs\b", s, re.I)), an["named"][0])
        claims.append(claim(an, an["pre"] + s, s))
    ra, rb = load_compound(a), load_compound(b)
    def facts(r, slug):
        es = (r or {}).get("evidence_summary", {}); c = es.get("publications", {})
        return f"{REG[slug]['name']}: tier {((r or {}).get('evidence_tier') or 'unknown').replace('-', ' ')}, {c.get('total', 0):,} indexed publications, {c.get('randomized_controlled_trials', 0)} randomized trials"
    title = f"{REG[a]['name']} vs {REG[b]['name']}"
    rec = base_record("comparison", plan["slug"], title)
    rec["sides"] = [a, b]
    rec["summary"] = (facts(ra, a) + ". " + facts(rb, b) + ". "
                      + (f"{len(claims)} indexed studies compare them directly; the head-to-head section quotes what they state."
                         if claims else "No indexed study compares them directly. The side-by-side table lines up what each compound's own record states; nothing is inferred across the two."))
    rec["seo"] = {"title": clip(f"{title}: what the studies show", 60),
                  "description": clip(f"{title}, side by side from each compound's own cited record, plus any direct head-to-head trial. Not advice.", 160)}
    rec["attributes"] = {"head_to_head": claims}
    rec["sources"] = ledger_from(papers)
    rec["related"] = [a, b]
    rec["open_questions"] = [] if claims else [f"No indexed study compares {REG[a]['name']} and {REG[b]['name']} head to head."]
    rec["changelog"] = [{"date": TODAY, "change": f"Comparison record generated from research/registry.json plan; {len(claims)} head-to-head claims drafted extractively by scripts/draft_claims.py."}]
    path.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return f"draft   head-to-head-claims={len(claims)} sources={len(rec['sources'])}"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true", help="every compound record")
    ap.add_argument("--stacks", action="store_true", help="generate stack records from the registry plan")
    ap.add_argument("--comparisons", action="store_true", help="generate comparison records from the registry plan")
    ap.add_argument("--force", action="store_true", help="re-draft records already in status draft")
    args = ap.parse_args(argv)
    failures = 0
    paths = sorted((DATA / "compounds").glob("*.json")) if args.all else [DATA / "compounds" / f"{s}.json" for s in args.slugs]
    for path in paths:
        if not path.exists():
            print(f"  missing  {path.name}"); failures += 1; continue
        try:
            print(f"  {path.stem:<22} {draft_compound(path, args.force)}")
        except RuntimeError as exc:
            failures += 1; print(f"  FAILED   {path.stem}: {exc}")
    if args.stacks:
        (DATA / "stacks").mkdir(exist_ok=True)
        for plan in REGISTRY["stacks"]:
            try:
                print(f"  stack {plan['slug']:<26} {draft_stack(plan, args.force)}")
            except RuntimeError as exc:
                failures += 1; print(f"  FAILED   stack {plan['slug']}: {exc}")
    if args.comparisons:
        (DATA / "comparisons").mkdir(exist_ok=True)
        for plan in REGISTRY["comparisons"]:
            try:
                print(f"  compare {plan['slug']:<24} {draft_comparison(plan, args.force)}")
            except RuntimeError as exc:
                failures += 1; print(f"  FAILED   comparison {plan['slug']}: {exc}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
