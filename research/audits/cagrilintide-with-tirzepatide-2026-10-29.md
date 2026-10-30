# cagrilintide-with-tirzepatide audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/cagrilintide-with-tirzepatide.json were written before the page.

## Part 1: audit


Built from `dist/blog/cagrilintide-with-tirzepatide/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 4 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 25 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 11 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrilintide-with-tirzepatide`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.novonordisk.com': 19, 'europepmc.org': 25, 'www.eurekalert.org': 7, 'www.accessdata.fda.gov': 5, 'www.fda.gov': 2}).

### Page facts

| | |
|---|---|
| Title (58) | Cagrilintide With Tirzepatide: Dosage, Trials and Evidence |
| Description (154) | No trial has tested cagrilintide with tirzepatide. Each drug's own doses, the CagriSema vs tirzepatide head-to-head results, and why blends are unstudied. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrilintide-with-tirzepatide |
| H1 / H2 / H3 | ['Cagrilintide with tirzepatide: what has and has not been tested'] / 11 / 0 |
| Words (total / own prose / quoted) | 2209 / 1691 / 0 |
| Readability Flesch, grade, avg sentence: all | 6, 18.2, 23.6 |
| … own prose only | 13, 16.2, 19.0 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrilintide dosage with tirzepatide` | 1× (0.05%); title False, H1 False, first 100 words False |
| Links | 11 internal (5.0/1k words); 58 external {'www.novonordisk.com': 19, 'europepmc.org': 25, 'www.eurekalert.org': 7, 'www.accessdata.fda.gov': 5, 'www.fda.gov': 2}; new-tab 58/58 |
| Formatting | {'tables': 4, 'captions': 4, 'quotes_with_cite': 0, 'abbr': 0, 'time': 19, 'details': 6, 'images': 0, 'bold_own': 13} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-02-23', '2026-09-21', '2026-09-30', '2026-10-29'] |

### H2 sequence

1. At a glance
2. Has cagrilintide been tested with tirzepatide?
3. Cagrilintide and tirzepatide doses, each drug on its own
4. Why two appetite-suppressing drugs together are a separate question
5. Cagrilintide vs tirzepatide: what the head-to-head trials measured
6. Cagrilintide and tirzepatide blends
7. More in this topic
8. Questions people ask
9. Sources
10. Related records
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 13 (avg sentence 19.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Primary query `cagrilintide dosage with tirzepatide` (1,300/mo) absent from the H1 | `accept-record` (done) | H1 now leads with it; the opening sentence already answered it with the boundary (no combined dose exists). | record | writer |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/cagrilintide-with-tirzepatide/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 4 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 25 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 11 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrilintide-with-tirzepatide`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.novonordisk.com': 19, 'europepmc.org': 25, 'www.eurekalert.org': 7, 'www.accessdata.fda.gov': 5, 'www.fda.gov': 2}).

### Page facts

| | |
|---|---|
| Title (58) | Cagrilintide With Tirzepatide: Dosage, Trials and Evidence |
| Description (154) | No trial has tested cagrilintide with tirzepatide. Each drug's own doses, the CagriSema vs tirzepatide head-to-head results, and why blends are unstudied. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrilintide-with-tirzepatide |
| H1 / H2 / H3 | ['Cagrilintide dosage with tirzepatide: what has and has not been tested'] / 11 / 0 |
| Words (total / own prose / quoted) | 2210 / 1691 / 0 |
| Readability Flesch, grade, avg sentence: all | 6, 18.2, 23.6 |
| … own prose only | 13, 16.2, 19.0 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrilintide dosage with tirzepatide` | 2× (0.09%); title False, H1 True, first 100 words True |
| Links | 11 internal (5.0/1k words); 58 external {'www.novonordisk.com': 19, 'europepmc.org': 25, 'www.eurekalert.org': 7, 'www.accessdata.fda.gov': 5, 'www.fda.gov': 2}; new-tab 58/58 |
| Formatting | {'tables': 4, 'captions': 4, 'quotes_with_cite': 0, 'abbr': 0, 'time': 19, 'details': 6, 'images': 0, 'bold_own': 13} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-02-23', '2026-09-21', '2026-09-30', '2026-10-29'] |

### H2 sequence

1. At a glance
2. Has cagrilintide been tested with tirzepatide?
3. Cagrilintide and tirzepatide doses, each drug on its own
4. Why two appetite-suppressing drugs together are a separate question
5. Cagrilintide vs tirzepatide: what the head-to-head trials measured
6. Cagrilintide and tirzepatide blends
7. More in this topic
8. Questions people ask
9. Sources
10. Related records
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 13 (avg sentence 19.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
