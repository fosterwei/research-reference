# Peptide Research Reference — GitHub Agent Starter

Hosting-agnostic WordPress starter for a global English research-reference site.

The agent drafts, validates, and opens pull requests for programmatic pages and editorial posts. It must not publish directly or invent medical, safety, regulatory, or affiliate claims.

## Layout

- `agent/AGENT.md` — operating policy and release gates
- `docs/` — content contract and launch checklist
- `data/` — reviewed JSON examples
- `scripts/` — dependency-free validation
- `.github/` — Actions, PR, and issue templates
- `wp-content/` — custom plugin and lightweight theme scaffold

Compatible with SiteGround and Hostinger WordPress staging; no provider-specific API is required.

## What this starter does

This repository is the implementation foundation for the agreed project:

- one unified WordPress domain;
- global English research readers;
- programmatic pages for compounds, stacks, comparisons, cycles, and tools;
- editorial posts at `/blog/{slug}`;
- hybrid presentation: Elementor for marketing pages, custom templates for programmatic pages, and Gutenberg for posts;
- research-reference content only—no personalized treatment or dosing recommendations;
- primary-source collection plus human review;
- 30–50 page pilot before expansion;
- no affiliate modules during the pilot;
- GitHub pull-request approval before any production change.

## How to use the repository

### Content workflow

1. Create an Issue from the `New or update content record` template.
2. Add a JSON record under `data/` using the compound or post example.
3. Attach source URLs, publication dates, evidence tiers, author, and reviewer.
4. Run `python scripts/validate_content.py`.
5. Open a pull request. The GitHub Action repeats the validation automatically.
6. Have an editor review factual, safety, regulatory, and medical-sensitive claims.
7. Merge only after approval, then import/publish through WordPress staging.

### Record states

`discovered` → `researched` → `draft` → `reviewed` → `published` → `stale` → `retired`.

Only reviewed and published records with complete sources should be indexable. Placeholder, duplicate, incomplete, or stale records must remain noindex and out of the sitemap.

### WordPress installation

Copy `wp-content/plugins/research-database` to the WordPress plugins directory and activate it. Copy `wp-content/themes/research-reference` to the themes directory and activate it. The current plugin registers `compound`, `stack`, and `comparison` post types and marks unpublished records noindex. Extend it with custom fields, full templates, schema, sitemap integration, and import tooling before production use.

### GitHub Actions

`.github/workflows/content-quality.yml` runs on every pull request. It currently validates JSON syntax, required fields, slug format, duplicate slugs, and sources for reviewed/published records. Add link, schema, canonical, uniqueness, word-count, and sitemap tests as the page system is implemented.

## Safety and agent boundaries

The agent may draft and validate research-reference content, but it must not invent citations, convert community schedules into clinical facts, make personal recommendations, publish directly to production, or add affiliate recommendations during the pilot. A named human reviewer is required for safety, regulatory, administration, and medical claims.

## Hosting notes

The repository is hosting-agnostic. On SiteGround or Hostinger, use HTTPS, staging, automated backups, PHP 8.2+, caching/object cache where available, a managed database, and a deployment process that requires a reviewed merge. Keep production WordPress credentials in hosting/GitHub secrets; never commit them.

## Current limitations and next build milestones

This is a scaffold, not a finished website. Next milestones are: (1) custom field model and admin UI; (2) complete compound/stack/comparison/cycle/tool templates; (3) Gutenberg editorial workflow; (4) source importer and freshness checks; (5) schema/canonical/sitemap generation; (6) internal-link graph; (7) staging importer and deployment; (8) 20–30 compound, 2–3 comparison/stack, 5–8 post, 1–2 tool pilot.

## Repository map

| Path | Purpose |
|---|---|
| `agent/AGENT.md` | Agent mission, allowed actions, prohibited actions, evidence labels, release gates |
| `docs/content-contract.md` | Page types, URL patterns, editorial taxonomy, index states |
| `docs/launch-checklist.md` | Pilot launch QA checklist |
| `data/*.json` | Structured records and examples |
| `scripts/validate_content.py` | Dependency-free content gate |
| `.github/workflows/` | Pull-request automation |
| `.github/ISSUE_TEMPLATE/` | Structured content requests |
| `wp-content/plugins/` | WordPress content-type and SEO-control code |
| `wp-content/themes/` | Lightweight presentation scaffold |
