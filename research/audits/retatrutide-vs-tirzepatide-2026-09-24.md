# Retatrutide vs tirzepatide audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: 408fc38 (page/retatrutide-vs-tirzepatide, pre-merge build). Nineteenth page written end to end under the sequencing rule, and the first comparison page: stages 1-5 in research/intents/retatrutide-vs-tirzepatide.json before any guide text.

## Part 1: audit

Built from `dist/compare/retatrutide-vs-tirzepatide/index.html`.

### Content quality score: 47/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 4 data tables, 8 cited verbatim quotations, measured-absence statements present |
| Expertise | 6/25 | 10 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 5 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/retatrutide-vs-tirzepatide`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 10}).

### Page facts

| | |
|---|---|
| Title (56) | Retatrutide vs Tirzepatide: No Head-to-Head Trial Exists |
| Description (160) | No trial has given both to the same people. What retatrutide's phase 2 and tirzepatide's phase 3 trials each measured, the indirect estimates, doses and status. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/retatrutide-vs-tirzepatide |
| H1 / H2 / H3 | ['Retatrutide vs tirzepatide: no trial has compared them in people, and what that means for every number you have seen'] / 21 / 0 |
| Words (total / own prose / quoted) | 4859 / 3722 / 237 |
| Readability Flesch, grade, avg sentence: all | 22, 15.2, 20.2 |
| … own prose only | 27, 13.7, 17.1 |
| … quotations only | -31, 24.7, 28.8 |
| Keyword `retatrutide vs tirzepatide` | 2× (0.04%); title True, H1 True, first 100 words True |
| Links | 5 internal (1.0/1k words); 10 external {'europepmc.org': 10}; new-tab 10/10 |
| Formatting | {'tables': 4, 'captions': 4, 'quotes_with_cite': 8, 'abbr': 2, 'time': 15, 'details': 18, 'images': 0, 'bold_own': 45} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. The trial that would answer this has not been run
5. Side by side, from each record
6. Every trial behind the comparison, with what it actually tested
7. The numbers people quote, and what each one came from
8. Studies that compared them directly
9. Three receptors against two: what the glucagon arm adds
10. Doses in the trials and on the label
11. Side effects, and why the comparison is harder than it looks
12. Switching between them: what has been studied
13. Availability: one is approved, the other is in phase 3
14. What the evidence lets you say, and what it does not
15. Common mistakes in this comparison
16. Open questions
17. Questions people ask
18. Sources
19. Reference card
20. Related records
21. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 27 (avg sentence 17.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.0 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| The page claimed eight head-to-head studies in its pill, its at-a-glance fact, its reference card and its section heading | `accept-template` (done) | The record's eight claims are papers naming both compounds, which is what the fetcher matched, not studies comparing them. The wording said the opposite of the page's central finding. Fixed in ComparisonV2.astro for every comparison page: the pill now reads "8 studies name both", the fact and card say "studies naming both", and the default section lede tells the reader to check each card's design line. | template | engineer (done) |
| The section heading still read "Studies that compared them directly" | `accept-record` (map, done) | Headings belong in the intent map. Added a head-to-head query with the heading "The eight studies that name both, and what each one is" and a boundary naming what the eight actually are. | intent map | writer |
| A network meta-analysis of 24,214 participants was labelled "Clinical trial, humans, n=214" | `accept-record` (done) + `accept-script` (open) | The drafter read "24 214" as a sample size and the design as a trial. All eight claims relabelled by hand with what each study is: four reviews or meta-analyses, three animal or cell studies, one peptide-design paper. The head-to-head drafter needs a design filter and a thousands-separator fix. | record, script | writer done; engineer open |
| The two landmark trials were not in the ledger | `accept-record` (done) + `accept-script` (open) | A comparison page's ledger was built only from papers naming both compounds, so neither the retatrutide phase 2 trial nor SURMOUNT-1 was in it, although every figure on the page comes from them. Both added by hand. The comparison fetcher should pull each side's pivotal trials. | record, script | writer done; engineer open |
| Expertise 6/25, driven by 10 primary-source links | `reject-policy` (partial) | A comparison record's ledger is the papers that bear on the comparison, ten after the additions. The two compound records it sits between carry 36 and 28 sources and are linked from the page. Padding this ledger with tirzepatide's 2,756 publications would raise the score and inform nobody. | none | — |
| Tirzepatide's approved label is not in the ledger | `accept-record` (boundary, done) | Label doses are cited editorially with pending_source and the dose section says so; open_actions asks for the label. | record | writer |
| Internal links 1.0/1k words | `accept-template` (partial) | Both compound records, semaglutide, cagrilintide and the comparison directory are linked from guide prose; automatic entity linking remains the open template item. | template | engineer, open |
| Own-prose Flesch 22 | `reject-policy` | design.md §9.7 budgets sentence length (met); network meta-analysis, gastrointestinal and glucagon receptor drive syllables. Precedent: all prior audits. | none | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| Dosage intent, including "retatrutide dose equivalent to tirzepatide" | `reject-policy` (partial) | Content boundary: trial doses and label doses appear, attributed to the trial or the label that set them. No equivalence is offered, because none is published, and the dose section says so. Precedent: every compound page. | none | — |
| Cost and price queries measured in the same batch | `reject-policy` | Scope rule in docs/content-sop.md: commercial intent declined, so they are absent from the map. | none | — |

## Part 3: exit audit

Built from `dist/compare/retatrutide-vs-tirzepatide/index.html`.

### Content quality score: 47/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 4 data tables, 8 cited verbatim quotations, measured-absence statements present |
| Expertise | 6/25 | 10 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 5 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/retatrutide-vs-tirzepatide`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 10}).

