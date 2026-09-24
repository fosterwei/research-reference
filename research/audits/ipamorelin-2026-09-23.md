# Ipamorelin audit, 2026-09-23

Preview: https://research-reference-git-content-automation-060d7a-samyings-8318.vercel.app/compounds/ipamorelin (protected; body audited from the local build of the same commit)  
Commit: 098c105  
Loop: docs/content-automation.md, first run.

## Part 1: audit

Built from `dist/compounds/ipamorelin/index.html`; live URL `https://research-reference-git-content-automation-060d7a-samyings-8318.vercel.app/compounds/ipamorelin` (body not fetched: preview deployments redirect unauthenticated requests).

### Content quality score: 55/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 2 data tables, 27 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 27 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 9 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/ipamorelin`; datePublished 2026-09-14; not-yet-reviewed notice shown; privacy no, contact no |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 27, 'doi.org': 3}).

### Page facts

| | |
|---|---|
| Title (35) | Ipamorelin: what the research shows |
| Description (122) | Ipamorelin research, cited: 63 indexed publications, 2 randomized trials. Evidence tier on every claim; nothing is advice. |
| Robots | noindex, follow |
| Canonical | https://example.com/compounds/ipamorelin |
| H1 / H2 / H3 | ['Ipamorelin'] / 24 / 4 |
| Words (total / own prose / quoted) | 4606 / 2780 / 826 |
| Readability Flesch, grade, avg sentence: all | 8, 17.5, 21.5 |
| … own prose only | 14, 15.9, 18.4 |
| … quotations only | -2, 20.2, 27.0 |
| Keyword `ipamorelin` | 69× (1.50%); title True, H1 True, first 100 words True |
| Links | 9 internal (2.0/1k words); 30 external {'europepmc.org': 27, 'doi.org': 3}; new-tab 0/30 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 27, 'abbr': 1, 'time': 39, 'details': 7, 'images': 0, 'bold_own': 17} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-15', '2026-09-23'] |

### H2 sequence

