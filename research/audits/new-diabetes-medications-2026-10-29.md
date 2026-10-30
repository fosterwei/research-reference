# new-diabetes-medications audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/new-diabetes-medications.json were written before the page.

## Part 1: audit


Built from `dist/blog/new-diabetes-medications/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 28 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 15 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/new-diabetes-medications`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.novonordisk-us.com': 9, 'www.prnewswire.com': 21, 'www.pharmacytimes.com': 5, 'investor.lilly.com': 12, 'europepmc.org': 28, 'diabetesonthenet.com': 3, 'www.novonordisk.com': 2}).

### Page facts

| | |
|---|---|
| Title (58) | New Diabetes Medications: 2026 Approvals and What's Coming |
| Description (136) | The new type 2 diabetes medications approved in 2026, the late-stage drugs behind them, and what guidelines now put alongside metformin. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/new-diabetes-medications |
| H1 / H2 / H3 | ['New diabetes medications: what has been approved recently, and what is coming'] / 11 / 2 |
| Words (total / own prose / quoted) | 2852 / 2463 / 0 |
| Readability Flesch, grade, avg sentence: all | 17, 16.5, 22.9 |
| … own prose only | 21, 15.6, 21.0 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `new diabetes medications` | 5× (0.18%); title True, H1 True, first 100 words True |
| Links | 15 internal (5.3/1k words); 80 external {'www.novonordisk-us.com': 9, 'www.prnewswire.com': 21, 'www.pharmacytimes.com': 5, 'investor.lilly.com': 12, 'europepmc.org': 28, 'diabetesonthenet.com': 3, 'www.novonordisk.com': 2}; new-tab 80/80 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 23, 'details': 7, 'images': 0, 'bold_own': 24} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. New diabetes medications approved in 2026
3. Is there a new pill for type 2 diabetes?
4. What is the new drug replacing metformin?
5. Medicines similar to metformin
6. Once-weekly insulins: Awiqli and Onswik
7. Late-stage diabetes drugs: what is coming
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 21 (avg sentence 21.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
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


Built from `dist/blog/new-diabetes-medications/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 28 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 15 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/new-diabetes-medications`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.novonordisk-us.com': 9, 'www.prnewswire.com': 21, 'www.pharmacytimes.com': 5, 'investor.lilly.com': 12, 'europepmc.org': 28, 'diabetesonthenet.com': 3, 'www.novonordisk.com': 2}).

### Page facts

| | |
|---|---|
| Title (58) | New Diabetes Medications: 2026 Approvals and What's Coming |
| Description (136) | The new type 2 diabetes medications approved in 2026, the late-stage drugs behind them, and what guidelines now put alongside metformin. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/new-diabetes-medications |
| H1 / H2 / H3 | ['New diabetes medications: what has been approved recently, and what is coming'] / 11 / 2 |
| Words (total / own prose / quoted) | 2852 / 2463 / 0 |
| Readability Flesch, grade, avg sentence: all | 17, 16.5, 22.9 |
| … own prose only | 21, 15.6, 21.0 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `new diabetes medications` | 5× (0.18%); title True, H1 True, first 100 words True |
| Links | 15 internal (5.3/1k words); 80 external {'www.novonordisk-us.com': 9, 'www.prnewswire.com': 21, 'www.pharmacytimes.com': 5, 'investor.lilly.com': 12, 'europepmc.org': 28, 'diabetesonthenet.com': 3, 'www.novonordisk.com': 2}; new-tab 80/80 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 23, 'details': 7, 'images': 0, 'bold_own': 24} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. New diabetes medications approved in 2026
3. Is there a new pill for type 2 diabetes?
4. What is the new drug replacing metformin?
5. Medicines similar to metformin
6. Once-weekly insulins: Awiqli and Onswik
7. Late-stage diabetes drugs: what is coming
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 21 (avg sentence 21.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
