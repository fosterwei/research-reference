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

Compound pages were planned at `/protocols/{slug}` and renamed before indexing, at a time when the site declined dosing guidance entirely. On 2026-11-07 the owner widened the scope: compound and stack pages may now carry a **protocol layer** that answers how a compound has been dosed, under the rules in the Protocol layer section below. URLs do not change; the protocol is a section of the existing page, anchored at `#protocol`, so the record keeps one URL and one review.

## Editorial posts

Posts live in `data/posts/` and publish at `/blog/{slug}`. They must add interpretation beyond the programmatic pages they link to.

Categories: Research, Evidence, Safety & Regulation, Methodology, Industry News, Reviews.

### Guide series: index → pillar → sub

A post can belong to a guide series, which arranges posts as a three-level tree for readers and
search engines. Rendered by `src/layouts/GuideV2.astro`; rules in `src/lib/guides.ts`; checked by
`scripts/validate_content.py`.

| Field | Meaning |
|---|---|
| `series` | Series key shared by every page in it (`cagrilintide`) |
| `role` | `index` (exactly one per series), `pillar` (one per topic) or `sub` |
| `parent` | Path of the page above. A pillar's parent is the series index; a sub's parent is a topic pillar. A pillar may be an existing record page (e.g. `/stacks/cagrisema`) |
| `topics` | Index only: ordered `[{label, pillar, blurb?}]`; every topic pillar must exist |
| `order` | Reading order among siblings |
| `topic`, `short_title` | Topic label shown on the page; short name used in breadcrumbs |
| `about` | Record paths the post is about; those records list it under "Related records" |
| `sections` | `[{id, heading, lede?, html}]`, the written body, one H2 each |
| `faq` | `[{question, answer}]` |
| `seo` | `{title ≤ 60, description ≤ 160}` |

Citations in `body`, `excerpt`, `sections` and `faq` are written `[[n]]`, where n is the 1-based
position of the source in `sources[]`; the page renders a superscript `[n]` linking straight to
that source. Every marker needs a source and every source needs a marker. External links in prose
appear only through markers, so the nofollow policy holds. Each page renders visible breadcrumbs
and `BreadcrumbList` JSON-LD, links up to its parent, and lists its children (pillar) or siblings
(sub). Guide posts with `sections[]` go through the same content loop as record pages
(`research/intents/<slug>.json`, an audit with triage and exit run; `scripts/loop_status.py`).

## Record states

`discovered` → `researched` → `draft` → `reviewed` → `published` → `stale` → `retired`

- Records in `draft`, `reviewed` or `published` are indexable and enter the sitemap; `discovered`, `researched`, `stale` and `retired` render noindex.
- `reviewed` marks that a named person has checked the record; their name and credential then appear on the page. It is not a precondition for indexing.
- Every non-editorial claim cites at least one source; editorial claims are labelled as such on the page.

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
| `editorial` | Written from general knowledge, not from a ledger source: mechanism, history, class context, regulatory status, what is commonly reported. Marked on the page as editorial synthesis; may carry `pending_source: true` when a known document is still to be added |

## Protocol layer

Added 2026-11-07. A compound or stack record may carry `attributes.protocol`, a list of
claims in the standard claim shape whose `fields` describe a regimen:

| Field | Meaning |
|---|---|
| `phase` | Where in the regimen this row sits: `start`, `step`, `maintenance`, `cycle`, or `single` |
| `dose` | As the source states it, with unit |
| `frequency` | As the source states it |
| `route` | As the source states it |
| `duration` | How long this phase ran or runs |
| `population` | Who the source gave it to |

Three provenances are allowed, rendered as three distinct blocks, never merged:

1. **Approved label** (`approved-label`): dosing from a regulator-approved label, cited to
   the label. The only provenance that may be called a dose "for" an indication.
2. **As studied** (`human-clinical-trial`, `observational-human`): regimens trials actually
   administered, one row per arm or phase, cited to the paper. Animal regimens may appear
   only under their own label and never in a human table.
3. **Practical protocol** (`editorial`): a synthesised schedule written by us. This is the
   widening. Every step must name, in `source_ids`, the studied or labelled rows it is
   derived from; a step with no basis is invalid. The section states that it is a
   synthesis and not a prescription, carries the site-wide notice, and is signed by the
   reviewer separately through `review.protocol_reviewed_at`. Until that date is set the
   block renders with an "awaiting pharmacist review" tag and the page stays indexable.

**How a practical protocol is written** (added 2026-11-07). Each step carries
`fields.weeks` (when it applies: `1–4`, `13–48`, `by week 24`, `every day`) and
`fields.action` (one thing to do, in the imperative, with dose, frequency and
route); `value` is the reason, naming the trial. The page renders the steps
twice: as a week-by-week table of `weeks` and `action`, and as a numbered list
that leads with the action and follows with the reason and basis. Operational
points the sources state, such as when to delay a step, how to apply a topical,
or what side effect to expect when, are editorial claims with `fields.phase:
"note"` and their own `action` and basis; they render as "Practical notes".
Timing comes from the full text where the abstract is silent (Europe PMC open
access); where no source on the page states the escalation, the step says so
instead of filling it in. The validator rejects a step without `weeks` or
`action`.

