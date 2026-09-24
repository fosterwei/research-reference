# Kisspeptin audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: 7bdfc69 (page/kisspeptin, pre-merge build). Seventh page written end to end under the sequencing rule: stages 1–5 in research/intents/kisspeptin.json before any guide text.

## Part 1: audit

Built from `dist/compounds/kisspeptin/index.html`.

### Content quality score: 55/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 5 data tables, 22 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 30 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 8 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/kisspeptin`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 30}).

### Page facts

| | |
|---|---|
| Title (54) | Kisspeptin (KP-10, KP-54): Trials, Doses, Side Effects |
| Description (160) | Kisspeptin peptide: every human trial with isoform, dose and duration, the desensitisation problem, what the testosterone and libido uses rest on, side effects. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/kisspeptin |
| H1 / H2 / H3 | ['Kisspeptin (KP-10, KP-54) peptide: what the human trials measured, the desensitisation problem, and what the testosterone and libido uses rest on'] / 31 / 3 |
| Words (total / own prose / quoted) | 8857 / 5821 / 691 |
| Readability Flesch, grade, avg sentence: all | 13, 17.5, 24.4 |
| … own prose only | 23, 14.7, 19.0 |
| … quotations only | -2, 20.0, 25.8 |
| Keyword `kisspeptin` | 216× (2.44%); title True, H1 True, first 100 words True |
| Links | 8 internal (0.9/1k words); 30 external {'europepmc.org': 30}; new-tab 30/30 |
| Formatting | {'tables': 5, 'captions': 5, 'quotes_with_cite': 22, 'abbr': 0, 'time': 38, 'details': 20, 'images': 0, 'bold_own': 28} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What kisspeptin is, and what KP-10 and KP-54 mean
3. What the evidence level means
4. Kisspeptin in two minutes
5. How kisspeptin works: the switch above GnRH
6. Trial by trial: what kisspeptin did in people
7. What the evidence shows
8. Doses reported in studies
9. Every kisspeptin dose in the trials, in one table
10. Side effects: what the trials recorded, and the desensitisation problem
11. Who kisspeptin is discussed for, and the cautions that recur
12. Biomarkers measured in studies
13. Reported interactions
14. Reported timelines
15. What is measured over time, and what is not
16. Escalation schedules used in studies
17. Study durations
18. Routes: what the trials used
19. Weight-normalized doses, as published
20. What people report outside the literature
21. Storage and handling
22. Common mistakes in how kisspeptin is discussed
23. Kisspeptin vs hCG, clomiphene, GnRH, PT-141 and the kisspeptin-pathway drugs
24. How it compares
25. Regulatory status: not approved; the approved drugs act on its pathway
26. Open questions and limitations
27. Questions people ask
28. Sources
29. Reference card
30. Related records
31. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 23 (avg sentence 19.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 0.9 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| Own-prose Flesch 23 (avg sentence 19.0) | `reject-policy` | design.md §9.7 budgets sentence length (met, near the ceiling); terminology (gonadotropin, desensitisation, hypothalamic amenorrhoea) drives syllables. Precedent: all prior audits. | none | — |
| Internal links 0.9/1k | `accept-template` (partial) + `accept-record` | Two directory links added beside PT-141 and IGF-1 LR3; an 8,900-word page with 30 source links dilutes the ratio by design; automatic entity linking remains the open template item. | record, template | writer done; engineer open |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| "Escalation schedules" section quoted 'escalating clinical interest' as a dose-escalation design; found on reading the build | `accept-record` (done) + `accept-script` (open) | Claim removed; the escalation regex joins the dose, duration and interactions regexes as open script items. | record, script | writer done; engineer open |
| Drafter missed every nmol/kg dose in the abstracts | `accept-record` (done) + `accept-script` (open) | Nine dose claims, two weight-normalized and four timeline claims written by hand from the abstracts. | record, script | writer done; engineer open |
| Twenty human rows exceed the HumanTrials cap of 12; five of them are studies that measured kisspeptin or tested fezolinetant rather than administering kisspeptin | `accept-record` (done) + `accept-script` (open) | The guide's trial table labels those rows 'measured only'; the drafter should separate administered from measured. Precedent for the table: SS-31, DSIP. | record, script | writer done; engineer open |
| Dhillo 2005, George 2011 and Jayasena 2009 cited without ledger sources | `accept-record` (boundary, done) | Named in the guide as not yet in the ledger; open_actions list them. | record | writer |

## Part 3: exit audit

Built from `dist/compounds/kisspeptin/index.html`.

### Content quality score: 55/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 5 data tables, 21 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 30 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 8 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/kisspeptin`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 30}).

### Page facts

| | |
|---|---|
| Title (54) | Kisspeptin (KP-10, KP-54): Trials, Doses, Side Effects |
| Description (160) | Kisspeptin peptide: every human trial with isoform, dose and duration, the desensitisation problem, what the testosterone and libido uses rest on, side effects. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/kisspeptin |
| H1 / H2 / H3 | ['Kisspeptin (KP-10, KP-54) peptide: what the human trials measured, the desensitisation problem, and what the testosterone and libido uses rest on'] / 30 / 3 |
| Words (total / own prose / quoted) | 8826 / 5828 / 666 |
| Readability Flesch, grade, avg sentence: all | 13, 17.4, 24.4 |
| … own prose only | 23, 14.7, 19.0 |
| … quotations only | -1, 19.8, 25.8 |
| Keyword `kisspeptin` | 215× (2.44%); title True, H1 True, first 100 words True |
| Links | 8 internal (0.9/1k words); 30 external {'europepmc.org': 30}; new-tab 30/30 |
| Formatting | {'tables': 5, 'captions': 5, 'quotes_with_cite': 21, 'abbr': 0, 'time': 38, 'details': 20, 'images': 0, 'bold_own': 28} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What kisspeptin is, and what KP-10 and KP-54 mean
3. What the evidence level means
4. Kisspeptin in two minutes
5. How kisspeptin works: the switch above GnRH
6. Trial by trial: what kisspeptin did in people
7. What the evidence shows
8. Doses reported in studies
9. Every kisspeptin dose in the trials, in one table
10. Side effects: what the trials recorded, and the desensitisation problem
11. Who kisspeptin is discussed for, and the cautions that recur
12. Biomarkers measured in studies
13. Reported interactions
14. Reported timelines
15. What is measured over time, and what is not
16. Study durations
17. Routes: what the trials used
18. Weight-normalized doses, as published
19. What people report outside the literature
20. Storage and handling
21. Common mistakes in how kisspeptin is discussed
22. Kisspeptin vs hCG, clomiphene, GnRH, PT-141 and the kisspeptin-pathway drugs
23. How it compares
24. Regulatory status: not approved; the approved drugs act on its pathway
25. Open questions and limitations
26. Questions people ask
27. Sources
28. Reference card
29. Related records
30. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 23 (avg sentence 19.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 0.9 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 55/100: the remaining deductions (reviewer, author, Flesch, image) are `defer-reviewer` or `reject-policy` items and cannot move here.
- Accepted items landed: the escalation section is gone from the build; the two directory links are present; hand-written dose and timeline claims render in their sections.
- Not looped: the exit run confirms the accepted items and nothing else.