### Page facts

| | |
|---|---|
| Title (56) | Retatrutide vs Tirzepatide: No Head-to-Head Trial Exists |
| Description (160) | No trial has given both to the same people. What retatrutide's phase 2 and tirzepatide's phase 3 trials each measured, the indirect estimates, doses and status. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/retatrutide-vs-tirzepatide |
| H1 / H2 / H3 | ['Retatrutide vs tirzepatide: no trial has compared them in people, and what that means for every number you have seen'] / 21 / 0 |
| Words (total / own prose / quoted) | 4923 / 3759 / 237 |
| Readability Flesch, grade, avg sentence: all | 23, 15.1, 20.3 |
| … own prose only | 27, 13.7, 17.1 |
| … quotations only | -31, 24.7, 28.8 |
| Keyword `retatrutide vs tirzepatide` | 2× (0.04%); title True, H1 True, first 100 words True |
| Links | 5 internal (1.0/1k words); 10 external {'europepmc.org': 10}; new-tab 10/10 |
| Formatting | {'tables': 4, 'captions': 4, 'quotes_with_cite': 8, 'abbr': 2, 'time': 15, 'details': 18, 'images': 0, 'bold_own': 45} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. The trial that would answer this has not been run
5. Side by side, from each record
6. Every trial behind the comparison, with what it actually tested
7. The numbers people quote, and what each one came from
8. The eight studies that name both, and what each one is
9. Three receptors against two: what the glucagon arm adds
10. Doses in the trials and on the label
11. Side effects, and why the comparison is harder than it looks
12. Switching between them: what has been studied
13. Availability: one is approved, the other is in phase 3
14. What the evidence lets you say, and what it does not
15. Common mistakes in this comparison
16. Open questions
17. Questions people ask
18. Sources
19. Reference card
20. Related records
21. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 27 (avg sentence 17.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.0 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 47/100. The two accepted items were wording, not content: the template no longer calls eight papers head-to-head studies, and the section heading now says what the eight are. Neither moves a heuristic that counts tables, links and quotations.
- The deductions that remain are reviewer, author, image, Flesch and ledger size. Four are `defer-reviewer` or `reject-policy`; the fifth is a property of a comparison record.
- Confirmed in the built HTML: the pill reads "8 studies name both", the head-to-head lede names the four reviews, three animal studies and one design paper, and the mouse study is identified as the only one that gave both compounds to the same subjects.
- Not looped: the exit run confirms the accepted items landed and nothing else.
