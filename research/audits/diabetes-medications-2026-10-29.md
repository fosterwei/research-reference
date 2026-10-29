# diabetes-medications audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/diabetes-medications.json were written before the page.

## Part 1: audit


Built from `dist/blog/diabetes-medications/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 3 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 23 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 18 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/diabetes-medications`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 23, 'www.accessdata.fda.gov': 15, 'www.novonordisk-us.com': 3, 'investor.lilly.com': 2}).

### Page facts

| | |
|---|---|
| Title (54) | Diabetes Medications List: Every Class Compared (2026) |
| Description (148) | Compare every type 2 diabetes medication class: how it works, A1C and weight effect, hypoglycemia risk, pill or injection, and how ADA 2026 chooses. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/diabetes-medications |
| H1 / H2 / H3 | ['Diabetes medications: every class, how each works, and where amylin drugs fit'] / 12 / 0 |
| Words (total / own prose / quoted) | 3186 / 2461 / 0 |
| Readability Flesch, grade, avg sentence: all | 11, 18.4, 26.6 |
| … own prose only | 19, 16.0, 21.5 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `diabetes medications` | 14× (0.44%); title True, H1 True, first 100 words True |
| Links | 18 internal (5.6/1k words); 43 external {'europepmc.org': 23, 'www.accessdata.fda.gov': 15, 'www.novonordisk-us.com': 3, 'investor.lilly.com': 2}; new-tab 43/43 |
| Formatting | {'tables': 3, 'captions': 3, 'quotes_with_cite': 0, 'abbr': 0, 'time': 17, 'details': 7, 'images': 0, 'bold_own': 35} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-04-01', '2026-10-29'] |

### H2 sequence

1. At a glance
2. Diabetes medications list: every class in one table
3. How diabetes drugs lower blood sugar: five routes
4. Oral diabetes medications and injectable diabetes medicines
5. Which medicine is best for a diabetic patient? How the 2026 ADA guidelines choose
6. Side effects of diabetes medication, class by class
7. Where amylin drugs such as cagrilintide fit
8. New diabetes drugs, prediabetes and remission
9. Every guide in this topic
10. Questions people ask
11. Sources
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 19 (avg sentence 21.5 words). Quotations are verbatim by policy; this measures only the text we wrote.
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


Built from `dist/blog/diabetes-medications/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 3 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 23 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 18 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/diabetes-medications`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 23, 'www.accessdata.fda.gov': 15, 'www.novonordisk-us.com': 3, 'investor.lilly.com': 2}).

### Page facts

| | |
|---|---|
| Title (54) | Diabetes Medications List: Every Class Compared (2026) |
| Description (148) | Compare every type 2 diabetes medication class: how it works, A1C and weight effect, hypoglycemia risk, pill or injection, and how ADA 2026 chooses. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/diabetes-medications |
| H1 / H2 / H3 | ['Diabetes medications: every class, how each works, and where amylin drugs fit'] / 12 / 0 |
| Words (total / own prose / quoted) | 3186 / 2461 / 0 |
| Readability Flesch, grade, avg sentence: all | 11, 18.4, 26.6 |
| … own prose only | 19, 16.0, 21.5 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `diabetes medications` | 14× (0.44%); title True, H1 True, first 100 words True |
| Links | 18 internal (5.6/1k words); 43 external {'europepmc.org': 23, 'www.accessdata.fda.gov': 15, 'www.novonordisk-us.com': 3, 'investor.lilly.com': 2}; new-tab 43/43 |
| Formatting | {'tables': 3, 'captions': 3, 'quotes_with_cite': 0, 'abbr': 0, 'time': 17, 'details': 7, 'images': 0, 'bold_own': 35} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-04-01', '2026-10-29'] |

### H2 sequence

1. At a glance
2. Diabetes medications list: every class in one table
3. How diabetes drugs lower blood sugar: five routes
4. Oral diabetes medications and injectable diabetes medicines
5. Which medicine is best for a diabetic patient? How the 2026 ADA guidelines choose
6. Side effects of diabetes medication, class by class
7. Where amylin drugs such as cagrilintide fit
8. New diabetes drugs, prediabetes and remission
9. Every guide in this topic
10. Questions people ask
11. Sources
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 19 (avg sentence 21.5 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
