# Content contract

This file is the single source of truth for page types, URLs, record states, and evidence labels. `scripts/validate_content.py` and the Research Database plugin mirror these lists; change all three together.

## Programmatic pages

| Type | Folder | URL | Required unique value |
|---|---|---|---|
| Compound | `data/compounds/` | `/compounds/{slug}` | facts, evidence boundaries, references, related entities |
| Stack | `data/stacks/` | `/stacks/{slug}` | component evidence, rationale, limitations |
| Comparison | `data/comparisons/` | `/compare/{slug}` | decision matrix and audience-specific conclusion |
| Cycle | `data/cycles/` | `/cycles/{slug}` | source-backed duration context and uncertainty |
| Tool | `data/tools/` | `/tools/{slug}` | transparent formula, inputs, outputs, examples |

Compound pages were previously planned at `/protocols/{slug}`. That was renamed before any URL was indexed because "protocols" signals dosing guidance, which this site explicitly does not provide. Cycle pages remain in the contract but must describe what studies report about durations, never recommend one.

## Editorial posts

Posts live in `data/posts/` and publish at `/blog/{slug}`. They must add interpretation beyond the programmatic pages they link to.

Categories: Research, Evidence, Safety & Regulation, Methodology, Industry News, Reviews.

## Record states

`discovered` → `researched` → `draft` → `reviewed` → `published` → `stale` → `retired`

- Only `published` records are indexable and enter the sitemap. The plugin enforces this from the `record_status` field.
- `reviewed` and `published` records must have a named author, a different named reviewer, a review date, at least one source, and a source citation on every claim.
- Records in any other state are noindex even if WordPress has published them.

## Evidence labels

Use these exact values in `evidence_tier` and in every claim's `evidence_label`:

| Label | Meaning |
|---|---|
| `approved-label` | Statement from an approved product label or regulator |
| `human-clinical-trial` | Interventional human trial |
| `observational-human` | Cohort, case series, registry, or survey in humans |
| `animal-preclinical` | Animal study |
| `mechanistic-in-vitro` | Cell, tissue, or mechanistic work |
| `community-reported` | Anecdotal or community protocol; never presented as clinical fact |

## Source ledger

Each source has `id`, `title`, `url` (http or https), `published` (YYYY-MM-DD), and optional `kind` (`peer-reviewed`, `regulatory`, `preprint`, `clinical-registry`, `manufacturer`, `community`, `other`). Claims reference sources by `id`, so a claim can never point at a source that is not in the ledger.

## Slugs

Lowercase words joined by single hyphens. Slugs must be unique within a URL prefix. Examples under `data/examples/` are excluded from uniqueness and are never imported.
