# Competitive baseline

Measured 2026-09-07 against `peptidedosingprotocols.com`, the closest structural
competitor to this project: the same page taxonomy (compound, stack, cycle),
the same programmatic approach, and a live index.

This file is the evidence base for `docs/page-template-spec.md`. Re-measure before
each expansion batch; do not treat these numbers as permanent.

## Method

89 pages fetched directly, comprising the 79 URLs in the competitor's four
programmatic sets plus four hub pages and six top-level pages. Body text reduced
to overlapping 6-word sequences with header, footer and navigation removed.
Boilerplate is any sequence appearing in at least 80% of the pages in a set.
Uniqueness is the share of a page's sequences that are not boilerplate.

## What the incumbent achieves

| Set | Pages | Mean unique | Range | Median words |
|---|---|---|---|---|
| Compound | 44 | 96.2% | 94.1–97.6% | 5,821 |
| Stack | 11 | 95.4% | 92.8–96.6% | 6,898 |
| Cycle | 11 | 95.4% | 93.4–97.1% | 4,159 |
| Deal | 12 | 91.5% | 87.9–95.3% | 1,870 |

Zero pages fall below 40% uniqueness. The highest similarity between any two
pages in the set is 15.1%. No page is under 300 words. Their flagship compound
page carries 20 sections, 86 subsections, 10 tables, 17 images, 12 citations to
PubMed or DOI, and a working reconstitution calculator.

**Implication for our release gates.** Our current floor of 40% unique body
content is a compliance threshold, not a competitive one. A page that clears 40%
in this niche is roughly half as differentiated as everything already ranking.
The gates in `agent/AGENT.md` now carry a competitive target of 85% alongside the
40% floor.

## Where they actually rank

Two representative queries, checked 2026-09-07:

| Query | Their position | Ahead of them |
|---|---|---|
| BPC-157 dosage protocol guide | 2 | perfectb.com |
| Wolverine stack BPC-157 TB-500 dosing | 4 | perfectb.com, peptideadvisors.org, spartanpeptides.com |

Two observations matter more than the positions. Clinical entities rank in these
results, including a medical clinic and two provider sites, which confirms that
credential signals carry weight on this topic. And a calculator page ranks on the
stack query, which is why `/tools/{slug}` deserves first-class treatment rather
than being an appendix to compound pages.

This is a two-query sample. Build a 50 to 100 term set with position data before
committing budget.

## The incumbent's structural weaknesses

Ordered by how much separation each one offers us.

1. **No reviewer.** All 78 of their content pages are authored by one person whose
   only declared credential in schema is a Bachelor of Science in Civil
   Engineering. Not one page declares `reviewedBy`. On a health topic this is the
   largest single gap in the market.
2. **Evidence is prose, not data.** They cite 12 sources per page but publish no
   structured evidence rows. Nobody in the niche does.
3. **No adverse-event frequencies.** Effects are listed without incidence.
4. **No interactions section** anywhere in the template.
5. **No video.** Zero video elements on any compound page, despite the site
   running a video sitemap.
6. **Freshness has stalled** on 33 of 78 pages, where modified date still equals
   publish date. Their sitemap `lastmod` is generation time, not revision time,
   so their freshness signal is already degraded.
7. **Titles truncate.** 44 titles exceed 65 characters, the longest at 111, so
   their result snippets are cut mid-phrase.
8. **Their monetized pages are their weakest content** on both word count and
   uniqueness, and carry 95 followed affiliate links with no `sponsored`
   attribute. That is live risk exposure, not a pattern to copy.

## What we must not copy

Their compound pages read as protocol instruction, including schedule
prescriptions and administration guidance framed for a reader to follow. This
project prohibits that, and the prohibition stands regardless of competitive
pressure.

The consequence is strategic, not merely procedural. We cannot win by matching
their prescriptiveness, so the differentiation has to come from evidence rigour:
structured study rows, explicit evidence labels, named review, stated
uncertainty, and honest revision history. `docs/page-template-spec.md` is built
on that basis, and every section that would otherwise invite personal guidance is
reframed to report what studies did rather than what a reader should do.
