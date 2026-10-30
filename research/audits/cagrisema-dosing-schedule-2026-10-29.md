# cagrisema-dosing-schedule audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/cagrisema-dosing-schedule.json were written before the page.

## Part 1: audit


Built from `dist/blog/cagrisema-dosing-schedule/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 29 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 10 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrisema-dosing-schedule`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 29, 'www.novonordisk-us.com': 5, 'www.accessdata.fda.gov': 3, 'www.novonordisk.com': 9}).

### Page facts

| | |
|---|---|
| Title (56) | CagriSema Dosage: The Trial Dosing Schedule Step by Step |
| Description (149) | CagriSema dosage in trials: 0.25/0.25 mg rising every 4 weeks to 2.4/2.4 mg, the flexible protocol, how many reached it, and why no dose is approved. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrisema-dosing-schedule |
| H1 / H2 / H3 | ['CagriSema dosing schedule: the trial titration step by step'] / 12 / 0 |
| Words (total / own prose / quoted) | 2027 / 1750 / 0 |
| Readability Flesch, grade, avg sentence: all | 21, 15.7, 21.7 |
| … own prose only | 23, 14.7, 18.7 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrisema dosage` | 2× (0.10%); title True, H1 False, first 100 words False |
| Links | 10 internal (4.9/1k words); 46 external {'europepmc.org': 29, 'www.novonordisk-us.com': 5, 'www.accessdata.fda.gov': 3, 'www.novonordisk.com': 9}; new-tab 46/46 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 16, 'details': 6, 'images': 0, 'bold_own': 15} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2024-12-20', '2025-12-18', '2026-02-23', '2026-10-29'] |

### H2 sequence

1. At a glance
2. The CagriSema dosing chart used in the trials
3. Maintenance: 2.4 mg of each, once a week
4. The flexible protocol, and the dose people actually reached
5. The lower 1.0/1.0 mg dose in the diabetes trials
6. One injection, two drugs: the co-formulation and its pen
7. Why no CagriSema dose is approved yet
8. More in this topic
9. Questions people ask
10. Sources
11. Related records
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 23 (avg sentence 18.7 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Primary query `cagrisema dosage` absent from the H1 | `accept-record` (done) | H1 now reads 'CagriSema dosage and dosing schedule'. | record | writer |
| Monthly titration ladder attributed to 'the trials' | `accept-record` (done) | Only the phase 2 paper prints the 0.25 → 0.5 → 1.0 → 1.7 → 2.4 mg ladder; phase 3 is cited only for escalating to 2.4 mg. | record | writer |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/cagrisema-dosing-schedule/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 29 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 10 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrisema-dosing-schedule`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 29, 'www.novonordisk-us.com': 5, 'www.accessdata.fda.gov': 3, 'www.novonordisk.com': 9}).

### Page facts

| | |
|---|---|
| Title (56) | CagriSema Dosage: The Trial Dosing Schedule Step by Step |
| Description (149) | CagriSema dosage in trials: 0.25/0.25 mg rising every 4 weeks to 2.4/2.4 mg, the flexible protocol, how many reached it, and why no dose is approved. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrisema-dosing-schedule |
| H1 / H2 / H3 | ['CagriSema dosage and dosing schedule: the trial titration step by step'] / 12 / 0 |
| Words (total / own prose / quoted) | 2029 / 1750 / 0 |
| Readability Flesch, grade, avg sentence: all | 21, 15.7, 21.7 |
| … own prose only | 23, 14.7, 18.7 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrisema dosage` | 3× (0.15%); title True, H1 True, first 100 words True |
| Links | 10 internal (4.9/1k words); 46 external {'europepmc.org': 29, 'www.novonordisk-us.com': 5, 'www.accessdata.fda.gov': 3, 'www.novonordisk.com': 9}; new-tab 46/46 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 16, 'details': 6, 'images': 0, 'bold_own': 15} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2024-12-20', '2025-12-18', '2026-02-23', '2026-10-29'] |

### H2 sequence

1. At a glance
2. The CagriSema dosing chart used in the trials
3. Maintenance: 2.4 mg of each, once a week
4. The flexible protocol, and the dose people actually reached
5. The lower 1.0/1.0 mg dose in the diabetes trials
6. One injection, two drugs: the co-formulation and its pen
7. Why no CagriSema dose is approved yet
8. More in this topic
9. Questions people ask
10. Sources
11. Related records
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 23 (avg sentence 18.7 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
