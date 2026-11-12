# Design reference: peptidedosingprotocols.com

What the incumbent's design does, sorted into what is worth taking for
dashnaiv.com, what is worth taking as an idea but not as executed, and what
to leave alone. `docs/design.md` stays the only design source for this site;
this file feeds decisions into it, it does not replace it. Nothing here is
to be copied one to one, colours included.

Measured 2026-11-11 from the homepage, `/protocol/bpc-157`,
`/peptide-cycles` and `/blog`, by reading the served HTML, stylesheet and
font files. The pages did not render in headless Chrome from this
environment, so layout facts come from the markup's own pixel values, not
from screenshots. Content measurements live in
`docs/competitive-baseline.md`.

## 1. The incumbent in a paragraph

A light, white-and-blue reference site: serif headings over a system sans
body, one blue doing every job (links, buttons, focus rings, section
headers), and a dark slate frame around the content (sticky header, footer,
a sticky bottom bar on phones) with cyan accents. Content is cut into
bordered white cards on alternating white and off-white bands. A protocol
page runs about 5,700 words in 26 section cards, with a sticky contents rail
on the left, a sticky "At a glance" panel beside the title, and partner
product cards placed between evidence sections. Light mode only, about
600 KB of HTML per page, hydrated React.

## 2. Take

Things that work for a long evidence page and fit our rules as they stand.

| What they do | Why it works | How it applies here |
|---|---|---|
| **Tables collapse into labelled rows on phones.** Under 768 px each cell becomes a row with its column name printed from `data-label` at the left and the value at the right. | A six-column dosage table stays readable at 390 px without side-scrolling; every value keeps its label. | Our tables scroll horizontally inside `.tblwrap`. Add `data-label` to `<td>` in the table components and a sub-768 rule in `compound-v2.css`. Keep the caption. Evidence tables with a long outcome column may still need the scroll; decide per table. |
| **The contents rail is capped to the viewport and scrolls on its own.** `max-height: calc(100vh - 12rem); overflow: auto`. | Twenty anchors never push the rail below the fold. | Our `.toc` is sticky with no cap; compound pages already have 20+ anchors. Add the cap. |
| **"Last reviewed" sits in the byline under the title**, with the author and role, before the body. | The freshness signal is where the reader looks first, not only in a status bar. | Guides have the reviewer in the status bar and "Updated" in a pill. Put a one-line byline under the dek: reviewer, credential, reviewed date; leave the status bar for state. |
| **The page template is declared on the site.** The home page lists the fourteen sections every guide has, in order, and the guide delivers them in that order. | A reader learns the page once. It also tells search engines the pages are uniform by design. | Say it once on `/about` or at the top of `/blog`: the section order every compound page and every guide follows. We already have the order in `docs/page-template-spec.md`; it is not shown to readers. |
| **Recurring named blocks**: "Evidence boundary", "Open question", "Format note", each with the same label on every page. | A reader recognises the block type before reading it. | We have absence statements and boundary copy; give them one fixed label each and the same position in every section that uses them. |
| **Anchors have a scroll margin** matching the sticky header, so a jumped-to heading is never hidden. | Basic, and often missed. | Only matters if our header becomes sticky (see §3). If it does, `section[id] { scroll-margin-top }` goes in with it. |
| **A metric-matched fallback font** (`size-adjust`, `ascent-override`) for the serif. | No layout shift when Source Serif 4 arrives. | We load Source Serif 4 and Source Sans 3 from Google Fonts with `swap` and a plain Georgia fallback. Add an `@font-face` fallback with `size-adjust` for both. |
| **Focus rings, 44 px targets, `aria-label` on icon buttons.** | Keyboard and touch work without thought. | We meet the targets; check that every icon-only control (FAQ chevrons, the mobile TOC summary) has a visible focus ring. |
| **Letter-indexed directories** for long lists. | Fifty entries scan faster with letter headings. | Already on the glossary (`.az`). Use the same on `/compounds` once it passes about forty records. |

## 3. Adapt

Ideas worth taking where the execution is not.

**A frame that separates site navigation from content.** Their dark header
and footer make the content area read as the document and the chrome as
the building. The effect is good; slate-950 with cyan is theirs. If we do
this, it is a deep version of our own blue (the brand `theme-color`
`#06336A` is the obvious start), applied to header and footer only, with our
`--paper` ground untouched. No sticky header unless the rail needs it, and
no bottom bar of any kind.

**One colour family does all the interface work.** Their page feels
coordinated because links, buttons, labels and bands are one blue. We
already have that in `--accent`; the lesson is restraint, not their hue.
Keep tier colours semantic and keep them out of the interface.

**An "At a glance" panel beside the title.** Theirs is a sticky right
column at 1024 px and above with four key/value rows and one action. Our
glance is a `dl` under the H1 in the content column. At 1280 px and above,
placing the glance beside the title block (and letting it stick while the
intro scrolls) uses the empty right margin our pages have now. Keep it a
`dl`, keep it free of actions.

**Format cards for sourced regimens.** Their dosing section shows each
regimen as a 2×2 of Approach / Duration / Review point / Evidence context.
For our protocol layer the structure is right; the labels become ours
(Regimen · Duration in the source · What was measured · Evidence tier), the
tier gets its dot, and the card carries the source id.

