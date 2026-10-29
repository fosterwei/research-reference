# type-2-diabetes-treatments audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/type-2-diabetes-treatments.json were written before the page.

## Part 1: audit


Built from `dist/blog/type-2-diabetes-treatments/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 30 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 11 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/type-2-diabetes-treatments`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 30, 'www.accessdata.fda.gov': 7}).

### Page facts

| | |
|---|---|
| Title (56) | Type 2 Diabetes Treatments: Steps in the 2026 Guidelines |
| Description (153) | How type 2 diabetes treatment is chosen in the 2026 ADA Standards: lifestyle, the first medicine, when GLP-1 injections and insulin start, and remission. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/type-2-diabetes-treatments |
| H1 / H2 / H3 | ['Type 2 diabetes treatments: how treatment is chosen, step by step, in current guidelines'] / 11 / 0 |
| Words (total / own prose / quoted) | 2249 / 1730 / 0 |
| Readability Flesch, grade, avg sentence: all | 20, 16.2, 23.0 |
| … own prose only | 24, 14.9, 19.9 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `type 2 diabetes treatments` | 2× (0.09%); title True, H1 True, first 100 words True |
| Links | 11 internal (4.9/1k words); 37 external {'europepmc.org': 30, 'www.accessdata.fda.gov': 7}; new-tab 37/37 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 14, 'details': 5, 'images': 0, 'bold_own': 15} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Diabetes mellitus type 2 treatment, step by step
3. Lifestyle treatment: food, activity and weight
4. How the first diabetes medicine is chosen
5. Type 2 diabetes injections: GLP-1 drugs, tirzepatide, insulin and amylin
6. Injectable insulin for type 2 diabetes: when it is used
7. Is there a cure for type 2 diabetes? What remission means
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 24 (avg sentence 19.9 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
4. No contextual link to another compound page in the body.

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No contextual link to a compound record | `accept-record` (done) | Semaglutide and tirzepatide link to their records. | record | writer |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/type-2-diabetes-treatments/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 30 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 13 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/type-2-diabetes-treatments`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 30, 'www.accessdata.fda.gov': 7}).

### Page facts

| | |
|---|---|
| Title (56) | Type 2 Diabetes Treatments: Steps in the 2026 Guidelines |
| Description (153) | How type 2 diabetes treatment is chosen in the 2026 ADA Standards: lifestyle, the first medicine, when GLP-1 injections and insulin start, and remission. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/type-2-diabetes-treatments |
| H1 / H2 / H3 | ['Type 2 diabetes treatments: how treatment is chosen, step by step, in current guidelines'] / 11 / 0 |
| Words (total / own prose / quoted) | 2249 / 1730 / 0 |
| Readability Flesch, grade, avg sentence: all | 20, 16.2, 23.0 |
| … own prose only | 24, 14.9, 19.9 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `type 2 diabetes treatments` | 2× (0.09%); title True, H1 True, first 100 words True |
| Links | 13 internal (5.8/1k words); 37 external {'europepmc.org': 30, 'www.accessdata.fda.gov': 7}; new-tab 37/37 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 14, 'details': 5, 'images': 0, 'bold_own': 15} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Diabetes mellitus type 2 treatment, step by step
3. Lifestyle treatment: food, activity and weight
4. How the first diabetes medicine is chosen
5. Type 2 diabetes injections: GLP-1 drugs, tirzepatide, insulin and amylin
6. Injectable insulin for type 2 diabetes: when it is used
7. Is there a cure for type 2 diabetes? What remission means
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 24 (avg sentence 19.9 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
