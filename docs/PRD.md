# Product requirements: Peptide Research Reference

Last updated: 2026-09-03. Owner: @fosterwei. Status: pilot scaffold.

## Problem

English-language information about research peptides is split between primary literature that is hard to read and community forums that present anecdote as fact. Readers who want to know what has actually been studied have no single, cited, non-promotional reference.

## Audience

- **Primary:** global English readers researching a specific compound, comparison, or stack who want cited facts and evidence boundaries.
- **Secondary:** editors and reviewers who need a structured, auditable content pipeline.
- **Not served:** anyone seeking personal dosing, treatment, or purchasing advice.

## Goals

1. One unified WordPress domain with programmatic pages for compounds, stacks, comparisons, cycles, and tools, plus editorial posts.
2. Every published claim is labeled with its evidence tier and cites a primary source.
3. A named human reviews every record before it becomes indexable.
4. The agent can draft and validate at scale, but cannot publish.

## Non-goals and why

| Non-goal | Reason |
|---|---|
| Personalized dosing or treatment advice | Legal and ethical exposure; contradicts the research-reference positioning that earns trust |
| Affiliate modules during the pilot | Commercial signals undermine E-E-A-T while the site has no track record; revisit after indexation review |
| Direct publishing by the agent | A single hallucinated claim on a medical topic is unrecoverable reputationally; PR review is the control |
| Indexing drafts or placeholders | Thin or duplicate pages harm the whole domain's crawl budget and quality signals |
| Provider-specific hosting integration | Keeps the repo portable between SiteGround, Hostinger, or any WordPress host |

## Pilot scope

| Content | Target count |
|---|---|
| Compound records | 20–30 |
| Stack or comparison pages | 2–3 |
| Editorial posts | 5–8 |
| Tools or calculators | 1–2 |

Hard cap of 50 indexable pages before the indexation review.

## Success metrics

Measured 4 weeks after the pilot goes live unless noted.

| Metric | Target |
|---|---|
| Validator pass rate on first PR run | ≥ 80% of agent-drafted PRs |
| Median time from PR open to human approval | ≤ 3 business days |
| Indexed pages vs published records (Search Console coverage) | ≥ 90% |
| Records with every claim source-cited | 100% (hard gate) |
| Search Console impressions | Baseline established; growth target set at review |
| Pages flagged stale at 8-week review | ≤ 10% |

## Milestones and acceptance criteria

| # | Milestone | Done when |
|---|---|---|
| 1 | Content contract, validator, CI | Validator enforces every list in `docs/content-contract.md`; CI runs on PR and push to main |
| 2 | Plugin: post types, record fields, index control | All five post types register; `record_status` gates noindex and sitemap; PHP lint passes |
| 3 | Theme scaffold | Activates on a clean WordPress 6.4+ install; renders record fields; Elementor can take over pages |
| 4 | Importer | A script reads `data/**/*.json` and creates or updates posts via REST on staging, idempotently |
| 5 | Schema, canonical, sitemap QA | Every page type passes Rich Results Test and has a self-canonical on staging |
| 6 | Internal-link graph | Each compound page links to its related stacks, comparisons, and posts, and vice versa |
| 7 | Pilot content | Counts in the pilot scope table are met, all in `published` state with named reviewers |
| 8 | Launch and indexation review | Search Console verified, sitemap submitted, 2–4 week review scheduled |

Milestones 1 to 3 are complete in this repository. Milestone 4 is next.

## Constraints

- Hosting-agnostic; PHP 8.2+; WordPress 6.4+.
- No runtime dependencies for the validator.
- Branch protection is unavailable on a free private repo. Until the repo is public or on GitHub Pro, PR-gating relies on CI plus the deploy step only shipping merged `main`.

## Open decisions

- Whether cycle pages stay in scope, given how close "cycle" sits to protocol advice.
- Which SEO plugin (core sitemap, Yoast, or Rank Math) staging will use; the plugin supports all three.
