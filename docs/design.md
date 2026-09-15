# Design and reading-experience spec

How programmatic pages look, read and behave. `docs/page-template-spec.md`
says *what sections* a page has; this document says *how they are rendered*.
Any agent or person changing `src/` builds against this file. Values here are
the ones in `src/styles/global.css` and `src/styles/compound-v2.css`; when the
two disagree, the stylesheet is wrong and this file is the reference until it
is corrected in the same pull request.

Status: the v2 design is live on one trial route, `/compounds/semaglutide`
(`src/pages/compounds/semaglutide.astro`). It becomes the shared template only
after review, by moving the v2 components into `[slug].astro` and deleting the
trial route. Do not apply v2 to other pages before that decision is recorded
in this file's changelog.

## 1. What the research found, and what we took from it

The incumbent (`docs/competitive-baseline.md`) was crawled and measured; its
semaglutide page was read closely as a reference for reading experience.

| Observed on the incumbent | Our response |
|---|---|
| Persistent table of contents in a sidebar, 23 in-page anchors | Adopted. Sticky, grouped, generated from the rendered sections so it cannot list a section that is not there. |
| A "quick start" / key-facts block before the body | Adopted as "At a glance": six fact tiles computed from the record. |
| 17 tables per page; dosage chart near the top | Adopted the principle: the evidence table is the first substantial block. Tables get sticky headers and zebra rows. |
| Every H2 prefixed with the compound name (20 of 20) | Rejected. Headings are descriptive or question-form; the entity is named in the title, dek and first paragraph. |
| 627 KB median HTML, hydration payload | Rejected. Budget is 100 KB HTML per page, no client JavaScript except the calculators. |
| Affiliate blocks, supplier CTAs, region selector | Rejected during the pilot per `agent/AGENT.md`; nothing on the page invites a purchase. |
| "Coming soon" placeholder pages returning 200 | Rejected. Unknown paths return 404; empty sections are not rendered. |
| Author line without credentials; no reviewer | Inverted. The reviewed-by block is the second element on the page and says "not yet reviewed" until a named, credentialed reviewer signs. |
| Its visual identity: colours, logo, layout signature | Not copied. Structure and reading patterns are generic UX; the look is ours. |

Reading-experience problems found in our own first template, which the v2
design corrects: no navigation on a 22-section page; claims rendered as a
dense list where study metadata ran into the quotation; a definition-list
snapshot with no hierarchy; shared methodology text indistinguishable from
compound-specific evidence; no visual difference between draft and reviewed.

## 2. Principles

1. **Evidence first, then method, then context.** The study table is the
   first substantial block after "What it is". Shared method notes sit in one
   visually distinct band. Comparisons, regulation, FAQ and sources follow.
2. **Metadata and quotation are separate objects.** A claim renders study
   design, species, sample size, year and tier on a meta row; the verbatim
   sentence below it in the serif face; the source id last. Never a run-on.
3. **Nothing renders empty.** A section whose record field is empty is
   omitted, and the table of contents omits it too. A visible heading over
   nothing is a defect (`docs/page-template-spec.md`).
4. **Shared text looks shared.** Method notes, caveats and the reference card
   sit on `--sunk` or inside a bordered card so a reader can tell template
   text from evidence about this compound.
5. **State is visible.** Draft records carry a status pill in the title block
   and a status bar above the body. Published records carry the reviewer's
   name and credential in the same positions.
6. **No affordance implies advice.** No body-weight input, no "your dose", no
   schedule builder, no purchase link. Calculators state their formula and
   refuse personal parameters (`docs/page-template-spec.md`, Tool page).
7. **Verifiable in one click.** Every claim links to its source id; every
   source row has the id, date and outbound link. The evidence table's study
   column links to the same anchors.
8. **Readable at length.** Our own prose (dek, summary, ledes, FAQ, open
   questions) is capped at about 22 words per sentence. Quotations are never
   edited for length or readability; they are verbatim by policy.

## 3. Tokens

