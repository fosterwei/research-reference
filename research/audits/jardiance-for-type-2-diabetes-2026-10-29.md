# jardiance-for-type-2-diabetes audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/jardiance-for-type-2-diabetes.json were written before the page.

## Part 1: audit


Built from `dist/blog/jardiance-for-type-2-diabetes/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 38 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 13 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/jardiance-for-type-2-diabetes`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.accessdata.fda.gov': 22, 'europepmc.org': 38, 'www.novonordisk-us.com': 2}).

### Page facts

| | |
|---|---|
| Title (52) | Jardiance for Type 2 Diabetes: SGLT2, A1C and Trials |
| Description (146) | Jardiance (empagliflozin) is an SGLT2 inhibitor, not insulin. Its A1C effect, EMPA-REG OUTCOME, heart and kidney uses, side effects and pill look. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/jardiance-for-type-2-diabetes |
| H1 / H2 / H3 | ['Jardiance for type 2 diabetes: how empagliflozin works and what its trials found'] / 11 / 0 |
| Words (total / own prose / quoted) | 2249 / 1818 / 0 |
| Readability Flesch, grade, avg sentence: all | 17, 16.6, 23.1 |
| … own prose only | 20, 15.6, 20.6 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `jardiance diabetes` | 0× (0.00%); title False, H1 False, first 100 words False |
| Links | 13 internal (5.8/1k words); 62 external {'www.accessdata.fda.gov': 22, 'europepmc.org': 38, 'www.novonordisk-us.com': 2}; new-tab 62/62 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 16, 'details': 7, 'images': 0, 'bold_own': 14} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-10-29'] |

### H2 sequence

1. At a glance
2. Is Jardiance insulin? What the SGLT2 class does
3. How much Jardiance lowers A1C
4. EMPA-REG OUTCOME and the heart and kidney trials
5. Jardiance side effects and label warnings
6. What does a Jardiance pill look like?
7. Jardiance vs GLP-1 and amylin drugs
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 20 (avg sentence 20.6 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Keyword `jardiance diabetes` counted 0× | `reject-policy` | Exact-phrase artifact: title, H1 and opening say 'Jardiance for type 2 diabetes'. | none | — |
| Label statements written without opening the label | `accept-record` (open) | Checked against the current label's known content (indications incl. children 10+, heart failure, CKD; not recommended in type 1; 10/25 mg; UTI and genital mycotic infections; tablet description). Confirm against the PDF; listed in the PR body. | record | owner |
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/jardiance-for-type-2-diabetes/index.html`.

### Content quality score: 49/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 2 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 8/25 | 38 primary-source links; reviewer absent; author named |
| Authoritativeness | 15/25 | publisher set in JSON-LD; /about exists; 13 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/jardiance-for-type-2-diabetes`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.accessdata.fda.gov': 22, 'europepmc.org': 38, 'www.novonordisk-us.com': 2}).

### Page facts

| | |
|---|---|
| Title (52) | Jardiance for Type 2 Diabetes: SGLT2, A1C and Trials |
| Description (146) | Jardiance (empagliflozin) is an SGLT2 inhibitor, not insulin. Its A1C effect, EMPA-REG OUTCOME, heart and kidney uses, side effects and pill look. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/jardiance-for-type-2-diabetes |
| H1 / H2 / H3 | ['Jardiance for type 2 diabetes: how empagliflozin works and what its trials found'] / 11 / 0 |
| Words (total / own prose / quoted) | 2249 / 1818 / 0 |
| Readability Flesch, grade, avg sentence: all | 17, 16.6, 23.1 |
| … own prose only | 20, 15.6, 20.6 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `jardiance diabetes` | 0× (0.00%); title False, H1 False, first 100 words False |
| Links | 13 internal (5.8/1k words); 62 external {'www.accessdata.fda.gov': 22, 'europepmc.org': 38, 'www.novonordisk-us.com': 2}; new-tab 62/62 |
| Formatting | {'tables': 2, 'captions': 2, 'quotes_with_cite': 0, 'abbr': 0, 'time': 16, 'details': 7, 'images': 0, 'bold_own': 14} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2025-12-18', '2026-10-29'] |

### H2 sequence

1. At a glance
2. Is Jardiance insulin? What the SGLT2 class does
3. How much Jardiance lowers A1C
4. EMPA-REG OUTCOME and the heart and kidney trials
5. Jardiance side effects and label warnings
6. What does a Jardiance pill look like?
7. Jardiance vs GLP-1 and amylin drugs
8. More in this topic
9. Questions people ask
10. Sources
11. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 20 (avg sentence 20.6 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
