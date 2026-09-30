# Tesamorelin audit, 2026-09-29

Built locally from this commit; Vercel preview protection is still on, so the local build of the
same commit is the artifact (docs/content-automation.md step 3). Commit: ff41838

## Part 1: audit

Built from `dist/compounds/tesamorelin/index.html`.

### Content quality score: 93/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 3 data tables, 40 cited verbatim quotations, measured-absence statements present |
| Expertise | 23/25 | 27 primary-source links; reviewer named; author named |
| Authoritativeness | 25/25 | publisher set in JSON-LD; /about exists; 11 internal links |
| Trustworthiness | 30/30 | canonical `https://www.dashnaiv.com/compounds/tesamorelin`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 90/100 (heuristic)

### Who / how / why

- **Who**: reviewer and author in structured data.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.linkedin.com': 1, 'europepmc.org': 27}).

### Page facts

| | |
|---|---|
| Title (50) | Tesamorelin Dosage, Trial Results and Side Effects |
| Description (151) | Tesamorelin trials in full: the dose, what visceral fat did over 52 weeks, what happened after treatment stopped, and who the trials actually enrolled. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/compounds/tesamorelin |
| H1 / H2 / H3 | ['Tesamorelin: what the trials measured, in whom, and what happens when you stop'] / 24 / 3 |
| Words (total / own prose / quoted) | 5879 / 3510 / 918 |
| Readability Flesch, grade, avg sentence: all | 13, 17.3, 23.3 |
| … own prose only | 24, 14.5, 18.5 |
| … quotations only | -7, 20.0, 23.4 |
| Keyword `tesamorelin` | 98× (1.67%); title True, H1 True, first 100 words True |
| Links | 11 internal (1.9/1k words); 28 external {'www.linkedin.com': 1, 'europepmc.org': 27}; new-tab 27/28 |
| Formatting | {'tables': 3, 'captions': 3, 'quotes_with_cite': 40, 'abbr': 1, 'time': 39, 'details': 6, 'images': 0, 'bold_own': 14} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-29'] |

### H2 sequence

1. At a glance
2. What tesamorelin is, and the one condition it was approved for
3. What the evidence level means
4. Tesamorelin in two minutes
5. What the trials measured, and how much changed
6. What happened when treatment stopped
7. What the evidence shows
8. What dose did the trials use?
9. What side effects and safety signals the trials reported
10. Biomarkers measured in studies
11. Reported timelines
12. Study durations
13. Routes studied
14. Bodybuilding and anti-ageing use, and what evidence exists for it
15. Common mistakes in how tesamorelin is discussed
16. Other compounds in its class
17. Studied in combination
18. Egrifta, and what the approval actually covers
19. Open questions and limitations
20. Questions people ask
21. Sources
22. Reference card
23. Related records
24. Last reviewed and what changed

### Issues found

1. Own prose reads at Flesch 24 (avg sentence 18.5 words). Quotations are verbatim by policy; this measures only the text we wrote.
2. Internal links 1.9 per 1,000 words (guideline 3–5).
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).



## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Own prose Flesch 24, avg sentence 18.5 words | `reject-policy` | Inside the 22-word sentence-length minimum. The Flesch penalty comes from terms that cannot be simplified without misstating the trials: "visceral adipose tissue", "growth-hormone-releasing hormone", "fibrinolytic markers". `docs/design.md` puts accuracy first and the skill's own note says Flesch is not a ranking factor. | none | none |
| Internal links 1.9 per 1,000 words | `reject-policy` | Settled 2026-09-24 and recorded in `docs/content-automation.md`. The site-wide figure is diluted by the sources ledger, which is citations rather than prose. | none | none |
| No image, so no keyword in alt text | `reject-policy` | `docs/design.md` requires no images on a record page. | none | none |

No `accept` items. The page was written against the audit's criteria rather than corrected into them,
which is what running stages 1 and 2 before the writing is supposed to achieve.

## Part 3: exit audit

| | Result |
|---|---|
| Heuristic score | 93/100 |
| Trustworthiness | 30/30 |
| Intent coverage | 12 of 13 queries, **100% of measured demand** on a rendered answer |
| Uniqueness | 82.4% |
| Duplicate H2 / duplicate id | 0 / 0 |

The one unaddressed query is `tesamorelin vs ipamorelin`, which resolves onto the existing
comparison record rather than onto this page.

## What this page has that the SERP does not

The pivotal trial reported, in its own conclusion, that the visceral-fat reduction does not persist
after treatment stops. None of the three scored competitors carries that sentence, and two of them
carry no citation at all. The page also frames every result by the population the trials enrolled,
people with HIV and antiretroviral-associated abdominal fat accumulation, and states plainly that no
trial in the ledger gave tesamorelin to a healthy adult, which is what most of the measured demand
is asking about.

Worth recording about the SERP itself: the result at rank 2 for a 42,127-search query is a vendor
product page carrying eight words of body text, and the page at rank 8 has no H2 element at all.
The difficulty score of 3 is believable rather than an artefact.

## Open, and not resolvable here

The Egrifta label sits at rank 7 for the head term and could not be retrieved: this sandbox reaches
Europe PMC but not accessdata.fda.gov, dailymed.nlm.nih.gov or clinicaltrials.gov. The approval
facts on this page come from ChEMBL and from the trials, not from the label. Neither pivotal trial
abstract declares a ClinicalTrials.gov number, so no registration table is possible for this
compound from Europe PMC alone.
