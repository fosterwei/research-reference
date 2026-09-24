# Ipamorelin vs GHRP-6 audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: 91b7529 (page/ipamorelin-vs-ghrp-6, pre-merge build). Twenty-seventh page written end to end under the sequencing rule.

## Part 1: audit

Built from `dist/compare/ipamorelin-vs-ghrp-6/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 2 data tables, 13 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 11 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/ipamorelin-vs-ghrp-6`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 11}).

### Page facts

| | |
|---|---|
| Title (56) | Ipamorelin vs GHRP-6: Selectivity, and Two Failed Trials |
| Description (136) | Ipamorelin vs GHRP-6: selectivity, potency, the rat comparisons, and the randomised human trials in which neither compound beat placebo. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/ipamorelin-vs-ghrp-6 |
| H1 / H2 / H3 | ['Ipamorelin vs GHRP-6: the same receptor, one designed not to raise cortisol, and no human comparison'] / 19 / 0 |
| Words (total / own prose / quoted) | 3457 / 2569 / 398 |
| Readability Flesch, grade, avg sentence: all | 23, 15.0, 19.8 |
| … own prose only | 28, 13.3, 16.0 |
| … quotations only | 4, 22.5, 39.3 |
| Keyword `ipamorelin vs ghrp 6` | 0× (0.00%); title False, H1 False, first 100 words False |
| Links | 4 internal (1.2/1k words); 11 external {'europepmc.org': 11}; new-tab 11/11 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 13, 'abbr': 0, 'time': 16, 'details': 13, 'images': 0, 'bold_own': 35} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. Selectivity: the whole of the difference
5. What each has shown in people
6. The direct comparisons, which are in rats
7. Side by side, from each record
8. Studies that name both compounds
9. The rest of the family, briefly
10. Doses as studied
11. Status: neither is an approved medicine
12. What the evidence lets you say
13. Common mistakes in this comparison
14. Open questions
15. Questions people ask
16. Sources
17. Reference card
18. Related records
19. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 28 (avg sentence 16.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.2 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| The guide cited two trials that were not in this record's ledger | `accept-record` (done, self-caught) | The page's central claim is that neither compound changed a clinical outcome, and the two trials behind it, ipamorelin's postoperative-ileus study and GHRP-6's 2026 stroke trial, sat in the compound records rather than here. Both added by hand with the pharmacokinetic and diagnostic-testing studies, so every statement on the page can be checked from its own sources. | record | writer |
| Expertise 6/25 in the first local run, on eight sources | `accept-record` (done) + `reject-policy` (partial) | Eleven after the additions. A comparison ledger of two unapproved research compounds is small because the literature is; both compound records are linked and carry 30 and 48 sources. | record | writer |
| The seven drafted head-to-head claims are all animal or analytical work | no action | They are genuine direct comparisons, which is rare here, and the guide says so and quotes their doses. Nothing to correct. | none | — |
| Internal links 1.2/1k words | `accept-template` (partial) | Both compound records and the CJC-1295 stack are linked from guide prose; automatic entity linking remains the open template item. | template | engineer, open |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| The cluster is 201 searches, the smallest in the queue | no action, measured | Recorded rather than used as a reason to skip. Google Ads volume exceeds clickstream on almost every term, which is vendors bidding on a question researchers rarely type, and the page exists because the record existed and would otherwise render without content. | none | — |
| Dosage intent | `reject-policy` (partial) | Content boundary: the rat comparison's doses appear because a study gave them; human dose figures stay on the compound records. | none | — |

## Part 3: exit audit

Built from `dist/compare/ipamorelin-vs-ghrp-6/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 2 data tables, 13 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 11 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/ipamorelin-vs-ghrp-6`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 11}).

### Page facts

| | |
|---|---|
| Title (56) | Ipamorelin vs GHRP-6: Selectivity, and Two Failed Trials |
| Description (136) | Ipamorelin vs GHRP-6: selectivity, potency, the rat comparisons, and the randomised human trials in which neither compound beat placebo. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/ipamorelin-vs-ghrp-6 |
| H1 / H2 / H3 | ['Ipamorelin vs GHRP-6: the same receptor, one designed not to raise cortisol, and no human comparison'] / 19 / 0 |
| Words (total / own prose / quoted) | 3457 / 2569 / 398 |
| Readability Flesch, grade, avg sentence: all | 23, 15.0, 19.8 |
| … own prose only | 28, 13.3, 16.0 |
| … quotations only | 4, 22.5, 39.3 |
| Keyword `ipamorelin vs ghrp 6` | 0× (0.00%); title False, H1 False, first 100 words False |
| Links | 4 internal (1.2/1k words); 11 external {'europepmc.org': 11}; new-tab 11/11 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 13, 'abbr': 0, 'time': 16, 'details': 13, 'images': 0, 'bold_own': 35} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. Selectivity: the whole of the difference
5. What each has shown in people
6. The direct comparisons, which are in rats
7. Side by side, from each record
8. Studies that name both compounds
9. The rest of the family, briefly
10. Doses as studied
11. Status: neither is an approved medicine
12. What the evidence lets you say
13. Common mistakes in this comparison
14. Open questions
15. Questions people ask
16. Sources
17. Reference card
18. Related records
19. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 28 (avg sentence 16.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.2 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score moved between the first local run and Part 1 when the two trials behind the page's central claim were added to the ledger.
- Part 1 and Part 3 agree: no further change was made after the additions.
- Confirmed in the built HTML: the human-evidence table renders with both failed trials, and the rat comparison quotes its doses.
- Not looped: the exit run confirms the record and nothing else.
