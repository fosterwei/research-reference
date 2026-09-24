# Retatrutide with MOTS-c audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: 3cf0b06 (page/retatrutide-mots-c, pre-merge build). Twenty-ninth page written end to end under the sequencing rule.

## Part 1: audit

Built from `dist/stacks/retatrutide-mots-c/index.html`.

### Content quality score: 43/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 2 data tables, 5 cited verbatim quotations, measured-absence statements present |
| Expertise | 3/25 | 5 primary-source links; reviewer absent; author absent |
| Authoritativeness | 12/25 | publisher set in JSON-LD; /about exists; 8 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/stacks/retatrutide-mots-c`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 5}).

### Page facts

| | |
|---|---|
| Title (58) | Retatrutide + MOTS-c: No Study, and MOTS-c Was Never Given |
| Description (160) | Retatrutide with MOTS-c: no study has tested the pair, and no published study has ever given MOTS-c to a person. Its human research measures circulating levels. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/stacks/retatrutide-mots-c |
| H1 / H2 / H3 | ['Retatrutide with MOTS-c: no study has tested the pair, and none has ever given MOTS-c to a person'] / 19 / 0 |
| Words (total / own prose / quoted) | 3079 / 2404 / 116 |
| Readability Flesch, grade, avg sentence: all | 29, 13.5, 17.6 |
| … own prose only | 32, 12.5, 14.5 |
| … quotations only | -61, 48.9, 109.0 |
| Keyword `retatrutide mots c` | 0× (0.00%); title False, H1 False, first 100 words False |
| Links | 8 internal (2.6/1k words); 5 external {'europepmc.org': 5}; new-tab 5/5 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 5, 'abbr': 0, 'time': 10, 'details': 13, 'images': 0, 'bold_own': 18} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What this stack is
3. This stack in two minutes
4. What has been tested as a combination
5. What MOTS-c's human literature actually measured
6. Each component on its own evidence
7. Why the two are paired, and what that rests on
8. What has been tested as a combination
9. Doses: one from a trial, one from rodents
10. Side effects: one well characterised, one unknown
11. Who this is discussed for, and what is unresolved
12. Status: neither is available
13. Common mistakes in how this stack is discussed
14. Open questions
15. Questions people ask
16. Sources
17. Reference card
18. Related records
19. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 32 (avg sentence 14.5 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 2.6 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| The first local run had one source and no quotations | `accept-record` (done) | The page's central claim is that MOTS-c's human literature measures rather than administers, so the four studies behind it were added and quoted inline with citation links, alongside the retatrutide trial. Five sources and five quotations. | record | writer |
| Expertise 3/25 with five primary-source links | `reject-policy` (partial) | Five is what bears on this page: the four human MOTS-c studies that establish the measured-not-given finding and the retatrutide trial. MOTS-c's own record carries 45 sources and is linked; padding this ledger with them would restate that record rather than inform this one. | none | — |
| Score 43/100 | `reject-policy` (subject, documented) | The floor for a stack with no combination evidence, as on the tesamorelin-plus-ipamorelin, glow and selank-semax pages. | none | — |
| The combination ledger is empty | no action | That is the finding and the guide leads with it. | none | — |
| Internal links 2.6/1k words | no action | The highest of any page written under this loop, because the argument needs the four records where the same measured-not-given pattern appears. | none | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| The incumbent ranks second for this query with 7,846 words and twelve dosing tables | `reject-policy` (partial) | Its warnings are accurate and its protocol is not, and this page says both. The response is the evidence check it omits, not a longer protocol. | none | — |
| Dosage intent | `reject-policy` (partial) | Content boundary: no dose for the pair is published; MOTS-c's published doses are rodent milligrams per kilogram, which are named as such and not converted. | none | — |
| The stack phrasings measure zero clickstream | no action, measured | Recorded with the Google Ads volume beside it, which is the signature of a product marketed ahead of its audience, and the page says so. | none | — |

## Part 3: exit audit

Built from `dist/stacks/retatrutide-mots-c/index.html`.

### Content quality score: 43/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 2 data tables, 5 cited verbatim quotations, measured-absence statements present |
| Expertise | 3/25 | 5 primary-source links; reviewer absent; author absent |
| Authoritativeness | 12/25 | publisher set in JSON-LD; /about exists; 8 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/stacks/retatrutide-mots-c`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 5}).

### Page facts

| | |
|---|---|
| Title (58) | Retatrutide + MOTS-c: No Study, and MOTS-c Was Never Given |
| Description (160) | Retatrutide with MOTS-c: no study has tested the pair, and no published study has ever given MOTS-c to a person. Its human research measures circulating levels. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/stacks/retatrutide-mots-c |
| H1 / H2 / H3 | ['Retatrutide with MOTS-c: no study has tested the pair, and none has ever given MOTS-c to a person'] / 19 / 0 |
| Words (total / own prose / quoted) | 3079 / 2404 / 116 |
| Readability Flesch, grade, avg sentence: all | 29, 13.5, 17.6 |
| … own prose only | 32, 12.5, 14.5 |
| … quotations only | -61, 48.9, 109.0 |
| Keyword `retatrutide mots c` | 0× (0.00%); title False, H1 False, first 100 words False |
| Links | 8 internal (2.6/1k words); 5 external {'europepmc.org': 5}; new-tab 5/5 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 5, 'abbr': 0, 'time': 10, 'details': 13, 'images': 0, 'bold_own': 18} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What this stack is
3. This stack in two minutes
4. What has been tested as a combination
5. What MOTS-c's human literature actually measured
6. Each component on its own evidence
7. Why the two are paired, and what that rests on
8. What has been tested as a combination
9. Doses: one from a trial, one from rodents
10. Side effects: one well characterised, one unknown
11. Who this is discussed for, and what is unresolved
12. Status: neither is available
13. Common mistakes in how this stack is discussed
14. Open questions
15. Questions people ask
16. Sources
17. Reference card
18. Related records
19. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 32 (avg sentence 14.5 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 2.6 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 43/100 between the runs shown, both taken after the four MOTS-c studies were added and quoted.
- The earlier run, with one source and no quotations, is recorded in the triage.
- Confirmed in the built HTML: the table of what each human MOTS-c study measured renders, and five quotations carry citation links.
- Not looped: the exit run confirms the record and nothing else.
