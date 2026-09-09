# Pilot launch checklist

## Infrastructure
- [ ] WordPress staging configured on SiteGround or Hostinger.
- [ ] HTTPS, backups, caching, PHP 8.2+ and database monitoring enabled.
- [ ] Research Database plugin activated; `/compounds/`, `/stacks/`, `/compare/`, `/cycles/`, `/tools/` resolve (rewrite rules flushed on activation).
- [ ] Research Reference theme activated; a draft record renders the review notice, evidence labels, and source list.
- [ ] Production credentials stored only in hosting or GitHub secrets.
- [ ] WordPress application password created for the importer; `WP_URL`, `WP_USER` and `WP_APP_PASSWORD` set in the environment, never committed.
- [ ] `python3 scripts/import_to_wordpress.py --dry-run` reviewed before the first real import.
- [ ] Importer re-run once with no source change; every record reports `unchanged`.

## Content
- [ ] `python3 scripts/fetch_evidence.py --all --dry-run` run; compounds with no indexed human trials have their human-dosing sections suppressed, not padded.
- [ ] 20–30 compound records in `published` state with named reviewers.
- [ ] 2–3 stack/comparison pages reviewed.
- [ ] 5–8 editorial posts reviewed.
- [ ] 1–2 calculators/tools tested with edge cases.
- [ ] `python3 scripts/validate_content.py` passes on `main`.

## Index safety
- [ ] A record in `draft` state that WordPress has published returns `noindex` and is absent from the sitemap.
- [ ] Canonical, robots, sitemap and schema inspected on every page type.
- [ ] Medical, safety, and regulatory claims each cite a source id and carry an evidence label.
- [ ] No affiliate modules in pilot.

## Measurement
- [ ] Search Console and analytics configured; sitemap submitted.
- [ ] Baseline for the metrics in `docs/PRD.md` recorded.
- [ ] Batch review scheduled 2–4 weeks after launch.
- [ ] Every indexable record has a named reviewer with a stated credential.
- [ ] Uniqueness measured per page and recorded in `uniqueness_pct`.
- [ ] Titles within 60 characters and descriptions within 160, checked across all page types.
- [ ] Sitemap contains no redirecting or placeholder URLs.
- [ ] `lastmod` matches record revision time, not build time.
- [ ] Mixed-case and trailing-slash URL variants resolve to the canonical page.
- [ ] Unknown slugs return 404 rather than a 200 placeholder.
- [ ] Competitive baseline re-measured before the next expansion batch.
