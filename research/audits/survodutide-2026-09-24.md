# Survodutide audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: e254346 (page/survodutide, pre-merge build). Twelfth page written end to end under the sequencing rule: stages 1–5 in research/intents/survodutide.json before any guide text.

## Part 1: audit

Built from `dist/compounds/survodutide/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 13/20 | 6 data tables, 34 cited verbatim quotations, measured-absence statements absent |
| Expertise | 9/25 | 23 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 11 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/survodutide`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'doi.org': 3, 'europepmc.org': 23}).

### Page facts

| | |
|---|---|
| Title (55) | Survodutide: Phase 3 Trials, Dose, Side Effects, Status |
| Description (159) | Survodutide (BI 456906): the June 2026 phase 3 results with dose and duration, indirect comparisons with tirzepatide and retatrutide, side effects, and status. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/survodutide |
| H1 / H2 / H3 | ["Survodutide (BI 456906): what the phase 3 trials found, how it compares with tirzepatide and retatrutide, and what 'survodutide peptide' vials are"] / 31 / 3 |
| Words (total / own prose / quoted) | 8445 / 5360 / 1129 |
| Readability Flesch, grade, avg sentence: all | 11, 17.5, 23.2 |
| … own prose only | 21, 14.9, 18.1 |
| … quotations only | 0, 20.6, 29.3 |
| Keyword `survodutide` | 124× (1.47%); title True, H1 True, first 100 words True |
| Links | 11 internal (1.3/1k words); 26 external {'doi.org': 3, 'europepmc.org': 23}; new-tab 26/26 |
| Formatting | {'tables': 6, 'captions': 6, 'quotes_with_cite': 34, 'abbr': 3, 'time': 36, 'details': 17, 'images': 0, 'bold_own': 31} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What survodutide is, and where its trials stand
3. What the evidence level means
4. Survodutide in two minutes
5. How survodutide works: glucagon plus GLP-1 in one molecule
6. What happened in the human studies?
7. Trial by trial: what survodutide did in people
8. What the evidence shows
9. Doses reported in studies
10. Every survodutide dose in the trials, in one table
11. Side effects: what the trials recorded, and what is still being measured
12. Who survodutide is discussed for, and the cautions that recur
13. Biomarkers measured in studies
14. Reported interactions
15. Reported timelines
16. What is measured over time, and what is not
17. Escalation schedules used in studies
18. Study durations
19. Routes: once-weekly subcutaneous injection in every trial
20. What people report outside the literature
21. Storage and handling
22. Common mistakes in how survodutide is discussed
23. Survodutide vs tirzepatide, semaglutide, retatrutide and mazdutide
24. How it compares
25. Regulatory status: phase 3 complete in obesity, not yet approved
26. Open questions and limitations
27. Questions people ask
28. Sources
29. Reference card
30. Related records
31. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 21 (avg sentence 18.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.3 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| Own-prose Flesch 21 (avg sentence 18.1) | `reject-policy` | design.md §9.7 budgets sentence length (met); terminology (glucagon receptor, steatotic, estimand) drives syllables. Precedent: all prior audits. | none | — |
| Internal links 1.3/1k | `accept-template` (partial) | Guide prose links tirzepatide, semaglutide, retatrutide, cagrilintide, the CagriSema stack and the comparison directory (11 unique); an 8,400-word page with 26 source links dilutes the ratio by design; automatic entity linking remains the open template item. | template | engineer, open |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| 'Measured-absence statements absent' (Experience 13/20) | `reject-policy` | No absence block renders because every mapped field has claims; the audit rewards absence statements as a proxy for honesty, and this record has none to make. Not a defect. | none | — |
| "Escalation schedules" quoted the NEJM paper's estimand sentence as a dose-escalation design; found on reading the build | `accept-record` (done) + `accept-script` (open) | Claims removed; the titration claims from the design paper kept. Same escalation-regex item as kisspeptin and ARA-290. | record, script | writer done; engineer open |
| Drafter tagged 'interactive response technology' (randomisation) as a drug interaction | `accept-record` (done) + `accept-script` (open) | Removed; the NPY2R-agonist combination claim from a mouse study kept as genuine. Same regex item. | record, script | writer done; engineer open |
| Investigational phase 3 medicine written although the queue rule defers approved medicines | judgment, recorded | Not approved, so the rule does not bar it; the SERP is clinical publishers (KD 17), so the page targets the 'survodutide peptide' searcher and the comparison queries. Recorded in the map's queue_note. | queue | owner aware |
| Regulatory status cited without filing documents | `accept-record` (boundary, done) | Editorial with pending_source; open_actions name what to add. | record | writer |

## Part 3: exit audit

Built from `dist/compounds/survodutide/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 13/20 | 6 data tables, 33 cited verbatim quotations, measured-absence statements absent |
| Expertise | 9/25 | 23 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 11 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/survodutide`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'doi.org': 3, 'europepmc.org': 23}).

### Page facts

| | |
|---|---|
| Title (55) | Survodutide: Phase 3 Trials, Dose, Side Effects, Status |
| Description (159) | Survodutide (BI 456906): the June 2026 phase 3 results with dose and duration, indirect comparisons with tirzepatide and retatrutide, side effects, and status. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/survodutide |
| H1 / H2 / H3 | ["Survodutide (BI 456906): what the phase 3 trials found, how it compares with tirzepatide and retatrutide, and what 'survodutide peptide' vials are"] / 31 / 3 |
| Words (total / own prose / quoted) | 8404 / 5351 / 1095 |
| Readability Flesch, grade, avg sentence: all | 11, 17.4, 23.1 |
| … own prose only | 21, 14.8, 18.1 |
| … quotations only | 2, 20.3, 29.2 |
| Keyword `survodutide` | 123× (1.46%); title True, H1 True, first 100 words True |
| Links | 11 internal (1.3/1k words); 26 external {'doi.org': 3, 'europepmc.org': 23}; new-tab 26/26 |
| Formatting | {'tables': 6, 'captions': 6, 'quotes_with_cite': 33, 'abbr': 3, 'time': 36, 'details': 17, 'images': 0, 'bold_own': 31} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What survodutide is, and where its trials stand
3. What the evidence level means
4. Survodutide in two minutes
5. How survodutide works: glucagon plus GLP-1 in one molecule
6. What happened in the human studies?
7. Trial by trial: what survodutide did in people
8. What the evidence shows
9. Doses reported in studies
10. Every survodutide dose in the trials, in one table
11. Side effects: what the trials recorded, and what is still being measured
12. Who survodutide is discussed for, and the cautions that recur
13. Biomarkers measured in studies
14. Reported interactions
15. Reported timelines
16. What is measured over time, and what is not
17. Escalation schedules used in studies
18. Study durations
19. Routes: once-weekly subcutaneous injection in every trial
20. What people report outside the literature
21. Storage and handling
22. Common mistakes in how survodutide is discussed
23. Survodutide vs tirzepatide, semaglutide, retatrutide and mazdutide
24. How it compares
25. Regulatory status: phase 3 complete in obesity, not yet approved
26. Open questions and limitations
27. Questions people ask
28. Sources
29. Reference card
30. Related records
31. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 21 (avg sentence 18.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.3 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 53/100: the remaining deductions (reviewer, author, Flesch, image, no absence statements) are `defer-reviewer` or `reject-policy` items and cannot move here.
- Accepted items landed: the estimand quotation is gone from the escalation section; twelve trial cards and the trial table render.
- Not looped: the exit run confirms the accepted items and nothing else.
