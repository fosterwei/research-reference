# ipamorelin-vs-tesamorelin audit, 2026-09-24

Commit: 414354b (pre-merge build; SOP backfill pass, docs/content-automation.md).

## Part 1: audit

Built from `dist/compare/ipamorelin-vs-tesamorelin/index.html`.

### Content quality score: 41/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements present |
| Expertise | 3/25 | 0 primary-source links; reviewer absent; author absent |
| Authoritativeness | 10/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/ipamorelin-vs-tesamorelin`; datePublished 2026-09-24; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({}).

### Page facts

| | |
|---|---|
| Title (49) | Ipamorelin vs Tesamorelin: Approved vs Unapproved |
| Description (155) | Ipamorelin vs tesamorelin: an FDA-approved GHRH analogue with phase 3 trials against a ghrelin mimetic with two, the only approved dose, and no comparison. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/ipamorelin-vs-tesamorelin |
| H1 / H2 / H3 | ['Ipamorelin vs tesamorelin: an approved medicine with a label against an unapproved compound with two trials'] / 11 / 0 |
| Words (total / own prose / quoted) | 1102 / 676 / 0 |
| Readability Flesch, grade, avg sentence: all | 15, 15.7, 18.4 |
| … own prose only | 23, 13.2, 12.7 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `ipamorelin vs tesamorelin` | 4× (0.36%); title True, H1 True, first 100 words True |
| Links | 4 internal (3.6/1k words); 0 external {}; new-tab 0/0 |
| Formatting | {'tables': 2, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 3, 'details': 7, 'images': 0, 'bold_own': 6} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. Ipamorelin vs tesamorelin in two minutes
4. Side by side, from each record
5. What differs, point by point
6. Studies that compared them directly
7. How the two are discussed as choices
8. Open questions
9. Questions people ask
10. Related records
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 23 (avg sentence 12.7 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Own-prose Flesch low | `reject-policy` | design.md §9.7 budgets sentence length (met); terminology drives syllables. Precedent: ipamorelin, BPC-157 audits. | none | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin audit. | none | — |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). | record | — |
| Internal link density below 3/1k | `accept-template` (partial) | Guide prose links peers, stacks, class page, calculator; long pages with 25 to 37 external source links dilute the ratio by design. Automatic entity linking is the open template item. | template | engineer, open |
| No head-to-head study | `reject-policy` | Same as above. | none | — |

## Part 3: exit audit

Built from `dist/compare/ipamorelin-vs-tesamorelin/index.html`.

### Content quality score: 41/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements present |
| Expertise | 3/25 | 0 primary-source links; reviewer absent; author absent |
| Authoritativeness | 10/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/ipamorelin-vs-tesamorelin`; datePublished 2026-09-24; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({}).

### Page facts

| | |
|---|---|
| Title (49) | Ipamorelin vs Tesamorelin: Approved vs Unapproved |
| Description (155) | Ipamorelin vs tesamorelin: an FDA-approved GHRH analogue with phase 3 trials against a ghrelin mimetic with two, the only approved dose, and no comparison. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/ipamorelin-vs-tesamorelin |
| H1 / H2 / H3 | ['Ipamorelin vs tesamorelin: an approved medicine with a label against an unapproved compound with two trials'] / 11 / 0 |
| Words (total / own prose / quoted) | 1102 / 676 / 0 |
| Readability Flesch, grade, avg sentence: all | 15, 15.7, 18.4 |
| … own prose only | 23, 13.2, 12.7 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `ipamorelin vs tesamorelin` | 4× (0.36%); title True, H1 True, first 100 words True |
| Links | 4 internal (3.6/1k words); 0 external {}; new-tab 0/0 |
| Formatting | {'tables': 2, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 3, 'details': 7, 'images': 0, 'bold_own': 6} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. Ipamorelin vs tesamorelin in two minutes
4. Side by side, from each record
5. What differs, point by point
6. Studies that compared them directly
7. How the two are discussed as choices
8. Open questions
9. Questions people ask
10. Related records
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 23 (avg sentence 12.7 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison

- Content quality 41 → 41; the movement available without a reviewer landed. Formatting row: ``.
- This audit was written in a backfill pass after `scripts/loop_status.py` showed the loop had been compressed; the process note is in the SOP.
