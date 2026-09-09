#!/usr/bin/env python3
"""Fetch cited evidence for compound records from Europe PMC and ChEMBL.

Usage:
    python3 scripts/fetch_evidence.py bpc-157 semaglutide     # named slugs
    python3 scripts/fetch_evidence.py --all                   # every seed entry
    python3 scripts/fetch_evidence.py --all --dry-run         # counts only, no files

For each compound in research/compounds.seed.json this writes:

    data/compounds/<slug>.json   a record in status "researched": the source
                                 ledger is filled with real, resolvable
                                 citations; every claim list is left empty
    research/<slug>.md           a research brief: per template section, the
                                 candidate papers with abstracts, evidence tier,
                                 species and any dose excerpts, for the writer

What this script deliberately does not do: it writes no claims. Deciding what a
paper supports, and how to phrase it, is human work under agent/AGENT.md. The
script imports cited source metadata, which AGENT.md allows, and stops there.

It never overwrites a record that a human has moved past "researched".

Standard library only. Europe PMC and ChEMBL need no API key.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
SEED = ROOT / "research" / "compounds.seed.json"
RECORDS = ROOT / "data" / "compounds"
BRIEFS = ROOT / "research"

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
CHEMBL = "https://www.ebi.ac.uk/chembl/api/data/molecule/search.json"
CHEMBL_MOL = "https://www.ebi.ac.uk/chembl/api/data/molecule/{id}.json"

PAUSE = 0.35          # seconds between calls; Europe PMC asks for restraint
RETRIES = 5
TIMEOUT = 30

# Template sections that literature queries can feed, keyed by the attribute
# field they inform in the record. Query fragments are ANDed to the alias query.
# Sections not listed here (regulatory, comparison, FAQ, open questions) are
# either computed, human-only, or fed by ChEMBL.
SECTION_QUERIES: dict[str, tuple[str, str]] = {
    "routes_studied": (
        "Routes studied",
        '(subcutaneous OR intravenous OR intranasal OR oral OR topical OR intraperitoneal OR "route of administration")',
    ),
    "study_doses": (
        "Doses reported in studies",
        '(dose OR dosage OR dosing OR "mg/kg" OR pharmacokinetic*)',
    ),
    "escalation_schedules": (
        "Escalation schedules used in studies",
        '("dose escalation" OR "dose-escalation" OR titration OR "dose-ranging" OR "dose ranging")',
    ),
    "interactions": (
        "Reported interactions",
        '("drug interaction*" OR "drug-drug" OR coadministration OR co-administration OR concomitant)',
    ),
    "exclusion_criteria": (
        "Exclusion criteria in studies",
        '("exclusion criteria" OR "inclusion criteria" OR eligibility OR "were excluded")',
    ),
    "adverse_events": (
        "Adverse events and frequency",
        '("adverse event*" OR "adverse effect*" OR "adverse reaction*" OR safety OR tolerability OR "side effect*")',
    ),
    "biomarkers_monitored": (
        "Biomarkers measured in studies",
        '(biomarker* OR "laboratory parameter*" OR "blood test*" OR "serum level*" OR "plasma level*")',
    ),
    "reported_timelines": (
        "Reported timelines",
        '(onset OR "time course" OR "duration of action" OR "half-life" OR "half life" OR "time to")',
    ),
    "storage": (
        "Storage and stability",
        '(stability OR storage OR degradation OR "shelf life" OR "shelf-life" OR lyophil* OR reconstitut*)',
    ),
}

TIER_ORDER = [  # ranking only; "community-reported" is assigned when nothing is indexed
    "approved-label",
    "human-clinical-trial",
    "observational-human",
    "animal-preclinical",
    "mechanistic-in-vitro",
]

TRIAL_TYPES = {
    "Randomized Controlled Trial",
    "Clinical Trial",
    "Clinical Trial, Phase I",
    "Clinical Trial, Phase II",
    "Clinical Trial, Phase III",
    "Clinical Trial, Phase IV",
    "Controlled Clinical Trial",
    "Pragmatic Clinical Trial",
}
REVIEW_TYPES = {"Review", "Systematic Review", "Meta-Analysis"}
OBSERVATIONAL_TYPES = {
    "Observational Study",
    "Cohort Studies",
    "Case Reports",
    "Case-Control Studies",
    "Cross-Sectional Studies",
    "Multicenter Study",
    "Comparative Study",
}
# Age-group headings are assigned only to studies of human subjects, which
# separates real human evidence from human cell-line work that also carries
# the MeSH heading "Humans".
AGE_MESH = {
    "Adult", "Middle Aged", "Aged", "Aged, 80 and over", "Young Adult",
    "Adolescent", "Child", "Child, Preschool", "Infant", "Infant, Newborn",
}
IN_VITRO_MESH = {"In Vitro Techniques", "Cell Line", "Cells, Cultured", "Cell Line, Tumor"}
SPECIES_MESH = [
    "Humans", "Rats", "Mice", "Rabbits", "Dogs", "Swine", "Cattle", "Sheep",
    "Macaca", "Zebrafish", "Chickens", "Cats", "Guinea Pigs", "Hamsters",
]

DOSE_RE = re.compile(
    r"[^.]*?\b\d+(?:\.\d+)?\s?(?:mg|mcg|µg|μg|ng|IU|units?)(?:\s?/\s?kg)?\b[^.]*\.",
    re.IGNORECASE,
)
TAG_RE = re.compile(r"<[^>]+>")


# ---- HTTP -----------------------------------------------------------------


def get_json(url: str, params: dict | None = None) -> dict:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    last: Exception | None = None
    for attempt in range(RETRIES):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json",
                                                       "User-Agent": "research-reference-fetcher/0.1"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                data = json.loads(response.read().decode("utf-8"))
            time.sleep(PAUSE)
            return data
        except (urllib.error.URLError, OSError, ValueError) as exc:  # noqa: PERF203
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"gave up on {url[:120]}: {last}")


# ---- Europe PMC -----------------------------------------------------------


def alias_query(names: list[str]) -> str:
    """Match the compound in title, abstract or keywords only.

    Europe PMC searches open-access full text by default, which is far too
    loose: a review that mentions a compound once in passing ranks above the
    studies about it. Restricting to these three fields fixes most of that.
    """
    parts = []
    for n in names:
        parts.extend([f'TITLE:"{n}"', f'ABSTRACT:"{n}"', f'KW:"{n}"'])
    return "(" + " OR ".join(parts) + ")"


def hit_count(query: str) -> int:
    data = get_json(EPMC, {"query": query, "format": "json", "pageSize": 1})
    return int(data.get("hitCount", 0))


NOT_REVIEWS = 'NOT PUB_TYPE:"Review" NOT PUB_TYPE:"Systematic Review" NOT PUB_TYPE:"Meta-Analysis"'
ONLY_REVIEWS = '(PUB_TYPE:"Review" OR PUB_TYPE:"Systematic Review" OR PUB_TYPE:"Meta-Analysis")'


def search(query: str, page_size: int, sort: str | None = None) -> list[dict]:
    params = {"query": query, "format": "json", "resultType": "core", "pageSize": page_size}
    if sort:
        params["sort"] = sort
    data = get_json(EPMC, params)
    return data.get("resultList", {}).get("result", [])


def strip_tags(text: str | None) -> str:
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", html.unescape(text or ""))).strip()


KEYWORD_SPECIES = [
    ("Humans", r"\b(patients?|participants?|volunteers?|subjects?|men|women|adults?)\b"),
    ("Rats", r"\brats?\b"), ("Mice", r"\b(mice|mouse|murine)\b"), ("Rabbits", r"\brabbits?\b"),
    ("Dogs", r"\b(dogs?|canine)\b"), ("Swine", r"\b(pigs?|swine|porcine)\b"), ("Zebrafish", r"\bzebrafish\b"),
]
TRIAL_WORDS = re.compile(r"\b(randomi[sz]ed|placebo[- ]controlled|double[- ]blind|phase (?:1|2|3|i{1,3})\b|clinical trial)", re.I)
IN_VITRO_WORDS = re.compile(r"\b(in vitro|cell line|cultured cells|cell culture|hek293|hela|caco-2)\b", re.I)


def classify_from_text(paper: dict) -> tuple[str, str]:
    """Fallback for papers not yet MeSH-indexed: read title and abstract.

    MEDLINE indexing lags publication by months, so recent papers arrive with
    no headings at all. Keyword heuristics are cruder than MeSH but far better
    than leaving a third of the candidates unclassified.
    """
    text = f"{strip_tags(paper.get('title'))} {strip_tags(paper.get('abstractText'))}"
    species = [name for name, pattern in KEYWORD_SPECIES if re.search(pattern, text, re.I)]
    human = "Humans" in species
    animal = any(s != "Humans" for s in species)
    label = ", ".join(species) or "not indexed"
    if TRIAL_WORDS.search(text) and human:
        return "human-clinical-trial", label
    if human and not animal:
        return "observational-human", label
    if animal:
        return "animal-preclinical", label
    if IN_VITRO_WORDS.search(text):
        return "mechanistic-in-vitro", label
    return "unclassified", label


def classify(paper: dict) -> tuple[str, str]:
    """Return (evidence tier or 'review'/'unclassified', species)."""
    pub_types = set(paper.get("pubTypeList", {}).get("pubType", []))
    mesh = {m.get("descriptorName", "") for m in paper.get("meshHeadingList", {}).get("meshHeading", [])}
    if not mesh and not (pub_types & (REVIEW_TYPES | TRIAL_TYPES)):
        return classify_from_text(paper)
    species = ", ".join(s for s in SPECIES_MESH if s in mesh) or "not indexed"
    human_subjects = "Humans" in mesh and bool(mesh & AGE_MESH or pub_types & OBSERVATIONAL_TYPES)
    animal = bool(mesh & set(SPECIES_MESH[1:])) or "Animals" in mesh

    if pub_types & REVIEW_TYPES:
        return "review", species
    if pub_types & TRIAL_TYPES:
        return "human-clinical-trial", species
    if human_subjects:
        return "observational-human", species
    if animal:
        return "animal-preclinical", species
    if mesh & IN_VITRO_MESH or "Humans" in mesh:
        return "mechanistic-in-vitro", species
    return "mechanistic-in-vitro", species


def source_id(paper: dict) -> str | None:
    if paper.get("pmid"):
        return f"pmid-{paper['pmid']}"
    if paper.get("doi"):
        return "doi-" + re.sub(r"[^a-z0-9]+", "-", paper["doi"].lower()).strip("-")
    return None


def source_url(paper: dict) -> str:
    if paper.get("pmid"):
        return f"https://europepmc.org/article/MED/{paper['pmid']}"
    if paper.get("doi"):
        return f"https://doi.org/{paper['doi']}"
    return f"https://europepmc.org/article/{paper.get('source', 'MED')}/{paper.get('id', '')}"


def source_kind(paper: dict) -> str:
    return "preprint" if paper.get("source") == "PPR" else "peer-reviewed"


def dose_excerpts(abstract: str, limit: int = 3) -> list[str]:
    seen: list[str] = []
    for match in DOSE_RE.finditer(abstract):
        sentence = match.group(0).strip()
        if sentence not in seen:
            seen.append(sentence)
        if len(seen) >= limit:
            break
    return seen


# ---- ChEMBL ---------------------------------------------------------------


def phase_of(mol: dict | None) -> float:
    """ChEMBL serialises max_phase inconsistently (4, "4.0", None); normalise."""
    try:
        return float((mol or {}).get("max_phase") or 0)
    except (TypeError, ValueError):
        return 0.0



def chembl_lookup(names: list[str]) -> dict | None:
    """Best ChEMBL molecule whose preferred name or synonym matches exactly."""
    wanted = {n.lower() for n in names}
    try:
        data = get_json(CHEMBL, {"q": names[0], "limit": 25})
    except RuntimeError:
        return None
    best = None
    for mol in data.get("molecules", []):
        candidates = {(mol.get("pref_name") or "").lower()}
        candidates |= {s.get("molecule_synonym", "").lower() for s in mol.get("molecule_synonyms", [])}
        if candidates & wanted:
            if best is None or phase_of(mol) > phase_of(best):
                best = mol
    if best is None:
        return None
    return {
        "chembl_id": best.get("molecule_chembl_id"),
        "pref_name": best.get("pref_name"),
        "molecule_type": best.get("molecule_type"),
        "max_phase": phase_of(best),
        "first_approval": best.get("first_approval"),
        "atc": best.get("atc_classifications") or [],
        "synonyms": sorted({s.get("molecule_synonym") for s in best.get("molecule_synonyms", []) if s.get("molecule_synonym")})[:12],
        "url": f"https://www.ebi.ac.uk/chembl/compound_report_card/{best.get('molecule_chembl_id')}/",
    }


# ---- Assembly -------------------------------------------------------------


def fetch_compound(entry: dict, max_papers: int, counts_only: bool = False) -> dict:
    """Full fetch, or just the landscape counts when counts_only (dry runs)."""
    names = [entry["name"], *entry.get("aliases", [])]
    base = alias_query(names)
    today = dt.date.today().isoformat()

    counts = {
        "total": hit_count(base),
        "randomized_controlled_trials": hit_count(f'{base} AND PUB_TYPE:"Randomized Controlled Trial"'),
        "clinical_trials": hit_count(f'{base} AND PUB_TYPE:"Clinical Trial"'),
        "reviews": hit_count(f'{base} AND PUB_TYPE:"Review"'),
        "human_indexed": hit_count(f'{base} AND MESH:"Humans"'),
        "animal_indexed": hit_count(f'{base} AND MESH:"Animals" NOT MESH:"Humans"'),
    }

    if counts_only:
        return {"entry": entry, "counts": counts, "sections": {}, "ledger": {},
                "reviews": [], "mentions": [],
                "tier": ("human-clinical-trial" if counts["clinical_trials"] or counts["randomized_controlled_trials"]
                         else "observational-human" if counts["human_indexed"]
                         else "animal-preclinical" if counts["animal_indexed"]
                         else "mechanistic-in-vitro" if counts["total"] else "community-reported"),
                "chembl": None, "retrieved": today}

    has_trials = bool(counts["clinical_trials"] or counts["randomized_controlled_trials"])
    trial_filter = '(PUB_TYPE:"Randomized Controlled Trial" OR PUB_TYPE:"Clinical Trial")'
    ledger: dict[str, dict] = {}
    sections: dict[str, list[dict]] = {}
    shown: dict[str, str] = {}   # source id -> first section label that showed it in full
    for field, (label, fragment) in SECTION_QUERIES.items():
        common = f"{base} AND {fragment} AND HAS_ABSTRACT:y AND (SRC:MED OR SRC:PPR) {NOT_REVIEWS}"
        papers: list[dict] = []
        if has_trials:
            # Evidence first: human trials fill the section before anything else.
            papers.extend(search(f"{common} AND {trial_filter}", max_papers))
        if len(papers) < max_papers:
            seen_ids = {source_id(p) for p in papers}
            papers.extend(p for p in search(common, max_papers * 2) if source_id(p) not in seen_ids)
        # Prefer papers not already shown in full under an earlier section.
        papers.sort(key=lambda p: source_id(p) in shown)
        papers = papers[:max_papers]
        rows = []
        for paper in papers:
            sid = source_id(paper)
            if not sid:
                continue
            tier, species = classify(paper)
            abstract = strip_tags(paper.get("abstractText"))
            rows.append({
                "id": sid, "tier": tier, "species": species, "also_under": shown.get(sid),
                "title": strip_tags(paper.get("title")),
                "journal": paper.get("journalTitle") or paper.get("journalInfo", {}).get("journal", {}).get("title", ""),
                "year": paper.get("pubYear"), "cited_by": paper.get("citedByCount", 0),
                "url": source_url(paper), "abstract": abstract,
                "dose_excerpts": dose_excerpts(abstract) if field in ("study_doses", "escalation_schedules") else [],
            })
            shown.setdefault(sid, label)
            ledger.setdefault(sid, {
                "id": sid,
                "title": strip_tags(paper.get("title")),
                "url": source_url(paper),
                "published": paper.get("firstPublicationDate") or f"{paper.get('pubYear', '1900')}-01-01",
                "kind": source_kind(paper),
            })
        sections[field] = rows

    reviews = []
    for paper in search(f"{base} AND {ONLY_REVIEWS} AND HAS_ABSTRACT:y AND SRC:MED", 5, sort="CITED desc"):
        sid = source_id(paper)
        if not sid:
            continue
        reviews.append({
            "id": sid, "title": strip_tags(paper.get("title")), "year": paper.get("pubYear"),
            "journal": paper.get("journalTitle", ""), "cited_by": paper.get("citedByCount", 0),
            "url": source_url(paper), "abstract": strip_tags(paper.get("abstractText")),
        })
        ledger.setdefault(sid, {
            "id": sid, "title": strip_tags(paper.get("title")), "url": source_url(paper),
            "published": paper.get("firstPublicationDate") or f"{paper.get('pubYear', '1900')}-01-01",
            "kind": source_kind(paper),
        })

    # A compound with nothing in any title or abstract may still be mentioned
    # in passing inside open-access full text. Show those so the writer knows
    # the literature was searched, but keep them out of the ledger: a paper
    # that mentions a compound once is not a source about it.
    mentions: list[dict] = []
    if counts["total"] == 0:
        loose = "(" + " OR ".join(f'"{n}"' for n in names) + ")"
        for paper in search(f"{loose} AND SRC:MED", 5):
            mentions.append({"title": strip_tags(paper.get("title")), "year": paper.get("pubYear"),
                             "journal": paper.get("journalTitle", ""), "url": source_url(paper)})

    primary_tiers = {r["tier"] for rows in sections.values() for r in rows if r["tier"] in TIER_ORDER}
    chembl = chembl_lookup(names)
    if chembl and phase_of(chembl) >= 4:
        primary_tiers.add("approved-label")
    tier = next((t for t in TIER_ORDER if t in primary_tiers), "mechanistic-in-vitro")
    # The landscape counts cap the tier. A handful of misclassified candidate
    # papers must not promote a compound with no indexed human trials.
    if tier == "human-clinical-trial" and not (counts["clinical_trials"] or counts["randomized_controlled_trials"]):
        tier = "observational-human"
    if tier in ("human-clinical-trial", "observational-human") and not counts["human_indexed"]:
        tier = "animal-preclinical"
    if counts["total"] == 0 and not chembl:
        # Nothing indexed anywhere: whatever circulates about it is anecdote.
        tier = "community-reported"

    return {"entry": entry, "counts": counts, "sections": sections, "ledger": ledger,
            "reviews": reviews, "mentions": mentions, "tier": tier, "chembl": chembl, "retrieved": today}


def build_record(result: dict) -> dict:
    entry, counts, chembl = result["entry"], result["counts"], result["chembl"]
    name, slug = entry["name"], entry["slug"]
    summary = (
        f"Research record for {name}. Europe PMC indexes {counts['total']} publications, "
        f"including {counts['randomized_controlled_trials']} randomized controlled trials, "
        f"as of {result['retrieved']}. Claims are pending human authorship and review."
    )
    description = (
        f"Cited overview of published {name} research: {counts['total']} indexed publications, "
        f"{counts['randomized_controlled_trials']} randomized controlled trials. Evidence tier on every claim."
    )
    if len(description) > 160:
        description = description[:157].rstrip() + "..."
    title = f"{name}: what the research shows"
    if len(title) > 60:
        title = f"{name} research overview"[:60]

    regulatory_note = []
    if chembl:
        phase = phase_of(chembl)
        regulatory_note.append({
            "value": (
                f"ChEMBL {chembl['chembl_id']}: maximum clinical phase {phase:g}"
                + (f", first approval {chembl['first_approval']}" if chembl.get("first_approval") else "")
                + (f", ATC {', '.join(chembl['atc'])}" if chembl.get("atc") else "")
                + ". Jurisdiction-level status pending human review."
            ),
            "evidence_label": "approved-label" if phase >= 4 else "human-clinical-trial" if phase >= 1 else "mechanistic-in-vitro",
            "source_ids": [],
        })

    aliases = sorted(set(entry.get("aliases", [])) | set((chembl or {}).get("synonyms", [])))
    return {
        "type": "compound",
        "preferred_name": name,
        "aliases": aliases,
        "slug": slug,
        "status": "researched",
        "evidence_tier": result["tier"],
        "summary": summary,
        "seo": {"title": title, "description": description},
        "attributes": {
            **{field: [] for field in SECTION_QUERIES},
            "study_durations": [],
            "weight_normalized_doses": [],
            "regulatory_status": regulatory_note,
        },
        "evidence_summary": {
            "retrieved_at": result["retrieved"],
            "source": "Europe PMC, ChEMBL",
            "publications": counts,
            "candidate_papers_by_tier": {
                t: sum(1 for rows in result["sections"].values() for r in rows if r["tier"] == t)
                for t in [*TIER_ORDER, "review", "unclassified"]
            },
            "chembl": chembl,
        },
        "comparison_peers": [],
        "open_questions": [],
        "media": {"walkthrough_video": "", "transcript": ""},
        "faq": [],
        "sources": sorted(result["ledger"].values(), key=lambda s: s["published"], reverse=True),
        "related": [],
        "uniqueness_pct": None,
        "review": {"author": "", "reviewer": "", "reviewer_credential": "", "reviewed_at": ""},
        "changelog": [{
            "date": result["retrieved"],
            "change": "Evidence fetched from Europe PMC and ChEMBL by scripts/fetch_evidence.py; claims not yet written.",
        }],
    }


def build_brief(result: dict) -> str:
    entry, counts, chembl, sections = result["entry"], result["counts"], result["chembl"], result["sections"]
    name = entry["name"]
    out: list[str] = []
    out.append(f"# {name} — research brief\n")
    out.append(f"Retrieved {result['retrieved']} from Europe PMC and ChEMBL by `scripts/fetch_evidence.py`. "
               f"Suggested overall tier: **`{result['tier']}`**. Every figure below is a candidate for a human "
               f"to read, judge and cite. Nothing here is a claim yet.\n")
    out.append("## Evidence landscape\n")
    out.append("| Measure | Count |\n|---|---|")
    for key, label in [("total", "Publications indexed"), ("randomized_controlled_trials", "Randomized controlled trials"),
                       ("clinical_trials", "Clinical trials, any design"), ("reviews", "Reviews"),
                       ("human_indexed", "Indexed with MeSH Humans"), ("animal_indexed", "Indexed as animal-only")]:
        out.append(f"| {label} | {counts[key]} |")
    out.append("")
    if counts["randomized_controlled_trials"] == 0 and counts["clinical_trials"] == 0:
        out.append("> **No human clinical trials are indexed.** Sections that describe human dosing, escalation, "
                   "exclusion criteria or adverse-event frequencies cannot be honestly populated and must be "
                   "suppressed, not padded. Say so on the page.\n")

    out.append("## Identity (ChEMBL)\n")
    if entry.get("sequence"):
        out.append(f"- Sequence: `{entry['sequence']}` (not used as a search term; it matches any paper printing a sequence)")
    if chembl:
        out.append(f"- `{chembl['chembl_id']}` **{chembl.get('pref_name') or name}**, type {chembl.get('molecule_type')}")
        out.append(f"- Maximum clinical phase: {chembl.get('max_phase')}"
                   + (f"; first approval {chembl['first_approval']}" if chembl.get("first_approval") else "; no approval recorded"))
        if chembl.get("atc"):
            out.append(f"- ATC: {', '.join(chembl['atc'])}")
        if chembl.get("synonyms"):
            out.append(f"- Synonyms: {', '.join(chembl['synonyms'])}")
        out.append(f"- {chembl['url']}\n")
    else:
        out.append("- No ChEMBL record matches this name or its aliases. That usually means the compound has "
                   "never entered a registered clinical development programme, which is itself relevant to "
                   "the regulatory-status section.\n")

    empty: list[str] = []
    for field, (label, _) in SECTION_QUERIES.items():
        rows = sections.get(field, [])
        if not rows:
            empty.append(label)
            continue
        out.append(f"## {label}\n")
        out.append(f"Record field: `attributes.{field}`. {len(rows)} candidate papers, most cited first.\n")
        for i, r in enumerate(rows, 1):
            if r.get("also_under") and r["also_under"] != label:
                out.append(f"{i}. *{r['title']}* — `{r['tier']}`, {r['year']}, `{r['id']}`. Abstract shown under **{r['also_under']}**.")
                continue
            out.append(f"### {i}. {r['title']}\n")
            out.append(f"- **Tier:** `{r['tier']}` · **Species:** {r['species']} · {r['year']} · {r['journal'] or 'journal not indexed'} · cited by {r['cited_by']}")
            out.append(f"- **Source id:** `{r['id']}` · {r['url']}")
            if r["dose_excerpts"]:
                out.append("- **Dose mentions in abstract:**")
                for ex in r["dose_excerpts"]:
                    out.append(f"  - {ex}")
            if r["abstract"]:
                out.append(f"\n> {r['abstract'][:1400]}{'…' if len(r['abstract']) > 1400 else ''}\n")
            else:
                out.append("")
    if result.get("reviews"):
        out.append("## Background reading (secondary sources)\n")
        out.append("Reviews and meta-analyses, most cited first. Useful for orientation; cite the primary studies they point to, not the review, wherever possible.\n")
        for r in result["reviews"]:
            out.append(f"- **{r['title']}** · {r['year']} · {r['journal'] or 'journal not indexed'} · cited by {r['cited_by']} · `{r['id']}` · {r['url']}")
        out.append("")
    if result.get("mentions"):
        out.append("## Mentioned in full text only\n")
        out.append("No indexed paper names this compound in its title or abstract. These papers mention it "
                   "somewhere in their open-access full text. They are not sources about the compound and were "
                   "not added to the ledger; they show where the name appears in the literature at all.\n")
        for m in result["mentions"]:
            out.append(f"- {m['title']} · {m['year']} · {m['journal'] or 'journal not indexed'} · {m['url']}")
        out.append("")
    if empty:
        out.append("## Sections with no candidate evidence\n")
        out.append("Per `docs/page-template-spec.md` these must be suppressed, not rendered empty:\n")
        for label in empty:
            out.append(f"- {label}")
        out.append("")
    out.append("## Source ledger\n")
    out.append(f"{len(result['ledger'])} unique sources written to `data/compounds/{entry['slug']}.json`.\n")
    return "\n".join(out)


# ---- CLI ------------------------------------------------------------------


def load_seed() -> list[dict]:
    entries = json.loads(SEED.read_text(encoding="utf-8"))
    for e in entries:
        if not e.get("name") or not e.get("slug"):
            raise SystemExit(f"seed entry needs name and slug: {e}")
    return entries


def existing_status(slug: str) -> str | None:
    path = RECORDS / f"{slug}.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("status")
    except ValueError:
        return "unreadable"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("slugs", nargs="*", help="seed slugs to fetch")
    parser.add_argument("--all", action="store_true", help="fetch every seed entry")
    parser.add_argument("--dry-run", action="store_true", help="print evidence counts only, write nothing")
    parser.add_argument("--max-papers", type=int, default=8, help="candidate papers per section (default 8)")
    parser.add_argument("--force", action="store_true", help="refresh an existing 'researched' record")
    args = parser.parse_args(argv)
    # Progress lines should appear as each compound finishes, even when piped.
    sys.stdout.reconfigure(line_buffering=True)

    seed = load_seed()
    if args.all:
        chosen = seed
    else:
        wanted = set(args.slugs)
        chosen = [e for e in seed if e["slug"] in wanted]
        missing = wanted - {e["slug"] for e in chosen}
        if missing:
            print(f"not in {SEED.relative_to(ROOT)}: {', '.join(sorted(missing))}")
            return 1
    if not chosen:
        parser.print_help()
        return 1

    RECORDS.mkdir(parents=True, exist_ok=True)
    BRIEFS.mkdir(parents=True, exist_ok=True)
    failures = 0
    for entry in chosen:
        slug = entry["slug"]
        status = existing_status(slug)
        if status and status not in ("discovered", "researched"):
            print(f"  skip      {slug}: record is '{status}', a human owns it now")
            continue
        if status == "researched" and not args.force and not args.dry_run:
            print(f"  skip      {slug}: already researched (use --force to refresh)")
            continue
        try:
            result = fetch_compound(entry, args.max_papers, counts_only=args.dry_run)
        except RuntimeError as exc:
            failures += 1
            print(f"  FAILED    {slug}: {exc}")
            continue
        c = result["counts"]
        line = (f"{slug:<22} total={c['total']:<6} RCT={c['randomized_controlled_trials']:<4} "
                f"trials={c['clinical_trials']:<4} tier={result['tier']}")
        if args.dry_run:
            print(f"  plan      {line}")
            continue
        record = build_record(result)
        (RECORDS / f"{slug}.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        (BRIEFS / f"{slug}.md").write_text(build_brief(result), encoding="utf-8")
        print(f"  wrote     {line}  sources={len(record['sources'])}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
