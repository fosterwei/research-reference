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
