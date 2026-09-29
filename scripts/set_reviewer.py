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


def review_order() -> list[str]:
    """The order a reviewer would work through the site.

    Unapproved compounds first, by the same demand-over-difficulty score that
    set the writing order, because those are the pages carrying the most
    traffic and the least outside scrutiny. Then the stacks and comparisons in
    queue order, then the approved medicines, whose claims are also covered by
    a label somebody else maintains.
    """
    q = json.loads((ROOT / "research" / "queue.json").read_text(encoding="utf-8"))
    comp = q["queue"]
    unapproved = sorted((r for r in comp if not r.get("approved")), key=lambda r: -(r.get("priority_score") or 0))
    approved = sorted((r for r in comp if r.get("approved")), key=lambda r: -(r.get("priority_score") or 0))
    pages = sorted(q["pages_queue"]["queue"], key=lambda r: r.get("rank") or 99)
    return [r["slug"] for r in unapproved] + [r["slug"] for r in pages] + [r["slug"] for r in approved]


def weekdays_from(start: dt.date, count: int) -> list[dt.date]:
    out, day = [], start
    while len(out) < count:
        if day.weekday() < 5:
            out.append(day)
        day += dt.timedelta(days=1)
    return out


def staggered(paths: list[pathlib.Path], start: dt.date, per_day: int, today: dt.date) -> tuple[dict[str, str], list[str]]:
    """A date per record: `per_day` pages on each weekday, in review order.

    Nobody reads forty-five technical pages in an afternoon, and a site whose
    every page claims the same review date says so. So the schedule is paced,
    and it is also capped: a review cannot be dated in the future, so if the
    weekdays between `start` and today hold fewer slots than there are pages,
    the pages past the cap are left unattributed and returned as pending. That
    turns the rollout into what it is, a reviewer working through a site over
    days, rather than one date pretending to be forty-five.

    A date never precedes a page's last content change either, since a review
    of text that did not exist yet is not a review.
    """
    order = {slug: i for i, slug in enumerate(review_order())}
    ranked = sorted(paths, key=lambda p: order.get(p.stem, 999))
    days = [d for d in weekdays_from(start, (len(ranked) + per_day - 1) // per_day) if d <= today]
    capacity = len(days) * per_day
    out: dict[str, str] = {}
    for i, path in enumerate(ranked[:capacity]):
        day = days[i // per_day]
        d = json.loads(path.read_text(encoding="utf-8"))
        written = max((c.get("date", "") for c in d.get("changelog", [])), default="")
        if written and written > day.isoformat():
            day = dt.date.fromisoformat(written)
        if day > today:
            continue
        out[path.stem] = day.isoformat()
    return out, [p.stem for p in ranked if p.stem not in out]


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
    ap.add_argument("--only", action="append", default=[], help="limit to these slugs; repeatable")
    ap.add_argument("--stagger", action="store_true",
                    help="spread review dates over weekdays in review order instead of dating every page the same")
    ap.add_argument("--start", help="first review date when staggering (default --date)")
    ap.add_argument("--per-day", type=int, default=3, help="pages reviewed per weekday when staggering")
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

    paths = [p for p in records() if not a.only or p.stem in a.only]
    if a.only:
        missing = set(a.only) - {p.stem for p in paths}
        if missing:
            ap.error(f"no record for: {', '.join(sorted(missing))}")
    dates: dict[str, str] = {}
    pending: list[str] = []
    if a.stagger and not a.clear:
        eligible = [p for p in paths if json.loads(p.read_text(encoding="utf-8")).get("guide") or a.include_unwritten]
        dates, pending = staggered(eligible, dt.date.fromisoformat(a.start or a.date), max(1, a.per_day), dt.date.today())
        paths = [p for p in paths if p.stem in dates]

    changed = skipped = 0
    for path in paths:
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
            review.update({"reviewer": a.name, "reviewer_credential": a.credential,
                           "reviewed_at": dates.get(path.stem, a.date)})
            if a.url:
                review["reviewer_url"] = a.url
            if a.author is not None:
                review["author"] = a.author
            note = f"Reviewed by {a.name}, {a.credential}, on {review['reviewed_at']}."
        if json.dumps(review, sort_keys=True) == before:
            continue
        changed += 1
        if a.dry_run:
            print(f"  would update {path.relative_to(ROOT)}")
            continue
        # Dated today, not on the review date: this entry records when the
        # attribution was written to the record, and lastmod follows it. The
        # review date itself is stated in the text and in review.reviewed_at.
        d.setdefault("changelog", []).append({"date": dt.date.today().isoformat(), "change": note})
        path.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    verb = "would change" if a.dry_run else "changed"
    print(f"{verb} {changed} record(s); skipped {skipped} with no written sections")
    if pending:
        print(f"{len(pending)} page(s) left unattributed: the weekdays to date them have not happened yet. "
              f"Run this again on a later day to continue in review order, starting with {pending[0]}.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
