# hypoglycemic-drugs audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/hypoglycemic-drugs.json were written before the page.

## Part 1: audit


Built from `dist/blog/hypoglycemic-drugs/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 28 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 10 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/hypoglycemic-drugs`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 28, 'www.accessdata.fda.gov': 4, 'www.fda.gov': 3}).

### Page facts

| | |
|---|---|
| Title (60) | Hypoglycemic Drugs: Classes, Lows and Drugs That Raise Sugar |
| Description (144) | Hypoglycemic and antidiabetic drug classes in one table, which ones cause low blood sugar, and a list of common drugs that increase blood sugar. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/hypoglycemic-drugs |
| H1 / H2 / H3 | ['Hypoglycemic drugs: the glucose-lowering classes, and the medicines that raise blood sugar'] / 11 / 0 |
| Words (total / own prose / quoted) | 2016 / 1473 / 0 |
| Readability Flesch, grade, avg sentence: all | 8, 17.5, 21.6 |
| … own prose only | 22, 14.7, 18.1 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `hypoglycemic drugs` | 8× (0.40%); title True, H1 True, first 100 words True |
| Links | 10 internal (5.0/1k words); 35 external {'europepmc.org': 28, 'www.accessdata.fda.gov': 4, 'www.fda.gov': 3}; new-tab 35/35 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 11, 'details': 5, 'images': 0, 'bold_own': 11} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2012-02-28', '2026-10-29'] |

### H2 sequence

1. At a glance
2. What are hypoglycemic agents? The terms explained
3. Oral hypoglycemic drugs: classification table
4. Which diabetes drugs cause hypoglycemia?
5. Drugs that increase blood sugar
6. Statins and blood sugar: how large is the risk?
7. Steroids and cancer medicines in the 2026 guidelines
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 22 (avg sentence 18.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
4. No contextual link to another compound page in the body.

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No contextual link to a compound record | `accept-record` (done) | Tirzepatide links to its record (semaglutide is not mentioned in the prose). | record | writer |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/hypoglycemic-drugs/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 28 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 11 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/hypoglycemic-drugs`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 28, 'www.accessdata.fda.gov': 4, 'www.fda.gov': 3}).

### Page facts

| | |
|---|---|
| Title (60) | Hypoglycemic Drugs: Classes, Lows and Drugs That Raise Sugar |
| Description (144) | Hypoglycemic and antidiabetic drug classes in one table, which ones cause low blood sugar, and a list of common drugs that increase blood sugar. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/hypoglycemic-drugs |
| H1 / H2 / H3 | ['Hypoglycemic drugs: the glucose-lowering classes, and the medicines that raise blood sugar'] / 11 / 0 |
| Words (total / own prose / quoted) | 2016 / 1473 / 0 |
| Readability Flesch, grade, avg sentence: all | 8, 17.5, 21.6 |
| … own prose only | 22, 14.7, 18.1 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `hypoglycemic drugs` | 8× (0.40%); title True, H1 True, first 100 words True |
| Links | 11 internal (5.5/1k words); 35 external {'europepmc.org': 28, 'www.accessdata.fda.gov': 4, 'www.fda.gov': 3}; new-tab 35/35 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 11, 'details': 5, 'images': 0, 'bold_own': 11} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2012-02-28', '2026-10-29'] |

### H2 sequence

1. At a glance
2. What are hypoglycemic agents? The terms explained
3. Oral hypoglycemic drugs: classification table
4. Which diabetes drugs cause hypoglycemia?
5. Drugs that increase blood sugar
6. Statins and blood sugar: how large is the risk?
7. Steroids and cancer medicines in the 2026 guidelines
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 22 (avg sentence 18.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