Defined once in `src/styles/global.css`; components reference tokens, never
literals, so dark mode is a token swap.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#fbfbf9` | `#0e1317` | page ground |
| `--surface` | `#ffffff` | `#151c22` | cards, header |
| `--sunk` | `#f1f3f5` | `#111820` | method band, table headers, code |
| `--rule` | `#dde2e7` | `#28323b` | borders, dividers |
| `--ink` | `#17202a` | `#e4e9ee` | body text |
| `--ink-2` | `#4a5663` | `#a7b1bb` | secondary text, ledes |
| `--ink-3` | `#6f7c89` | `#7f8a95` | labels, eyebrows, meta |
| `--accent` | `#1f5fa8` | `#5a9be0` | links, active TOC item |
| `--t-approved` | `#12704a` | `#2fb07e` | tier: approved label |
| `--t-trial` | `#1f5fa8` | `#5a9be0` | tier: human clinical trial |
| `--t-obs` | `#5b6ea8` | `#8fa0d6` | tier: observational, human |
| `--t-animal` | `#b4700f` | `#d49a3a` | tier: animal, preclinical |
| `--t-vitro` | `#8a5a2b` | `#c48a5a` | tier: mechanistic, in vitro |
| `--t-community` | `#a8324a` | `#e07a90` | tier: community-reported |

v2 additions (`compound-v2.css`, `:root` and dark): `--v2-warn-bg/bd/fg`
`#fbf4e4 / #e6c98a / #5a3d0a` for the draft state; `--v2-ok-bg/bd/fg`
`#e7f3ec / #a9d3bb / #12523a` for reviewed; `--v2-accent-soft #e8eff8`;
`--v2-zebra #fcfcfb`.

Tier colours are semantic. They are never used decoratively and never
reassigned; a tier is always shown as a 9 px dot plus its label, never colour
alone.

### Type

| Role | Face | Fallback | Size / line-height |
|---|---|---|---|
| Headings, dek, quotations | Source Serif 4 (600 headings, 400 quotes) | Georgia, Times New Roman | H1 `clamp(38px, 4vw, 52px)` / 1.05; H2 26 px; H3 20 px; dek 21 px / 1.45; quote 17.5 px / 1.55 |
| Body, UI | Source Sans 3 (400, 600) | system-ui, Segoe UI | 17 px / 1.6; lede 16 px; meta 12.5 px; table 14 px |
| Ids, labels, eyebrows | ui-monospace | Menlo, Consolas | 11 px, letter-spacing .12em, uppercase for eyebrows; 10.5 px for table headers |

Fonts load from Google Fonts with `display=swap`, only on pages that use the
v2 layout, through `Base.astro`'s `head` slot. Never Inter, Roboto, Arial or
Fraunces. Two families plus monospace, no more.

### Space, shape, motion

Radius 6 px on cards and tiles, 999 px on pills, 3 px on code. Borders 1 px
`--rule`. No shadows. Content column gap 44 px desktop, 32 px mobile; section
internal gap 16 px; card padding 16 × 18 px. The only motion is the FAQ
chevron rotating on open; respect `prefers-reduced-motion`.

## 4. Compound page anatomy (v2)

Container 1200 px, 32 px side padding. Two-column grid from 901 px:
`232px minmax(0,1fr)`, 56 px gap, sidebar sticky at `top: 24px`. Single
column at or below 900 px.

Order, with the component that renders each part:

