# cagrisema-approval-timeline audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/cagrisema-approval-timeline.json were written before the page.

## Part 1: audit


Built from `dist/blog/cagrisema-approval-timeline/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 22 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 8 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrisema-approval-timeline`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.prnewswire.com': 15, 'www.novonordisk.com': 34, 'europepmc.org': 22, 'www.globenewswire.com': 3, 'www.reuters.com': 3}).

### Page facts

| | |
|---|---|
| Title (56) | CagriSema News: Trials, FDA Filing and Approval Timeline |
| Description (149) | Novo Nordisk filed CagriSema with the FDA in December 2025 and expects a decision in Q4 2026. Every trial result, dated, and why no price exists yet. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrisema-approval-timeline |
| H1 / H2 / H3 | ["CagriSema news: Novo Nordisk's trials, filing and approval timeline"] / 13 / 0 |
| Words (total / own prose / quoted) | 2790 / 2281 / 0 |
| Readability Flesch, grade, avg sentence: all | 15, 16.8, 22.9 |
| … own prose only | 20, 15.4, 19.6 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrisema trial` | 5× (0.18%); title False, H1 False, first 100 words True |
| Links | 8 internal (2.9/1k words); 77 external {'www.prnewswire.com': 15, 'www.novonordisk.com': 34, 'europepmc.org': 22, 'www.globenewswire.com': 3, 'www.reuters.com': 3}; new-tab 77/77 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 21, 'details': 8, 'images': 0, 'bold_own': 26} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Where CagriSema stands in October 2026
3. CagriSema timeline, 2021 to 2026
4. The CagriSema trial programme and why the numbers differ
5. REDEFINE 4: the head-to-head result against tirzepatide
6. When will CagriSema be available?
7. CagriSema cost and price: why there is no number yet
8. What to watch for next in CagriSema news
9. More in this topic
10. Questions people ask
11. Sources
12. Related records
13. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 20 (avg sentence 19.6 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. Internal links 2.9 per 1,000 words (guideline 3–5).
4. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Internal links 2.9 per 1,000 words | `accept-record` (done) | Semaglutide and tirzepatide now link to their compound records. | record | writer |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/cagrisema-approval-timeline/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 22 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 9 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrisema-approval-timeline`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.prnewswire.com': 15, 'www.novonordisk.com': 34, 'europepmc.org': 22, 'www.globenewswire.com': 3, 'www.reuters.com': 3}).

### Page facts

| | |
|---|---|
| Title (56) | CagriSema News: Trials, FDA Filing and Approval Timeline |
| Description (149) | Novo Nordisk filed CagriSema with the FDA in December 2025 and expects a decision in Q4 2026. Every trial result, dated, and why no price exists yet. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrisema-approval-timeline |
| H1 / H2 / H3 | ["CagriSema news: Novo Nordisk's trials, filing and approval timeline"] / 13 / 0 |
| Words (total / own prose / quoted) | 2792 / 2283 / 0 |
| Readability Flesch, grade, avg sentence: all | 15, 16.8, 22.9 |
| … own prose only | 20, 15.4, 19.6 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrisema trial` | 5× (0.18%); title False, H1 False, first 100 words True |
| Links | 9 internal (3.2/1k words); 77 external {'www.prnewswire.com': 15, 'www.novonordisk.com': 34, 'europepmc.org': 22, 'www.globenewswire.com': 3, 'www.reuters.com': 3}; new-tab 77/77 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 21, 'details': 8, 'images': 0, 'bold_own': 26} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Where CagriSema stands in October 2026
3. CagriSema timeline, 2021 to 2026
4. The CagriSema trial programme and why the numbers differ
5. REDEFINE 4: the head-to-head result against tirzepatide
6. When will CagriSema be available?
7. CagriSema cost and price: why there is no number yet
8. What to watch for next in CagriSema news
9. More in this topic
10. Questions people ask
11. Sources
12. Related records
13. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 20 (avg sentence 19.6 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
