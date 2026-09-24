# cjc-1295-ipamorelin audit, 2026-09-24

Commit: 414354b (pre-merge build; SOP backfill pass, docs/content-automation.md).

## Part 1: audit

Built from `dist/stacks/cjc-1295-ipamorelin/index.html`.

### Content quality score: 41/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 2 data tables, 3 cited verbatim quotations, measured-absence statements present |
| Expertise | 3/25 | 3 primary-source links; reviewer absent; author absent |
| Authoritativeness | 10/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/stacks/cjc-1295-ipamorelin`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 3}).

### Page facts

| | |
|---|---|
| Title (59) | CJC-1295 + Ipamorelin: Doses That Circulate vs the Evidence |
| Description (155) | CJC-1295 with ipamorelin: how the two act, the DAC question every schedule depends on, what each compound's studies show, and why no trial tested the pair. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/stacks/cjc-1295-ipamorelin |
| H1 / H2 / H3 | ['CJC-1295 and ipamorelin: how the blend works, the doses that circulate, and what studies actually tested'] / 14 / 0 |
| Words (total / own prose / quoted) | 2080 / 1491 / 112 |
| Readability Flesch, grade, avg sentence: all | 31, 13.6, 18.7 |
| … own prose only | 37, 11.8, 14.9 |
| … quotations only | -17, 24.7, 36.7 |
| Keyword `cjc 1295 ipamorelin` | 1× (0.05%); title False, H1 False, first 100 words False |
| Links | 4 internal (1.9/1k words); 3 external {'europepmc.org': 3}; new-tab 3/3 |
| Formatting | {'tables': 2, 'captions': 1, 'quotes_with_cite': 3, 'abbr': 0, 'time': 7, 'details': 9, 'images': 0, 'bold_own': 7} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What the CJC-1295 and ipamorelin blend is
3. CJC-1295 and ipamorelin in two minutes
4. Each component on its own evidence
5. What has been tested as a combination
6. CJC-1295 and ipamorelin dosage: what circulates versus what studies used
7. How the two act, and why the pairing has pharmacological logic
8. Who discusses using it, and the cautions that recur
9. Common mistakes in how this blend is discussed
10. Open questions
11. Questions people ask
12. Sources
13. Related records
14. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 37 (avg sentence 14.9 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.9 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Own-prose Flesch low | `reject-policy` | design.md §9.7 budgets sentence length (met); terminology drives syllables. Precedent: ipamorelin, BPC-157 audits. | none | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin audit. | none | — |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). | record | — |
| Internal link density below 3/1k | `accept-template` (partial) | Guide prose links peers, stacks, class page, calculator; long pages with 25 to 37 external source links dilute the ratio by design. Automatic entity linking is the open template item. | template | engineer, open |
| 2006 CJC-1295 DAC study not in this stack's ledger | `accept-record` (blocked) | It is in the compound literature; add to the stack ledger when Europe PMC is reachable. | record | writer |

## Part 3: exit audit

Built from `dist/stacks/cjc-1295-ipamorelin/index.html`.

### Content quality score: 41/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 2 data tables, 3 cited verbatim quotations, measured-absence statements present |
| Expertise | 3/25 | 3 primary-source links; reviewer absent; author absent |
| Authoritativeness | 10/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/stacks/cjc-1295-ipamorelin`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 3}).

### Page facts

| | |
|---|---|
| Title (59) | CJC-1295 + Ipamorelin: Doses That Circulate vs the Evidence |
| Description (155) | CJC-1295 with ipamorelin: how the two act, the DAC question every schedule depends on, what each compound's studies show, and why no trial tested the pair. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/stacks/cjc-1295-ipamorelin |
| H1 / H2 / H3 | ['CJC-1295 and ipamorelin: how the blend works, the doses that circulate, and what studies actually tested'] / 14 / 0 |
| Words (total / own prose / quoted) | 2080 / 1491 / 112 |
| Readability Flesch, grade, avg sentence: all | 31, 13.6, 18.7 |
| … own prose only | 37, 11.8, 14.9 |
| … quotations only | -17, 24.7, 36.7 |
| Keyword `cjc 1295 ipamorelin` | 1× (0.05%); title False, H1 False, first 100 words False |
| Links | 4 internal (1.9/1k words); 3 external {'europepmc.org': 3}; new-tab 3/3 |
| Formatting | {'tables': 2, 'captions': 1, 'quotes_with_cite': 3, 'abbr': 0, 'time': 7, 'details': 9, 'images': 0, 'bold_own': 7} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What the CJC-1295 and ipamorelin blend is
3. CJC-1295 and ipamorelin in two minutes
4. Each component on its own evidence
5. What has been tested as a combination
6. CJC-1295 and ipamorelin dosage: what circulates versus what studies used
7. How the two act, and why the pairing has pharmacological logic
8. Who discusses using it, and the cautions that recur
9. Common mistakes in how this blend is discussed
10. Open questions
11. Questions people ask
12. Sources
13. Related records
14. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 37 (avg sentence 14.9 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.9 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison

- Content quality 41 → 41; the movement available without a reviewer landed. Formatting row: ``.
- This audit was written in a backfill pass after `scripts/loop_status.py` showed the loop had been compressed; the process note is in the SOP.