| # | Block | Component | Renders when |
|---|---|---|---|
| 1 | Title block: eyebrow crumbs (Compound · class · target), H1, dek, pills | `semaglutide.astro` (title) | always |
| 2 | Table of contents | `v2/Toc.astro` | always; mobile: `<details>` card "On this page · N sections" |
| 3 | At a glance: 6 fact tiles | `v2/FactTiles.astro` | always |
| 4 | Status bar (draft / reviewed) | `v2/StatusBar.astro` | always |
| 5 | What it is | summary paragraph, `.prose-lg` | always |
| 6 | What the evidence shows | `v2/EvidenceTable.astro` | `attributes.evidence_table` non-empty |
| 7 | Evidence sections, first five in spec order | `v2/ClaimCards.astro` | each field non-empty |
| 8 | Method band: reconstitution mathematics, reading a CoA, equipment | `shared/*` inside `.method` | any evidence exists |
| 9 | Remaining evidence sections | `v2/ClaimCards.astro` | each field non-empty |
| 10 | How it compares | `Compare.astro` in `.card.clip` | registry peers exist |
| 11 | Regulatory status | `v2/ClaimCards.astro` | field non-empty |
| 12 | Open questions | `.list` | non-empty |
| 13 | Questions people ask | `v2/Faq.astro` | non-empty |
| 14 | Sources | `v2/Sources.astro` | non-empty |
| 15 | Reference card | `v2/RefCard.astro` | always |
| 16 | Related records | `.cards` | peers, stacks or comparisons exist |
| 17 | Last reviewed and what changed | `.list` | changelog non-empty |

The TOC is built from the same `secs` array that gates the sections. Adding a
section means adding one entry there, nowhere else.

### The dek and pills

Dek: one sentence, computed from the record: "What {publications} indexed
publications and {RCTs} randomized trials actually state about {name},
sentence by sentence, each tied to its source and labeled by the kind of
evidence it is." Pills, in order: tier; status (`Draft · not yet reviewed`
in the warn style, or `Reviewed {date}`); `{n} sources`; `Updated {lastmod}`;
aliases, dashed border, brand names only (no registry codes, no
digit-bearing synonyms), at most three.

### Fact tiles

Six, in this order: evidence tier (large tier chip); indexed publications;
randomized controlled trials with "plus N indexed as other clinical trials"
beneath; approval (year, or "not approved", with ChEMBL phase and ATC); routes
reported; studied in. The last two derive from `evidence_table.fields`.
Values in the serif at 22 px (19 px for text values), labels in mono
uppercase, a one-line source note in `--ink-3`. Three across on desktop, two
on mobile. Tabular numerals.

### Claim cards

```
┌─────────────────────────────────────────────────────────┐
│ Randomized controlled trial · humans · n = 99 · 2026  ● Human clinical trial │  meta row, 12.5 px
│ Doses stated in the abstract: 2·4 mg; 30 mg              │  extra line, 14 px (only if present)
│ “Eligible participants were randomly assigned to …”      │  serif 17.5 px, <q>
│ Source pmid-42456707 · quoted verbatim from the abstract │  mono 12 px
└─────────────────────────────────────────────────────────┘
```

The split comes from `src/lib/claims.ts` (`parseClaim`): the drafter's
prefix becomes the meta row, its structured extract the extra line, the
`source_excerpt` the quotation. A claim without an excerpt (a registry entry)
renders as plain text with its tier. Cards stack with a 12 px gap; no
per-card colour, the tier dot carries it.

### Evidence table

Columns: Study (first author + year, linked to the source anchor), Design,
n (right-aligned, tabular), Species, Dose, Route, Duration, Reported outcome
(min-width 260 px), Tier. Header sticky inside a scroll container capped at
70 vh; zebra rows in `--v2-zebra`; a dash wherever the abstract did not state
a value. Footer line states the row count and the dash convention.

### Status bar

Full-width, 12 × 16 px padding, 15 px text, an inline SVG info glyph. Draft:
warn colours, "Not yet reviewed." with the status in `<code>` and a link to
`#changelog`. Reviewed: ok colours, reviewer name, credential and date. It is
never hidden; an unreviewed page must say so where a reader will see it.

### Method band

`background: var(--sunk)`, 1 px rules above and below, bleeds to the content
column edges (`margin: 8px -32px`). Two-column grid of the shared notes with
an eyebrow "Method note · shared across compounds" on each; the third note
spans both columns. Each note has an id (`method-recon`, `method-coa`,
`method-equipment`) so the TOC can address it.

### FAQ, sources, reference card

