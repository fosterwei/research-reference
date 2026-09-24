# Sermorelin vs tesamorelin audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: 7f02de7 (page/sermorelin-vs-tesamorelin, pre-merge build). Twenty-first page written end to end under the sequencing rule: stages 1-5 in research/intents/sermorelin-vs-tesamorelin.json before any guide text.

## Part 1: audit

Built from `dist/compare/sermorelin-vs-tesamorelin/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 4 data tables, 11 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 11 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 5 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/sermorelin-vs-tesamorelin`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 11}).

### Page facts

| | |
|---|---|
| Title (54) | Sermorelin vs Tesamorelin: Approval, Trials, and Doses |
| Description (159) | Sermorelin vs tesamorelin: no trial has compared them. One is approved for one condition, the other left the US market in 2008. Trials, doses and side effects. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/sermorelin-vs-tesamorelin |
| H1 / H2 / H3 | ["Sermorelin vs tesamorelin: one is an approved medicine for one condition, the other's approved product left the market in 2008, and no trial has compared them"] / 20 / 0 |
| Words (total / own prose / quoted) | 4595 / 3399 / 402 |
| Readability Flesch, grade, avg sentence: all | 20, 16.0, 22.2 |
| … own prose only | 26, 14.2, 18.3 |
| … quotations only | -9, 23.0, 34.3 |
| Keyword `sermorelin vs tesamorelin` | 2× (0.04%); title True, H1 True, first 100 words True |
| Links | 5 internal (1.1/1k words); 11 external {'europepmc.org': 11}; new-tab 11/11 |
| Formatting | {'tables': 4, 'captions': 4, 'quotes_with_cite': 11, 'abbr': 0, 'time': 16, 'details': 14, 'images': 0, 'bold_own': 34} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. Approval status: the difference most pages get wrong
5. No trial has compared them, and the studies naming both are about doping tests
6. Side by side, from each record
7. What each one was actually tested for
8. Doses: one label, one history
9. Side effects, and the asymmetry in how well they are known
10. Taking both: what it would and would not add
11. Same receptor, two molecules, thirty years apart
12. Studies that name both compounds
13. What the evidence lets you say
14. Common mistakes in this comparison
15. Open questions
16. Questions people ask
17. Sources
18. Reference card
19. Related records
20. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 26 (avg sentence 18.3 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.1 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| The five head-to-head claims are anti-doping assay papers, not comparisons | `accept-record` (done) + `accept-script` (open) | Kept in the ledger, because they are the honest answer to what names both compounds, and a guide section says what they are. Six papers that bear on the comparison were added by hand: the pivotal tesamorelin trial, its pooled phase 3 analysis, the liver-fat trial, the integrase-inhibitor subgroup, the cognition trial of GHRH 1-29 and the 1987 paediatric trial. The comparison fetcher needs to pull each side's pivotal trials; same script item as the retatrutide comparison. | record, script | writer done; engineer open |
| Both compounds are approved medicines, which the queue defers | `reject-policy` (scope, documented) | The deferral rule exists because approved compounds' SERPs are held by clinical publishers. This one is not: every result in the top ten is a clinic, a telehealth service, a supplement retailer or a pharmacy chain, and the AI Overview cites eight of the same commercial pages. The judgment and its evidence are recorded in the map's scope note. Precedent: SS-31 and survodutide, written for the same reason. | none | — |
| The page answers component questions (`tesamorelin dosage`, `sermorelin benefits`) that belong to compound pages | `accept-record` (scope, done) | Both compound records are deferred and have no written sections, so no page on this site answers them. The dose and trial tables cover both compounds, so answering here is accurate rather than opportunistic, and the map records it. Revisit when either compound page is written. | intent map | writer |
| Expertise 9/25 with 11 primary-source links | `reject-policy` (partial) | A comparison ledger holds the papers that bear on the comparison. Tesamorelin's own record carries 27 sources and sermorelin's 40, both linked from this page. | none | — |
| Sermorelin's own record is built from GHRH-antagonist cancer papers matched by the alias | `accept-record` (open, other record) | Noticed while writing this page: that ledger is mostly antagonist and detection papers, not sermorelin studies. It needs the same hand curation, on that record, when it is written. Logged in open_actions. | record | writer, open |
| The 2008 discontinuation and the label indication are cited without ledger documents | `accept-record` (boundary, done) | Editorial with pending_source, and open_actions names the documents. Leaving the discontinuation out would reproduce the error every ranking page makes. | record | writer |
| Internal links 1.1/1k words | `accept-template` (partial) | Both compound records and both adjacent comparisons are linked from guide prose; automatic entity linking remains the open template item. | template | engineer, open |
| Own-prose Flesch 26 | `reject-policy` | design.md §9.7 budgets sentence length, met at 18.3 words. Precedent: all prior audits. | none | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| Dosage intent, the largest single query at 4,935 | `reject-policy` (partial) | Content boundary: the dose table carries the label and trial doses and states that compounded sermorelin figures come from neither, so they are not reproduced. | none | — |
| Cost queries measured in the same batch | `reject-policy` | Scope rule in docs/content-sop.md. | none | — |

## Part 3: exit audit

Built from `dist/compare/sermorelin-vs-tesamorelin/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 4 data tables, 11 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 11 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 5 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/sermorelin-vs-tesamorelin`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 11}).

### Page facts

| | |
|---|---|
| Title (54) | Sermorelin vs Tesamorelin: Approval, Trials, and Doses |
| Description (159) | Sermorelin vs tesamorelin: no trial has compared them. One is approved for one condition, the other left the US market in 2008. Trials, doses and side effects. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/sermorelin-vs-tesamorelin |
| H1 / H2 / H3 | ["Sermorelin vs tesamorelin: one is an approved medicine for one condition, the other's approved product left the market in 2008, and no trial has compared them"] / 20 / 0 |
| Words (total / own prose / quoted) | 4595 / 3399 / 402 |
| Readability Flesch, grade, avg sentence: all | 20, 16.0, 22.2 |
| … own prose only | 26, 14.2, 18.3 |
| … quotations only | -9, 23.0, 34.3 |
| Keyword `sermorelin vs tesamorelin` | 2× (0.04%); title True, H1 True, first 100 words True |
| Links | 5 internal (1.1/1k words); 11 external {'europepmc.org': 11}; new-tab 11/11 |
| Formatting | {'tables': 4, 'captions': 4, 'quotes_with_cite': 11, 'abbr': 0, 'time': 16, 'details': 14, 'images': 0, 'bold_own': 34} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. Approval status: the difference most pages get wrong
5. No trial has compared them, and the studies naming both are about doping tests
6. Side by side, from each record
7. What each one was actually tested for
8. Doses: one label, one history
9. Side effects, and the asymmetry in how well they are known
10. Taking both: what it would and would not add
11. Same receptor, two molecules, thirty years apart
12. Studies that name both compounds
13. What the evidence lets you say
14. Common mistakes in this comparison
15. Open questions
16. Questions people ask
17. Sources
18. Reference card
19. Related records
20. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 26 (avg sentence 18.3 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.1 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 53/100. Every accepted item was applied before Part 1 was taken; the exit run confirms the record is what the triage says it is.
- The remaining deductions are reviewer, author, image and ledger size. Three are `defer-reviewer` or `reject-policy`; the fourth is a property of a comparison record.
- Confirmed in the built HTML: eleven quotations with citations, the regulatory table showing the 2008 discontinuation, the six-row trial table, and the section explaining that the studies naming both compounds are doping assays.
- Not looped: the exit run confirms the record and nothing else.
