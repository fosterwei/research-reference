# prediabetes-medication audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/prediabetes-medication.json were written before the page.

## Part 1: audit


Built from `dist/blog/prediabetes-medication/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 63 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 13 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/prediabetes-medication`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 63, 'www.accessdata.fda.gov': 9, 'www.novonordisk-us.com': 2}).

### Page facts

| | |
|---|---|
| Title (55) | Prediabetes Medication: What the Prevention Trials Show |
| Description (145) | Which drugs delay diabetes in prediabetes: metformin, acarbose, pioglitazone, semaglutide and tirzepatide trial results, and the ADA 2026 advice. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/prediabetes-medication |
| H1 / H2 / H3 | ['Prediabetes medication: what the prevention trials showed'] / 11 / 0 |
| Words (total / own prose / quoted) | 2431 / 2006 / 0 |
| Readability Flesch, grade, avg sentence: all | 17, 16.0, 20.7 |
| … own prose only | 23, 14.6, 18.2 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `prediabetes medication` | 9× (0.37%); title True, H1 True, first 100 words True |
| Links | 13 internal (5.3/1k words); 74 external {'europepmc.org': 63, 'www.accessdata.fda.gov': 9, 'www.novonordisk-us.com': 2}; new-tab 74/74 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 18, 'details': 7, 'images': 0, 'bold_own': 17} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-10-29'] |

### H2 sequence

1. At a glance
2. Prediabetes medications tested in prevention trials
3. Metformin vs lifestyle change: the Diabetes Prevention Program
4. What the ADA 2026 Standards say about medicine for prediabetes
5. Is any medication FDA-approved for prediabetes?
6. Acarbose, pioglitazone and GLP-1 drugs: the trade-offs
7. What is the best medicine for prediabetes?
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 23 (avg sentence 18.2 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/prediabetes-medication/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 63 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 13 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/prediabetes-medication`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 63, 'www.accessdata.fda.gov': 9, 'www.novonordisk-us.com': 2}).

### Page facts

| | |
|---|---|
| Title (55) | Prediabetes Medication: What the Prevention Trials Show |
| Description (145) | Which drugs delay diabetes in prediabetes: metformin, acarbose, pioglitazone, semaglutide and tirzepatide trial results, and the ADA 2026 advice. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/prediabetes-medication |
| H1 / H2 / H3 | ['Prediabetes medication: what the prevention trials showed'] / 11 / 0 |
| Words (total / own prose / quoted) | 2431 / 2006 / 0 |
| Readability Flesch, grade, avg sentence: all | 17, 16.0, 20.7 |
| … own prose only | 23, 14.6, 18.2 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `prediabetes medication` | 9× (0.37%); title True, H1 True, first 100 words True |
| Links | 13 internal (5.3/1k words); 74 external {'europepmc.org': 63, 'www.accessdata.fda.gov': 9, 'www.novonordisk-us.com': 2}; new-tab 74/74 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 18, 'details': 7, 'images': 0, 'bold_own': 17} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-10-29'] |

### H2 sequence

1. At a glance
2. Prediabetes medications tested in prevention trials
3. Metformin vs lifestyle change: the Diabetes Prevention Program
4. What the ADA 2026 Standards say about medicine for prediabetes
5. Is any medication FDA-approved for prediabetes?
6. Acarbose, pioglitazone and GLP-1 drugs: the trade-offs
7. What is the best medicine for prediabetes?
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 23 (avg sentence 18.2 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