FAQ: native `<details>`, first item open, summary in serif 18 px with a
rotating chevron, answer 64 ch max. Sources: `<ol>` of two-column rows
(number, then title link with a mono meta line of id · date · kind), each row
carrying its source id as the anchor claims link to. Reference card: bordered
card, two-column key/value grid, generated date and path in the header,
a foot note that figures are as published and not recommendations.

## 5. Other page types

Stack, comparison, tool and post pages use the same tokens and components.
Until they get a v2 pass they keep the current single-column layout.

- **Stack**: component evidence matrix (table) first; then a **mandatory**
  combination-evidence section that renders the sentence "No published study
  tested this combination" in a status bar when empty. Never inherit a
  stronger tier than the weakest component.
- **Comparison**: side-by-side table from both records; head-to-head claims
  as claim cards; the same "no direct comparison indexed" statement when
  empty.
- **Tool**: formula stated in prose before the control; every input labelled
  with its unit; no field for body weight, age or condition; result in mono.
- **Post**: prose column, 66 ch, same status bar.

## 6. Budgets and rules the build checks

| Rule | Limit | Checked by |
|---|---|---|
| HTML per page | ≤ 100 KB | `scripts/measure_pages.py` (size) |
| Client JavaScript | none, except tool pages | review |
| Title including site suffix | ≤ 60 chars; drop the suffix whenever the combined title would exceed 60 | `Base.astro` `siteSuffix` prop; v2 page opts in |
| Meta description | ≤ 160 chars | `scripts/validate_content.py` |
| Own prose | ≤ ~22 words per sentence | review; `measure_pages.py` reports Flesch |
| Internal links | 3–5 per 1,000 words, descriptive anchors | `measure_pages.py` (to implement) |
| Uniqueness | ≥ 40% gate, 85% target | `measure_pages.py --write` |
| Touch targets on mobile | ≥ 44 px | review |
| Contrast | WCAG AA on both themes | review; tier dots always paired with text |
| Canonical | absolute, real hostname, self-referencing | `site-url.mjs` rejects wildcard and invalid hosts |
| Images | none required; any image has alt text and fixed dimensions | review |
| Formatting minimums | see §9.10 | `measure_pages.py` (to implement) |

## 7. Anti-patterns

Do not ship any of these, whatever a reference site does:

- a heading prefixed with the compound name on every section;
- an empty section, a "coming soon" page, or a placeholder tile;
- a fake mobile status bar or keyboard in mockups;
- emoji or dingbats as icons; icons are inline SVG on a 24 px grid;
- gradient heroes, one radius-and-shadow on every block, accent-bar cards;
- Inter, Roboto, Arial or Fraunces;
- affiliate blocks, supplier ratings, price tables (prohibited in the pilot);
- a dose or schedule presented outside a quotation with its source;
- colour as the only carrier of tier;
- a page that hides its draft state.

## 8. How changes to the design are made

1. Propose on the design canvas or as a one-page trial route, never by
   editing the shared template first.
2. Build the trial with real record content; no lorem, no invented figures.
3. Run `npm run build` and `python3 scripts/measure_pages.py`; check the page
   at 390 px and 1440 px and in both colour schemes.
4. Record the decision and date in the changelog below, then move components
   into the shared template in a separate pull request.

## 9. Content formatting for reading experience

Structure is not enough; a 5,000-word page of uniform paragraphs is unread.
These rules govern the HTML the templates emit and the prose the drafting
scripts write. Each has a minimum the build can count, listed in the table at
the end of this section. Formatting is applied to **our own prose** (dek,
summary, ledes, FAQ, open questions, method notes, captions). **Quotations are
verbatim by `agent/AGENT.md`**; the one permitted change inside a quotation is
typographic emphasis, and it must be declared (9.3).

### 9.1 Emphasis

- **Bold the figure a reader is scanning for**, in our own prose: sample sizes,
  trial counts, years of approval, tier names, and the phrase *not yet
  reviewed*. Use `<b>` for scanning emphasis and `<strong>` only for
  importance a reader must not miss (a safety statement, an empty-evidence
  notice).
