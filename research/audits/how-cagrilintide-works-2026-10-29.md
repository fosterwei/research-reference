# how-cagrilintide-works audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/how-cagrilintide-works.json were written before the page.

## Part 1: audit


Built from `dist/blog/how-cagrilintide-works/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 5 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 81 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 16 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/how-cagrilintide-works`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 81, 'www.novonordisk.com': 11, 'annualreport.novonordisk.com': 6}).

### Page facts

| | |
|---|---|
| Title (58) | Cagrilintide Peptide: How It Works, Uses and Trial Results |
| Description (141) | Cagrilintide is a once-weekly amylin analogue. See how it acts on appetite, its half-life, what it is used for, and what the trials measured. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/how-cagrilintide-works |
| H1 / H2 / H3 | ['What cagrilintide is and how it works: amylin, appetite and what the trials measured'] / 14 / 2 |
| Words (total / own prose / quoted) | 3410 / 2750 / 0 |
| Readability Flesch, grade, avg sentence: all | 13, 17.1, 22.6 |
| … own prose only | 17, 15.5, 18.6 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrilintide peptide` | 6× (0.18%); title True, H1 False, first 100 words True |
| Links | 16 internal (4.7/1k words); 98 external {'europepmc.org': 81, 'www.novonordisk.com': 11, 'annualreport.novonordisk.com': 6}; new-tab 98/98 |
| Formatting | {'tables': 5, 'captions': 5, 'quotes_with_cite': 0, 'abbr': 0, 'time': 25, 'details': 7, 'images': 0, 'bold_own': 32} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-02-23', '2026-10-29'] |

### H2 sequence

1. At a glance
2. What the cagrilintide peptide is
3. Cagrilintide mechanism of action: amylin and calcitonin receptors
4. Cagrilintide half-life and why it is a weekly injection
5. What cagrilintide is used for
6. Cagrilintide benefits measured in trials
7. What cagrilintide does for men: what the trials show by sex
8. Cagrilintide among the amylin drugs
9. What the trials have not shown yet
10. Every guide in this topic
11. Questions people ask
12. Sources
13. Related records
14. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 17 (avg sentence 18.6 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Primary query `cagrilintide peptide` (3,600/mo) absent from the H1 | `accept-record` (done) | H1 reworded to name the cagrilintide peptide. | record | writer |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/how-cagrilintide-works/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 5 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 81 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 16 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/how-cagrilintide-works`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 81, 'www.novonordisk.com': 11, 'annualreport.novonordisk.com': 6}).

### Page facts

| | |
|---|---|
| Title (58) | Cagrilintide Peptide: How It Works, Uses and Trial Results |
| Description (141) | Cagrilintide is a once-weekly amylin analogue. See how it acts on appetite, its half-life, what it is used for, and what the trials measured. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/how-cagrilintide-works |
| H1 / H2 / H3 | ['What the cagrilintide peptide is and how it works: amylin, appetite and what the trials measured'] / 14 / 2 |
| Words (total / own prose / quoted) | 3412 / 2750 / 0 |
| Readability Flesch, grade, avg sentence: all | 13, 17.1, 22.6 |
| … own prose only | 17, 15.5, 18.6 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrilintide peptide` | 7× (0.21%); title True, H1 True, first 100 words True |
| Links | 16 internal (4.7/1k words); 98 external {'europepmc.org': 81, 'www.novonordisk.com': 11, 'annualreport.novonordisk.com': 6}; new-tab 98/98 |
| Formatting | {'tables': 5, 'captions': 5, 'quotes_with_cite': 0, 'abbr': 0, 'time': 25, 'details': 7, 'images': 0, 'bold_own': 32} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-02-23', '2026-10-29'] |

### H2 sequence

1. At a glance
2. What the cagrilintide peptide is
3. Cagrilintide mechanism of action: amylin and calcitonin receptors
4. Cagrilintide half-life and why it is a weekly injection
5. What cagrilintide is used for
6. Cagrilintide benefits measured in trials
7. What cagrilintide does for men: what the trials show by sex
8. Cagrilintide among the amylin drugs
9. What the trials have not shown yet
10. Every guide in this topic
11. Questions people ask
12. Sources
13. Related records
14. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 17 (avg sentence 18.6 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
