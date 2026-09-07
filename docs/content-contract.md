# Content contract

## Programmatic pages

| Type | URL | Required unique value |
|---|---|---|
| Compound | `/protocols/{slug}` | facts, evidence boundaries, references, related entities |
| Stack | `/stacks/{slug}` | component evidence, rationale, limitations |
| Comparison | `/compare/{slug}` | decision matrix and audience-specific conclusion |
| Cycle | `/cycles/{slug}` | source-backed duration context and uncertainty |
| Tool | `/tools/{slug}` | transparent formula, inputs, outputs, examples |

Section-level structure for each type is specified in `docs/page-template-spec.md`.
Tool pages are a first-class type, not a widget embedded in compound pages.

## Editorial posts
Posts use `/blog/{slug}` and must add interpretation beyond linked programmatic pages. Categories: Research, Evidence, Safety & Regulation, Methodology, Industry News, Reviews.

## Index states
`discovered`, `researched`, `draft`, `reviewed`, `published`, `stale`, `retired`. Only `published` records that pass quality gates enter the sitemap.

## Metadata limits

| Element | Limit |
|---|---|
| Title | 60 characters |
| Meta description | 160 characters |
| H1 | exactly one |
| Slug | lowercase, hyphenated, under 100 characters |

## Sitemap rules

Only `published` records that pass the quality gates enter the sitemap. Entries
must be final 200-status URLs; a redirecting or placeholder URL in the sitemap is
a defect. `lastmod` carries the record's revision timestamp, never the build time.
