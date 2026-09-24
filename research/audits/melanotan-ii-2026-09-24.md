# Melanotan II audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: c834f1f (page/melanotan-ii, pre-merge build). Seventeenth page written end to end under the sequencing rule: stages 1-5 in research/intents/melanotan-ii.json before any guide text.

## Part 1: audit

Built from `dist/compounds/melanotan-ii/index.html`.

### Content quality score: 55/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 6 data tables, 14 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 37 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 7 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/melanotan-ii`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 37}).

### Page facts

| | |
|---|---|
| Title (55) | Melanotan II (Tanning Injections): Trials, Doses, Risks |
| Description (147) | Melanotan 2: no tanning trial exists. Four erection studies, trial doses, side effects, case reports, how PT-141 and Scenesse differ, and legality. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/melanotan-ii |
| H1 / H2 / H3 | ["Melanotan II ('tanning injections', the Barbie drug): what four small trials found, why it was abandoned, and what the case reports and vials show"] / 31 / 3 |
| Words (total / own prose / quoted) | 8284 / 6008 / 359 |
| Readability Flesch, grade, avg sentence: all | 18, 16.2, 21.9 |
| … own prose only | 26, 14.1, 17.9 |
| … quotations only | 4, 18.8, 24.6 |
| Keyword `melanotan ii` | 93× (1.12%); title True, H1 True, first 100 words True |
| Links | 7 internal (0.8/1k words); 37 external {'europepmc.org': 37}; new-tab 37/37 |
| Formatting | {'tables': 6, 'captions': 6, 'quotes_with_cite': 14, 'abbr': 0, 'time': 45, 'details': 20, 'images': 0, 'bold_own': 25} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What melanotan II is, and what happened to it
3. What the evidence level means
4. Melanotan II in two minutes
5. How it works
6. What happened in the human studies?
7. Trial by trial: what melanotan II did in the men who received it, and what the case reports say since
8. What the evidence shows
9. Doses reported in studies
10. Every melanotan II dose in the trials, in one table
11. Side effects: what the trials recorded, and what the case reports added
12. Who melanotan II is discussed for, and the cautions that recur
13. Reported interactions
14. Reported timelines
15. What is measured over time, and what is not
16. Escalation schedules used in studies
17. Study durations
18. Routes: subcutaneous injection in every trial; nasal sprays untested and now in a case report
19. Weight-normalized doses, as published
20. What people report outside the literature
21. Storage and handling
22. Common mistakes in how melanotan II is discussed
23. Melanotan II vs melanotan I (afamelanotide, Scenesse), PT-141 and UV tanning
24. How it compares
25. Regulatory status: unlicensed and illegal to sell in the UK, US and Australia; never approved anywhere
26. Open questions and limitations
27. Questions people ask
28. Sources
29. Reference card
30. Related records
31. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 26 (avg sentence 17.9 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 0.8 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| Own-prose Flesch 26 (avg sentence 17.9) | `reject-policy` | design.md §9.7 budgets sentence length (met); the terminology (melanocortin, afamelanotide, bremelanotide) drives syllable count. Precedent: all prior audits. | none | — |
| Internal links 0.8/1k words | `accept-template` (partial) | Guide prose links the PT-141 record and the calculator (7 unique); a long page with 37 source links dilutes the ratio by design; automatic entity linking remains the open template item. | template | engineer, open |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| Thirteen ledger sources were about other molecules entirely, matched by the alias "MT-II" | `accept-record` (done) + `accept-script` (open) | Metallothionein II, a snake myotoxin, the visual area V5/MT and a genotype paper. Removed by hand at stage 0 with their claims, including a cadmium NMR row the drafter had filed as a dose escalation. The fetcher's publication counts still include them, and the page says so. Alias phrase-matching is the standing script item (precedent GHRP-6, Cartalax). | record, script | writer done; engineer open |
| Drafter's biomarker regex matched a trial-design sentence and a forensic "vials were labeled" sentence | `accept-record` (done) + `accept-script` (open) | Biomarker claims cleared; the mouse ethanol study kept as the one genuine co-administration claim; the escalation claim rewritten by hand from the pilot's stepwise design. Same regex item. | record, script | writer done; engineer open |
| Regulatory documents cited without ledger sources | `accept-record` (boundary, done) | The UK, US and Australian warnings and the bremelanotide-origin papers are editorial with pending_source; open_actions name each document. | record | writer |
| Dosage intent for a compound with four small trials | `reject-policy` (partial) | Content boundary of 2026-09-24: only trial-administered doses appear, all by body weight from the four human studies. The schedules that circulate are named as untested and not reproduced. Precedent: KPV, pinealon, DSIP, LL-37. | none | — |
| Commercial modifiers appeared in the demand batch | `reject-policy` | Scope rule in docs/content-sop.md: commercial intent declined, so they are absent from the map. | none | — |

## Part 3: exit audit

Built from `dist/compounds/melanotan-ii/index.html`.

### Content quality score: 55/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 6 data tables, 14 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 37 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 7 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/melanotan-ii`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 37}).

### Page facts

| | |
|---|---|
| Title (55) | Melanotan II (Tanning Injections): Trials, Doses, Risks |
| Description (147) | Melanotan 2: no tanning trial exists. Four erection studies, trial doses, side effects, case reports, how PT-141 and Scenesse differ, and legality. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compounds/melanotan-ii |
| H1 / H2 / H3 | ["Melanotan II ('tanning injections', the Barbie drug): what four small trials found, why it was abandoned, and what the case reports and vials show"] / 31 / 3 |
| Words (total / own prose / quoted) | 8284 / 6008 / 359 |
| Readability Flesch, grade, avg sentence: all | 18, 16.2, 21.9 |
| … own prose only | 26, 14.1, 17.9 |
| … quotations only | 4, 18.8, 24.6 |
| Keyword `melanotan ii` | 93× (1.12%); title True, H1 True, first 100 words True |
| Links | 7 internal (0.8/1k words); 37 external {'europepmc.org': 37}; new-tab 37/37 |
| Formatting | {'tables': 6, 'captions': 6, 'quotes_with_cite': 14, 'abbr': 0, 'time': 45, 'details': 20, 'images': 0, 'bold_own': 25} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What melanotan II is, and what happened to it
3. What the evidence level means
4. Melanotan II in two minutes
5. How it works
6. What happened in the human studies?
7. Trial by trial: what melanotan II did in the men who received it, and what the case reports say since
8. What the evidence shows
9. Doses reported in studies
10. Every melanotan II dose in the trials, in one table
11. Side effects: what the trials recorded, and what the case reports added
12. Who melanotan II is discussed for, and the cautions that recur
13. Reported interactions
14. Reported timelines
15. What is measured over time, and what is not
16. Escalation schedules used in studies
17. Study durations
18. Routes: subcutaneous injection in every trial; nasal sprays untested and now in a case report
19. Weight-normalized doses, as published
20. What people report outside the literature
21. Storage and handling
22. Common mistakes in how melanotan II is discussed
23. Melanotan II vs melanotan I (afamelanotide, Scenesse), PT-141 and UV tanning
24. How it compares
25. Regulatory status: unlicensed and illegal to sell in the UK, US and Australia; never approved anywhere
26. Open questions and limitations
27. Questions people ask
28. Sources
29. Reference card
30. Related records
31. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 26 (avg sentence 17.9 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 0.8 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 55/100: the remaining deductions (reviewer, author, Flesch, image) are `defer-reviewer` or `reject-policy` items and cannot move here.
- Nothing changed between the runs. The stage 0 cleanup and the hand-written claims were both in place before Part 1, so the two runs agree line for line.
- Not looped: the exit run confirms the record and nothing else.
