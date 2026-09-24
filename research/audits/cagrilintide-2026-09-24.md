# cagrilintide audit, 2026-09-24

Commit: 414354b (pre-merge build; SOP backfill pass, docs/content-automation.md).

## Part 1: audit

Built from `dist/compounds/cagrilintide/index.html`.

### Content quality score: 55/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 6 data tables, 45 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 31 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 12 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/cagrilintide`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 31}).

### Page facts

| | |
|---|---|
| Title (60) | Cagrilintide: CagriSema Results, Doses, Side Effects, Status |
| Description (159) | Cagrilintide explained: the phase 3 CagriSema results, the trial doses and titration, side effects, how it differs from semaglutide, and where approval stands. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/cagrilintide |
| H1 / H2 / H3 | ['Cagrilintide: CagriSema trial results, the doses and titration used, side effects and where approval stands'] / 33 / 3 |
| Words (total / own prose / quoted) | 8819 / 4984 / 1997 |
| Readability Flesch, grade, avg sentence: all | 3, 18.8, 24.0 |
| … own prose only | 17, 15.4, 17.8 |
| … quotations only | -24, 25.7, 36.5 |
| Keyword `cagrilintide` | 196× (2.22%); title True, H1 True, first 100 words True |
| Links | 12 internal (1.4/1k words); 31 external {'europepmc.org': 31}; new-tab 31/31 |
| Formatting | {'tables': 6, 'captions': 2, 'quotes_with_cite': 45, 'abbr': 3, 'time': 40, 'details': 18, 'images': 0, 'bold_own': 25} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What cagrilintide is and how it acts
3. What the evidence level means
4. Cagrilintide in two minutes
5. How cagrilintide works
6. What did the trials find?
7. What doses did the trials use?
8. Cagrilintide dosage chart: what the trials used
9. What side effects did the trials report?
10. Who cagrilintide is being developed for, and the cautions from the trials
11. Biomarkers measured in studies
12. Reported interactions
13. Reported timelines
14. What the trials measured over time
15. Escalation schedules used in studies
16. Study durations
17. Routes studied
18. What people report outside the trials
19. Reconstituting cagrilintide: concentrations for common vial sizes
20. Storage and handling
21. What the trials monitored
22. Common mistakes in how cagrilintide is discussed
23. Cagrilintide vs semaglutide, tirzepatide, retatrutide and survodutide
24. Exclusion criteria in studies
25. How it compares
26. CagriSema: cagrilintide with semaglutide
27. Is cagrilintide approved?
28. Open questions and limitations
29. Questions people ask
30. Sources
31. Reference card
32. Related records
33. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 17 (avg sentence 17.8 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.4 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Own-prose Flesch low | `reject-policy` | design.md §9.7 budgets sentence length (met); terminology drives syllables. Precedent: ipamorelin, BPC-157 audits. | none | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin audit. | none | — |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). | record | — |
| Internal link density below 3/1k | `accept-template` (partial) | Guide prose links peers, stacks, class page, calculator; long pages with 25 to 37 external source links dilute the ratio by design. Automatic entity linking is the open template item. | template | engineer, open |
| REDEFINE 1 monotherapy arm result (11.8%) not on page | `accept-record` | Reported at EASD 2025; add when the indexed abstract carries it. | record | writer |

## Part 3: exit audit

Built from `dist/compounds/cagrilintide/index.html`.

### Content quality score: 55/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 6 data tables, 45 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 31 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 12 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/cagrilintide`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 31}).

### Page facts

| | |
|---|---|
| Title (60) | Cagrilintide: CagriSema Results, Doses, Side Effects, Status |
| Description (159) | Cagrilintide explained: the phase 3 CagriSema results, the trial doses and titration, side effects, how it differs from semaglutide, and where approval stands. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/cagrilintide |
| H1 / H2 / H3 | ['Cagrilintide: CagriSema trial results, the doses and titration used, side effects and where approval stands'] / 33 / 3 |
| Words (total / own prose / quoted) | 8819 / 4984 / 1997 |
| Readability Flesch, grade, avg sentence: all | 3, 18.8, 24.0 |
| … own prose only | 17, 15.4, 17.8 |
| … quotations only | -24, 25.7, 36.5 |
| Keyword `cagrilintide` | 196× (2.22%); title True, H1 True, first 100 words True |
| Links | 12 internal (1.4/1k words); 31 external {'europepmc.org': 31}; new-tab 31/31 |
| Formatting | {'tables': 6, 'captions': 2, 'quotes_with_cite': 45, 'abbr': 3, 'time': 40, 'details': 18, 'images': 0, 'bold_own': 25} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What cagrilintide is and how it acts
3. What the evidence level means
4. Cagrilintide in two minutes
5. How cagrilintide works
6. What did the trials find?
7. What doses did the trials use?
8. Cagrilintide dosage chart: what the trials used
9. What side effects did the trials report?
10. Who cagrilintide is being developed for, and the cautions from the trials
11. Biomarkers measured in studies
12. Reported interactions
13. Reported timelines
14. What the trials measured over time
15. Escalation schedules used in studies
16. Study durations
17. Routes studied
18. What people report outside the trials
19. Reconstituting cagrilintide: concentrations for common vial sizes
20. Storage and handling
21. What the trials monitored
22. Common mistakes in how cagrilintide is discussed
23. Cagrilintide vs semaglutide, tirzepatide, retatrutide and survodutide
24. Exclusion criteria in studies
25. How it compares
26. CagriSema: cagrilintide with semaglutide
27. Is cagrilintide approved?
28. Open questions and limitations
29. Questions people ask
30. Sources
31. Reference card
32. Related records
33. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 17 (avg sentence 17.8 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.4 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison

- Content quality 55 → 55; the movement available without a reviewer landed. Formatting row: `cagrilintide                       6         2        22         4        19        45         1        40         3       1.2      13.6     31/31`.
- This audit was written in a backfill pass after `scripts/loop_status.py` showed the loop had been compressed; the process note is in the SOP.
