# Content SOP: how one programmatic page gets made

The pipeline can generate thirty-four compound pages from records without a
person thinking about any of them. That is the risk, not the feature. This
document is the process that runs **per page** before it is allowed to be
indexed: keyword research, SERP research, an intent map, a statement of
information gain, and an outline, in that order, each producing a file or a
field that the next stage reads.

The page count is small on purpose. Thirty-four compounds, eight stacks, eight
comparisons and three tools is a set a person can actually work through. Treat
each page as a page, not a row.

Related: `docs/page-template-spec.md` (which sections exist),
`docs/design.md` (how they are rendered), `docs/content-contract.md` (record
shape), `agent/AGENT.md` (what may be written at all).

## Scope: informational intent only

The pilot researches and answers **informational** queries: what a compound is,
what studies measured, what happened in trials, how compounds compare, what is
unknown. Commercial and transactional queries — where to buy, what it costs,
which supplier to trust — are **out of scope**. They are not researched, not
mapped, and not answered, because `agent/AGENT.md` prohibits vendor and
affiliate content during the pilot and because answering them well would require
expertise this site does not claim.

Leave them out of the intent map entirely rather than writing refusals into the
page. One line near the top of a page is enough to set the boundary, and the
page spends its words on the questions it can answer with evidence.

## The constraint that shapes every stage

Even inside informational intent, the most-searched question is dosage, and
this site does not recommend doses.

So "match search intent" cannot mean "give the searcher what they asked for".
Here it means:

> Answer the query **in the searcher's own words**, from the evidence, and
> state plainly when the evidence-based answer is that nothing was established.

A page that says "no human trial has set an ipamorelin dose; here is what the
two trials administered, and here is why that is not a recommendation" resolves
the query better than a vendor's invented number, and it is the only version of
the answer this site is permitted to publish. That is a content decision, not a
compliance afterthought, and stages 3 and 5 below encode it.

## Stages at a glance

| # | Stage | Produces | Exit gate |
|---|---|---|---|
| 0 | Record exists | `data/<type>/<slug>.json` at `researched` or `draft` | Source ledger non-empty, or a measured zero |
| 1 | Keyword research | `queries[]` in the intent map | Every query has a source; volumes real or explicitly null |
| 2 | SERP research | `competitors[]` in the intent map | At least two real competitors scored, or "thin SERP" recorded |
| 3 | Intent map | `research/intents/<slug>.json` | Every query has a `policy` and a destination |
| 4 | Information gain | `information_gain` in the intent map | One sentence naming something no competitor has |
| 5 | Outline | `outline[]` in the intent map | Every section maps to record data or a stated absence |
| 6 | Draft, format, measure | Record claims, built page | Validator passes; formatting and intent coverage reported |
| 7 | Human review | `review.reviewer_credential` | A named credentialed person signed it |

Stages 1 to 5 are research and cost money or time but touch no page. Stage 6 is
mechanical. Stage 7 is the launch blocker and cannot be automated.

## Stage 0: the record must exist first

Evidence precedes topic research. A page is never planned around a keyword and
then filled; it is planned around what the literature contains.

```bash
python3 scripts/fetch_evidence.py <slug>      # Europe PMC + ChEMBL -> source ledger + research/<slug>.md
```

Exit gate: the record has a populated `sources[]`, or a measured zero with
`publications.total = 0`. A zero is a finding, not a failure: it makes the page
short and honest and it is still worth publishing.

## Stage 1: keyword research

**Source of truth, in order of preference.**

1. **Search Console**, once pages are indexed. First-party, free, and the only
   record of queries that actually reached this site. Not available before the
   review gate opens. Design for it now and switch when it exists.
2. **DataForSEO**, configured and available today. Real volume, difficulty and
   intent classification.
3. **SERP-revealed demand**, free and always available: People Also Ask,
   autocomplete, and the H2s and FAQ questions of the pages that already rank.
   Overlap between two ranking pages is a strong demand signal.

**Commands.** Check cost before every paid call; the account balance is small
and the checker returns `needs_approval` for unrecognised endpoints.

```bash
"$HOME/.claude/skills/seo/bin/claude-seo" run dataforseo_costs.py check <endpoint> --count <n>
```

Then, through the `seo-dataforseo` skill: search volume for the seed set,
keyword difficulty in bulk, and search-intent classification. Seed the set from
the compound name plus its aliases crossed with the six intent heads above,
then keep whatever comes back with real volume.

