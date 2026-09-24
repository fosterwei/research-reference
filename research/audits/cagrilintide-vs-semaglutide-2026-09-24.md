# Cagrilintide vs semaglutide audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: ebfa3ad (page/cagrilintide-vs-semaglutide, pre-merge build). Twenty-sixth page written end to end under the sequencing rule.

## Part 1: audit

Built from `dist/compare/cagrilintide-vs-semaglutide/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 3 data tables, 11 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 10 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/cagrilintide-vs-semaglutide`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 10}).

### Page facts

| | |
|---|---|
| Title (56) | Cagrilintide vs Semaglutide: One Trial Tested Both Alone |
| Description (158) | Cagrilintide vs semaglutide: one trial randomised people to each alone. Semaglutide 16.1 per cent, cagrilintide 11.8 per cent, over 68 weeks at the same dose. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/cagrilintide-vs-semaglutide |
| H1 / H2 / H3 | ['Cagrilintide vs semaglutide: one trial gave each of them alone, and semaglutide won'] / 19 / 0 |
| Words (total / own prose / quoted) | 3455 / 2663 / 293 |
| Readability Flesch, grade, avg sentence: all | 13, 16.4, 20.2 |
| … own prose only | 19, 14.9, 17.0 |
| … quotations only | -18, 24.2, 34.0 |
| Keyword `cagrilintide vs semaglutide` | 2× (0.06%); title True, H1 True, first 100 words True |
| Links | 4 internal (1.2/1k words); 10 external {'europepmc.org': 10}; new-tab 10/10 |
| Formatting | {'tables': 3, 'captions': 3, 'quotes_with_cite': 11, 'abbr': 2, 'time': 15, 'details': 13, 'images': 0, 'bold_own': 41} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. The one trial that gave each of them alone
5. Cagrilintide on its own
6. Side by side, from each record
7. The trials each one has behind it
8. Studies that name both compounds
9. Two satiety signals, two different receptors
10. Doses as studied
11. Status: one approved, one investigational
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
3. Own prose reads at Flesch 19 (avg sentence 17.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.2 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| Measured-absence statements absent in the first local run | `accept-record` (done) | The page is unusual in having a direct answer, so the absences were phrased positively and the check found none. Rewritten so the open question about outcome data reads as the absence it is. | record | writer |
| A meta-analysis of 5,425 participants and two pharmacokinetic studies were drafted as clinical trials | `accept-record` (done) + `accept-script` (open) | The same relabelling applied on the CagriSema record, which shares these sources. Standing design-filter item. | record, script | writer done; engineer open |
| The two semaglutide landmark trials were missing from the ledger | `accept-record` (done) | A comparison ledger built from papers naming both compounds contained neither STEP 1 nor the cardiovascular outcome trial, although the page's second-largest claim rests on them. Added by hand. | record | writer |
| Semaglutide is an approved medicine, which the queue defers | `reject-policy` (scope, documented) | Same judgment as the sermorelin and retatrutide comparisons, with the opposite evidence: this results set is held by the New England Journal, PubMed, the Lancet and specialist trade press. The page is written not because the results set is weak but because it can be answered correctly from trial arms, and because the comparison record already existed. | none | — |
| Expertise 9/25 with ten primary-source links | `reject-policy` (partial) | Ten is the literature that bears on the comparison. Both compound records are linked and carry 31 and 27 sources. | none | — |
| Internal links 1.2/1k words | `accept-template` (partial) | Both compound records and the CagriSema stack are linked from guide prose; automatic entity linking remains the open template item. | template | engineer, open |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| The arm-level figures are manufacturer announcements rather than published numbers | `accept-record` (boundary, done) | Stated where they appear, with the estimand difference explained and cross-referenced to the CagriSema page, and recorded in open questions. | record | writer |
| The dosage cluster, 2,136 at KD 0, is redirected | `accept-record` (scope, done) | Cagrilintide's own record is written and carries its dose detail. | intent map | writer |

## Part 3: exit audit

Built from `dist/compare/cagrilintide-vs-semaglutide/index.html`.

### Content quality score: 53/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 3 data tables, 11 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 10 primary-source links; reviewer absent; author absent |
| Authoritativeness | 13/25 | publisher set in JSON-LD; /about exists; 4 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compare/cagrilintide-vs-semaglutide`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 10}).

### Page facts

| | |
|---|---|
| Title (56) | Cagrilintide vs Semaglutide: One Trial Tested Both Alone |
| Description (158) | Cagrilintide vs semaglutide: one trial randomised people to each alone. Semaglutide 16.1 per cent, cagrilintide 11.8 per cent, over 68 weeks at the same dose. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/compare/cagrilintide-vs-semaglutide |
| H1 / H2 / H3 | ['Cagrilintide vs semaglutide: one trial gave each of them alone, and semaglutide won'] / 19 / 0 |
| Words (total / own prose / quoted) | 3455 / 2663 / 293 |
| Readability Flesch, grade, avg sentence: all | 13, 16.4, 20.2 |
| … own prose only | 19, 14.9, 17.0 |
| … quotations only | -18, 24.2, 34.0 |
| Keyword `cagrilintide vs semaglutide` | 2× (0.06%); title True, H1 True, first 100 words True |
| Links | 4 internal (1.2/1k words); 10 external {'europepmc.org': 10}; new-tab 10/10 |
| Formatting | {'tables': 3, 'captions': 3, 'quotes_with_cite': 11, 'abbr': 2, 'time': 15, 'details': 13, 'images': 0, 'bold_own': 41} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. The short answer
3. The comparison in two minutes
4. The one trial that gave each of them alone
5. Cagrilintide on its own
6. Side by side, from each record
7. The trials each one has behind it
8. Studies that name both compounds
9. Two satiety signals, two different receptors
10. Doses as studied
11. Status: one approved, one investigational
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
3. Own prose reads at Flesch 19 (avg sentence 17.0 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.2 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score moved from 51 to the figure shown when the absence statement was rewritten; the rest of the heuristic is unchanged.
- The remaining deductions are reviewer, author, image and ledger size, all `defer-reviewer`, `reject-policy` or properties of a comparison record.
- Confirmed in the built HTML: the four-arm table renders with both monotherapy rows, eleven quotations carry citations, and the estimand caveat sits with the figures it qualifies.
- Not looped: the exit run confirms the record and nothing else.
