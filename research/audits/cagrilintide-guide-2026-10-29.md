# cagrilintide-guide audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/cagrilintide-guide.json were written before the page.

## Part 1: audit


Built from `dist/blog/cagrilintide-guide/index.html`.

### Content quality score: 43/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 5/25 | 9 primary-source links; reviewer absent; author named |
| Authoritativeness | 12/25 | publisher set in JSON-LD; /about exists; 24 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrilintide-guide`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 55/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 9}).

### Page facts

| | |
|---|---|
| Title (57) | Cagrilintide Guide: Every Topic, From Dosing to CagriSema |
| Description (158) | Every cagrilintide guide in one index: how it works, side effects, the trial doses, CagriSema, new weight-loss drugs and the diabetes medicines it would join. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrilintide-guide |
| H1 / H2 / H3 | ['Cagrilintide guide: how it works, the trial doses, CagriSema, and the diabetes medicines around it'] / 6 / 5 |
| Words (total / own prose / quoted) | 1571 / 1392 / 0 |
| Readability Flesch, grade, avg sentence: all | 24, 15.9, 24.1 |
| … own prose only | 26, 15.1, 21.9 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrilintide guide` | 2× (0.13%); title True, H1 True, first 100 words True |
| Links | 24 internal (15.3/1k words); 9 external {'europepmc.org': 9}; new-tab 9/9 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 7, 'details': 1, 'images': 0, 'bold_own': 14} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Every topic in this guide
3. How this guide is organised
4. Sources
5. Related records
6. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 26 (avg sentence 21.9 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Index page carries no measured query | `reject-policy` | Hub by design: every keyword in the map is routed to exactly one destination (research/plans/cagrilintide-guide-keyword-map.csv). | none | — |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/cagrilintide-guide/index.html`.

### Content quality score: 43/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 5/25 | 9 primary-source links; reviewer absent; author named |
| Authoritativeness | 12/25 | publisher set in JSON-LD; /about exists; 24 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrilintide-guide`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 55/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 9}).

### Page facts

| | |
|---|---|
| Title (57) | Cagrilintide Guide: Every Topic, From Dosing to CagriSema |
| Description (158) | Every cagrilintide guide in one index: how it works, side effects, the trial doses, CagriSema, new weight-loss drugs and the diabetes medicines it would join. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrilintide-guide |
| H1 / H2 / H3 | ['Cagrilintide guide: how it works, the trial doses, CagriSema, and the diabetes medicines around it'] / 6 / 5 |
| Words (total / own prose / quoted) | 1574 / 1395 / 0 |
| Readability Flesch, grade, avg sentence: all | 24, 15.9, 24.1 |
| … own prose only | 26, 15.1, 22.0 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrilintide guide` | 2× (0.13%); title True, H1 True, first 100 words True |
| Links | 24 internal (15.2/1k words); 9 external {'europepmc.org': 9}; new-tab 9/9 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 7, 'details': 1, 'images': 0, 'bold_own': 14} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Every topic in this guide
3. How this guide is organised
4. Sources
5. Related records
6. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 26 (avg sentence 22.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
