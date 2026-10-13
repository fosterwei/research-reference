#!/usr/bin/env python3
"""Keep every sitemap lastmod honest: it moves when a page's content moves.

    npm run build && python3 scripts/check_lastmod.py            # CI: check only
    npm run build && python3 scripts/check_lastmod.py --write    # after a change
    python3 scripts/check_lastmod.py --write --trivial "reason"  # cosmetic change

Why this exists. lastmod used to depend on someone remembering to add a
changelog entry. In the two weeks to 2026-10-13, 35 of 55 records drifted:
nineteen compounds gained a calculator section and nineteen calculator pages
were created on 12 October, and all thirty-eight still claimed 29 September.
The calculator pages claimed a date before they existed. Google treats a
sitemap whose dates are wrong as a sitemap whose dates can be ignored.

How. research/lastmod.json stores, per sitemap URL, a fingerprint of the
page's rendered content and the lastmod that content was published under.
After a build this script fingerprints every page again and compares.

  Content unchanged            nothing to do.
  Record page changed          its changelog must carry a newer date than the
                               manifest recorded, otherwise the change is
                               unrecorded and the build fails. Records print
                               their own date on the page, so the changelog has
                               to stay the single source of truth.
  Manifest page changed        homepage, directories, trust pages and per-
                               compound calculators print no date; --write
                               stamps today's date for them.
  Cosmetic change              --trivial "reason" accepts the new fingerprint
                               without moving any date, and logs the reason.
                               Google asks for lastmod to change on significant
                               updates only, so a renamed column is not news.

The fingerprint is the text inside <main>, plus tag names and link targets,
with scripts, styles, classes and ids removed. It catches what a reader sees
and where the links go, and ignores build noise like Astro's scoped-style
hashes.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html as htmllib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
MANIFEST = ROOT / "research" / "lastmod.json"

# Pages whose date comes from their own changelog, and which print it.
RECORD_PREFIXES = ("/compounds/", "/stacks/", "/compare/", "/tools/", "/blog/")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def is_record(path: str) -> bool:
    return path.startswith(RECORD_PREFIXES) and path.count("/") == 2


def page_file(path: str) -> pathlib.Path:
    return DIST / "index.html" if path == "/" else DIST / path.strip("/") / "index.html"


def fingerprint(html: str) -> str:
    m = re.search(r"(?is)<main\b[^>]*>(.*)</main>", html)
    body = m.group(1) if m else html
    body = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", body)

    def keep(tag: re.Match) -> str:
        slash, name = tag.group(1), tag.group(2).lower()
        href = re.search(r'\bhref="([^"]*)"', tag.group(0))
        return f"<{slash}{name}{' ' + href.group(1) if href else ''}>"

    body = re.sub(r"<\s*(/?)\s*([a-zA-Z][a-zA-Z0-9]*)\b[^>]*>", keep, body)
    body = " ".join(htmllib.unescape(body).split())
    return hashlib.sha1(body.encode("utf-8")).hexdigest()


def sitemap() -> dict[str, str | None]:
    xml = (DIST / "sitemap.xml").read_text(encoding="utf-8")
    out: dict[str, str | None] = {}
    for loc, mod in re.findall(r"<url><loc>([^<]+)</loc>(?:<lastmod>([^<]+)</lastmod>)?</url>", xml):
        out[re.sub(r"^https?://[^/]+", "", loc) or "/"] = mod or None
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--write", action="store_true", help="update the manifest after a change")
    ap.add_argument("--trivial", metavar="REASON", help="with --write: accept changed fingerprints without moving dates")
    ap.add_argument("--today", help="override today's date (YYYY-MM-DD), for tests")
    args = ap.parse_args()
    if args.trivial and not args.write:
        ap.error("--trivial only makes sense with --write")

    if not (DIST / "sitemap.xml").exists():
        print("dist/sitemap.xml not found: run npm run build first", file=sys.stderr)
        return 2

    today = args.today or dt.date.today().isoformat()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    pages: dict = manifest.setdefault("pages", {})
    trivial_log: list = manifest.setdefault("trivial", [])
    listed = sitemap()

    problems: list[str] = []
    changed: list[str] = []
    accepted_trivial: list[str] = []

    for path, mod in sorted(listed.items()):
        f = page_file(path)
        if not f.exists():
            problems.append(f"{path}: in the sitemap but not built")
            continue
        fp = fingerprint(f.read_text(encoding="utf-8", errors="ignore"))
        record = is_record(path)
        known = pages.get(path)

        if record:
            if not mod or not DATE.match(mod):
                problems.append(f"{path}: record has no valid changelog date ({mod!r})")
                continue
        if mod and DATE.match(mod) and mod > today:
            problems.append(f"{path}: lastmod {mod} is in the future")

        if known is None:
            if args.write:
                pages[path] = {"lastmod": mod if record else today, "hash": fp}
                changed.append(f"{path}: new page, lastmod {pages[path]['lastmod']}")
            else:
                problems.append(f"{path}: new page not in research/lastmod.json; run --write")
            continue

        if fp == known.get("hash"):
            if record and mod != known.get("lastmod"):
                # A changelog entry always renders, so this should be impossible.
                problems.append(f"{path}: changelog date moved to {mod} but the page did not change")
            elif not record and not mod:
                problems.append(f"{path}: tracked date {known.get('lastmod')} missing from the sitemap")
            continue

        # The page's content changed.
        if record and mod > known.get("lastmod", ""):
            if args.write:
                pages[path] = {"lastmod": mod, "hash": fp}
                changed.append(f"{path}: content changed, changelog dated {mod}")
            else:
                problems.append(f"{path}: content changed with a changelog entry dated {mod}; run --write")
            continue

        if args.trivial:
            known["hash"] = fp
            accepted_trivial.append(path)
            continue

        if record:
            problems.append(
                f"{path}: content changed but its newest changelog entry is still {mod}. "
                f"Add a dated entry saying what changed, or accept it as cosmetic with "
                f'--write --trivial "reason".')
        elif args.write:
            pages[path] = {"lastmod": today, "hash": fp}
            changed.append(f"{path}: content changed, lastmod {today}")
        else:
            problems.append(f"{path}: content changed since {known.get('lastmod')}; run --write")

    stale = sorted(set(pages) - set(listed))
    for path in stale:
        if args.write:
            del pages[path]
            changed.append(f"{path}: no longer in the sitemap, dropped")
        else:
            problems.append(f"{path}: tracked but no longer in the sitemap; run --write")

    if accepted_trivial:
        trivial_log.append({"date": today, "reason": args.trivial, "pages": accepted_trivial})

    print(f"{len(listed)} sitemap URLs | {len(pages)} tracked | "
          f"{sum(1 for p in listed if is_record(p))} dated by changelog, "
          f"{sum(1 for p in listed if not is_record(p))} by manifest")
    for line in changed:
        print(f"  updated  {line}")
    if accepted_trivial:
        print(f"  accepted {len(accepted_trivial)} cosmetic change(s) without moving dates: {args.trivial}")

    if args.write and (changed or accepted_trivial):
        MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {MANIFEST.relative_to(ROOT)}. Rebuild so the sitemap picks up new dates.")

    if problems:
        print(f"\nlastmod problems: {len(problems)}")
        for p in problems[:40]:
            print(f"  {p}")
        return 1
    print("lastmod: every date matches its page's content")
    return 0


if __name__ == "__main__":
    sys.exit(main())
