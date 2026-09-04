# Peptide Research Reference — GitHub Agent Starter

Hosting-agnostic WordPress starter for a global English research-reference site.

The agent drafts, validates, and opens pull requests for programmatic pages and editorial posts. It must not publish directly or invent medical, safety, regulatory, or affiliate claims.

Product goals, audience, non-goals, milestones, and success metrics are in [`docs/PRD.md`](docs/PRD.md). Page types, URLs, record states, and evidence labels are defined once in [`docs/content-contract.md`](docs/content-contract.md).

## Layout

| Path | Purpose |
|---|---|
| `docs/PRD.md` | Product requirements, non-goals, milestones, metrics |
| `docs/content-contract.md` | Canonical page types, URL patterns, record states, evidence labels, source ledger shape |
| `docs/launch-checklist.md` | Pilot launch QA checklist |
| `agent/AGENT.md` | Agent mission, allowed and prohibited actions, release gates |
| `data/<type>/*.json` | One JSON record per page; `data/examples/` holds reference templates |
| `scripts/validate_content.py` | Dependency-free content gate, mirrors the content contract |
| `.github/workflows/` | CI: validator on every PR and push to `main`, plus PHP lint |
| `.github/ISSUE_TEMPLATE/` | Structured issue form for content requests |
| `.github/CODEOWNERS` | Required reviewer per area |
| `wp-content/plugins/research-database/` | Post types, REST-exposed record fields, noindex and sitemap control |
| `wp-content/themes/research-reference/` | Lightweight Elementor-compatible theme with record templates |

Compatible with SiteGround and Hostinger WordPress staging; no provider-specific API is required.

## Content workflow

1. Open an Issue with the **New or update content record** form.
2. Add a JSON record in the folder for its type under `data/`, starting from the matching file in `data/examples/`.
3. Fill the source ledger: each source needs `id`, `title`, `url`, and `published` date. Every claim in `attributes` cites source ids and carries an evidence label.
4. Run `python3 scripts/validate_content.py`. It fails on unknown statuses, evidence labels, or types, invalid slugs, duplicate slugs, malformed sources, claims citing unknown sources, and reviewed/published records without a named author, a different named reviewer, and a review date.
5. Open a pull request. CI repeats the validation and lints the PHP.
6. A human editor reviews factual, safety, regulatory, and medical-sensitive claims and sets `review.reviewer`, `review.reviewed_at`, and `status: reviewed`.
7. Merge only after approval, then import to WordPress staging and set `status: published` once it is live.

### Record states

`discovered` → `researched` → `draft` → `reviewed` → `published` → `stale` → `retired`

Only `published` records are indexable. The plugin reads the `record_status` field and emits `noindex` and excludes the post from the sitemap in every other state, even if WordPress itself has published the post.

## WordPress installation

1. Copy `wp-content/plugins/research-database` into the site's plugins directory and activate it. Activation registers `compound`, `stack`, `comparison`, `cycle`, and `tool` post types and flushes rewrite rules so `/compounds/`, `/stacks/`, `/compare/`, `/cycles/`, and `/tools/` resolve immediately.
2. Copy `wp-content/themes/research-reference` into the themes directory and activate it. The theme is a complete classic theme (header, footer, index, page, single, and one template per record type). Elementor and Elementor Pro can take over pages, header, and footer.
3. Record fields (`record_status`, `evidence_tier`, `review_author`, `review_reviewer`, `reviewed_at`, `sources`, `attributes_json`) are registered on every record post type and exposed over REST, so the future importer needs no custom admin UI.
4. The plugin excludes non-published records from the core XML sitemap and from Yoast SEO and Rank Math sitemaps.

Requires PHP 8.2+ and WordPress 6.4+.

## GitHub Actions

`.github/workflows/content-quality.yml` runs on every pull request and every push to `main`. It validates the content records and runs `php -l` on every PHP file. Validator errors appear as inline annotations on the PR. The workflow has read-only permissions.

## Branch protection

This repository is private on a free GitHub plan, so branch protection rules are not available. Until it is made public or upgraded to GitHub Pro, the PR gate relies on CI results and on the deploy process only shipping merged `main`. `.github/CODEOWNERS` documents who must review each area and becomes enforceable the moment protection is enabled.

## Safety and agent boundaries

The agent may draft and validate research-reference content, but it must not invent citations, convert community schedules into clinical facts, make personal recommendations, publish directly to production, mark records reviewed or published, or add affiliate recommendations during the pilot. A named human reviewer is required for safety, regulatory, administration, and medical claims. Full policy: [`agent/AGENT.md`](agent/AGENT.md).

## Hosting notes

Use HTTPS, staging, automated backups, PHP 8.2+, caching and object cache where available, a managed database, and a deployment process that ships only reviewed merges. Keep production WordPress credentials in hosting or GitHub secrets; never commit them.

## Status and next milestone

Milestones 1 to 3 in [`docs/PRD.md`](docs/PRD.md) are complete: content contract with validator and CI, plugin with record-state index control, and an activatable theme. Milestone 4, the REST importer from `data/` to staging, is next.
