# Tesofensine audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: 43d31ae (page/tesofensine, pre-merge build). Eighth page written end to end under the sequencing rule: stages 1–5 in research/intents/tesofensine.json before any guide text.

## Part 1: audit

Built from `dist/compounds/tesofensine/index.html`.

### Content quality score: 55/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 5 data tables, 19 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 23 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 10 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/tesofensine`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 23}).

### Page facts

| | |
|---|---|
| Title (54) | Tesofensine: Trials, 0.5 mg Dose, Side Effects, Status |
| Description (151) | Tesofensine: the 2008 obesity trial, the failed Parkinson's trials, every dose, heart-rate and side-effect data, and where the Mexican approval stands. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/tesofensine |
| H1 / H2 / H3 | ["Tesofensine: what the obesity and Parkinson's trials found, why it is not a peptide, and where the Mexican approval stands"] / 30 / 3 |
| Words (total / own prose / quoted) | 7730 / 5164 / 558 |
| Readability Flesch, grade, avg sentence: all | 14, 17.0, 22.5 |
| … own prose only | 23, 14.3, 17.5 |
| … quotations only | -5, 20.5, 26.6 |
| Keyword `tesofensine` | 115× (1.49%); title True, H1 True, first 100 words True |
| Links | 10 internal (1.3/1k words); 23 external {'europepmc.org': 23}; new-tab 23/23 |
| Formatting | {'tables': 5, 'captions': 5, 'quotes_with_cite': 19, 'abbr': 1, 'time': 33, 'details': 18, 'images': 0, 'bold_own': 31} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What tesofensine is, and why it is not a peptide
3. What the evidence level means
4. Tesofensine in two minutes
5. How tesofensine works: three transporters, one appetite circuit
6. Trial by trial: what tesofensine did, and where it failed
7. What the evidence shows
8. Doses reported in studies
9. Every tesofensine dose in the trials, in one table
10. Side effects: what the trials recorded, with frequencies
11. Who tesofensine is discussed for, and the cautions that recur
12. Biomarkers measured in studies
13. Reported interactions
14. Reported timelines
15. What is measured over time, and what is not
16. Study durations
17. Routes: oral tablets in every efficacy trial
18. Weight-normalized doses, as published
19. What people report outside the literature
20. Storage and handling
21. Common mistakes in how tesofensine is discussed
22. Tesofensine vs semaglutide, tirzepatide, phentermine and sibutramine
23. How it compares
24. Regulatory status: not approved anywhere; the Mexican application
25. Open questions and limitations
26. Questions people ask
27. Sources
28. Reference card
29. Related records
30. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 23 (avg sentence 17.5 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.3 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| Own-prose Flesch 23 | `reject-policy` | design.md §9.7 budgets sentence length (17.5 words, met); terminology (noradrenaline, pharmacokinetic, hypothalamic) drives syllables. Precedent: all prior audits. | none | — |
| Internal links 1.3/1k | `accept-template` (partial) | Guide prose links semaglutide, tirzepatide, AOD-9604, SLU-PP-332 and the directories (10 unique); a 7,700-word page with 23 source links dilutes the ratio by design; automatic entity linking remains the open template item. | template | engineer, open |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| "Study durations" quoted a review's '12 months' that referred to other drugs' phase 3 trials; found on reading the build | `accept-record` (done) + `accept-script` (open) | Claim removed; the duration regex is an open script item (DSIP precedent). | record, script | writer done; engineer open |
| Drafter's interactions regex matched covariate modelling ('CL(CR) and sex') | `accept-record` (done) + `accept-script` (open) | Claim removed; levodopa and itraconazole co-administration claims kept as genuine interactions. Same regex item. | record, script | writer done; engineer open |
| Thirteen human rows exceed the HumanTrials cap of 12 | `accept-record` (done) | The guide's trial table carries every human study with dose, endpoint and result. Precedent: SS-31, DSIP, kisspeptin. | record | writer |
| Phase 3 results, COFEPRIS timeline and the Lancet heart-rate figures cited without ledger sources | `accept-record` (boundary, done) | Editorial claims marked pending_source and attributed to the developer's filings or the full text; open_actions name the documents. A ranking page's contrary approval claim is recorded in the competitor notes. | record | writer |
| 'tesofensine buy' and 'tesofensine cost' (100 clickstream together) | `reject-policy` | Commercial intent, out of scope per docs/content-sop.md; declined in the map. | none | — |

## Part 3: exit audit

Built from `dist/compounds/tesofensine/index.html`.

### Content quality score: 55/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 5 data tables, 18 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 23 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 10 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/tesofensine`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 23}).

### Page facts

| | |
|---|---|
| Title (54) | Tesofensine: Trials, 0.5 mg Dose, Side Effects, Status |
| Description (151) | Tesofensine: the 2008 obesity trial, the failed Parkinson's trials, every dose, heart-rate and side-effect data, and where the Mexican approval stands. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/tesofensine |
| H1 / H2 / H3 | ["Tesofensine: what the obesity and Parkinson's trials found, why it is not a peptide, and where the Mexican approval stands"] / 30 / 3 |
| Words (total / own prose / quoted) | 7704 / 5160 / 533 |
| Readability Flesch, grade, avg sentence: all | 14, 16.9, 22.4 |
| … own prose only | 24, 14.3, 17.4 |
| … quotations only | -4, 20.5, 26.9 |
| Keyword `tesofensine` | 115× (1.49%); title True, H1 True, first 100 words True |
| Links | 10 internal (1.3/1k words); 23 external {'europepmc.org': 23}; new-tab 23/23 |
| Formatting | {'tables': 5, 'captions': 5, 'quotes_with_cite': 18, 'abbr': 1, 'time': 33, 'details': 18, 'images': 0, 'bold_own': 31} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What tesofensine is, and why it is not a peptide
3. What the evidence level means
4. Tesofensine in two minutes
5. How tesofensine works: three transporters, one appetite circuit
6. Trial by trial: what tesofensine did, and where it failed
7. What the evidence shows
8. Doses reported in studies
9. Every tesofensine dose in the trials, in one table
10. Side effects: what the trials recorded, with frequencies
11. Who tesofensine is discussed for, and the cautions that recur
12. Biomarkers measured in studies
13. Reported interactions
14. Reported timelines
15. What is measured over time, and what is not
16. Study durations
17. Routes: oral tablets in every efficacy trial
18. Weight-normalized doses, as published
19. What people report outside the literature
20. Storage and handling
21. Common mistakes in how tesofensine is discussed
22. Tesofensine vs semaglutide, tirzepatide, phentermine and sibutramine
23. How it compares
24. Regulatory status: not approved anywhere; the Mexican application
25. Open questions and limitations
26. Questions people ask
27. Sources
28. Reference card
29. Related records
30. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 24 (avg sentence 17.4 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.3 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 55/100: the remaining deductions (reviewer, author, Flesch, image) are `defer-reviewer` or `reject-policy` items and cannot move here.
- Accepted items landed: the misdrafted duration claim is gone from the build; the trial table, dose table and frequency claims render.
- Not looped: the exit run confirms the accepted items and nothing else.
