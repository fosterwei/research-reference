# Retatrutide vs semaglutide audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: 803def8 (page/semaglutide-vs-retatrutide, pre-merge build). Twenty-fourth page written end to end under the sequencing rule: stages 1-5 in research/intents/semaglutide-vs-retatrutide.json before any guide text.

## Part 1: audit

Built from `dist/compare/semaglutide-vs-retatrutide/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 4 data tables, 12 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 12 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/semaglutide-vs-retatrutide`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 12}).

### Page facts

| | |
|---|---|
| Title (58) | Retatrutide vs Semaglutide: Weight Numbers vs Outcome Data |
| Description (151) | Retatrutide vs semaglutide: no head-to-head trial. The two weight figures, the outcome data only one of them has, doses, side effects and availability. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/semaglutide-vs-retatrutide |
| H1 / H2 / H3 | ['Retatrutide vs semaglutide: a bigger weight number set against four years of outcome data, with no trial comparing them'] / 21 / 0 |
| Words (total / own prose / quoted) | 4275 / 3186 / 405 |
| Readability Flesch, grade, avg sentence: all | 20, 15.2, 19.3 |
| … own prose only | 27, 13.4, 15.7 |
| … quotations only | -18, 25.0, 36.9 |
| Keyword `semaglutide vs retatrutide` | 1× (0.02%); title False, H1 False, first 100 words False |
| Links | 4 internal (0.9/1k words); 12 external {'europepmc.org': 12}; new-tab 12/12 |
| Formatting | {'tables': 4, 'captions': 4, 'quotes_with_cite': 12, 'abbr': 2, 'time': 17, 'details': 16, 'images': 0, 'bold_own': 48} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. The two weight figures, and what each trial was
5. The evidence that weight percentages hide
6. Nothing has compared them in people
7. Side by side, from each record
8. Studies that name both compounds
9. One receptor against three
10. Doses: a dose-finding trial against an approved label
11. Side effects, and why one column is far better known
12. Switching: what has been studied
13. Availability: one is a prescription medicine, the other is investigational
14. What the evidence lets you say
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
3. Own prose reads at Flesch 27 (avg sentence 15.7 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 0.9 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| A network meta-analysis of 24,214 participants was drafted as a clinical trial of 214 | `accept-record` (done) + `accept-script` (open) | The same misparse corrected on the retatrutide-versus-tirzepatide record two pages earlier, which is what makes it a script item rather than a one-off: the drafter reads a space-separated thousands figure as a sample size. All eight claims relabelled with what each study is. | record, script | writer done; engineer open |
| The pivotal trials for both compounds were missing from the ledger | `accept-record` (done) + `accept-script` (open) | Neither STEP 1 nor the retatrutide phase 2 trial was in a comparison record built only from papers naming both drugs, although every figure on the page comes from them. Added by hand with the cardiovascular outcome trial and a second network meta-analysis. Same fetcher item. | record, script | writer done; engineer open |
| Semaglutide is an approved medicine, which the queue defers | `reject-policy` (scope, documented) | The deferral applies to compound pages whose search results are held by clinical publishers. This comparison's are med spas, clinics and telehealth, with Forbes second and a mouse study fifth. Precedent: the sermorelin comparison, written for the same reason two pages earlier. | none | — |
| Expertise 9/25 with 12 primary-source links | `reject-policy` (partial) | The ledger is the papers that bear on the comparison. Both compound records are linked and carry 36 and 27 sources of their own. | none | — |
| Internal links 0.9/1k words | `accept-template` (partial) | Both compound records and the tirzepatide comparison are linked from guide prose; automatic entity linking remains the open template item. | template | engineer, open |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| Overlap with the retatrutide-versus-tirzepatide page written earlier today | no action, measured | Uniqueness is measured against every other page on the site and this one clears the gate comfortably. The two pages share a subject and differ in argument: that one is about a missing head-to-head between two drugs of similar standing, this one is about an asymmetry in outcome evidence. | none | — |
| Dosage intent | `reject-policy` (partial) | Content boundary: trial and label doses only, with an explicit statement that no equivalence between the two scales is published. | none | — |
| Cost queries measured in the same batch | `reject-policy` | Scope rule in docs/content-sop.md. | none | — |

## Part 3: exit audit

Built from `dist/compare/semaglutide-vs-retatrutide/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 4 data tables, 12 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 12 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/semaglutide-vs-retatrutide`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 12}).

### Page facts

| | |
|---|---|
| Title (58) | Retatrutide vs Semaglutide: Weight Numbers vs Outcome Data |
| Description (151) | Retatrutide vs semaglutide: no head-to-head trial. The two weight figures, the outcome data only one of them has, doses, side effects and availability. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/semaglutide-vs-retatrutide |
| H1 / H2 / H3 | ['Retatrutide vs semaglutide: a bigger weight number set against four years of outcome data, with no trial comparing them'] / 21 / 0 |
| Words (total / own prose / quoted) | 4275 / 3186 / 405 |
| Readability Flesch, grade, avg sentence: all | 20, 15.2, 19.3 |
| … own prose only | 27, 13.4, 15.7 |
| … quotations only | -18, 25.0, 36.9 |
| Keyword `semaglutide vs retatrutide` | 1× (0.02%); title False, H1 False, first 100 words False |
| Links | 4 internal (0.9/1k words); 12 external {'europepmc.org': 12}; new-tab 12/12 |
| Formatting | {'tables': 4, 'captions': 4, 'quotes_with_cite': 12, 'abbr': 2, 'time': 17, 'details': 16, 'images': 0, 'bold_own': 48} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. The two weight figures, and what each trial was
5. The evidence that weight percentages hide
6. Nothing has compared them in people
7. Side by side, from each record
8. Studies that name both compounds
9. One receptor against three
10. Doses: a dose-finding trial against an approved label
11. Side effects, and why one column is far better known
12. Switching: what has been studied
13. Availability: one is a prescription medicine, the other is investigational
14. What the evidence lets you say
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
3. Own prose reads at Flesch 27 (avg sentence 15.7 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 0.9 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 53/100. The accepted items were applied before Part 1 was taken.
- The remaining deductions are reviewer, author, image and ledger size, all `defer-reviewer`, `reject-policy` or properties of a comparison record.
- Confirmed in the built HTML: twelve quotations with citations, the two-trial table showing 338 people against 1,961, and the outcomes section carrying the hazard ratio from the 17,604-person trial.
- Not looped: the exit run confirms the record and nothing else.
