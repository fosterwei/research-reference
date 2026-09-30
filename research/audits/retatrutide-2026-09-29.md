# Retatrutide audit, 2026-09-29

Built locally from this commit; Vercel preview protection is still on, so the local build of the
same commit is the artifact (docs/content-automation.md step 3). Commit: 7fd89ba

## Part 1: audit

Built from `dist/compounds/retatrutide/index.html`.

### Content quality score: 93/100 (heuristic)

| Factor | Score | Signals |
|---|---|---|
| Experience | 15/20 | 4 data tables, 41 cited verbatim quotations, measured-absence statements present |
| Expertise | 23/25 | 33 primary-source links; reviewer named; author named |
| Authoritativeness | 25/25 | publisher set in JSON-LD; /about exists; 13 internal links |
| Trustworthiness | 30/30 | canonical `https://www.dashnaiv.com/compounds/retatrutide`; datePublished 2026-09-14; not-yet-reviewed notice absent; privacy yes, contact yes |

### AI citation readiness: 90/100 (heuristic)

### Who / how / why

- **Who**: reviewer and author in structured data.
- **How**: process disclosed on-page (yes: quotations labelled verbatim, changelog present yes).
- **Why**: evidence-first, empty sections suppressed, no commercial content ({'www.linkedin.com': 1, 'clinicaltrials.gov': 3, 'doi.org': 3, 'europepmc.org': 33}).

### Page facts

| | |
|---|---|
| Title (50) | Retatrutide Dosage, Trial Results and Side Effects |
| Description (150) | Retatrutide doses as the trials gave them, weight loss at 24 and 48 weeks for every dose group, side effects, and each registered trial by its number. |
| Robots | index, follow, max-image-preview:large |
| Canonical | https://www.dashnaiv.com/compounds/retatrutide |
| H1 / H2 / H3 | ['Retatrutide: the doses used in trials, what the weight-loss numbers actually were, and the trials still running'] / 25 / 3 |
| Words (total / own prose / quoted) | 6759 / 3733 / 1371 |
| Readability Flesch, grade, avg sentence: all | 7, 18.6, 25.6 |
| … own prose only | 20, 15.3, 19.3 |
| … quotations only | -11, 22.8, 32.3 |
| Keyword `retatrutide` | 130× (1.92%); title True, H1 True, first 100 words True |
| Links | 13 internal (1.9/1k words); 40 external {'www.linkedin.com': 1, 'clinicaltrials.gov': 3, 'doi.org': 3, 'europepmc.org': 33}; new-tab 36/40 |
| Formatting | {'tables': 4, 'captions': 4, 'quotes_with_cite': 41, 'abbr': 3, 'time': 47, 'details': 6, 'images': 0, 'bold_own': 13} |
| Footer links | ['/compounds', '/stacks', '/compare', '/tools', '/about', '/about#tiers', '/about#review', '/privacy', '/contact', '/about#not'] |
| Dates on page | ['2026-09-14', '2026-09-29'] |

### H2 sequence

1. At a glance
2. What retatrutide is, and why it acts on three receptors instead of one
3. What the evidence level means
4. Retatrutide in two minutes
5. How retatrutide is thought to work
6. What the weight-loss numbers were, dose by dose
7. The registered trials, and which have reported
8. What the evidence shows
9. What doses did the trials actually use?
10. What side effects were reported, and at which doses
11. Biomarkers measured in studies
12. Reported timelines
13. Study durations
14. How it is given, and how long it stays
15. Common mistakes in how retatrutide is discussed
16. Exclusion criteria in studies
17. Retatrutide and tirzepatide, and why the headline percentages do not compare
18. Studied in combination
19. Is retatrutide approved?
20. Open questions and limitations
21. Questions people ask
22. Sources
23. Reference card
24. Related records
25. Last reviewed and what changed

### Issues found

1. Own prose reads at Flesch 20 (avg sentence 19.3 words). Quotations are verbatim by policy; this measures only the text we wrote.
2. Internal links 1.9 per 1,000 words (guideline 3–5).
3. No image, so no image alt text carrying the keyword (design.md requires none; note only).



