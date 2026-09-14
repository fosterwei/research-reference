# Peptide Research Reference — GitHub Agent Starter

Hosting-agnostic WordPress starter for a global English research-reference site.

The agent drafts, validates, and opens pull requests for programmatic pages and editorial posts. It must not publish directly or invent medical, safety, regulatory, or affiliate claims.

Product goals, audience, non-goals, milestones, and success metrics are in [`docs/PRD.md`](docs/PRD.md). Page types, URLs, record states, and evidence labels are defined once in [`docs/content-contract.md`](docs/content-contract.md). Section-level page structure is specified in [`docs/page-template-spec.md`](docs/page-template-spec.md), and the competitive measurements behind the uniqueness target are in [`docs/competitive-baseline.md`](docs/competitive-baseline.md).

## Layout

| Path | Purpose |
|---|---|
| `docs/PRD.md` | Product requirements, non-goals, milestones, metrics |
| `docs/content-contract.md` | Canonical page types, URL patterns, record states, evidence labels, source ledger shape, metadata limits |
| `docs/page-template-spec.md` | Section-level structure per page type, shared-text budget, heading style |
| `docs/competitive-baseline.md` | Measured competitor benchmark behind the uniqueness target and metadata limits |
| `docs/launch-checklist.md` | Pilot launch QA checklist |
| `agent/AGENT.md` | Agent mission, allowed and prohibited actions, release gates |
| `data/<type>/*.json` | One JSON record per page; `data/examples/` holds reference templates |
| `scripts/validate_content.py` | Dependency-free content gate, mirrors the content contract |
| `scripts/import_to_wordpress.py` | Idempotent REST importer from `data/` to a WordPress staging site |
| `scripts/fetch_evidence.py` | Fills a compound record's source ledger from Europe PMC and ChEMBL; writes a research brief; never writes claims |
| `research/registry.json` | Compound registry: identity, class, target, peers, and the stack/comparison/tool plan by wave. Hand-maintained |
| `research/registry.md` | Generated table view of the registry joined with fetched evidence counts. Never edit by hand |
| `scripts/build_registry.py` | Builds `registry.md` and fails on dangling stack components, comparison sides or classes |
| `research/<slug>.md` | Per-compound research briefs with abstracts for the writer |
| `.github/workflows/` | CI: validator on every PR and push to `main`, plus PHP lint |
| `.github/ISSUE_TEMPLATE/` | Structured issue form for content requests |
| `.github/CODEOWNERS` | Required reviewer per area |
| `wp-content/plugins/research-database/` | Post types, REST-exposed record fields, noindex and sitemap control |
| `wp-content/themes/research-reference/` | Lightweight Elementor-compatible theme with record templates |
| `src/`, `astro.config.mjs`, `vercel.json`, `middleware.ts` | Static site: Astro pages built from `data/`, deployed on Vercel |

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

Milestones 1 to 4 in [`docs/PRD.md`](docs/PRD.md) are complete: content contract with validator and CI, plugin with record-state index control, an activatable theme, and the REST importer. Milestone 5, schema and canonical QA, is next and needs a staging host.

## Researching a compound

The compound list, its taxonomy and the page plan live in `research/registry.json`.
Identity goes in the registry; evidence goes in records. A half-life or a dose is a
claim with a source, never a table cell.

```bash
python3 scripts/build_registry.py --check   # cross-reference check, runs in CI
python3 scripts/build_registry.py           # regenerate research/registry.md
```

`scripts/fetch_evidence.py` reads the registry and runs targeted Europe PMC queries for each section in
`docs/page-template-spec.md`, classifies every paper's evidence tier from its
publication type and MeSH species headings, looks the compound up in ChEMBL, and
writes two files: a record in status `researched` whose source ledger holds real,
resolvable citations, and a brief under `research/` with the abstracts so the
writer works from evidence rather than memory.

```bash
python3 scripts/fetch_evidence.py --all --dry-run   # evidence landscape only
python3 scripts/fetch_evidence.py bpc-157           # one record and one brief
```

It writes no claims. Under `agent/AGENT.md` deciding what a paper supports is
human work; the script imports cited source metadata and stops. It also refuses
to touch any record a human has moved past `researched`. Standard library only,
no API key.

## Building the site (Vercel)

The records under `data/` have two renderers that read the same files. The
static site is an Astro app at the repository root; the WordPress consumer in
`wp-content/` is retained and still builds in CI. `data/` is the source of
truth for both.

```bash
npm ci
SITE_URL=https://your-domain.example npm run build   # writes dist/
npm run dev                                          # local preview
```

On Vercel: import the repository, leave the root directory as the repo root,
framework preset Astro, and set `SITE_URL` to the production origin. Every pull
request gets a preview deployment, which is where a reviewer sees the rendered
page with its evidence labels and sources before approving.

Index safety is built in: a record is indexable only in status `published`;
everything else renders with `noindex` and is excluded from `/sitemap.xml`,
whose `lastmod` comes from the record's changelog. Unknown paths return a real
404, and `middleware.ts` redirects mixed-case URLs to the lowercase slug.

Astro 5 is pinned because it supports Node 20; Astro 6+ needs Node 22 and is a
one-line upgrade once every build environment has it.

## Importing to staging

The importer validates first and refuses to send anything CI would reject. It
matches records on slug, so re-running updates instead of duplicating, and a
record whose source has not changed reports `unchanged` and is not rewritten.
Only records in the `published` state become published WordPress posts;
everything else lands as a draft and stays out of the sitemap.

```bash
export WP_URL=https://staging.example.com
export WP_USER=your-wp-user
export WP_APP_PASSWORD='application password from WP profile'

python3 scripts/import_to_wordpress.py --dry-run   # plan
python3 scripts/import_to_wordpress.py             # import
```

Credentials come from the environment only. Never commit them.
