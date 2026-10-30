# new-weight-loss-drugs audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/new-weight-loss-drugs.json were written before the page.

## Part 1: audit


Built from `dist/blog/new-weight-loss-drugs/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 17 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 17 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/new-weight-loss-drugs`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.prnewswire.com': 21, 'www.fda.gov': 9, 'investor.lilly.com': 25, 'www.novonordisk.com': 16, 'europepmc.org': 17, 'www.globenewswire.com': 7, 'www.whitehouse.gov': 3}).

### Page facts

| | |
|---|---|
| Title (59) | New Weight-Loss Drugs: 2025-2026 FDA Approvals and Pipeline |
| Description (147) | Every weight-loss drug announcement from 2025 to October 2026, dated: the Wegovy pill, Foundayo, Wegovy HD, CagriSema's FDA review and retatrutide. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/new-weight-loss-drugs |
| H1 / H2 / H3 | ['New weight-loss drugs: the 2025-2026 announcements, and where cagrilintide stands'] / 13 / 2 |
| Words (total / own prose / quoted) | 3050 / 2483 / 0 |
| Readability Flesch, grade, avg sentence: all | 13, 18.3, 27.7 |
| … own prose only | 18, 16.3, 22.7 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `weight loss drug announcement` | 0× (0.00%); title False, H1 False, first 100 words False |
| Links | 17 internal (5.6/1k words); 98 external {'www.prnewswire.com': 21, 'www.fda.gov': 9, 'investor.lilly.com': 25, 'www.novonordisk.com': 16, 'europepmc.org': 17, 'www.globenewswire.com': 7, 'www.whitehouse.gov': 3}; new-tab 98/98 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 24, 'details': 7, 'images': 0, 'bold_own': 36} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Weight-loss drug announcements, dated
3. The newest weight-loss pills the FDA approved
4. Wegovy HD: the 7.2 mg semaglutide dose
5. The late-stage pipeline: filed, and in phase 3
6. Cagrilintide news: where cagrilintide stands
7. The November 2025 GLP-1 pricing announcement
8. What the new drugs share: side effects and stopping treatment
9. How to read obesity drug news
10. Questions people ask
11. Sources
12. Related records
13. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 18 (avg sentence 22.7 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Primary query `weight loss drug announcement` missing | `accept-record` (done) | Opening sentence now uses the searcher's phrase. | record | writer |
| Average sentence 22.7 words, over the §9.7 budget | `accept-record` (done) | Four long sentences split; exit run 21.2. | record | writer |
| REDEFINE 4 figures without their estimand | `accept-record` (done) | Labelled 'in people who took treatment as intended', matching the other pages. | record | writer |
| 'First 100 words' check still false | `reject-policy` | The audit counts from the top of main (H1, dek, at-a-glance list); the phrase is in the first sentence of the page's own opening. | none | — |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/new-weight-loss-drugs/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 17 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 17 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/new-weight-loss-drugs`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.prnewswire.com': 21, 'www.fda.gov': 9, 'investor.lilly.com': 25, 'www.novonordisk.com': 16, 'europepmc.org': 17, 'www.globenewswire.com': 7, 'www.whitehouse.gov': 3}).

### Page facts

| | |
|---|---|
| Title (59) | New Weight-Loss Drugs: 2025-2026 FDA Approvals and Pipeline |
| Description (147) | Every weight-loss drug announcement from 2025 to October 2026, dated: the Wegovy pill, Foundayo, Wegovy HD, CagriSema's FDA review and retatrutide. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/new-weight-loss-drugs |
| H1 / H2 / H3 | ['New weight-loss drugs: the 2025-2026 announcements, and where cagrilintide stands'] / 13 / 2 |
| Words (total / own prose / quoted) | 3057 / 2490 / 0 |
| Readability Flesch, grade, avg sentence: all | 15, 17.6, 25.8 |
| … own prose only | 20, 15.7, 21.2 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `weight loss drug announcement` | 1× (0.03%); title False, H1 False, first 100 words False |
| Links | 17 internal (5.6/1k words); 98 external {'www.prnewswire.com': 21, 'www.fda.gov': 9, 'investor.lilly.com': 25, 'www.novonordisk.com': 16, 'europepmc.org': 17, 'www.globenewswire.com': 7, 'www.whitehouse.gov': 3}; new-tab 98/98 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 24, 'details': 7, 'images': 0, 'bold_own': 36} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Weight-loss drug announcements, dated
3. The newest weight-loss pills the FDA approved
4. Wegovy HD: the 7.2 mg semaglutide dose
5. The late-stage pipeline: filed, and in phase 3
6. Cagrilintide news: where cagrilintide stands
7. The November 2025 GLP-1 pricing announcement
8. What the new drugs share: side effects and stopping treatment
9. How to read obesity drug news
10. Questions people ask
11. Sources
12. Related records
13. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 20 (avg sentence 21.2 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