## Part 2: triage

| Suggestion | Label | Reason | Layer | Owner |
|---|---|---|---|---|
| Meta description 124 chars, target 130-160 | `accept-record` | Fixed. Rewritten to 150 characters and re-pointed at the doses and the trial numbers, which is what the page now leads with. Title also rewritten from "Retatrutide: what the research shows" to "Retatrutide Dosage, Trial Results and Side Effects": the measured demand is on `retatrutide dosage` (5,901 clicks, KD 0) and `retatrutide side effects` (7,173, KD 10), and the old title named neither. | record `seo` | writer |
| Own prose Flesch 20, avg sentence 19.3 words | `reject-policy` | Sentence length is inside the 22-word minimum. The Flesch penalty is driven by unavoidable terms: "glucose-dependent insulinotropic polypeptide", "least-squares mean", "gastrointestinal". Simplifying them would misstate the trials. `docs/design.md` puts accuracy above readability score, and the skill's own note says Flesch is not a ranking factor. | none | none |
| Internal links 1.9 per 1,000 words, guideline 3-5 | `reject-policy` | Settled on 2026-09-24 and recorded in `docs/content-automation.md`: across the written pages, other records are named 132 times in prose and 110 were already linked. Density stays near one per thousand because these are long single-subject pages. Measured, not argued: the editorial sections of this page link at 4.1/1k; the site-wide figure is diluted by the sources ledger, which is citations rather than prose. | none | none |
| No image, so no keyword in alt text | `reject-policy` | `docs/design.md` requires no images on a record page, and an image added to carry alt text would be decoration. The social card added on 2026-09-29 covers the sharing surface this note is really about. | none | none |
| Two sample sizes were screening counts, not enrolment | `accept-script` | Found while writing, not by the audit. `pmid-42250575` stored n=930 where the abstract says 930 were screened and 537 randomly assigned; `pmid-36354040` stored n=210 where 210 were screened and 72 enrolled. Fixed in `scripts/draft_claims.py`: assignment phrasing is now tried first and any candidate followed by "were screened" is rejected. Both rows corrected. A site-wide re-check of all 223 stored sample sizes is running separately. | `scripts/draft_claims.py` + records | engineer |
| Written escalation section collided with the generated one | `accept-record` | The generated `escalation` block rendered "No study in this record's ledger reports dose-escalation schedules" directly beneath a written section quoting those schedules from the trial abstract: a contradiction, a duplicate H2 and a duplicate element id. `escalation` added to the map's `suppress`. Caught by the duplicate-H2 rule added to `scripts/check_links.py` the same day, which is the first thing that rule has found. | intent map `suppress` | writer |

## Part 3: exit audit

Re-run after the accepted items landed.

| | First run | Exit run |
|---|---|---|
| Heuristic score | 93/100 | 93/100 |
| Trustworthiness | 30/30 | 30/30 |
| Meta description | 124 chars (flagged) | 150 chars |
| Title | generic, no measured query | names `dosage` and `side effects` |
| Duplicate H2 / duplicate id | 1 / 1 | 0 / 0 |
| Outbound domains | europepmc, doi, linkedin | + clinicaltrials.gov (3 links) |

The score did not move, and that is the expected result rather than a disappointment: the two
accepted items were a meta description and a heading collision, neither of which the heuristic
weighs. Intent coverage is 15 of 17 queries addressed, 98% of measured demand landing on a
rendered answer. The two unaddressed queries are `retatrutide weight loss` and
`retatrutide vs semaglutide`, both of which resolve onto sections written for higher-volume
siblings.

## Notes for the next page

The sandbox that built this page reaches Europe PMC but not clinicaltrials.gov, dailymed.nlm.nih.gov
or api.fda.gov. Every NCT number here is quoted from the published paper that declares it, and the
registry links are pointers rather than sources. The page says so in its own words. Broadening
citations to registry and label documents as sources in their own right needs an environment with
access to them.
