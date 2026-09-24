# Content automation: the loop one page goes through

`docs/content-sop.md` describes the research that produces a page's intent map.
This document is the operating loop around it: brief, generate, audit, triage,
adjust, gate. It is written so that a person can run it by hand today and so
that it can be wrapped as a single command once it has run cleanly on a few
pages. Judgment lives in one step, triage, and that is the step to watch before
anything runs unattended.

## The loop

| Step | Tool | Input | Output | Exit gate |
|---|---|---|---|---|
| 0 | `scripts/fetch_evidence.py` | slug | record at `researched` | ledger non-empty, or a measured zero |
| 1 | `/seo-content-brief <slug or url>` | record, SERP, DataForSEO | `research/intents/<slug>.json` | every query has a `policy`; volumes measured or explicitly null |
| 2 | `scripts/draft_claims.py`, `npm run build`, PR | record + intent map | built page on a Vercel preview URL | validator passes |
| 3 | `/seo-content <preview url>` | the built page | `research/audits/<slug>-<date>.md`, part 1 | report saved, score recorded |
| 4 | triage (a person) | the audit | `research/audits/<slug>-<date>.md`, part 2 | every suggestion labelled |
| 5 | adjust at the right layer | the triage | commits | accepted items applied; rejected items have a written reason |
| 6 | gate | build | `measure_pages.py` reports; second `/seo-content` run | minimums met; exit audit compared to the first, not looped |
| 7 | editorial check | the page | dated changelog entry; reviewer named if one reviewed | editorial passages accurate; nothing reads as an instruction |

Steps 1 and 3 are skills that already exist. Steps 0, 2 and 6 are scripts that
already exist. Steps 4 and 7 are people. Step 5 is whoever the triage assigns.

## Step 1: the brief is the intent map

`/seo-content-brief` produces a brief in the conversation. Nothing downstream
can act on a conversation, so the brief is written to
`research/intents/<slug>.json` before anything else happens. Every part of the
brief has a field there: queries with volumes and policies, scored competitors,
the information-gain paragraph, the outline, and `open_actions` for anything
the research exposed in the record. The renderer reads that file at build time
(`src/lib/intents.ts`), so the brief is not advice about the page; it is part of
the page.

Rules for the map are in `docs/content-sop.md` stage 3. The short version:
three policies (`evidence-only`, `evidence-with-boundary`, `redirect`), every
query carries one, and `boundary` is reader-facing copy that opens the section's
lede, not an instruction to a writer.

## Step 2: generate

```bash
python3 scripts/draft_claims.py <slug> --force
npm run build
python3 scripts/validate_content.py
```

Then open a PR. Vercel posts a preview URL on it within a minute; that URL is
what step 3 audits. The page is audited before it merges, not after.

## Step 3: audit

Run `/seo-content <preview url>/compounds/<slug>` and save the full report as
part 1 of `research/audits/<slug>-<date>.md`.

**Vercel preview protection.** Preview deployments redirect unauthenticated
requests (302 to a Vercel login, `x-robots-tag: noindex`), so neither the skill
nor a crawler can read them. Either turn Deployment Protection off for preview
environments in the Vercel project settings, or set a protection-bypass secret
and pass it as `?x-vercel-protection-bypass=<secret>`. Until one of those is
done, audit the local build of the same commit instead:

```bash
npm run build
python3 scripts/audit_page.py <slug> --url <preview url>/compounds/<slug>
```

`scripts/audit_page.py` computes the same checks deterministically (meta,
structured data, who/how/why, E-E-A-T sub-scores, readability of our own prose
separately from quotations, links, formatting) and prints part 1 as Markdown.
The HTML is byte-identical to what Vercel serves for that commit; only response
headers differ. Record the headline score, the
E-E-A-T breakdown and every issue verbatim. Do not edit the report; the triage
in part 2 is where judgment goes.

## Step 4: triage, the step that carries judgment

`/seo-content` scores against general web standards. Some of what it recommends
contradicts this site's rules, some cannot be fixed by editing content, and
some is exactly right. Each suggestion gets one of five labels, written into
part 2 of the audit file as a table.

