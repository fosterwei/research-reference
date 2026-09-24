# Selank and semax stack audit, 2026-09-24

Preview: Vercel preview protected (302); audited the local build of the same commit per docs/content-automation.md step 3.   Commit: 751def0 (page/selank-semax, pre-merge build). Twenty-eighth page written end to end under the sequencing rule.

## Part 1: audit

Built from `dist/stacks/selank-semax/index.html`.

### Content quality score: 41/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 2 data tables, 8 cited verbatim quotations, measured-absence statements present |
| Expertise | 3/25 | 8 primary-source links; reviewer absent; author absent |
| Authoritativeness | 10/25 | publisher set in JSON-LD; /about exists; 5 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/stacks/selank-semax`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 8}).

### Page facts

| | |
|---|---|
| Title (50) | Selank and Semax Together: Overlap, Not Complement |
| Description (147) | Selank and semax stack: the seven studies naming both, the shared enzyme target, the shared tripeptide tail, and what a combined nasal spray fixes. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/stacks/selank-semax |
| H1 / H2 / H3 | ['Selank and semax together: seven studies name both, none gave both to a person, and at one measured point they do the same thing'] / 19 / 0 |
| Words (total / own prose / quoted) | 3269 / 2467 / 219 |
| Readability Flesch, grade, avg sentence: all | 31, 13.8, 19.5 |
| … own prose only | 37, 12.1, 15.9 |
| … quotations only | -12, 22.6, 31.0 |
| Keyword `selank semax` | 0× (0.00%); title False, H1 False, first 100 words True |
| Links | 5 internal (1.5/1k words); 8 external {'europepmc.org': 8}; new-tab 8/8 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 8, 'abbr': 0, 'time': 13, 'details': 13, 'images': 0, 'bold_own': 11} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What this combination is
3. This combination in two minutes
4. What has been tested as a combination
5. Each component on its own evidence
6. What the seven studies naming both actually show
7. Where the two overlap, and why that matters for stacking
8. What has been tested as a combination
9. The combined nasal spray, and what it fixes
10. Doses: each component's own
11. Safety: what is known, and for which products
12. Who this is discussed for, and what is unresolved
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
3. Own prose reads at Flesch 37 (avg sentence 15.9 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.5 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Precedent: every audit since ipamorelin. | record | — |
| Expertise 3/25 on eight primary-source links | `reject-policy` | Eight is every indexed paper that names both compounds, which is the whole of this record's subject. Both component records are linked and carry 34 and 38 sources. Padding would raise the number and inform nobody. | none | — |
| Three drafted labels described what the studies were not | `accept-record` (done) | A functional-MRI study in 52 people was filed as a generic human study, a forensic analysis of seized products as an in-vitro study, and the enzyme experiment likewise. Relabelled so the evidence table can be read at a glance. | record | writer |
| Score 41/100, the same floor as the other no-combination stacks | `reject-policy` (subject, documented) | The heuristic rewards tables, quotations and source counts. This subject has eight papers and no combination study; seven of the eight are quoted and two tables are the honest number. Precedent: tesamorelin-plus-ipamorelin and the glow stack, both 41. | none | — |
| Internal links 1.5/1k words | `accept-template` (partial) | Both component records and the comparison page are linked from guide prose; automatic entity linking remains the open template item. | template | engineer, open |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com | no action | Local build without SITE_URL; Vercel resolves the host. Not a page defect. | none | — |
| Overlap with the selank-versus-semax comparison written earlier today | no action, measured | Uniqueness clears the gate. The comparison answers which to choose; this page answers whether taking both adds anything, and its central evidence, the shared enzyme target, appears only here. | none | — |
| Dosage intent | `reject-policy` (partial) | Content boundary: no dose for the pair is published, so none appears, and the component figures stay on their own records. | none | — |
| Vendor product queries in the measured set | `reject-policy` | Scope rule in docs/content-sop.md; a vendor selling both in one spray ranks seventh and is described rather than engaged with. | none | — |

## Part 3: exit audit

Built from `dist/stacks/selank-semax/index.html`.

### Content quality score: 41/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 12/20 | 2 data tables, 8 cited verbatim quotations, measured-absence statements present |
| Expertise | 3/25 | 8 primary-source links; reviewer absent; author absent |
| Authoritativeness | 10/25 | publisher set in JSON-LD; /about exists; 5 internal links |
| Trustworthiness | 16/30 | canonical `https://example.com/stacks/selank-semax`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'europepmc.org': 8}).

### Page facts

| | |
|---|---|
| Title (50) | Selank and Semax Together: Overlap, Not Complement |
| Description (147) | Selank and semax stack: the seven studies naming both, the shared enzyme target, the shared tripeptide tail, and what a combined nasal spray fixes. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://example.com/stacks/selank-semax |
| H1 / H2 / H3 | ['Selank and semax together: seven studies name both, none gave both to a person, and at one measured point they do the same thing'] / 19 / 0 |
| Words (total / own prose / quoted) | 3269 / 2467 / 219 |
| Readability Flesch, grade, avg sentence: all | 31, 13.8, 19.5 |
| … own prose only | 37, 12.1, 15.9 |
| … quotations only | -12, 22.6, 31.0 |
| Keyword `selank semax` | 0× (0.00%); title False, H1 False, first 100 words True |
| Links | 5 internal (1.5/1k words); 8 external {'europepmc.org': 8}; new-tab 8/8 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 8, 'abbr': 0, 'time': 13, 'details': 13, 'images': 0, 'bold_own': 11} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-24'] |

### H2 sequence

1. At a glance
2. What this combination is
3. This combination in two minutes
4. What has been tested as a combination
5. Each component on its own evidence
6. What the seven studies naming both actually show
7. Where the two overlap, and why that matters for stacking
8. What has been tested as a combination
9. The combined nasal spray, and what it fixes
10. Doses: each component's own
11. Safety: what is known, and for which products
12. Who this is discussed for, and what is unresolved
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
3. Own prose reads at Flesch 37 (avg sentence 15.9 words). Quotations are verbatim by policy; this measures only the text we wrote.
4. Internal links 1.5 per 1,000 words (guideline 3–5).
5. No image, so no image alt text carrying the keyword (design.md requires none; note only).


### Comparison with Part 1

- Score unchanged at 41/100. Every accepted item was applied before Part 1 was taken.
- The floor for a stack with no combination study, reached by the two other such pages written under this loop.
- Confirmed in the built HTML: the seven-study table renders with each paper's type, and the enzyme finding is quoted with its citation in the overlap section.
- Not looped: the exit run confirms the record and nothing else.
