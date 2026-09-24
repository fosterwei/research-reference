# Tesamorelin plus ipamorelin audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: ba24415 (page/tesamorelin-ipamorelin, pre-merge build). Twenty-third page written end to end under the sequencing rule: stages 1-5 in research/intents/tesamorelin-ipamorelin.json before any guide text.

## Part 1: audit

Built from `dist/stacks/tesamorelin-ipamorelin/index.html`.

### Content quality score: 41/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 2 data tables, 7 cited verbatim quotations, measured-absence statements present |
| Expertise | 3/25 | 9 primary-source links; reviewer absent; author absent |
| Authoritativeness | 10/25 | publisher set in JSON-LD; /about exists; 5 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/stacks/tesamorelin-ipamorelin`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 9}).

### Page facts

| | |
|---|---|
| Title (53) | Tesamorelin + Ipamorelin: No Combination Study Exists |
| Description (157) | Tesamorelin plus ipamorelin has never been studied as a combination. The synergy rationale, each component's own trials, the blend problem, doses and status. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/stacks/tesamorelin-ipamorelin |
| H1 / H2 / H3 | ['Tesamorelin plus ipamorelin: a blend that no study has tested, and the class-level synergy its rationale is borrowed from'] / 20 / 0 |
| Words (total / own prose / quoted) | 3963 / 3193 / 138 |
| Readability Flesch, grade, avg sentence: all | 26, 14.4, 19.1 |
| … own prose only | 30, 13.1, 16.1 |
| … quotations only | -35, 34.9, 67.5 |
| Keyword `tesamorelin ipamorelin` | 1× (0.03%); title False, H1 False, first 100 words True |
| Links | 5 internal (1.3/1k words); 9 external {'europepmc.org': 9}; new-tab 9/9 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 7, 'abbr': 0, 'time': 14, 'details': 15, 'images': 0, 'bold_own': 28} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What this combination is
3. This combination in two minutes
4. What has been tested as a combination: nothing
5. Each component on its own evidence
6. Why the two are combined, and what that reasoning rests on
7. What each component has actually shown
8. What has been tested as a combination
9. The pre-mixed vial, and what fixing a ratio does
10. Doses: each component's own, and nothing for the pair
11. Side effects: what each component's trials found
12. Who this is discussed for, and what is unresolved
13. Status: one approved product, one unapproved compound, and a blend that is neither
14. Common mistakes in how this combination is discussed
15. Open questions
16. Questions people ask
17. Sources
18. Reference card
19. Related records
20. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 30 (avg sentence 16.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.3 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| Score 41/100, the lowest of any page written under this loop | `reject-policy` (subject, documented) | The heuristic rewards tables, quotations and primary-source links, and this page's subject is a combination with no studies. Its ledger cannot hold combination evidence because none exists, and inventing proxies would be the failure mode the page exists to correct. What could honestly be added was added: seven inline quotations with citations and nine sources covering the class pharmacology and each component's pivotal trials, which moved quotations from zero to seven. | none | — |
| Zero cited verbatim quotations in the first local run | `accept-record` (done) | The stack layout renders quotations from combination claims, and there are none. Quotations were added inline in the guide prose instead, each with a `cite` link to its abstract: the 1995 synergy sentence, the 1991 dual-site description, the 1997 review, both tesamorelin results and both ipamorelin results. | record | writer |
| Expertise 3/25 with nine primary-source links | `reject-policy` (partial) | The ledger holds the papers that bear on the page: five on the class-level synergy the rationale borrows from, two tesamorelin trials, two ipamorelin trials. There is no tenth paper that would inform a reader about this combination. | none | — |
| The combination-evidence section renders an empty-state banner | no action | That is the intended behaviour and the page's central finding. The guide leads with it rather than burying it. | none | — |
| Class-level synergy evidence uses GHRP-6, not ipamorelin | `accept-record` (boundary, done) | Stated in the guide as the weakest link in the rationale, and recorded in open questions, rather than glossed. | record | writer |
| Tesamorelin's trial detail is carried by another page | `accept-record` (scope, done) | Its own record is deferred under the approved-medicine rule and unwritten, so the page links to the sermorelin comparison where those trials are set out. Revisit if that record is written. | intent map | writer |
| Internal links 1.3/1k words | `accept-template` (partial) | Ipamorelin's record and the sermorelin comparison are linked from guide prose; automatic entity linking remains the open template item. | template | engineer, open |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| Dosage and protocol intent | `reject-policy` (partial) | Content boundary: no dose for the pair appears, because none is published, and the blend section explains that the ratio in a vial was chosen by a seller. Each component's figures stay on its own record. | none | — |
| Cost and vendor queries measured in the same batch | `reject-policy` | Scope rule in docs/content-sop.md; two vendors rank in the top ten for this query and neither is engaged with. | none | — |

## Part 3: exit audit

Built from `dist/stacks/tesamorelin-ipamorelin/index.html`.

### Content quality score: 41/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 2 data tables, 7 cited verbatim quotations, measured-absence statements present |
| Expertise | 3/25 | 9 primary-source links; reviewer absent; author absent |
| Authoritativeness | 10/25 | publisher set in JSON-LD; /about exists; 5 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/stacks/tesamorelin-ipamorelin`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 9}).

### Page facts

| | |
|---|---|
| Title (53) | Tesamorelin + Ipamorelin: No Combination Study Exists |
| Description (157) | Tesamorelin plus ipamorelin has never been studied as a combination. The synergy rationale, each component's own trials, the blend problem, doses and status. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/stacks/tesamorelin-ipamorelin |
| H1 / H2 / H3 | ['Tesamorelin plus ipamorelin: a blend that no study has tested, and the class-level synergy its rationale is borrowed from'] / 20 / 0 |
| Words (total / own prose / quoted) | 3963 / 3193 / 138 |
| Readability Flesch, grade, avg sentence: all | 26, 14.4, 19.1 |
| … own prose only | 30, 13.1, 16.1 |
| … quotations only | -35, 34.9, 67.5 |
| Keyword `tesamorelin ipamorelin` | 1× (0.03%); title False, H1 False, first 100 words True |
| Links | 5 internal (1.3/1k words); 9 external {'europepmc.org': 9}; new-tab 9/9 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 7, 'abbr': 0, 'time': 14, 'details': 15, 'images': 0, 'bold_own': 28} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What this combination is
3. This combination in two minutes
4. What has been tested as a combination: nothing
5. Each component on its own evidence
6. Why the two are combined, and what that reasoning rests on
7. What each component has actually shown
8. What has been tested as a combination
9. The pre-mixed vial, and what fixing a ratio does
10. Doses: each component's own, and nothing for the pair
11. Side effects: what each component's trials found
12. Who this is discussed for, and what is unresolved
13. Status: one approved product, one unapproved compound, and a blend that is neither
14. Common mistakes in how this combination is discussed
15. Open questions
16. Questions people ask
17. Sources
18. Reference card
19. Related records
20. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. No author in structured data (`author` absent).
3. Own prose reads at Flesch 30 (avg sentence 16.1 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.3 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 41/100 between the runs shown, both taken after the quotations were added. The run before them scored the same with zero quotations, which is recorded in the triage.
- The score is the floor for a page whose subject has no evidence. Every component of the heuristic that can be raised honestly on this subject has been raised.
- Confirmed in the built HTML: the empty-combination banner renders, seven quotations carry citation links, and the component table shows ipamorelin's failed trial beside tesamorelin's approval.
- Not looped: the exit run confirms the record and nothing else.