| Label | Meaning | Who acts | Example from the semaglutide audit |
|---|---|---|---|
| `accept-template` | fix in `src/`; applies to every page | engineer | invalid canonical; missing `datePublished` |
| `accept-record` | fix in one record's data | writer | FDA and WADA documents missing from a ledger |
| `accept-script` | fix in a script, then re-run for all records | engineer | the interactions regex matching statistical interaction |
| `reject-policy` | conflicts with `agent/AGENT.md` or `docs/design.md`; the reason is written down | nobody, but the reason is kept | shorten the quoted abstract sentences; add a dosing section |
| `defer-reviewer` | only the credentialed reviewer can resolve | reviewer | author byline; whether a suspect evidence row stays |

Two rules make triage honest. A `reject-policy` always names the rule it
conflicts with, so the next page's triage can see the precedent. And a
suggestion is never labelled `reject` because it is inconvenient; if the only
reason to reject is effort, it is `accept` with a later date.

## Step 5: adjust at the right layer

Pages are rendered from records, templates, the drafting script and the intent
map. There is no page to edit. The rule from `docs/design.md` applies: fix at
the layer that fixes every page.

| Problem in the audit | Layer |
|---|---|
| wording in our own prose (dek, ledes, FAQ answers) | template, or the intent map's `boundary` / `answer` |
| a source missing, a claim wrong, a suspect table row | record |
| a whole class of claims misdrafted | `scripts/draft_claims.py`, then re-draft all |
| sections in the wrong order, headings not in the searcher's words | intent map |
| readability of quoted sentences | none; quotations are verbatim by policy |

## Step 6: gate and exit

```bash
npm run build
python3 scripts/validate_content.py
python3 scripts/measure_pages.py --formatting <slug>
python3 scripts/measure_pages.py --intent <slug>
python3 scripts/measure_pages.py --write
```

Then `python3 scripts/loop_status.py`. It prints, for every page with written
sections, which stages have left an artifact: measured volumes, scored
competitors, an information-gain statement, an outline, uniqueness written to
the record, formatting minimums met, an audit with a triage table, and an exit
run. A page is not finished until its row is all yes. This exists because the
loop was compressed on thirteen pages in one day once it felt routine, and the
gap was found by asking, not by a check.

Then run `/seo-content` (or `scripts/audit_page.py`) once more on the updated build and add it to the
audit file as part 3, beside the first run. Compare; do not loop. Some
deductions cannot move until step 7: a page with no named reviewer scores low
on trust whatever its content does, and running the audit again will not change
that. The exit check exists to confirm the accepted items landed, and nothing
else. Confirm each one in the built HTML before its triage row says "done":
the first ipamorelin run wrote "done" for two items a mid-script abort had
skipped, and the merge carried the gap to `main`.

## Step 7: human review

The reviewer reads the page on the preview, checks each claim against its
quoted sentence, its heading and its tier, rules on the `defer-reviewer` items,
and signs the record. Only then does `status` become `published`, the page
lose its `noindex`, and the URL enter the sitemap.

## Audit file layout

```
research/audits/<slug>-<YYYY-MM-DD>.md
  # <Compound> audit, <date>
  Preview: <url>   Commit: <sha>
  ## Part 1: audit          (verbatim /seo-content output)
  ## Part 2: triage         (table: suggestion | label | reason | layer | owner)
  ## Part 3: exit audit     (second run, with a three-line comparison)
```

## What is out of scope

Commercial and transactional intent, per `docs/content-sop.md`. The audit may
notice that competitors cover purchasing; that observation is labelled
`reject-policy` with the scope rule as its reason.

## Running it as one command, later

Once the loop has run cleanly on three pages, steps 1 to 3 and 6 can be chained
into a single `/page <slug>` command that stops at step 4 and waits for a
person. Not before. The first three runs are where the triage precedents are
written, and an automated loop that starts before they exist will either
accept everything or reject everything.

## Changelog

- 2026-09-23 — Written. First run: ipamorelin, recorded in
  `research/audits/ipamorelin-2026-09-23.md`.
