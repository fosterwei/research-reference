# eloralintide audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/eloralintide.json were written before the page.

## Part 1: audit


Built from `dist/blog/eloralintide/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 3 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 40 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 9 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/eloralintide`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 40, 'www.prnewswire.com': 16, 'www.novonordisk.com': 3, 'annualreport.novonordisk.com': 4}).

### Page facts

| | |
|---|---|
| Title (55) | Eloralintide (Eli Lilly): Trial Results vs Cagrilintide |
| Description (153) | Eloralintide is Eli Lilly's selective amylin agonist. See its phase 1 and 2 results, EloraTZP data, phase 3 status and how it compares with cagrilintide. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/eloralintide |
| H1 / H2 / H3 | ["Eloralintide: Eli Lilly's amylin drug, and how it compares with cagrilintide"] / 12 / 0 |
| Words (total / own prose / quoted) | 1913 / 1554 / 0 |
| Readability Flesch, grade, avg sentence: all | 4, 17.7, 20.5 |
| … own prose only | 12, 15.8, 17.0 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `eloralintide eli lilly` | 0× (0.00%); title False, H1 False, first 100 words True |
| Links | 9 internal (4.7/1k words); 63 external {'europepmc.org': 40, 'www.prnewswire.com': 16, 'www.novonordisk.com': 3, 'annualreport.novonordisk.com': 4}; new-tab 63/63 |
| Formatting | {'tables': 3, 'captions': 3, 'quotes_with_cite': 0, 'abbr': 0, 'time': 14, 'details': 5, 'images': 0, 'bold_own': 17} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-11-06', '2025-12-18', '2026-09-30', '2026-10-29'] |

### H2 sequence

1. At a glance
2. What eloralintide is: Lilly's selective amylin agonist
3. Eloralintide phase 1 results
4. Eloralintide phase 2 results: up to 20% weight loss in 48 weeks
5. Eloralintide with tirzepatide (EloraTZP)
6. Eloralintide development status, October 2026
7. Eloralintide vs cagrilintide
8. More in this topic
9. Questions people ask
10. Sources
11. Related records
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 12 (avg sentence 17.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Keyword `eloralintide eli lilly` counted 0× | `reject-policy` | Exact-phrase artifact: the H1 reads 'Eloralintide: Eli Lilly's amylin drug'. | none | — |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/eloralintide/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 3 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 40 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 9 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/eloralintide`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 40, 'www.prnewswire.com': 16, 'www.novonordisk.com': 3, 'annualreport.novonordisk.com': 4}).

### Page facts

| | |
|---|---|
| Title (55) | Eloralintide (Eli Lilly): Trial Results vs Cagrilintide |
| Description (153) | Eloralintide is Eli Lilly's selective amylin agonist. See its phase 1 and 2 results, EloraTZP data, phase 3 status and how it compares with cagrilintide. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/eloralintide |
| H1 / H2 / H3 | ["Eloralintide: Eli Lilly's amylin drug, and how it compares with cagrilintide"] / 12 / 0 |
| Words (total / own prose / quoted) | 1913 / 1554 / 0 |
| Readability Flesch, grade, avg sentence: all | 4, 17.7, 20.5 |
| … own prose only | 12, 15.8, 17.0 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `eloralintide eli lilly` | 0× (0.00%); title False, H1 False, first 100 words True |
| Links | 9 internal (4.7/1k words); 63 external {'europepmc.org': 40, 'www.prnewswire.com': 16, 'www.novonordisk.com': 3, 'annualreport.novonordisk.com': 4}; new-tab 63/63 |
| Formatting | {'tables': 3, 'captions': 3, 'quotes_with_cite': 0, 'abbr': 0, 'time': 14, 'details': 5, 'images': 0, 'bold_own': 17} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-11-06', '2025-12-18', '2026-09-30', '2026-10-29'] |

### H2 sequence

1. At a glance
2. What eloralintide is: Lilly's selective amylin agonist
3. Eloralintide phase 1 results
4. Eloralintide phase 2 results: up to 20% weight loss in 48 weeks
5. Eloralintide with tirzepatide (EloraTZP)
6. Eloralintide development status, October 2026
7. Eloralintide vs cagrilintide
8. More in this topic
9. Questions people ask
10. Sources
11. Related records
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 12 (avg sentence 17.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
