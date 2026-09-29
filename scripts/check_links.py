#!/usr/bin/env python3
"""Check the built site's links: nothing internal is broken, nothing outbound follows.

    npm run build && python3 scripts/check_links.py

Two rules, both easy to break by accident and invisible until someone clicks:

  1. Every internal href resolves to a page in dist/. A renamed slug or a typo
     in guide prose becomes a dead link that no test would otherwise catch.
  2. Every outbound anchor carries rel="nofollow". The site cites over a
     thousand papers, and the policy is that none of those citations passes
     ranking signal. A new component that forgets the attribute would quietly
     opt a page back in.
  3. Every social-card image referenced by og:image or twitter:image exists in
     dist/ and matches the width and height the page declares. A card that
     404s is invisible to fetch it, and a mismatched size is cropped by the
     platform rather than reported.

Same-page anchors (#id) are checked against the ids that page actually renders.
Standard library only; exits non-zero on the first category that fails.
"""
from __future__ import annotations

import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

ANCHOR = re.compile(r'<a\b[^>]*?href="([^"]+)"[^>]*?>', re.I)
IDS = re.compile(r'\bid="([^"]+)"')
META_IMG = re.compile(
    r'<meta\b[^>]*?(?:property|name)="(og:image|twitter:image)"[^>]*?content="([^"]+)"', re.I)
META_DIM = re.compile(
    r'<meta\b[^>]*?property="og:image:(width|height)"[^>]*?content="(\d+)"', re.I)


def image_size(path: pathlib.Path):
    """Width and height of a PNG or JPEG, without a third-party library."""
    data = path.read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")
    if data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker, length = data[i + 1], int.from_bytes(data[i + 2:i + 4], "big")
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                return (int.from_bytes(data[i + 7:i + 9], "big"),
                        int.from_bytes(data[i + 5:i + 7], "big"))
            i += 2 + length
    return None


def resolves(href: str) -> bool:
    path = href.split("#")[0].split("?")[0].strip("/")
    if not path:
        return (DIST / "index.html").exists()
    return ((DIST / path / "index.html").exists() or (DIST / path).exists()
            or (DIST / f"{path}.html").exists())


def main() -> int:
    if not DIST.exists():
        print("dist/ not found: run npm run build first", file=sys.stderr)
        return 2
    pages = sorted(DIST.rglob("index.html"))
    broken: Counter[str] = Counter()
    dead_anchor: Counter[str] = Counter()
    follows: Counter[str] = Counter()
    bad_card: Counter[str] = Counter()
    internal = outbound = cards = 0

    for page in pages:
        html = page.read_text(encoding="utf-8", errors="ignore")
        ids = set(IDS.findall(html))
        where = page.parent.relative_to(DIST).as_posix() or "/"

        declared = {k.lower(): int(v) for k, v in META_DIM.findall(html)}
        for prop, url in META_IMG.findall(html):
            cards += 1
            rel = re.sub(r"^https?://[^/]+", "", url).split("?")[0].lstrip("/")
            asset = DIST / rel
            if not asset.is_file():
                bad_card[f"{where} -> {prop} missing: /{rel}"] += 1
                continue
            size = image_size(asset)
            want = (declared.get("width"), declared.get("height"))
            if prop.lower() == "og:image" and all(want) and size and size != want:
                bad_card[f"{where} -> /{rel} is {size[0]}x{size[1]},"
                         f" declared {want[0]}x{want[1]}"] += 1
        for tag in ANCHOR.finditer(html):
            href = tag.group(1)
            if href.startswith("#"):
                if href[1:] not in ids:
                    dead_anchor[f"{where} -> {href}"] += 1
                continue
            if href.startswith(("http://", "https://")):
                outbound += 1
                if "nofollow" not in tag.group(0).lower():
                    follows[f"{where} -> {href.split('/')[2]}"] += 1
                continue
            if href.startswith(("mailto:", "tel:", "data:")):
                continue
            internal += 1
            if not resolves(href):
                broken[f"{where} -> {href}"] += 1

    print(f"{len(pages)} pages | {internal} internal links | "
          f"{outbound} outbound links | {cards} social-card refs")
    failed = False
    for label, counter in (("broken internal links", broken),
                           ("same-page anchors with no matching id", dead_anchor),
                           ("outbound links missing rel=nofollow", follows),
                           ("social-card images missing or mis-sized", bad_card)):
        if counter:
            failed = True
            print(f"\n{label}: {sum(counter.values())}")
            for item, n in counter.most_common(15):
                print(f"   {item}  x{n}")
        else:
            print(f"{label}: none")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