- At most **two bold runs per paragraph**, each at most five words. Never a
  whole sentence. Never a heading. Bold that is everywhere is bold nowhere.
- Italic (`<em>`) is for terms of art on first use and for study names
  (*FLOW*, *SURMOUNT-5*), never for emphasis.
- Never bold or colour a word as the sole signal of meaning; the tier dot is
  always paired with its label for this reason.

### 9.2 Tables

- **Every compound, stack and comparison page renders at least one data
  table.** When evidence exists it is the evidence table. When none exists,
  the page renders an *evidence landscape* table instead: indexed
  publications, randomized controlled trials, other clinical trials, human
  studies, animal studies, with a zero in each cell rather than an empty
  section. A zero in a table is information; a missing table is not.
- Every table has a `<caption>` (visible, set in `--ink-3`, above the table)
  stating what it shows and the dash convention: "22 primary studies,
  strongest evidence first. A dash means the abstract did not say."
- Header cells use `<th scope="col">`; the first column of a row-keyed table
  uses `<th scope="row">`. Numeric columns are right-aligned with
  `font-variant-numeric: tabular-nums`. Tables scroll inside their own
  container; the page never scrolls sideways.
- Use a table when the reader compares across rows or columns. Do not use a
  table for a single key/value set; that is a `<dl>` (9.5).

### 9.3 Quotations

- Every verbatim source sentence is a `<q>` (inline, inside a claim card) or
  a `<blockquote>` (a passage longer than two sentences), and in either case
  carries `cite="<source url>"` so the quotation is machine-attributable.
- The source line under a quotation states how it was produced: *quoted
  verbatim from the abstract*.
- Typographic emphasis inside a quotation is allowed for exactly one thing:
  the compound's own dose and route strings already extracted by the drafter
  (the `extra` field). Mark them with `<mark>` (not `<b>`), and change the
  source line to *quoted verbatim from the abstract, emphasis added*. Nothing
  else inside a quotation is ever marked, cut, reordered or corrected;
  spelling and decimal marks stay as the source printed them (7·5 mg stays
  7·5 mg).

### 9.4 Lists

- `<ul>` for unordered sets: open questions, aliases, related records.
- `<ol>` for anything with an order that carries meaning: the four
  certificate-of-analysis checks, sources (numbered so a reader can cite
  "source 12"), reconstitution steps, changelog in reverse chronological
  order.
- Each item is one point, at most two lines at the content width; an item
  that needs a second sentence becomes a paragraph. No single-item lists.
  No nested lists deeper than one level.
- Lists of figures align their numbers (tabular numerals) and lead with the
  figure: "**305** randomized controlled trials", not "There are 305".

### 9.5 Definition lists, code, abbreviations, dates

- Key/value data is a `<dl>`: the reference card, the snapshot on narrow
  screens, a study's design/n/species/dose block when shown outside a table.
- `<code>` marks identifiers and states, never emphasis: `pmid-42456707`,
  `CHEMBL2108724`, `draft`, `published`.
- Abbreviations are expanded once per page with `<abbr title="…">` on first
  use: RCT, GLP-1, MASH, AUD, HbA1c, ATC. After that the short form alone.
- Dates are `<time datetime="2026-09-14">14 Sep 2026</time>` in prose and
  cards; ISO form in tables and the changelog, where alignment matters.

### 9.6 Callouts and collapsibles

- A **status callout** (the `.status` component) carries any statement the
  reader must not miss: not yet reviewed; no indexed study names this
  compound; no published study tested this combination. One callout per
  message; never two adjacent callouts; never a callout for decoration.
- `<details>` collapses secondary material the reader may not want: FAQ
  items after the first, the source list beyond the first twelve, the mobile
  table of contents. Never collapse a claim, a caption, a warning or the
  first item of anything.

### 9.7 Paragraphs, sentences, headings

- Own prose: paragraphs of two to four sentences and at most about seventy
  words; the first sentence carries the point. One idea per paragraph.
