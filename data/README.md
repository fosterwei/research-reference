# Content records

One JSON file per record, in the folder for its type:

| Folder | `type` | Public URL |
|---|---|---|
| `compounds/` | `compound` | `/compounds/{slug}` |
| `stacks/` | `stack` | `/stacks/{slug}` |
| `comparisons/` | `comparison` | `/compare/{slug}` |
| `cycles/` | `cycle` | `/cycles/{slug}` |
| `tools/` | `tool` | `/tools/{slug}` |
| `posts/` | `post` | `/blog/{slug}` |

`examples/` holds reference templates. They are validated for shape but are never imported and do not take part in slug uniqueness.

Run `python3 scripts/validate_content.py` before opening a pull request. Allowed values for `status` and evidence labels are defined in `docs/content-contract.md` and enforced by the validator.

Records normally enter as `researched`, written by `scripts/fetch_evidence.py` with a
populated source ledger and empty claim lists. `scripts/draft_claims.py` then drafts
claims extractively from those sources, each with its verbatim `source_excerpt`, and
moves the record to `draft`. A writer edits or replaces the drafts; a named reviewer
moves the record to `reviewed`. Neither script touches anything past `draft`, and the
fetcher stops at `researched`. Stack and comparison records are generated from the plan
in `research/registry.json` by the same drafting script.
