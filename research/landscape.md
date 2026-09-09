# Evidence landscape

Dry-run sweep of every compound in `compounds.seed.json` on 2026-09-09, by `scripts/fetch_evidence.py --all --dry-run`. Counts are Europe PMC hits with the compound name or an alias in the title, abstract or keywords. The tier is the fetcher's suggestion from the counts alone; the full run refines it from the candidate papers and ChEMBL.

Sequence the pilot by this table. A compound with no indexed human trials cannot honestly carry the human-dosing, escalation, exclusion-criteria or adverse-event sections of the template, and those sections must be suppressed rather than padded.

| Compound | Indexed publications | RCTs | Clinical trials | Suggested tier |
|---|---|---|---|---|
| `semaglutide` | 6,039 | 305 | 198 | `human-clinical-trial` |
| `tirzepatide` | 2,731 | 131 | 107 | `human-clinical-trial` |
| `thymosin-alpha-1` | 1,078 | 65 | 61 | `human-clinical-trial` |
| `kisspeptin` | 3,844 | 44 | 34 | `human-clinical-trial` |
| `sermorelin` | 579 | 39 | 71 | `human-clinical-trial` |
| `ll-37` | 2,824 | 38 | 23 | `human-clinical-trial` |
| `ghrp-6` | 739 | 22 | 41 | `human-clinical-trial` |
| `tesamorelin` | 115 | 22 | 7 | `human-clinical-trial` |
| `ss-31` | 492 | 16 | 14 | `human-clinical-trial` |
| `cagrilintide` | 105 | 15 | 13 | `human-clinical-trial` |
| `bremelanotide-pt-141` | 127 | 14 | 9 | `human-clinical-trial` |
| `tesofensine` | 63 | 12 | 7 | `human-clinical-trial` |
| `survodutide` | 91 | 10 | 15 | `human-clinical-trial` |
| `tb-500` | 1,257 | 7 | 6 | `human-clinical-trial` |
| `dsip` | 559 | 7 | 18 | `human-clinical-trial` |
| `retatrutide` | 195 | 7 | 9 | `human-clinical-trial` |
| `humanin` | 589 | 5 | 3 | `human-clinical-trial` |
| `epitalon` | 169 | 5 | 5 | `human-clinical-trial` |
| `mots-c` | 276 | 4 | 1 | `human-clinical-trial` |
| `ara-290` | 39 | 3 | 1 | `human-clinical-trial` |
| `selank` | 96 | 2 | 2 | `human-clinical-trial` |
| `ipamorelin` | 63 | 2 | 2 | `human-clinical-trial` |
| `melanotan-ii` | 646 | 1 | 6 | `human-clinical-trial` |
| `semax` | 208 | 1 | 3 | `human-clinical-trial` |
| `ghk-cu` | 168 | 1 | 0 | `human-clinical-trial` |
| `cjc-1295` | 37 | 1 | 1 | `human-clinical-trial` |
| `bpc-157` | 228 | 0 | 0 | `observational-human` |
| `kpv` | 138 | 0 | 0 | `observational-human` |
| `igf-1-lr3` | 27 | 0 | 0 | `mechanistic-in-vitro` |
| `aod-9604` | 25 | 0 | 0 | `mechanistic-in-vitro` |
| `foxo4-dri` | 19 | 0 | 0 | `observational-human` |
| `pinealon` | 17 | 0 | 1 | `human-clinical-trial` |
| `slu-pp-332` | 12 | 0 | 0 | `observational-human` |
| `cartalax` | 0 | 0 | 0 | `mechanistic-in-vitro` |

## No indexed human trials (7 compounds)

`bpc-157`, `kpv`, `igf-1-lr3`, `aod-9604`, `foxo4-dri`, `slu-pp-332`, `cartalax`

These are the compounds where the incumbent's uniform 5,000-word template is weakest, and where a shorter, honestly tiered page is both more defensible and more useful. Alias caveats: `tb-500` counts include thymosin beta-4 literature generally, and `epitalon` counts include the pineal extract epithalamin; the briefs show which alias each paper matched.
