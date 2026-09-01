# Content contract

## Programmatic pages

| Type | URL | Required unique value |
|---|---|---|
| Compound | `/protocols/{slug}` | facts, evidence boundaries, references, related entities |
| Stack | `/stacks/{slug}` | component evidence, rationale, limitations |
| Comparison | `/compare/{slug}` | decision matrix and audience-specific conclusion |
| Cycle | `/cycles/{slug}` | source-backed duration context and uncertainty |
| Tool | `/tools/{slug}` | transparent formula, inputs, outputs, examples |

## Editorial posts
Posts use `/blog/{slug}` and must add interpretation beyond linked programmatic pages. Categories: Research, Evidence, Safety & Regulation, Methodology, Industry News, Reviews.

## Index states
`discovered`, `researched`, `draft`, `reviewed`, `published`, `stale`, `retired`. Only `published` records that pass quality gates enter the sitemap.