- Sentences average under about 22 words. Split at "and", "which" and
  "while" before reaching for a semicolon.
- Every H2 with more than three items beneath it has a lede of at most 25
  words saying what the section holds and how it was produced.
- Headings are sentence case, descriptive or question-form, without a
  trailing colon and without the compound name (the entity lives in the
  title, dek and first paragraph). FAQ questions are real questions a reader
  types, answered in the first sentence.

### 9.8 Numbers and units

- Thousands separators in prose and tables (6,039). Tabular numerals wherever
  numbers stack.
- A number and its unit never break across a line: `2.4&nbsp;mg`.
- Ranges use an en dash (0.25–1.0 mg); a change uses an arrow (0.25 mg →
  1.0 mg).
- Percentages carry their denominator when the source gives one: 80% (79 of
  99). A percentage without a denominator is not written in our prose.
- Inside quotations, numbers appear exactly as the source printed them.

### 9.9 Links

- Anchor text says where the link goes: "the FLOW trial", "source
  pmid-41728915", "tirzepatide", never "here" or "this study".
- External source links open in a new tab (`target="_blank"
  rel="noopener"`) so the reader keeps their place in a long page; internal
  links open in the same tab.
- Three to five internal links per 1,000 words, placed where the entity is
  mentioned in prose, not gathered at the end. Peer compounds named in the
  comparison table and the FAQ are linked at first mention.

### 9.10 Minimums per page

Counts the build should verify (`scripts/measure_pages.py`; the ones marked
*to implement* are not yet checked):

| Element | Minimum per compound page | Where it comes from | Checked |
|---|---|---|---|
| Data table with caption | 1 (evidence table, or the evidence-landscape table) | `EvidenceTable`, `LandscapeTable` | `measure_pages.py --formatting` |
| Bold runs in own prose | 6, none longer than 5 words, ≤ 2 per paragraph | `rich()` in `src/lib/format.ts` | `measure_pages.py --formatting` (count only) |
| `<ol>` | 1 (sources) | `Sources` | `measure_pages.py --formatting` |
| `<ul>` | 1 (open questions or related) | page | `measure_pages.py --formatting` |
| `<q>`/`<blockquote>` with `cite` | every quotation | `ClaimCards` | `measure_pages.py --formatting` |
| `<dl>` | 1 (reference card) | `RefCard` | `measure_pages.py --formatting` |
| `<abbr>` on first use | every abbreviation in own prose | drafting scripts | review |
| `<time>` | every date in prose and cards | `timeTag()` in components | `measure_pages.py --formatting` |
| Status callout | 1 when unreviewed or evidence is absent | `StatusBar` | yes |
| Section ledes | every H2 with > 3 items | page | review |
| Internal links | 3–5 per 1,000 words | page | `measure_pages.py --formatting` |
| Own-prose sentence length | ≤ ~22 words average | drafting scripts | `measure_pages.py --formatting` (paragraph text only) |

A page that fails a minimum is not broken; it is unread. Fix the template or
the drafting script, not the record, so the fix applies to every page.

## Changelog

- 2026-09-15 — Section 9 applied to the trial route `/compounds/semaglutide`
  (`src/lib/format.ts`, v2 components) and `scripts/measure_pages.py
  --formatting` reports the §9.10 counts. Own-prose sentence length remains
  above target because the drafted summary and FAQ sentences are long; that is
  a drafting-script change, tracked separately.
- 2026-09-15 — Section 9 added: content formatting rules for reading
  experience (emphasis, tables with captions, quotation markup and the
  emphasis-added rule, lists, definition lists, abbreviations, dates,
  callouts, paragraph and sentence limits, numbers, links) with per-page
  minimums for the build to check.
- 2026-09-15 — Spec written from the competitive baseline, the semaglutide
  design canvas and the trial route. v2 live on `/compounds/semaglutide`
  only; the other compound pages, stacks, comparisons and tools remain on
  the first template pending review.
