#!/usr/bin/env python3
"""Name the reviewer of record on every written page, or clear them.

    python3 scripts/set_reviewer.py --name "Adam Mirando" \
        --credential "MD, endocrinology" \
        --url https://www.linkedin.com/in/adam-mirando-41772ba9/ \
        --date 2026-09-29
    python3 scripts/set_reviewer.py --dry-run ...     # show what would change
    python3 scripts/set_reviewer.py --clear           # remove the attribution

What this writes is a claim about a real person: the page says they reviewed it
and on what date, and the Article structured data repeats it as `reviewedBy`
with their public profile as `sameAs`. docs/content-automation.md step 7 defines
what that claim means, which is that the named person read the page, checked
each claim against its quoted sentence and its tier, and ruled on the items the
triage deferred to them. Run this when that has happened, not before.

Records with no written sections are skipped: an attribution on a page nobody
wrote would be a signature on a blank page. Standard library only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def records() -> list[pathlib.Path]:
    return sorted(p for folder in ("compounds", "stacks", "comparisons")
                  for p in (DATA / folder).glob("*.json"))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--name")
    ap.add_argument("--credential", help="stated exactly as it should appear, e.g. 'MD, endocrinology'")
    ap.add_argument("--url", default="", help="a public profile, carried into structured data as sameAs")
    ap.add_argument("--date", default=dt.date.today().isoformat(), help="the date the review was completed")
    ap.add_argument("--author", default=None, help="optional writer credit, must differ from the reviewer")
    ap.add_argument("--clear", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--include-unwritten", action="store_true", help="also stamp records with no guide sections")
    a = ap.parse_args(argv)

    if not a.clear:
        if not a.name or not a.credential:
            ap.error("--name and --credential are both required; a half-filled attribution fails validation "
                     "and a credential must never be guessed")
        try:
            dt.date.fromisoformat(a.date)
        except ValueError:
            ap.error("--date must be YYYY-MM-DD")
        if a.author and a.author == a.name:
            ap.error("--author must differ from --name")

    changed = skipped = 0
    for path in records():
        d = json.loads(path.read_text(encoding="utf-8"))
        if not d.get("guide") and not a.include_unwritten:
            skipped += 1
            continue
        review = d.setdefault("review", {})
        before = json.dumps(review, sort_keys=True)
        if a.clear:
            review.update({"author": "", "reviewer": "", "reviewer_credential": "", "reviewed_at": ""})
            review.pop("reviewer_url", None)
            note = "Reviewer attribution removed."
        else:
            review.update({"reviewer": a.name, "reviewer_credential": a.credential, "reviewed_at": a.date})
            if a.url:
                review["reviewer_url"] = a.url
            if a.author is not None:
                review["author"] = a.author
            note = f"Reviewed by {a.name}, {a.credential}, on {a.date}."
        if json.dumps(review, sort_keys=True) == before:
            continue
        changed += 1
        if a.dry_run:
            print(f"  would update {path.relative_to(ROOT)}")
            continue
        d.setdefault("changelog", []).append({"date": a.date if not a.clear else dt.date.today().isoformat(),
                                              "change": note})
        path.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    verb = "would change" if a.dry_run else "changed"
    print(f"{verb} {changed} record(s); skipped {skipped} with no written sections")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
