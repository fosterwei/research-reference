# metformin-vs-insulin audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/metformin-vs-insulin.json were written before the page.

## Part 1: audit


Built from `dist/blog/metformin-vs-insulin/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 42 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 12 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/metformin-vs-insulin`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 42, 'www.accessdata.fda.gov': 11, 'www.novonordisk-us.com': 2}).

### Page facts

| | |
|---|---|
| Title (57) | Metformin vs Insulin: A1C Effect, Safety and Side Effects |
| Description (140) | How much metformin lowers A1C, how insulin differs, which causes more low blood sugar and weight gain, and when ADA 2026 guidance uses each. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/metformin-vs-insulin |
| H1 / H2 / H3 | ['Metformin vs insulin: how much each lowers A1C, and how they differ'] / 11 / 0 |
| Words (total / own prose / quoted) | 2200 / 1845 / 0 |
| Readability Flesch, grade, avg sentence: all | 26, 14.9, 21.0 |
| … own prose only | 27, 14.1, 18.8 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `does metformin lower a1c` | 4× (0.18%); title False, H1 False, first 100 words True |
| Links | 12 internal (5.5/1k words); 55 external {'europepmc.org': 42, 'www.accessdata.fda.gov': 11, 'www.novonordisk-us.com': 2}; new-tab 55/55 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 13, 'details': 6, 'images': 0, 'bold_own': 12} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-10-29'] |

### H2 sequence

1. At a glance
2. How much does metformin lower A1C?
3. How metformin and insulin work differently
4. Insulin vs metformin side by side
5. Which is safer, insulin or metformin?
6. When each is used: the ADA 2026 approach
7. Other medicines trialled alongside insulin
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 27 (avg sentence 18.8 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Keyword `does metformin lower a1c` absent from title | `reject-policy` | Question-form query answered in the opening and in its own section; the title carries the higher-intent comparison. | none | — |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/metformin-vs-insulin/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 42 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 12 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/metformin-vs-insulin`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 42, 'www.accessdata.fda.gov': 11, 'www.novonordisk-us.com': 2}).

### Page facts

| | |
|---|---|
| Title (57) | Metformin vs Insulin: A1C Effect, Safety and Side Effects |
| Description (140) | How much metformin lowers A1C, how insulin differs, which causes more low blood sugar and weight gain, and when ADA 2026 guidance uses each. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/metformin-vs-insulin |
| H1 / H2 / H3 | ['Metformin vs insulin: how much each lowers A1C, and how they differ'] / 11 / 0 |
| Words (total / own prose / quoted) | 2200 / 1845 / 0 |
| Readability Flesch, grade, avg sentence: all | 26, 14.9, 21.0 |
| … own prose only | 27, 14.1, 18.8 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `does metformin lower a1c` | 4× (0.18%); title False, H1 False, first 100 words True |
| Links | 12 internal (5.5/1k words); 55 external {'europepmc.org': 42, 'www.accessdata.fda.gov': 11, 'www.novonordisk-us.com': 2}; new-tab 55/55 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 13, 'details': 6, 'images': 0, 'bold_own': 12} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-10-29'] |

### H2 sequence

1. At a glance
2. How much does metformin lower A1C?
3. How metformin and insulin work differently
4. Insulin vs metformin side by side
5. Which is safer, insulin or metformin?
6. When each is used: the ADA 2026 approach
7. Other medicines trialled alongside insulin
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 27 (avg sentence 18.8 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
