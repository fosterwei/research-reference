# cagrilintide-with-retatrutide audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/cagrilintide-with-retatrutide.json were written before the page.

## Part 1: audit


Built from `dist/blog/cagrilintide-with-retatrutide/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 30 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 10 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrilintide-with-retatrutide`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 30, 'www.novonordisk.com': 3, 'www.prnewswire.com': 12, 'www.novonordisk-us.com': 3}).

### Page facts

| | |
|---|---|
| Title (54) | Cagrilintide Dosage With Retatrutide: What Trials Show |
| Description (154) | No trial has tested cagrilintide with retatrutide. Each drug's own trial doses, retatrutide's phase 3 status, the one rat study, and what is known by sex. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrilintide-with-retatrutide |
| H1 / H2 / H3 | ['Cagrilintide with retatrutide: what the evidence covers'] / 12 / 0 |
| Words (total / own prose / quoted) | 2275 / 1833 / 0 |
| Readability Flesch, grade, avg sentence: all | 16, 16.6, 22.2 |
| … own prose only | 18, 15.3, 18.1 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `what is cagrilintide retatrutide for men` | 2× (0.09%); title False, H1 False, first 100 words False |
| Links | 10 internal (4.4/1k words); 48 external {'europepmc.org': 30, 'www.novonordisk.com': 3, 'www.prnewswire.com': 12, 'www.novonordisk-us.com': 3}; new-tab 48/48 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 16, 'details': 6, 'images': 0, 'bold_own': 17} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-06-06', '2026-07-23', '2026-10-29'] |

### H2 sequence

1. At a glance
2. What "cagri reta" means, and what a blend is
3. Retatrutide and cagrilintide together: one study, in rats
4. Cagrilintide dosage with retatrutide: each drug's own trial doses
5. Why two drugs' doses do not add up to a combination dose
6. Cagrilintide and retatrutide for men: what the trials show by sex
7. Retatrutide's status: phase 3 results and Lilly's filing plan
8. More in this topic
9. Questions people ask
10. Sources
11. Related records
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 18 (avg sentence 18.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Keyword `what is cagrilintide retatrutide for men` absent | `reject-policy` | Ungrammatical query; answered in its own section with the sex-subgroup data that exist (retatrutide phase 2) and the absence for the combination. | none | — |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/cagrilintide-with-retatrutide/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 30 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 10 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/cagrilintide-with-retatrutide`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 30, 'www.novonordisk.com': 3, 'www.prnewswire.com': 12, 'www.novonordisk-us.com': 3}).

### Page facts

| | |
|---|---|
| Title (54) | Cagrilintide Dosage With Retatrutide: What Trials Show |
| Description (154) | No trial has tested cagrilintide with retatrutide. Each drug's own trial doses, retatrutide's phase 3 status, the one rat study, and what is known by sex. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/cagrilintide-with-retatrutide |
| H1 / H2 / H3 | ['Cagrilintide with retatrutide: what the evidence covers'] / 12 / 0 |
| Words (total / own prose / quoted) | 2276 / 1834 / 0 |
| Readability Flesch, grade, avg sentence: all | 16, 16.6, 22.2 |
| … own prose only | 18, 15.3, 18.1 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `what is cagrilintide retatrutide for men` | 2× (0.09%); title False, H1 False, first 100 words False |
| Links | 10 internal (4.4/1k words); 48 external {'europepmc.org': 30, 'www.novonordisk.com': 3, 'www.prnewswire.com': 12, 'www.novonordisk-us.com': 3}; new-tab 48/48 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 16, 'details': 6, 'images': 0, 'bold_own': 17} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-06-06', '2026-07-23', '2026-10-29'] |

### H2 sequence

1. At a glance
2. What "cagri reta" means, and what a blend is
3. Retatrutide and cagrilintide together: one study, in rats
4. Cagrilintide dosage with retatrutide: each drug's own trial doses
5. Why two drugs' doses do not add up to a combination dose
6. Cagrilintide and retatrutide for men: what the trials show by sex
7. Retatrutide's status: phase 3 results and Lilly's filing plan
8. More in this topic
9. Questions people ask
10. Sources
11. Related records
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 18 (avg sentence 18.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