**Use the right volume column.** Google Ads returns **0** for most terms it
classifies as pharmaceutical, and for research peptides that is most of the
set: on the ipamorelin run, 21 of 28 keywords came back 0 from Ads, including
`ipamorelin` itself, which DataForSEO's clickstream column puts at about 20,800
searches a month. Labs' own `search_volume` mirrors Ads and inherits the same
zeros. So the instrument is `dataforseo_labs/google/keyword_overview` with
`include_clickstream_data: true`, and the figure recorded is
`clickstream_keyword_info.search_volume`. Keep the Ads number beside it: the
few terms Ads does report (combination and comparison phrasings) are a useful
cross-check, and where the two agree the number is solid.

**Record volumes honestly.** Each query carries
`"volume": {"clickstream": N, "google_ads": N, "kd": N, "source": "..."}`; a
missing figure is `null`, never a guess. `"source"` names the endpoint and the
date so a later reader can tell measured demand from inference.

**Measured cost.** Stage 1 for one compound page, 28 keywords, four endpoints
(Ads search volume, Labs keyword overview, bulk difficulty, search intent):
**$0.15**. The whole compound set is about $5.

**Then read what the numbers say before writing anything.** The ipamorelin run
changed the plan: demand sits on the combination and comparison queries
(`cjc 1295 ipamorelin dosage` 8,100/mo, `ipamorelin vs sermorelin` 4,400/mo)
far more than on the compound alone, and the comparison the registry planned
(`vs ghrp-6`, 90/mo) was chosen for evidence availability, not demand. Stage 1
is allowed to add stack and comparison pages to the plan; that is one of the
things it is for.

Exit gate: `queries[]` has at least five entries, each with `query`, `source`
and a `volume` object; queries are ordered by clickstream volume, and any
demand the registry plan does not cover is recorded as an `open_action`.

## Stage 2: SERP research

For the head term and the top two or three query heads, record who actually
ranks. Exclude non-competitors: Wikipedia, Reddit, PubMed and other government
or primary-source domains, vendor product pages, patent filings, and clinic
service pages. What remains is the real competition.

Score each on depth, formatting, SEO and UX out of ten, and note the single
biggest gap. Two questions matter more than the score:

- **What format does Google reward here?** Long-form explainer, comparison
  table, FAQ, or something else.
- **What does every competitor fail to do?** That is the opening.

If fewer than two real competitors survive filtering, record `"thin_serp": true`
and say so in the brief rather than padding the table.

Exit gate: `competitors[]` with at least two scored entries, or `thin_serp`.

## Stage 3: the intent map

The artifact this SOP exists to produce: `research/intents/<slug>.json`. It is
the bridge between what people search and what the page is allowed to say.

```json
{
  "slug": "ipamorelin",
  "generated": "2026-09-20",
  "sources": ["serp-paa", "competitor-h2", "dataforseo-search-volume"],
  "thin_serp": false,
  "queries": [
    {
      "query": "ipamorelin dosage",
      "volume": { "clickstream": 3408, "google_ads": 0, "kd": 7, "source": "dataforseo keyword_overview, US/en, 2026-09-20" },
      "source": "competitor-h2+paa",
      "intent": "informational",
      "policy": "evidence-with-boundary",
      "section": "study_doses",
      "heading": "What doses did studies use?"
    }
  ],
  "competitors": [
    { "url": "...", "words": 7053, "score": 25, "gap": "no credentialed reviewer; dosing without trial support" }
  ],
  "information_gain": "...",
  "outline": ["glance", "what", "human-trials", "evidence", "doses", "..."]
}
```

### The `policy` field

Three values in normal use. This is the mechanism that reconciles search intent
with `agent/AGENT.md`, and every query must carry one.

| policy | Meaning | Typical queries |
|---|---|---|
| `evidence-only` | Answer from claims. If no claim exists, state the absence explicitly and name what was searched. | side effects, half-life, results, mechanism, what it measured |
| `evidence-with-boundary` | Answer from claims **and** say in the same breath what the answer is not. | dosage, cycle length, how long to use |
| `redirect` | Answer by pointing to the record that holds it. | "X vs Y", stacking, class questions |

`evidence-with-boundary` carries a `boundary` field: **reader-facing copy** that
the renderer places at the start of the section's lede, verbatim. It is not an
instruction to a writer; write it as the sentence the reader will see. "These are the doses studies administered, not a
recommended range, and no human trial established a dose for the uses this
compound is marketed for" is the whole mechanism in one sentence. Without it the
section is a dosing guide with citations, which is the thing the site exists not
to be.

A fourth value, `decline`, exists for a query that must be answered with "this
page does not cover that". It should be rare. Commercial queries do not need it
because they never enter the map (see Scope above).

### Heading rewriting

Where a query maps to a section, `heading` may replace the spec's default
heading with the searcher's phrasing. "Adverse events and frequency" becomes
"What side effects did studies report?" when that is how the query is typed. The
content, the claims and the tiers do not change; only the words above them do.
`docs/design.md` already permits question-form headings.

