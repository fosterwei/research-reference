# Page template spec

Section-level structure for each programmatic page type. Derived from the
measured incumbent baseline in `docs/competitive-baseline.md` and constrained by
the prohibitions in `agent/AGENT.md`.

## How to read this

- **Source** says where a section's content comes from. `Per record` means it
  varies by compound and counts toward uniqueness. `Shared` means template text
  identical across pages, which counts *against* uniqueness. `Computed` means
  derived from record fields.
- **Label** marks sections where every claim needs an evidence label.
- Sections marked **NEW** are absent from the incumbent template. They are the
  differentiation, not the filler.
- A section whose record fields are empty must be **suppressed, not rendered
  empty**. A visible heading with no content is a quality signal against us.

## Shared-text budget

Uniqueness is measured after removing header, footer and navigation, so template
prose counts against every page carrying it. Keep the total of all `Shared`
sections under 600 words. At the section budgets below that puts a fully
populated compound page near 90% unique before computed sections are counted,
against the incumbent's 96.2% mean.

## Compound page — `/protocols/{slug}`

| # | Section | Contents | Words | Source | Label |
|---|---|---|---|---|---|
| 1 | Snapshot | Reported dose ranges, routes, half-life, study durations, evidence tier | 120 | Per record | yes |
| 2 | **Reviewed by** NEW | Reviewer name, credential, review date, link to changelog | 60 | Shared | — |
| 3 | What it is | Identity, class, aliases, what it has been studied for | 350 | Per record | yes |
| 4 | **What the evidence shows** NEW | Evidence table: study, year, design, n, species, dose, route, duration, outcome, label | 600 | Per record | yes |
| 5 | Doses reported in studies | Published dose ranges by route, with the study each comes from | 450 | Per record | yes |
| 6 | **Weight-normalized doses** NEW | mg/kg figures *as published*, plus why they do not transfer between species | 250 | Computed | yes |
| 7 | Reconstitution mathematics | Concentration and volume math, worked examples | 400 | Computed | — |
| 8 | **Preparation walkthrough** NEW | Short video plus full transcript, no administration instruction | 200 | Per record | — |
| 9 | Equipment described in studies | What published protocols used | 200 | Shared | — |
| 10 | **Escalation schedules used in studies** NEW | How trials stepped doses, reported as study design | 300 | Per record | yes |
| 11 | **Reported interactions** NEW | Interaction table with mechanism and label | 350 | Per record | yes |
| 12 | Exclusion criteria in studies | Who published trials excluded, and why | 250 | Per record | yes |
| 13 | **Adverse events and frequency** NEW | Event, incidence, denominator, source | 400 | Per record | yes |
| 14 | Biomarkers measured in studies | What trials monitored and at what interval | 350 | Per record | yes |
| 15 | Reported timelines | Onset and duration observed, with study context | 300 | Per record | yes |
| 16 | Storage and stability | Temperatures, reconstituted stability windows | 200 | Per record | yes |
| 17 | **Reading a certificate of analysis** NEW | How to interpret purity documentation, methodology only | 300 | Shared | — |
| 18 | Common misreadings of the evidence | Where community summaries diverge from sources | 350 | Per record | yes |
| 19 | How it compares | Comparison table against peer compounds | 400 | Computed | yes |
| 20 | Regulatory status | By jurisdiction, with date checked | 250 | Per record | yes |
| 21 | Open questions | What is genuinely unknown, stated plainly | 200 | Per record | — |
| 22 | Questions people ask | FAQ, each answer self-contained | 500 | Per record | yes |
| 23 | Sources | Full citations, DOI or PubMed, publication dates | 300 | Per record | — |
| 24 | **Reference card** NEW | Printable summary, generated not hand-made | 60 | Computed | — |
| 25 | Related records | Internal links from the entity graph | 100 | Computed | — |
| 26 | **Last reviewed and what changed** NEW | Revision history with dates | 80 | Per record | — |

Total near 6,300 words when fully populated, against the incumbent's 5,484 on
their strongest page.

### Section ordering rationale

The reviewer block sits at position 2 because it is the differentiator and
belongs above the fold. The evidence table sits at 4, before dose reporting,
because doses are meaningless without the study context that produced them.
Putting the table first also makes the most citable block on the page the
earliest substantial content, which matters for extraction into AI answers.

## Stack page — `/stacks/{slug}`

Inherits the compound spine with four changes.

| Change | Detail |
|---|---|
| Add | **Component evidence matrix**: each component's own evidence label, so a stack of two weakly evidenced compounds cannot inherit a strong label |
| Add | **Combination evidence**, stated separately, including the case where no study tested the combination |
| Add | **Format comparison**: pre-blended against separate preparation, with the mathematics for each |
| Replace | Single schedule becomes a **combined schedule** resolving components with different reported frequencies onto one calendar |

The combination-evidence section is mandatory even when empty of positive
findings. "No published study tested this combination" is the single most
valuable sentence such a page can carry, and it is the sentence the incumbent
pattern omits.

## Cycle page — `/cycles/{slug}`

Question-form headings throughout. The incumbent's cycle template is their
best-built set precisely because it asks real questions rather than prefixing a
compound name to generic labels. Structure as a duration ladder: what the
shortest reported duration was, what the common range is, what the longest
reported is, where each figure comes from, and what remains unstudied. Each rung
is a distinct question with its own answer and its own sources.

## Tool page — `/tools/{slug}`

Promote to a first-class page type rather than an embedded widget. A calculator
page ranks in this niche, per the baseline. Required: the formula stated in the
open, every input defined with units, worked examples covering edge cases, the
assumptions the formula makes, and what it deliberately does not compute.

Tools must not accept personal parameters that turn a calculation into advice.
Concentration and volume mathematics are permitted. Anything that takes a body
weight or a condition and returns a recommended dose is not.

## Heading style

Use question-form or plain descriptive headings. Do not prefix the entity name to
every heading. The incumbent repeats the compound name across all 20 of their
headings, which helps no reader and no machine, and reads as keyword stuffing.
Name the entity in the title, the snapshot, and the first line of body text, then
write normally.

## Metadata limits

| Element | Limit | Reason |
|---|---|---|
| Title | 60 characters | 44 incumbent titles exceed 65 and truncate in results |
| Description | 160 characters | 34 incumbent descriptions exceed it |
| H1 | Exactly one | Enforced by the validator |
| Slug | Lowercase, hyphenated, under 100 characters | Matches existing contract |

Reserve the first 55 characters of a title for the entity name and the page's
purpose. Move qualifiers into subheadings.

## Post-pilot sections

Deliberately excluded while `agent/AGENT.md` prohibits affiliate content: cost
per cycle, supplier comparison, and availability. Each has genuine search demand
and each should be reconsidered only when the affiliate prohibition is lifted,
with `rel="sponsored nofollow"` from the first commit. The incumbent's monetized
pages are their weakest content and carry 95 followed affiliate links, which is
the failure mode to avoid rather than imitate.
