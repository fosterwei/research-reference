# Thymosin alpha-1 audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: 1c5b211 (page/thymosin-alpha-1, pre-merge build). Fourteenth page written end to end under the sequencing rule: stages 1–5 in research/intents/thymosin-alpha-1.json before any guide text.

## Part 1: audit

Built from `dist/compounds/thymosin-alpha-1/index.html`.

### Content quality score: 47/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 5 data tables, 8 cited verbatim quotations, measured-absence statements absent |
| Expertise | 6/25 | 24 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 9 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/thymosin-alpha-1`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 24}).

### Page facts

| | |
|---|---|
| Title (57) | Thymosin Alpha-1 (Zadaxin): 65 Trials, Dose, Side Effects |
| Description (159) | Thymosin alpha-1 (thymalfasin, Zadaxin): what 65 randomized trials found, the two big negative ones, the licensed dose, side effects, and where it is approved. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/thymosin-alpha-1 |
| H1 / H2 / H3 | ['Thymosin alpha-1 (thymalfasin, Zadaxin) peptide: what 65 randomized trials found, where it is approved, and what the gray-market vials rest on'] / 30 / 3 |
| Words (total / own prose / quoted) | 7749 / 5314 / 259 |
| Readability Flesch, grade, avg sentence: all | 15, 17.0, 23.9 |
| … own prose only | 24, 14.4, 18.3 |
| … quotations only | 6, 20.1, 31.0 |
| Keyword `thymosin alpha 1` | 15× (0.19%); title False, H1 False, first 100 words False |
| Links | 9 internal (1.2/1k words); 24 external {'europepmc.org': 24}; new-tab 24/24 |
| Formatting | {'tables': 5, 'captions': 5, 'quotes_with_cite': 8, 'abbr': 0, 'time': 33, 'details': 19, 'images': 0, 'bold_own': 32} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What thymosin alpha-1 is, and what the trials found
3. What the evidence level means
4. Thymosin alpha-1 in two minutes
5. How it works
6. Trial by trial: what thymosin alpha-1 did, and did not do
7. What the evidence shows
8. Doses reported in studies
9. Every thymosin alpha-1 dose in the trials, in one table
10. Side effects: what randomized trials of 1,100 people recorded
11. Who thymosin alpha-1 is discussed for, and the cautions that recur
12. Biomarkers measured in studies
13. Reported interactions
14. Reported timelines
15. What is measured over time, and what is not
16. Study durations
17. Routes: subcutaneous injection in every trial and on the label
18. What people report outside the literature
19. Storage and handling
20. Common mistakes in how thymosin alpha-1 is discussed
21. Thymosin alpha-1 vs TB-500 (thymosin beta-4), LL-37 and interferon
22. Exclusion criteria in studies
23. How it compares
24. Regulatory status: approved in 35 countries, not in the United States, and on FDA's category 2 list
25. Open questions and limitations
26. Questions people ask
27. Sources
28. Reference card
29. Related records
30. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 24 (avg sentence 18.3 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.2 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| Own-prose Flesch 24 (avg sentence 18.3) | `reject-policy` | design.md §9.7 budgets sentence length (met); terminology (thymalfasin, pancreatitis, immunomodulatory) drives syllables. Precedent: all prior audits. | none | — |
| Internal links 1.2/1k | `accept-template` (partial) | Guide prose links TB-500, LL-37, BPC-157 and the calculator (9 unique); a 7,700-word page with 24 source links dilutes the ratio by design; automatic entity linking remains the open template item. | template | engineer, open |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| Only 8 cited quotations and no absence statements (Experience 10/20) | `reject-policy` | Eighteen rows quote their abstracts; the drafter's field claims were sparse because the trial abstracts state doses in prose the regex misses, and hand-written claims quote the key sentences. The count reflects the drafter, not the literature; the guide's twelve-trial table carries the detail. | none (script item open) | — |
| Thirteen human rows exceed the HumanTrials cap of 12, so no trial cards render | `accept-record` (done) | The guide's trial-by-trial table carries every trial with dose, endpoint and verdict. Precedent: SS-31, DSIP, kisspeptin, survodutide. | record | writer |
| A hepatitis study of nucleic acid polymers (REP 2139) in which thymosin was a comparator sat in the evidence table | `accept-record` (done) + `accept-script` (open) | Row removed; the fetcher cannot tell comparator from subject. Same alias/subject item as GHRP-6. | record, script | writer done; engineer open |
| Approved-abroad medicine listed as unapproved by the queue | judgment, recorded | ChEMBL records no first_approval because thymalfasin is not FDA-approved; it is approved in about 35 countries. The SERP is reviews, a status page and clinics, not clinical publishers, so the deferral rule's reason does not apply. Recorded in the map's queue_note and the regulatory section; fetch_evidence needs a non-US approval source. | queue, script | owner aware; engineer open |
| Zadaxin label facts (half-life, contraindications) and FDA 2023 notice cited without ledger sources | `accept-record` (boundary, done) | Editorial with pending_source; open_actions name the documents. | record | writer |

## Part 3: exit audit

Built from `dist/compounds/thymosin-alpha-1/index.html`.

### Content quality score: 47/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 5 data tables, 8 cited verbatim quotations, measured-absence statements absent |
| Expertise | 6/25 | 24 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 9 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/thymosin-alpha-1`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 24}).

