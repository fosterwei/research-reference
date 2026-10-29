# cagrilintide-side-effects audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/cagrilintide-side-effects.json were written before the page.

## Part 1: audit


Built from `dist/blog/cagrilintide-side-effects/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 59 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 11 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrilintide-side-effects`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 59, 'www.novonordisk.com': 8, 'annualreport.novonordisk.com': 2}).

### Page facts

| | |
|---|---|
| Title (55) | Cagrilintide Side Effects: Rates From Every Major Trial |
| Description (153) | Cagrilintide side effects in numbers: nausea, constipation, injection-site reactions and dropouts, trial by trial, compared with semaglutide and placebo. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrilintide-side-effects |
| H1 / H2 / H3 | ['Cagrilintide side effects: how often each one happened in the trials'] / 13 / 0 |
| Words (total / own prose / quoted) | 2157 / 1718 / 0 |
| Readability Flesch, grade, avg sentence: all | 4, 17.8, 20.6 |
| … own prose only | 10, 16.1, 17.1 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrilintide side effects` | 10× (0.46%); title True, H1 True, first 100 words True |
| Links | 11 internal (5.1/1k words); 69 external {'europepmc.org': 59, 'www.novonordisk.com': 8, 'annualreport.novonordisk.com': 2}; new-tab 69/69 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 20, 'details': 6, 'images': 0, 'bold_own': 24} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-10-29'] |

### H2 sequence

1. At a glance
2. Cagrilintide side effect rates, trial by trial
3. Nausea, constipation and other stomach effects
4. Injection-site reactions
5. Cagrilintide side effects compared with semaglutide and placebo
6. When cagrilintide side effects happen
7. Serious adverse events and dedicated safety studies
8. What is not known about cagrilintide safety
9. More in this topic
10. Questions people ask
11. Sources
12. Related records
13. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 10 (avg sentence 17.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
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


Built from `dist/blog/cagrilintide-side-effects/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 59 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 11 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrilintide-side-effects`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 59, 'www.novonordisk.com': 8, 'annualreport.novonordisk.com': 2}).

### Page facts

| | |
|---|---|
| Title (55) | Cagrilintide Side Effects: Rates From Every Major Trial |
| Description (153) | Cagrilintide side effects in numbers: nausea, constipation, injection-site reactions and dropouts, trial by trial, compared with semaglutide and placebo. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrilintide-side-effects |
| H1 / H2 / H3 | ['Cagrilintide side effects: how often each one happened in the trials'] / 13 / 0 |
| Words (total / own prose / quoted) | 2157 / 1718 / 0 |
| Readability Flesch, grade, avg sentence: all | 4, 17.8, 20.6 |
| … own prose only | 10, 16.1, 17.1 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `cagrilintide side effects` | 10× (0.46%); title True, H1 True, first 100 words True |
| Links | 11 internal (5.1/1k words); 69 external {'europepmc.org': 59, 'www.novonordisk.com': 8, 'annualreport.novonordisk.com': 2}; new-tab 69/69 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 20, 'details': 6, 'images': 0, 'bold_own': 24} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-10-29'] |

### H2 sequence

1. At a glance
2. Cagrilintide side effect rates, trial by trial
3. Nausea, constipation and other stomach effects
4. Injection-site reactions
5. Cagrilintide side effects compared with semaglutide and placebo
6. When cagrilintide side effects happen
7. Serious adverse events and dedicated safety studies
8. What is not known about cagrilintide safety
9. More in this topic
10. Questions people ask
11. Sources
12. Related records
13. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 10 (avg sentence 17.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
