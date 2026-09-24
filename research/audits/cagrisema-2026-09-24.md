# CagriSema audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: 3043e83 (page/cagrisema, pre-merge build). Twentieth page written end to end under the sequencing rule, and the first stack page: stages 1-5 in research/intents/cagrisema.json before any guide text.

## Part 1: audit

Built from `dist/stacks/cagrisema/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 6 data tables, 15 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 15 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 5 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/stacks/cagrisema`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 15}).

### Page facts

| | |
|---|---|
| Title (48) | CagriSema: Trial Results, Components, and Status |
| Description (154) | CagriSema: seven human trials, the four-arm comparison against each component, the head-to-head trial against tirzepatide, doses, side effects and status. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/stacks/cagrisema |
| H1 / H2 / H3 | ['CagriSema (cagrilintide plus semaglutide): the one combination on this site that was actually tested, what its trials found, and where it fell short'] / 21 / 1 |
| Words (total / own prose / quoted) | 5505 / 4244 / 422 |
| Readability Flesch, grade, avg sentence: all | 17, 15.9, 20.2 |
| … own prose only | 23, 14.5, 17.7 |
| … quotations only | -11, 20.9, 24.6 |
| Keyword `cagrisema` | 69× (1.25%); title True, H1 True, first 100 words True |
| Links | 5 internal (0.9/1k words); 15 external {'europepmc.org': 15}; new-tab 15/15 |
| Formatting | {'tables': 6, 'captions': 6, 'quotes_with_cite': 15, 'abbr': 3, 'time': 20, 'details': 18, 'images': 0, 'bold_own': 46} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What CagriSema is, and how far it has got
3. CagriSema in two minutes
4. Each component on its own evidence
5. Every trial in the programme, and what each one measured
6. Does the combination beat its own components?
7. Why the same trial is quoted as 20.4% and as 22.7%
8. CagriSema against tirzepatide: the head-to-head trial that missed its endpoint
9. What has been tested as a combination
10. Two hormones, two different hungers
11. Doses in the trials
12. Side effects, measured against the components and against placebo
13. Availability: filed, not approved, and not purchasable
14. Common mistakes in how CagriSema is discussed
15. What circulates outside the trials
16. Open questions
17. Questions people ask
18. Sources
19. Reference card
20. Related records
21. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 23 (avg sentence 17.7 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 0.9 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| First run scored 39/100: measured-absence statements absent, 8 primary-source links | `accept-record` (done) | The ledger held only the eight papers the fetcher matched. A Europe PMC search found 250 papers naming CagriSema; seven were added by hand because each answers something the page needed: two meta-analyses against the components, a network meta-analysis including tirzepatide, a REDEFINE 1 secondary analysis, the dual-chamber pen usability study, a fat-free-mass meta-analysis and a brainstem co-agonism study. Score moved to 53. | record, script | writer done; engineer open |
| A meta-analysis of 5,425 participants was labelled a clinical trial, and two pharmacokinetic studies of 33 and 32 adults were labelled one trial of 14 | `accept-record` (done) + `accept-script` (open) | Both relabelled. The drafter reads any participant count in an abstract as a trial sample size and any human paper as a trial. Same design-filter item raised on the retatrutide comparison. | record, script | writer done; engineer open |
| The muscle-loss question had no figure | `accept-record` (done) | Answered with the 2026 fat-free-mass meta-analysis, labelled as a class figure for incretin therapies rather than a CagriSema measurement, with the absence stated in open questions. | record | writer |
| REDEFINE 2 and REDEFINE 4 results are manufacturer announcements | `accept-record` (boundary, done) | Marked as announced rather than published throughout, in the trial table and in the changelog, with pending_source. REDEFINE 4 is the head-to-head result against tirzepatide and would be omitted entirely if only published papers were allowed; naming its source is better than leaving the reader with the impression that no comparison exists. | record | writer |
| Expertise 9/25 with 15 primary-source links | `reject-policy` (partial) | The ledger is now every paper that bears on the combination. The remainder of the 250 hits are reviews naming CagriSema in passing; adding them would raise the count and inform nobody. | none | — |
| Internal links 0.9/1k words | `accept-template` (partial) | Both component records, the retatrutide comparison and the compound directory are linked from guide prose; automatic entity linking remains the open template item. | template | engineer, open |
| Own-prose Flesch 19 | `reject-policy` | design.md §9.7 budgets sentence length (met, 19.2 words); cagrilintide, semaglutide, tirzepatide and estimand drive syllables, and three of those four are unavoidable on this page. | none | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| Dosage intent | `reject-policy` (partial) | Content boundary: trial doses of a fixed-dose product appear, with a statement that the product is not purchasable and that assembling it from parts is not the tested intervention. | none | — |
| Cost and purchase queries measured in the same batch | `reject-policy` | Scope rule in docs/content-sop.md, and there is nothing to buy. | none | — |
| The head term `cagrilintide` (17,146, KD 0) is not answered on this page | `reject-policy` (scope) | It belongs to the component's own written record and is mapped as a redirect there. A stack page competing with its own component page for the component's name would split the site against itself. | none | — |

## Part 3: exit audit

Built from `dist/stacks/cagrisema/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 6 data tables, 15 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 15 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 5 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/stacks/cagrisema`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 15}).

### Page facts

| | |
|---|---|
| Title (48) | CagriSema: Trial Results, Components, and Status |
| Description (154) | CagriSema: seven human trials, the four-arm comparison against each component, the head-to-head trial against tirzepatide, doses, side effects and status. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/stacks/cagrisema |
| H1 / H2 / H3 | ['CagriSema (cagrilintide plus semaglutide): the one combination on this site that was actually tested, what its trials found, and where it fell short'] / 21 / 1 |
| Words (total / own prose / quoted) | 5505 / 4244 / 422 |
| Readability Flesch, grade, avg sentence: all | 17, 15.9, 20.2 |
| … own prose only | 23, 14.5, 17.7 |
| … quotations only | -11, 20.9, 24.6 |
| Keyword `cagrisema` | 69× (1.25%); title True, H1 True, first 100 words True |
| Links | 5 internal (0.9/1k words); 15 external {'europepmc.org': 15}; new-tab 15/15 |
| Formatting | {'tables': 6, 'captions': 6, 'quotes_with_cite': 15, 'abbr': 3, 'time': 20, 'details': 18, 'images': 0, 'bold_own': 46} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What CagriSema is, and how far it has got
3. CagriSema in two minutes
4. Each component on its own evidence
5. Every trial in the programme, and what each one measured
6. Does the combination beat its own components?
7. Why the same trial is quoted as 20.4% and as 22.7%
8. CagriSema against tirzepatide: the head-to-head trial that missed its endpoint
9. What has been tested as a combination
10. Two hormones, two different hungers
11. Doses in the trials
12. Side effects, measured against the components and against placebo
13. Availability: filed, not approved, and not purchasable
14. Common mistakes in how CagriSema is discussed
15. What circulates outside the trials
16. Open questions
17. Questions people ask
18. Sources
19. Reference card
20. Related records
21. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 23 (avg sentence 17.7 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 0.9 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Part 1 here is the second local run, after the ledger was extended; the first run scored 39/100 with eight sources and no measured-absence statement, and is described in the triage row that records the fix.
- Score 53/100 in both runs shown. The accepted items had landed before Part 1 was taken, so the two runs agree.
- Confirmed in the built HTML: fifteen combination studies indexed, the four-arm component table, the network meta-analysis beside the head-to-head result, and the fat-free-mass figure labelled as a class estimate.
- Not looped: the exit run confirms the record and nothing else.