**A calculator result that is the biggest thing in the section.** Their
result panel prints the draw ("5 units · 0.05 mL on a U-100 insulin
syringe") large, on a dark ground. Our calculators print the result in mono
at body size. Make the number large and the unit explicit; the dark panel is
optional and should use `--sunk`, not a new colour.

**Section openers.** Every one of their sections opens with a blue band and
an icon. The band is their signature; it is also the "accent-bar card" our
anti-patterns list. What is worth keeping is that a section is recognisable
as a section at a glance. Our answer stays typographic: the serif H2 and a
lede, with the rail and the `--sunk` method band carrying the structure.

## 4. Ignore

- **The compound name on every H2** (21 of 21). Already rejected in
  `docs/design.md` §1.
- **A card around everything**, one radius and one shadow on sections,
  products, stats and FAQ alike, and the same lift-and-shadow hover on cards
  and buttons. Hierarchy should come from type and spacing.
- **The commercial layer**: partner product cards between evidence sections,
  discount codes with copy buttons, "Shop" first in the navigation, deals
  pages, supplier reviews, the sticky partner bar on phones, copper and
  violet promo colours, gradient promo panels. Out of scope here
  (`agent/AGENT.md`), and the reason their page makes a reader pass two
  shops to reach the dosage chart.
- **The hero kit**: three pills, two buttons, five big-number stat tiles and
  a floating-card illustration. Our homepage decision (a quotation instead
  of counters) stands.
- **Uppercase tracked labels** above most blocks, including table headers
  and every key/value row. We use the mono eyebrow sparingly; keep it that
  way.
- **An icon on every heading**: 140 inline SVGs per page carrying no
  information.
- **Light mode only.** Ours is a token swap; keep both.
- **600 KB hydrated pages** for text. Our 100 KB budget stands.
- **Tier invisible.** Human trials, animal work and community reports in
  the same type and colour; the evidence boundary is a paragraph, not a
  state. Our dot-plus-label rule is the better answer.

## 5. Changes to propose, in order

Each is small enough for one pull request and follows `docs/design.md` §8
(trial route or canvas first, decision recorded in the changelog).

1. Phone table collapse with `data-label` (`compound-v2.css`, table
   components, `format.ts` if captions move).
2. Rail capped to the viewport with its own scroll (`compound-v2.css`
   `.toc`).
3. Byline under the dek on guides and compound pages: reviewer, credential,
   reviewed date (`GuideV2.astro`, `CompoundV2.astro`).
4. Metric-matched font fallbacks (`Base.astro` head slot or `global.css`).
5. Fixed labels and positions for the boundary and absence blocks
   (`docs/content-contract.md`, then the layouts).
6. Glance panel beside the title at 1280 px and above (trial on one route).
7. Larger calculator result with explicit unit (`Protocol.astro`,
   calculator pages).
8. Deep-blue header and footer from our own brand colour, no sticky header
   (trial on one route; both colour schemes).

## 6. Measured facts, for reference only

Kept so the comparisons above can be checked. Not a specification.

**Colour.** shadcn-style HSL tokens on `:root`, read as `hsl(var(--x))`:
background `#ffffff`, surface `#f5f7f9`, border `#e1e6ea`, foreground
`#1d2530`, muted text `#535f6e`, primary `#346cb2`, "clinical" band blue
`#3666a1`, callout text `#28548a`, callout fill `#f1f5f9`. Chrome:
slate-950 `#020617` with cyan-300/400 accents. Promo: copper `#9a6a4c`,
violet `#4c1d95`, a 138° gradient `#081b45 → #1039a8 → #1248e8`.

**Type.** Source Serif 4 variable (200–900), self-hosted via `next/font`,
on h1–h4; `system-ui` body at 16 px / 1.625 with a 68ch measure; mono
`ui-monospace` stack. H1 36 → 60 px semibold, tracking −0.02em (protocol);
36 → 58 px bold (home). H2 24 → 30 px. H3 16–20 px. Secondary text 14 px /
24 px. Eyebrows 12 px uppercase, tracking 0.10–0.12em.

**Layout.** 1400 px container, 16 px gutters. Home sections 56 / 80 px
vertical padding, alternating white and surface, each headed by a two-column
row (title left, lede right, bottom rule). Protocol page: title grid
`1fr / 420px` (480 px from 1280), then `280px / 1fr` (300 / 900 px max from
1280) with a 40 px gap; 26 section cards, 20–32 px padding, `shadow-sm`,
`scroll-margin-top` 7 rem; header band pulled to the card edge with
negative margins. Rail sticky at `top: 7rem`, `max-height: calc(100vh -
12rem)`. Breakpoints 400, 420, 560, 640, 768, 1024, 1280, 1400 px.

**Shape and motion.** Radius 8 px on cards and buttons, 12–16 px on panels,
28 px on author cards. Transitions 150 ms; hover lift 2 px with shadow;
product images scale 1.04; no `prefers-reduced-motion` rule.

**Counts, `/protocol/bpc-157`.** 5,713 words in `<main>`, 21 H2, 74 H3, 10
tables, 15 images, 108 links of which 13 are affiliate redirects, 27
buttons, 647 KB HTML. Home: 3,155 words, 219 links, `FAQPage` JSON-LD; no
JSON-LD found on the protocol page.
