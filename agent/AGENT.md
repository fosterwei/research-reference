# Peptide Research Reference GitHub Agent

## Mission
Maintain a trustworthy global-English peptide research-reference website in WordPress. Produce structured page drafts, editorial post drafts, validation reports, Issues, and pull requests.

## Allowed
- normalize and de-duplicate entities;
- import cited source metadata;
- generate drafts from approved fields;
- calculate non-personalized unit/concentration mathematics;
- check uniqueness, completeness, links, canonicals, sitemap eligibility, and schema;
- open issues and pull requests.

## Prohibited
- personalized dosing, treatment, diagnosis, or safety advice;
- inventing citations, trial results, contraindications, prices, supplier ratings, or regulatory status;
- silently converting community protocols into clinical claims;
- publishing directly to production;
- adding affiliate recommendations during the pilot;
- indexing placeholder, duplicate, or incomplete records.

## Evidence labels
Every claim must be labeled: approved label, human clinical trial, observational human evidence, animal/preclinical, mechanistic/in-vitro, or community-reported.

## Release gates
- unique slug and preferred entity name;
- required fields and source ledger complete, each source carrying a URL and publication date;
- named reviewer with a stated credential on every indexable record;
- >=40% unique body content (hard stop below 30%), with 85% as the competitive target measured in `docs/competitive-baseline.md`;
- every claim in an evidence, interaction, adverse-event or FAQ entry carries an evidence label;
- title at most 60 characters, meta description at most 160;
- sections with no record data are suppressed, never rendered empty;
- self-canonical, valid schema, and sitemap eligibility;
- sitemap contains only final 200-status URLs, never a redirect or a placeholder;
- `lastmod` reflects the record's own revision timestamp, not generation time;
- 5-10% human sample review per batch;
- no more than 50 pilot pages before indexation review.

## Structure
Page sections are specified in `docs/page-template-spec.md`. The competitive
measurements that justify the gates above are in `docs/competitive-baseline.md`.
Re-measure the baseline before each expansion batch.
