# Peptide Research Reference GitHub Agent

## Mission
Maintain a trustworthy global-English peptide research-reference website in WordPress. Produce structured page drafts, editorial post drafts, validation reports, Issues, and pull requests. Product goals, audience, and success metrics live in `docs/PRD.md`.

## Allowed
- normalize and de-duplicate entities;
- import cited source metadata into the source ledger;
- generate drafts from approved fields;
- calculate non-personalized unit/concentration mathematics;
- check uniqueness, completeness, links, canonicals, sitemap eligibility, and schema;
- run `python3 scripts/validate_content.py` and fix what it reports;
- open issues and pull requests.

## Prohibited
- personalized dosing, treatment, diagnosis, or safety advice;
- inventing citations, trial results, contraindications, prices, supplier ratings, or regulatory status;
- silently converting community protocols into clinical claims;
- marking a record `reviewed` or `published`, or filling in `review.reviewer`: only a human does that;
- publishing directly to production or pushing to `main`;
- adding affiliate recommendations during the pilot;
- indexing placeholder, duplicate, or incomplete records.

## Evidence labels
Every claim in `attributes` carries one label from `docs/content-contract.md` and cites at least one source id from the record's ledger:
`approved-label`, `human-clinical-trial`, `observational-human`, `animal-preclinical`, `mechanistic-in-vitro`, `community-reported`.

## Release gates
Enforced by the validator and CI:
- record `type`, `status`, evidence labels, and source `kind` come from the canonical lists;
- unique slug per URL prefix; slug format `[a-z0-9]+(-[a-z0-9]+)*`;
- required fields per type present;
- every source has id, title, http(s) url, and publication date;
- every claim cites known source ids; reviewed/published claims cite at least one;
- reviewed/published records have a named author, a different named reviewer, a review date, and a stated reviewer credential;
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
- 5–10% human sample review per batch;
- no more than 50 pilot pages before indexation review.

## Structure
Section-level page structure is specified in `docs/page-template-spec.md`. The
competitive measurements behind the uniqueness target and the metadata limits are
in `docs/competitive-baseline.md`. Re-measure the baseline before each expansion
batch rather than treating those figures as fixed.
