# subcutaneous-injection-sites audit, 2026-10-29

Preview: audited the local build of branch `feat/cagrilintide-guide` per docs/content-automation.md step 3 (Vercel previews redirect unauthenticated requests). Guide post in the cagrilintide series; stages 1-5 in research/intents/subcutaneous-injection-sites.json were written before the page.

## Part 1: audit


Built from `dist/blog/subcutaneous-injection-sites/index.html`.

### Content quality score: 43/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 5/25 | 8 primary-source links; reviewer absent; author named |
| Authoritativeness | 12/25 | publisher set in JSON-LD; /about exists; 9 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/subcutaneous-injection-sites`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.accessdata.fda.gov': 14, 'pi.lilly.com': 20, 'medlineplus.gov': 5, 'www.cdc.gov': 8, 'europepmc.org': 8}).

### Page facts

| | |
|---|---|
| Title (54) | Subcutaneous Injection Sites: Where and How It's Given |
| Description (154) | Subcutaneous injection sites explained: belly, thigh and upper arm, what GLP-1 pen labels and CDC guidance say, the angle, and what CagriSema trials used. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/subcutaneous-injection-sites |
| H1 / H2 / H3 | ['Subcutaneous injection sites: where weekly injections go, and what the trials specified'] / 12 / 0 |
| Words (total / own prose / quoted) | 2178 / 1829 / 0 |
| Readability Flesch, grade, avg sentence: all | 28, 15.0, 22.9 |
| … own prose only | 32, 13.5, 19.3 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `subcutaneous injection` | 22× (1.01%); title True, H1 True, first 100 words True |
| Links | 9 internal (4.1/1k words); 55 external {'www.accessdata.fda.gov': 14, 'pi.lilly.com': 20, 'medlineplus.gov': 5, 'www.cdc.gov': 8, 'europepmc.org': 8}; new-tab 55/55 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 12, 'details': 7, 'images': 0, 'bold_own': 25} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. What a subcutaneous injection is, and what the abbreviations mean
3. Possible injection sites for a subcutaneous shot
4. The best place on the stomach for a shot, and why sites rotate
5. How a subcutaneous injection is given: the steps in the instructions
6. Subcutaneous vs intramuscular injection, and the degree of injection
7. What the cagrilintide and CagriSema trials specified
8. More in this topic
9. Questions people ask
10. Sources
11. Related records
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 32 (avg sentence 19.3 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).

## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| No named reviewer / author | `defer-reviewer` | Shown only when a real person reviews (policy since 2026-09-23). Same on every page in the site. | record | — |
| No image | `reject-policy` | design.md §6. Precedent: ipamorelin. | none | — |
| Canonical shows example.com in the audit | no action | Local build without SITE_URL; CI and Vercel build with the production origin. | none | — |
| FDA label `published` dates | `accept-record` (open) | Several label PDFs could not be opened from this environment (TLS failure on fda.gov and DailyMed); their dates are the label year and must be replaced with the label revision dates. Listed in the PR body. | record | owner |
| Own-prose Flesch below 40 | `reject-policy` | design.md §9.7 budgets sentence length (average under about 22 words, met here); drug, trial and class names drive syllables and cannot be swapped out. | none | — |

## Part 3: exit audit


Built from `dist/blog/subcutaneous-injection-sites/index.html`.

### Content quality score: 43/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 10/20 | 1 data tables, 0 cited verbatim quotations, measured-absence statements absent |
| Expertise | 5/25 | 8 primary-source links; reviewer absent; author named |
| Authoritativeness | 12/25 | publisher set in JSON-LD; /about exists; 9 internal links |
| Trustworthiness | 16/30 | canonical `https://www.dashnaiv.com/blog/subcutaneous-injection-sites`; datePublished 2026-10-29; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 60/100 (heuristic)

### Who / how / why

- **Who**: no named person; the page says so.
- **How**: process disclosed on-page (no: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.accessdata.fda.gov': 14, 'pi.lilly.com': 20, 'medlineplus.gov': 5, 'www.cdc.gov': 8, 'europepmc.org': 8}).

### Page facts

| | |
|---|---|
| Title (54) | Subcutaneous Injection Sites: Where and How It's Given |
| Description (154) | Subcutaneous injection sites explained: belly, thigh and upper arm, what GLP-1 pen labels and CDC guidance say, the angle, and what CagriSema trials used. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/blog/subcutaneous-injection-sites |
| H1 / H2 / H3 | ['Subcutaneous injection sites: where weekly injections go, and what the trials specified'] / 12 / 0 |
| Words (total / own prose / quoted) | 2179 / 1830 / 0 |
| Readability Flesch, grade, avg sentence: all | 28, 15.0, 22.9 |
| … own prose only | 32, 13.5, 19.3 |
| … quotations only | 0, 0.0, 0.0 |
| Keyword `subcutaneous injection` | 22× (1.01%); title True, H1 True, first 100 words True |
| Links | 9 internal (4.1/1k words); 55 external {'www.accessdata.fda.gov': 14, 'pi.lilly.com': 20, 'medlineplus.gov': 5, 'www.cdc.gov': 8, 'europepmc.org': 8}; new-tab 55/55 |
| Formatting | {'tables': 1, 'captions': 1, 'quotes_with_cite': 0, 'abbr': 0, 'time': 12, 'details': 7, 'images': 0, 'bold_own': 25} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/blog', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-10-29'] |

### H2 sequence

1. At a glance
2. What a subcutaneous injection is, and what the abbreviations mean
3. Possible injection sites for a subcutaneous shot
4. The best place on the stomach for a shot, and why sites rotate
5. How a subcutaneous injection is given: the steps in the instructions
6. Subcutaneous vs intramuscular injection, and the degree of injection
7. What the cagrilintide and CagriSema trials specified
8. More in this topic
9. Questions people ask
10. Sources
11. Related records
12. Last reviewed and what changed

### Issues found

1. No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.
2. Own prose reads at Flesch 32 (avg sentence 19.3 words). Quotations are verbatim by policy; this measures only the text we wrote.
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).
