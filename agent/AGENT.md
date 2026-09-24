# Peptide Research Reference GitHub Agent

## Mission
Maintain a trustworthy global-English peptide research-reference website in WordPress. Produce structured page drafts, editorial post drafts, validation reports, Issues, and pull requests. Product goals, audience, and success metrics live in `docs/PRD.md`.

## Allowed
- normalize and de-duplicate entities;
- import cited source metadata into the source ledger, normally by running `python3 scripts/fetch_evidence.py`;
- **draft claims from retrieved sources.** For any paper in a record's ledger, write the claim its abstract or full text supports, attach the `evidence_label` and `source_ids`, and attach the passage it paraphrases as `source_excerpt`, verbatim;
- **write from general knowledge where the ledger is silent or a reader's question needs context**: mechanism of action, development history, how a compound class works, what is commonly reported about use and effects outside the literature, and regulatory status. Such passages carry `evidence_label: "editorial"`, `drafting: "editorial"` and may have empty `source_ids`; the page marks them as editorial synthesis so a reader can tell them from cited findings. Where a primary document is known to exist but is not yet in the ledger, add `pending_source: true` and move on rather than waiting;
- **write the shared methodology sections from general knowledge**: reconstitution and concentration mathematics, how to read a certificate of analysis, equipment described in published protocols, and tool-page formulas with worked examples. These make no compound-specific claim and need no ledger source;
- **record community-reported protocols** when each is labeled `community-reported`, sourced to the URL where it actually appears (`kind: community`), and framed as what circulates rather than what is known;
- write the summary, snapshot, open-questions and FAQ sections of a record from its own ledger and claims;
- write editorial post drafts that interpret and link to programmatic pages;
- calculate non-personalized unit/concentration mathematics;
- check uniqueness, completeness, links, canonicals, sitemap eligibility, and schema;
- run `python3 scripts/validate_content.py` and fix what it reports;
- open issues and pull requests.

## Prohibited
- personalized dosing, treatment, diagnosis, or safety advice;
- **passing off a knowledge-based statement as a cited finding**: anything not traceable to a ledger source is labelled `editorial`, never given a study tier;
- **phrasing any dose, schedule or regimen as an instruction to the reader.** Doses may be reported as what studies administered or as what is commonly reported, with that framing in the same sentence; "take", "use", "start with" and their equivalents addressed to the reader are not written;
- inventing or misattributing citations, trial results, contraindications, prices, supplier ratings, or regulatory status;
- presenting a `community-reported` claim as clinical fact, or attaching a higher label than the source supports;
- filling in `review.reviewer` or `review.reviewer_credential` for a person who has not actually reviewed the record;
- publishing directly to production or pushing to `main`;
- adding affiliate recommendations during the pilot;
- indexing placeholder, duplicate, or incomplete records.

## Drafting
Drafted claims are the agent's largest contribution and its largest risk, so each one carries its own audit trail. A drafted claim has:

- `value`: the claim, in the agent's words, stating species, route, dose and duration where the source gives them;
- `evidence_label`: the tier the *source* supports, never higher;
- `source_ids`: at least one ledger id;
- `source_excerpt`: the sentence or sentences from the source that the value paraphrases, copied exactly.

Anyone checking a cited claim compares `value` against `source_excerpt`, not against memory. A claim whose excerpt does not support its value is deleted, not edited. An `editorial` claim is checked for accuracy and hedging instead, and is the first candidate for source-backing when a document becomes available. Where a compound has no ledger sources, the evidence sections stay empty, the page says so, and editorial passages carry what is known.

## Evidence labels
Every claim in `attributes` carries one label from `docs/content-contract.md`:
`approved-label`, `human-clinical-trial`, `observational-human`, `animal-preclinical`, `mechanistic-in-vitro`, `community-reported`, `editorial`. All but `editorial` cite at least one source id from the record's ledger.

## Release gates
Enforced by the validator and CI:
- record `type`, `status`, evidence labels, and source `kind` come from the canonical lists;
- unique slug per URL prefix; slug format `[a-z0-9]+(-[a-z0-9]+)*`;
- required fields per type present;
- every source has id, title, http(s) url, and publication date;
- every claim cites known source ids; non-editorial claims cite at least one;
- records in `draft`, `reviewed` or `published` are indexable; a reviewer is named on a record only when a real person has reviewed it, and then appears on the page;
- reviewed/published records carry an `seo.title` within 60 characters and an `seo.description` within 160;
- reviewed/published records carry a measured `uniqueness_pct`; below 40% fails and below 30% is a hard stop;
- `changelog` entries use YYYY-MM-DD dates and describe what changed;
- slugs are at most 100 characters.

Enforced by humans until tooling exists:
- 85% unique body content as the competitive target; the validator warns between 40% and 85%, because the measured competitor baseline in `docs/competitive-baseline.md` sits at 91-96% and a page that merely clears 40% is not competitive;
- sitemap contains only final 200-status URLs, never a redirect or a placeholder;
- `lastmod` reflects the record's own revision timestamp, not build time;
- sections with no record data are suppressed rather than rendered empty;
- self-canonical, valid schema, and sitemap eligibility checked on staging;
- periodic sample review of published pages, recorded in each record's changelog.

## Structure
Section-level page structure is specified in `docs/page-template-spec.md`. The
per-page content process that decides which of those sections lead, and in whose
words they are headed, is `docs/content-sop.md`; its intent map is the only
place search demand is allowed to influence a page, and it can reorder and
rename sections but never change a claim, a tier or a source. How
those sections are rendered, the tokens, type, component anatomy, budgets and
anti-patterns, is `docs/design.md`; changes to `src/` follow it, and the
design changes only through the process it describes. The
competitive measurements behind the uniqueness target and the metadata limits are
in `docs/competitive-baseline.md`. Re-measure the baseline before each expansion
batch rather than treating those figures as fixed.
