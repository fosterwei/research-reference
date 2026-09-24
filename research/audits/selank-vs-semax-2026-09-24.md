# Selank vs semax audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: 8f34890 (page/selank-vs-semax, pre-merge build). Twenty-second page written end to end under the sequencing rule: stages 1-5 in research/intents/selank-vs-semax.json before any guide text, with the map corrected in its own commit when the head-to-head study was found.

## Part 1: audit

Built from `dist/compare/selank-vs-semax/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 2 data tables, 10 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 10 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/selank-vs-semax`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 10}).

### Page facts

| | |
|---|---|
| Title (56) | Selank vs Semax: Trials, Shared Design, and What Is Sold |
| Description (159) | Selank vs semax: one study has given both to the same people. What each was tested for, the design they share, and why the forms sold in the West are untested. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/selank-vs-semax |
| H1 / H2 / H3 | ['Selank vs semax: two Russian peptides built on the same tail, tested for different things, and compared head to head exactly once'] / 21 / 0 |
| Words (total / own prose / quoted) | 4626 / 3727 / 268 |
| Readability Flesch, grade, avg sentence: all | 27, 14.6, 20.5 |
| … own prose only | 32, 13.1, 17.6 |
| … quotations only | 8, 18.6, 26.0 |
| Keyword `selank vs semax` | 2× (0.04%); title True, H1 True, first 100 words True |
| Links | 4 internal (0.9/1k words); 10 external {'europepmc.org': 10}; new-tab 10/10 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 10, 'abbr': 0, 'time': 15, 'details': 16, 'images': 0, 'bold_own': 37} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. The one study that gave both to the same people
5. Same tail, different heads: how both were built
6. Side by side, from each record
7. What each one was tested for, and in whom
8. What is actually sold: the acetylated and amidated versions
9. Doses and routes
10. Side effects, and how thin the safety evidence is
11. Taking both: what has been tested
12. Legal status: approved in Russia, unapproved everywhere else
13. Studies that name both compounds
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
3. Own prose reads at Flesch 32 (avg sentence 17.6 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 0.9 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| The only study that gave both compounds to people was missing from the ledger | `accept-record` (done) + `accept-script` (open) | The 2020 functional-MRI study in 52 healthy participants sits in both compound records and ranks seventh on the target query, and the comparison record did not have it. Added by hand with eight trial papers from the two compound records, and the intent map's H1, dek, information gain and boundary sentences were corrected before any guide text was written. The head-to-head fetcher needs to search each side's record as well as the pair. | record, script | writer done; engineer open |
| The two drafted head-to-head claims are animal work | `accept-record` (done) | Kept and labelled. One of them, a rat study of the tripeptide both compounds share at one end, turned out to be the most interesting fact about the pair and carries a guide section. | record | writer |
| Both compound records carry alias misfires | `accept-record` (open, other records) | An orthodontic measurement abbreviated SeMax and unrelated papers matched to Selank appear as human rows on those records. Noticed while writing this page; logged for those records rather than fixed here. | record | writer, open |
| Internal links 0.9/1k words | `accept-template` (partial) | Both compound records, the comparison directory and the compound directory are linked from guide prose, which took the count from three to four. A comparison page has two subjects and few natural internal targets; automatic entity linking remains the open template item. | template | engineer, open |
| Expertise 9/25 with 10 primary-source links | `reject-policy` (partial) | The ledger is the studies that bear on the comparison. The compound records carry 34 and 38 sources and are linked from the page. | none | — |
| Own-prose Flesch 32 | no action | Above the site's usual range, because this page's subject allows plainer sentences than a dosing page does. Recorded for comparison with the other audits. | none | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| Component queries for dose and form (42,432 for the two names alone) are redirected rather than answered | `accept-record` (scope, done) | Both compounds have written records carrying their dosing detail. Duplicating it here would split the site against itself, which is the opposite of the judgment made on the sermorelin comparison, where neither compound record was written. | intent map | writer |
| The acetylated forms sold in the West have no trial evidence to cite | `accept-record` (measured absence, done) | The absence is the finding and is stated as one, in a guide section and in open questions. Precedent: FOXO4-DRI's human-trial section. | record | writer |
| Dosage intent | `reject-policy` (partial) | Content boundary: dose figures live on each compound's record with their own sources, and this page points there rather than repeating them. | none | — |

## Part 3: exit audit

Built from `dist/compare/selank-vs-semax/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 2 data tables, 10 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 10 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/selank-vs-semax`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 10}).

### Page facts

| | |
|---|---|
| Title (56) | Selank vs Semax: Trials, Shared Design, and What Is Sold |
| Description (159) | Selank vs semax: one study has given both to the same people. What each was tested for, the design they share, and why the forms sold in the West are untested. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/selank-vs-semax |
| H1 / H2 / H3 | ['Selank vs semax: two Russian peptides built on the same tail, tested for different things, and compared head to head exactly once'] / 21 / 0 |
| Words (total / own prose / quoted) | 4626 / 3727 / 268 |
| Readability Flesch, grade, avg sentence: all | 27, 14.6, 20.5 |
| … own prose only | 32, 13.1, 17.6 |
| … quotations only | 8, 18.6, 26.0 |
| Keyword `selank vs semax` | 2× (0.04%); title True, H1 True, first 100 words True |
| Links | 4 internal (0.9/1k words); 10 external {'europepmc.org': 10}; new-tab 10/10 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 10, 'abbr': 0, 'time': 15, 'details': 16, 'images': 0, 'bold_own': 37} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. The one study that gave both to the same people
5. Same tail, different heads: how both were built
6. Side by side, from each record
7. What each one was tested for, and in whom
8. What is actually sold: the acetylated and amidated versions
9. Doses and routes
10. Side effects, and how thin the safety evidence is
11. Taking both: what has been tested
12. Legal status: approved in Russia, unapproved everywhere else
13. Studies that name both compounds
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
3. Own prose reads at Flesch 32 (avg sentence 17.6 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 0.9 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 53/100 between the two runs shown. Both were taken after the ledger correction; the run before it is described in the triage row about the missing head-to-head study.
- One accepted item landed between the runs that preceded these: two navigation links were added to the choosing section, taking internal links from three to four.
- The remaining deductions are reviewer, author, image and ledger size, all `defer-reviewer`, `reject-policy` or properties of a comparison record.
- Not looped: the exit run confirms the record and nothing else.
