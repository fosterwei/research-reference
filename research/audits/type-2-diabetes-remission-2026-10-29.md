# type-2-diabetes-remission audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/type-2-diabetes-remission.json were written before the page.

## Part 1: audit


Built from `dist/blog/type-2-diabetes-remission/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 68 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 15 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/type-2-diabetes-remission`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 68}).

### Page facts

| | |
|---|---|
| Title (55) | How to Cure Diabetes? What Type 2 Remission Trials Show |
| Description (154) | Type 2 diabetes has no proven cure, but trials show remission: HbA1c under 6.5% off drugs. See the rates from DiRECT, DIADEM-I, surgery and GLP-1 studies. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/type-2-diabetes-remission |
| H1 / H2 / H3 | ['Can type 2 diabetes be cured? What remission trials show'] / 11 / 0 |
| Words (total / own prose / quoted) | 2795 / 2505 / 0 |
| Readability Flesch, grade, avg sentence: all | 24, 15.2, 21.2 |
| … own prose only | 26, 14.5, 19.7 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `how to cure diabetes` | 0× (0.00%); title True, H1 False, first 100 words False |
| Links | 15 internal (5.4/1k words); 68 external {'europepmc.org': 68}; new-tab 68/68 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 20, 'details': 7, 'images': 0, 'bold_own': 19} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Why remission, not cure, is the right word
3. Low-calorie diet trials: DiRECT and DIADEM-I
4. Remission rates across the main trials
5. Metabolic surgery and long-term remission
6. Do GLP-1 and amylin drugs put diabetes into remission?
7. Alternative treatments for type 2 diabetes: what the evidence covers
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 26 (avg sentence 19.7 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Primary query `how to cure diabetes` absent from the opening | `accept-record` (done) | Opening now names the query and answers it: no cure, remission is the evidence term. | record | writer |
| H1 does not repeat 'how to cure diabetes' | `reject-policy` | The SEO title carries the query; the H1 states what the evidence supports. A YMYL heading promising a cure would misinform. | none | — |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/type-2-diabetes-remission/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 68 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 15 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/type-2-diabetes-remission`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 68}).

### Page facts

| | |
|---|---|
| Title (55) | How to Cure Diabetes? What Type 2 Remission Trials Show |
| Description (154) | Type 2 diabetes has no proven cure, but trials show remission: HbA1c under 6.5% off drugs. See the rates from DiRECT, DIADEM-I, surgery and GLP-1 studies. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/type-2-diabetes-remission |
| H1 / H2 / H3 | ['Can type 2 diabetes be cured? What remission trials show'] / 11 / 0 |
| Words (total / own prose / quoted) | 2805 / 2515 / 0 |
| Readability Flesch, grade, avg sentence: all | 24, 15.1, 21.1 |
| … own prose only | 27, 14.4, 19.6 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `how to cure diabetes` | 1× (0.04%); title True, H1 False, first 100 words False |
| Links | 15 internal (5.3/1k words); 68 external {'europepmc.org': 68}; new-tab 68/68 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 20, 'details': 7, 'images': 0, 'bold_own': 19} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Why remission, not cure, is the right word
3. Low-calorie diet trials: DiRECT and DIADEM-I
4. Remission rates across the main trials
5. Metabolic surgery and long-term remission
6. Do GLP-1 and amylin drugs put diabetes into remission?
7. Alternative treatments for type 2 diabetes: what the evidence covers
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 27 (avg sentence 19.6 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