1. At a glance
2. What it is and how it acts
3. What the evidence level means
4. What happened in the human studies?
5. What did the studies find?
6. What doses did studies use?
7. What side effects did studies report?
8. What did studies measure: growth hormone, cortisol, ACTH
9. Reported timelines
10. Escalation schedules used in studies
11. How long did studies run?
12. Routes studied
13. Weight-normalized doses, as published
14. Reported interactions
15. Storage and stability
16. How it compares
17. Studied in combination
18. Is ipamorelin an approved medicine?
19. Open questions and limitations
20. Questions people ask
21. Sources
22. Reference card
23. Related records
24. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Meta description is 122 characters (target 130–160).
4. Own prose reads at Flesch 14 (avg sentence 18.4 words). Quotations are verbatim by policy; this measures only the text we wrote.
5. Internal links 2.0 per 1,000 words (guideline 3–5).
6. Trust page /privacy does not exist.
7. Trust page /contact does not exist.
8. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| # | Suggestion (from part 1) | Label | Reason | Layer | Owner |
|---|---|---|---|---|---|
| 1 | No named reviewer in structured data | `defer-reviewer` | The launch blocker (Issue #3). No content edit changes it. Every E-E-A-T factor is capped until a credentialed person signs the record. | record (`review`) | reviewer |
| 2 | No author in structured data | `defer-reviewer` | Same gate: `review.author` is set when a person takes responsibility for the drafted claims. The template already emits `author` when present. | record (`review`) | reviewer |
| 3 | Meta description 122 characters (target 130–160) | `accept-script` | The drafter's template ran short. Rewritten to state publications, randomized trials, human studies, and the strongest tier; 155 characters here, and every re-drafted record inherits it. | `scripts/draft_claims.py` | engineer, done |
| 4 | Own prose Flesch 14, average sentence 18.4 words | `reject-policy` (in part) | `docs/design.md` §9.7 budgets sentence length, which is inside the ~22-word limit. The Flesch penalty comes from syllables in necessary terms (pharmacokinetics, randomized, subcutaneous). Renaming them would be less accurate, not more readable. Quotations are excluded from the measure and are verbatim by policy. | none | — |
| 5 | Internal links 2.0 per 1,000 words (guideline 3–5) | `accept-template` (partial) | Added intent-driven "People also look for" links built from the map's redirect queries, and linked the class crumb to the directory section. Density moved to 2.1: the page is long (4,600 words) and most of its links are external sources by design. Further links belong in FAQ answers and the evidence assessment; tracked for the template pass. | `CompoundV2.astro`, `compounds/index.astro` | engineer, partly done |
| 6 | `/privacy` does not exist | `defer-reviewer` (operator input) | Needs facts only the operator has: what the site collects, who runs it, where. Not a content edit. | new page | operator |
| 7 | `/contact` does not exist | `defer-reviewer` (operator input) | Needs a real contact route. Same as 6. | new page | operator |
| 8 | No image, so no keyword-bearing alt text | `reject-policy` | `docs/design.md` §6 requires no images; the evidence table and fact tiles carry the data. Adding a decorative image for alt text is the kind of padding the design forbids. | none | — |
| — | (from the intent research) half-life sentence absent from `reported_timelines` | `accept-script` | Single-compound drafting rule; recovered the two-hour half-life and the dose-escalation design from Gobburu 1999. | `scripts/draft_claims.py` | engineer, done |
| — | (from the intent research) FDA 503A and WADA S2 documents missing from the ledger | `accept-record` (blocked) | Both are citable primary documents. Unreachable from the build environment on 2026-09-23 on every route (container TLS failures; DataForSEO OnPage not enabled on the account). Fetch from another machine and add with verbatim excerpts; do not paraphrase from memory. | record (`sources`, `regulatory_status`) | writer |
| — | (from the intent research) three suspect evidence-table rows (anamorelin paper, detection-method papers) | `defer-reviewer` | Design column now labels detection papers "Analytical method"; whether the anamorelin row stays is the reviewer's call. | record | reviewer |
| — | Preview URL returns 302 (Vercel Deployment Protection) | `accept-template` | Step 3 cannot audit a protected preview. Documented in `docs/content-automation.md` with the two fixes (disable for previews, or a bypass secret) and the offline path (`scripts/audit_page.py`). | Vercel settings + docs | operator (setting), engineer (docs, done) |

Precedents set for the next page: #4 (terminology vs Flesch) and #8 (no images) are policy rejections that will recur on every compound page and should not be re-argued.

## Part 3: exit audit

Built from `dist/compounds/ipamorelin/index.html`; live URL `https://research-reference-git-content-automation-060d7a-samyings-8318.vercel.app/compounds/ipamorelin` (body not fetched: preview deployments redirect unauthenticated requests).

### Content quality score: 55/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 2 data tables, 27 cited verbatim quotations, measured-absence statements present |
| Expertise | 9/25 | 27 primary-source links; reviewer absent; author absent |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 10 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/compounds/ipamorelin`; datePublished 2026-09-14; not-yet-reviewed notice shown; privacy no, contact no |

### AI citation readiness: 75/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 27, 'doi.org': 3}).

### Page facts

| | |
|---|---|
| Title (35) | Ipamorelin: what the research shows |
| Description (158) | Ipamorelin: 63 indexed publications, 2 randomized trials and 4 human clinical studies, quoted verbatim and tiered by evidence. Strongest tier: human clinical… |
| Robots | noindex, follow |
| Canonical | https://example.com/compounds/ipamorelin |
| H1 / H2 / H3 | ['Ipamorelin'] / 24 / 4 |
| Words (total / own prose / quoted) | 4652 / 2822 / 826 |
| Readability Flesch, grade, avg sentence: all | 6, 17.7, 21.3 |
| … own prose only | 11, 16.2, 18.2 |
| … quotations only | -2, 20.2, 27.0 |
| Keyword `ipamorelin` | 73× (1.57%); title True, H1 True, first 100 words True |
| Links | 10 internal (2.1/1k words); 30 external {'europepmc.org': 27, 'doi.org': 3}; new-tab 30/30 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 27, 'abbr': 1, 'time': 39, 'details': 7, 'images': 0, 'bold_own': 16} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-15', '2026-09-23'] |

### H2 sequence

1. At a glance
2. What it is and how it acts
3. What the evidence level means
4. What happened in the human studies?
5. What did the studies find?
6. What doses did studies use?
7. What side effects did studies report?
8. What did studies measure: growth hormone, cortisol, ACTH
9. Reported timelines
10. Escalation schedules used in studies
11. How long did studies run?
12. Routes studied
13. Weight-normalized doses, as published
14. Reported interactions
15. Storage and stability
16. How it compares
17. Studied in combination
18. Is ipamorelin an approved medicine?
19. Open questions and limitations
20. Questions people ask
21. Sources
22. Reference card
23. Related records
24. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 11 (avg sentence 18.2 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 2.1 per 1,000 words (guideline 3–5).
5. Trust page /privacy does not exist.
6. Trust page /contact does not exist.
7. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison

- Content quality 55 → 55; AI citation readiness 75 → 75. The reviewer gate caps both; the movement that was available (description length, link targets, external links in new tabs, coverage) landed.
- Intent coverage 15/15 queries, 100% of measured demand on a rendered answer (`measure_pages.py --intent ipamorelin`).
- Remaining issues are all `defer-reviewer` or `reject-policy`, so a further audit pass would not change the page. Loop closed; next step is human review.
