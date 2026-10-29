# amylin-analogs audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/amylin-analogs.json were written before the page.

## Part 1: audit


Built from `dist/blog/amylin-analogs/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 45 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 8 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/amylin-analogs`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'dailymed.nlm.nih.gov': 10, 'europepmc.org': 45, 'www.novonordisk.com': 15, 'investor.lilly.com': 2, 'www.eurekalert.org': 3}).

### Page facts

| | |
|---|---|
| Title (55) | Amylin Analogs: Pramlintide, Cagrilintide and New Drugs |
| Description (160) | What amylin analogs do, how pramlintide works and what its label says, and the amylin drugs in development: cagrilintide, eloralintide, petrelintide, amycretin. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/amylin-analogs |
| H1 / H2 / H3 | ['Amylin analogs: pramlintide, cagrilintide and the amylin drugs in development'] / 12 / 0 |
| Words (total / own prose / quoted) | 2500 / 1988 / 0 |
| Readability Flesch, grade, avg sentence: all | 6, 18.6, 25.2 |
| … own prose only | 13, 16.5, 19.9 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `amylin drug` | 13× (0.52%); title False, H1 True, first 100 words True |
| Links | 8 internal (3.2/1k words); 75 external {'dailymed.nlm.nih.gov': 10, 'europepmc.org': 45, 'www.novonordisk.com': 15, 'investor.lilly.com': 2, 'www.eurekalert.org': 3}; new-tab 75/75 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 21, 'details': 7, 'images': 0, 'bold_own': 23} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-11-06', '2025-12-18', '2026-09-30', '2026-10-29'] |

### H2 sequence

1. At a glance
2. What amylin does, and what an amylin agonist copies
3. Pramlintide mechanism of action as an amylin analog
4. Pramlintide (Symlin): what the label says
5. Cagrilintide: the first long-acting amylin analog to reach phase 3
6. Amylin drugs in development: eloralintide, petrelintide, amycretin and others
7. How the amylin drugs compare so far
8. More in this topic
9. Questions people ask
10. Sources
11. Related records
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 13 (avg sentence 19.9 words). Quotations are verbatim by policy; this measures only the text we wrote.
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


Built from `dist/blog/amylin-analogs/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 45 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 8 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/amylin-analogs`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'dailymed.nlm.nih.gov': 10, 'europepmc.org': 45, 'www.novonordisk.com': 15, 'investor.lilly.com': 2, 'www.eurekalert.org': 3}).

### Page facts

| | |
|---|---|
| Title (55) | Amylin Analogs: Pramlintide, Cagrilintide and New Drugs |
| Description (160) | What amylin analogs do, how pramlintide works and what its label says, and the amylin drugs in development: cagrilintide, eloralintide, petrelintide, amycretin. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/amylin-analogs |
| H1 / H2 / H3 | ['Amylin analogs: pramlintide, cagrilintide and the amylin drugs in development'] / 12 / 0 |
| Words (total / own prose / quoted) | 2500 / 1988 / 0 |
| Readability Flesch, grade, avg sentence: all | 6, 18.6, 25.2 |
| … own prose only | 13, 16.5, 19.9 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `amylin drug` | 13× (0.52%); title False, H1 True, first 100 words True |
| Links | 8 internal (3.2/1k words); 75 external {'dailymed.nlm.nih.gov': 10, 'europepmc.org': 45, 'www.novonordisk.com': 15, 'investor.lilly.com': 2, 'www.eurekalert.org': 3}; new-tab 75/75 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 21, 'details': 7, 'images': 0, 'bold_own': 23} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-11-06', '2025-12-18', '2026-09-30', '2026-10-29'] |

### H2 sequence

1. At a glance
2. What amylin does, and what an amylin agonist copies
3. Pramlintide mechanism of action as an amylin analog
4. Pramlintide (Symlin): what the label says
5. Cagrilintide: the first long-acting amylin analog to reach phase 3
6. Amylin drugs in development: eloralintide, petrelintide, amycretin and others
7. How the amylin drugs compare so far
8. More in this topic
9. Questions people ask
10. Sources
11. Related records
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 13 (avg sentence 19.9 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