### Page facts

| | |
|---|---|
| Title (57) | Thymosin Alpha-1 (Zadaxin): 65 Trials, Dose, Side Effects |
| Description (159) | Thymosin alpha-1 (thymalfasin, Zadaxin): what 65 randomized trials found, the two big negative ones, the licensed dose, side effects, and where it is approved. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/thymosin-alpha-1 |
| H1 / H2 / H3 | ['Thymosin alpha-1 (thymalfasin, Zadaxin) peptide: what 65 randomized trials found, where it is approved, and what the gray-market vials rest on'] / 30 / 3 |
| Words (total / own prose / quoted) | 7749 / 5314 / 259 |
| Readability Flesch, grade, avg sentence: all | 15, 17.0, 23.9 |
| … own prose only | 24, 14.4, 18.3 |
| … quotations only | 6, 20.1, 31.0 |
| Keyword `thymosin alpha 1` | 15× (0.19%); title False, H1 False, first 100 words False |
| Links | 9 internal (1.2/1k words); 24 external {'europepmc.org': 24}; new-tab 24/24 |
| Formatting | {'tables': 5, 'captions': 5, 'quotes_with_cite': 8, 'abbr': 0, 'time': 33, 'details': 19, 'images': 0, 'bold_own': 32} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What thymosin alpha-1 is, and what the trials found
3. What the evidence level means
4. Thymosin alpha-1 in two minutes
5. How it works
6. Trial by trial: what thymosin alpha-1 did, and did not do
7. What the evidence shows
8. Doses reported in studies
9. Every thymosin alpha-1 dose in the trials, in one table
10. Side effects: what randomized trials of 1,100 people recorded
11. Who thymosin alpha-1 is discussed for, and the cautions that recur
12. Biomarkers measured in studies
13. Reported interactions
14. Reported timelines
15. What is measured over time, and what is not
16. Study durations
17. Routes: subcutaneous injection in every trial and on the label
18. What people report outside the literature
19. Storage and handling
20. Common mistakes in how thymosin alpha-1 is discussed
21. Thymosin alpha-1 vs TB-500 (thymosin beta-4), LL-37 and interferon
22. Exclusion criteria in studies
23. How it compares
24. Regulatory status: approved in 35 countries, not in the United States, and on FDA's category 2 list
25. Open questions and limitations
26. Questions people ask
27. Sources
28. Reference card
29. Related records
30. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 24 (avg sentence 18.3 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.2 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 47/100, below the other queue pages because the drafter produced few field claims from prose-heavy trial abstracts; the remaining deductions are `defer-reviewer` or `reject-policy` items.
- Nothing changed between the runs; the record was built once with the comparator study removed, so the two parts agree.
- Not looped: the exit run confirms the record and nothing else.