Exit gate: every entry in `queries[]` has a `policy`, and every non-`decline`
entry has either a `section` or an FAQ destination.

## Stage 4: information gain

One paragraph naming **exactly** what this page offers that no ranking
competitor does. Not "more detail" and not "better formatting".

For this site the gain is almost always one of three things, and it is real:

- **The studies shown as data**, not described in prose: the evidence table with
  design, n, species, dose, route, duration and outcome, each row linked to its
  source. No competitor on any peptide SERP does this.
- **Verbatim quotation with tiering**, so a reader sees the sentence the claim
  came from and how strong that evidence is.
- **A measured statement of absence**: "two of sixty-three indexed publications
  are human trials, and neither tests the outcomes this compound is marketed
  for." Competitors cannot write that sentence because they have not counted.

Exit gate: `information_gain` is one specific paragraph, and a reader could
check it against the record.

## Stage 5: outline

Order sections by intent rank, within policy. The spec order in
`docs/page-template-spec.md` is the fallback when no intent map exists.

Rules:

1. **The evidence answer comes first.** For a scarce-evidence compound, a
   "What happened in the human trials?" section directly after "What it is"
   answers most queries at once and belongs above everything else.
2. **Top query heads move up**, using their mapped section and rewritten
   heading.
3. **Unmapped queries become FAQ items** in the searcher's words, answered from
   claims or with an explicit absence statement.
4. **Differentiators follow, not lead.** The method notes, reference card and
   changelog are what make the page trustworthy, but they are not what the
   searcher came for.

Exit gate: every outline entry maps to record data or to a stated absence, and
no entry promises something the record cannot support.

## Stage 6: draft, format, measure

Mechanical, and already built.

```bash
python3 scripts/draft_claims.py <slug> --force     # extractive claims from the ledger
npm run build
python3 scripts/measure_pages.py --formatting <slug>   # docs/design.md section 9.10 minimums
python3 scripts/measure_pages.py --write               # uniqueness_pct
python3 scripts/validate_content.py
```

Exit gate: the validator passes, the formatting report meets the section 9.10
minimums, and uniqueness clears the 40% floor.

## Stage 7: human review

The gate nothing automates. A named person with a stated credential checks
each claim against its quoted excerpt, confirms the excerpt belongs under its
heading, and confirms the tier. Only then may `status` become `published` and
the page become indexable.

Until that happens every page renders `noindex` and stays out of the sitemap,
which is correct and is not a bug to work around.

## Per page type

| Type | Query heads that matter | Notes |
|---|---|---|
| Compound | dosage, side effects, half-life, legality, results, vs | The full SOP applies. |
| Stack | "X and Y together", "X Y stack", dosing of the pair | The combination-evidence section is mandatory and usually says no study tested it. That sentence **is** the information gain. |
| Comparison | "X vs Y", "which is better" | Lead with the side-by-side table. If no head-to-head study exists, say so above the table, not below. |
| Tool | "reconstitution calculator", "peptide dose calculator" | Intent is transactional-adjacent: the user wants the arithmetic done. State the formula, accept no personal parameters. |

## Cost control

The DataForSEO balance is small. Before any paid call, run the cost check, and
prefer the cheap path: one bulk search-volume call for a page's whole seed set
beats one call per query, and SERP-revealed demand costs nothing at all.

Never spend on a page whose record is still empty; stage 0 comes first for a
reason.

## Worked example

`research/intents/ipamorelin.json` is the first intent map. It was built from
SERP evidence, then re-run with measured volumes once DataForSEO was
configured. It carries fifteen informational queries ordered by demand across
the three policies, the four scored competitors, a `demand_findings` list, the
information-gain paragraph the outline was ordered around, and the
`open_actions` the research exposed.

Two of those actions are worth noting because they show the SOP working as
intended rather than rubber-stamping the page. The research found that
`reported_timelines` is empty even though Gobburu 1999 states the two-hour
half-life in its abstract, which is a drafting miss, not an absence of evidence.
And it found that `regulatory_status` rests only on the ChEMBL phase when two
citable primary documents exist. Neither would have surfaced from the record
alone; both came from asking what people search for.

## Changelog

- 2026-09-20 — Stage 1 run on ipamorelin with DataForSEO. Clickstream adopted as
  the volume column after Google Ads returned 0 for 21 of 28 terms; cost and
  demand findings recorded; stage 1 may now add pages to the registry plan.
- 2026-09-20 — SOP written. Stages 1 to 5 are new process; stages 0, 6 and 7
  describe what already existed. The `policy` field and the intent map are the
  new mechanism. Commercial and transactional intent placed out of scope for the
  pilot.
