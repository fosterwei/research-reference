# glucose-pills audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/glucose-pills.json were written before the page.

## Part 1: audit


Built from `dist/blog/glucose-pills/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 38 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 11 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/glucose-pills`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'diabetes.org': 14, 'europepmc.org': 38}).

### Page facts

| | |
|---|---|
| Title (51) | Glucose Pills: Glucose Tablets vs Blood Sugar Pills |
| Description (154) | Glucose pills mean two things: glucose tablets that treat lows (4-5 g each, 15-15 rule) and prescription pills that lower blood sugar. See which is which. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/glucose-pills |
| H1 / H2 / H3 | ['Glucose pills: glucose tablets for lows versus pills that lower blood sugar'] / 11 / 2 |
| Words (total / own prose / quoted) | 2467 / 2057 / 0 |
| Readability Flesch, grade, avg sentence: all | 29, 14.9, 22.8 |
| … own prose only | 34, 13.6, 20.1 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `glucose pills` | 15× (0.61%); title True, H1 True, first 100 words True |
| Links | 11 internal (4.5/1k words); 52 external {'diabetes.org': 14, 'europepmc.org': 38}; new-tab 52/52 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 10, 'details': 6, 'images': 0, 'bold_own': 14} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Two meanings of glucose pills, side by side
3. Glucose tablets and the 15-15 rule
4. Do glucose tablets work better than candy or juice?
5. Who with type 2 diabetes needs glucose tablets
6. Glucose pills for diabetes: the tablets that lower blood sugar
7. What "best glucose tablets for type 2 diabetes" comes down to
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 34 (avg sentence 20.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
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


Built from `dist/blog/glucose-pills/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 38 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 11 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/glucose-pills`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'diabetes.org': 14, 'europepmc.org': 38}).

### Page facts

| | |
|---|---|
| Title (51) | Glucose Pills: Glucose Tablets vs Blood Sugar Pills |
| Description (154) | Glucose pills mean two things: glucose tablets that treat lows (4-5 g each, 15-15 rule) and prescription pills that lower blood sugar. See which is which. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/glucose-pills |
| H1 / H2 / H3 | ['Glucose pills: glucose tablets for lows versus pills that lower blood sugar'] / 11 / 2 |
| Words (total / own prose / quoted) | 2467 / 2057 / 0 |
| Readability Flesch, grade, avg sentence: all | 29, 14.9, 22.8 |
| … own prose only | 34, 13.6, 20.1 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `glucose pills` | 15× (0.61%); title True, H1 True, first 100 words True |
| Links | 11 internal (4.5/1k words); 52 external {'diabetes.org': 14, 'europepmc.org': 38}; new-tab 52/52 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 10, 'details': 6, 'images': 0, 'bold_own': 14} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. Two meanings of glucose pills, side by side
3. Glucose tablets and the 15-15 rule
4. Do glucose tablets work better than candy or juice?
5. Who with type 2 diabetes needs glucose tablets
6. Glucose pills for diabetes: the tablets that lower blood sugar
7. What "best glucose tablets for type 2 diabetes" comes down to
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 34 (avg sentence 20.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