**How the protocol is presented** (added 2026-11-08). The owner asked for the
layout readers know from dosing-guide sites, with data still from authoritative
sources. The section opens with a quick-start box (starting dose, titration
path, frequency, route, evidence count), shows the schedule as a table with
weeks, dose, action and basis, ends with "Practical notes and troubleshooting",
and feeds dosing questions ("What is the starting dose of X?", "What is the X
dosing schedule?", "What is the approved dose of X?", "What doses of X have been
studied in humans?") into the page FAQ and its FAQPage markup. All of it is read
from the same claims by `src/lib/protocol.ts`; the presentation never computes
a dose. Supply lists, vendor reviews and affiliate links from those sites are
not adopted.

`community-reported` regimens stay where they were: in the dosage chart, labelled as
circulating, sourced to where they appear. They are not a protocol provenance.

What remains out of scope: a body-weight input that returns a dose, purchase links,
supplier recommendations, and any protocol for a compound with no human regimen in its
ledger (the section is not rendered rather than filled from animal data).

The site's standing notice changes from "nothing here is dosing advice" to "general
information from published studies and labels, not individual medical advice." Every
template that printed the old sentence prints the new one; `scripts/check_links.py`
fails the build if the old sentence survives on a page that renders a protocol.

## Plain language and citation marks

Changed 2026-11-08 at the owner's direction: pages no longer show verbatim
abstract sentences. Every extractive claim carries `plain`, a one- or
two-sentence plain-English statement of what its source reports, and the page
shows `plain` followed by a numbered citation mark (`[3]`) that links to the
numbered Sources list. `source_excerpt` stays in the record so the reviewer and
the validator can check `plain` against the source; it is not rendered.

How `plain` is written (E-E-A-T, after studying how dosing-guide sites write
evidence, and stricter): say which study (design, population, size, year,
first author when known); then the result with its own numbers, units,
comparison and time point, never rounded or added to; name the evidence level
in words (species for animal work, "in cells grown in a lab" for in-vitro, "no
control group" for uncontrolled work); add the limit that matters; report,
never advise; explain a technical term once in brackets; at most 45 words.

Enforced by `scripts/validate_content.py` (`check_plain`): an extractive claim
outside the protocol table without `plain` fails the build unless its record is
listed with a reason in `research/plain-pending.json`; `plain` may not carry a
citation mark or id. The drafting check (numbers in `plain` must appear in the
source, animal or in-vitro claims must say so, banned advice words, length)
runs before a rewrite is merged.

## Fixed sections

Side effects, who should avoid, blood tests, storage, regulatory status and
reported use always render as their own section when the record has a finding
for them. "Who should avoid" holds only real exclusions: a trial's exclusion
or eligibility criteria, or an approved label's contraindications and
pregnancy, breast-feeding or caution statements. A sentence that says who was
enrolled or how people were assigned is design, not an exclusion, and does not
belong there. Storage comes from the approved label where one exists, and
otherwise from stability studies. Minor sections with a single finding are
gathered into one section on the page rather than given an H2 each.

## Claim fields

Every entry in `attributes.<field>` is a claim object. Required: `value`, `evidence_label`, `source_ids`. Optional, and expected on anything the agent drafted:

| Field | Meaning |
|---|---|
| `source_excerpt` | The sentence or sentences from the source that `value` restates, copied exactly. The reviewer checks `value` against this, not against memory. Required when `drafting` is `extractive`; enforced by the validator. |
| `drafting` | How the claim was produced. `extractive` means `value` is a verbatim source sentence prefixed with study context (design, species, n, year) and nothing else. Absent means a person wrote it. |
| `fields` | Structured columns for the evidence table (`study`, `year`, `design`, `n`, `species`, `dose`, `route`, `duration`, `outcome`). Used only under `attributes.evidence_table`. |

`attributes.evidence_table` holds one claim per primary study in the ledger and renders as the "What the evidence shows" table. Reviews never appear in it.

## Source ledger

Each source has `id`, `title`, `url` (http or https), `published` (YYYY-MM-DD), and optional `kind` (`peer-reviewed`, `regulatory`, `preprint`, `clinical-registry`, `manufacturer`, `community`, `other`). Claims reference sources by `id`, so a claim can never point at a source that is not in the ledger.

## Slugs

Lowercase words joined by single hyphens. Slugs must be unique within a URL prefix. Examples under `data/examples/` are excluded from uniqueness and are never imported.

## Metadata limits

| Element | Limit | Reason |
|---|---|---|
| `seo.title` | 60 characters | Longer titles truncate in results; 44 of the incumbent's titles exceed 65 |
| `seo.description` | 160 characters | 34 of the incumbent's descriptions exceed it |
| H1 | exactly one per page | Rendered by the theme, not stored in the record |
| Slug | lowercase, hyphenated, at most 100 characters | Enforced by the validator |

Reserve the first 55 characters of a title for the entity name and the page's
purpose, and move qualifiers into subheadings.

## Sitemap rules

Records in `draft`, `reviewed` or `published` that pass the gates enter the sitemap. Entries must be
final 200-status URLs; a redirecting or placeholder URL in the sitemap is a
defect. `lastmod` carries the record's own revision timestamp from `changelog`,
never the build time.

## Section structure

`docs/page-template-spec.md` specifies the sections each page type renders, which
sections vary per record and which are shared template text. Shared text counts
against measured uniqueness, so the spec caps it.
