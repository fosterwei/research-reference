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
  4. No page prints a record's workflow status to a reader. `status` is internal
     state: it drives nothing a visitor needs and every record sat at 'draft'
     long after being written and reviewed, so the compounds directory labelled
     all 34 of them "draft" and every compound page repeated it in its compare
     table. 226 times across 35 pages before it was noticed.
  5. No page renders the same H2 twice. A generic block heading and an authored
     one drifted into the same words on 32 pages, twice into an exact match, and
     nothing in the build could see it.
  6. robots.txt and the sitemap agree. The Sitemap line must name the same
     origin the build used, and no URL in the sitemap may be blocked by a
     Disallow rule. A robots.txt that blocks a page the sitemap advertises is
     the one SEO error that silently un-indexes a site while every other check
     still passes, and the two files are generated in different places here.
  7. Every icon and manifest in <link rel> resolves, and each icon matches any
     sizes="" it declares. A favicon is the one asset nobody notices is broken,
     because the browser silently falls back to a blank page glyph. The web
     manifest is parsed too: its icons are referenced from nowhere else, so
     without this they are unreachable by every other check here.

Same-page anchors (#id) are checked against the ids that page actually renders.
Standard library only; exits non-zero on the first category that fails.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
from collections import Counter
from html import unescape

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

ANCHOR = re.compile(r'<a\b[^>]*?href="([^"]+)"[^>]*?>', re.I)
IDS = re.compile(r'\bid="([^"]+)"')
META_IMG = re.compile(
    r'<meta\b[^>]*?(?:property|name)="(og:image|twitter:image)"[^>]*?content="([^"]+)"', re.I)
META_DIM = re.compile(
    r'<meta\b[^>]*?property="og:image:(width|height)"[^>]*?content="(\d+)"', re.I)
LINK_ASSET = re.compile(
    r'<link\b[^>]*?rel="(icon|apple-touch-icon|manifest)"[^>]*?>', re.I)
LINK_HREF = re.compile(r'href="([^"]+)"', re.I)
LINK_SIZES = re.compile(r'sizes="(\d+)x(\d+)"', re.I)
H2 = re.compile(r'(?is)<h2[^>]*>(.*?)</h2>')
# The workflow vocabulary from src/content.config.ts. A reader has no use for
# any of it, and seeing it in a <code> element means a template printed the
# field rather than what the field is for.
STATUSES = ('discovered', 'researched', 'draft', 'reviewed', 'published', 'stale', 'retired')
STATUS_CODE = re.compile(
    r'(?is)<code[^>]*>\s*(' + '|'.join(STATUSES) + r')\s*</code>')
TAGS = re.compile(r'(?s)<[^>]+>')


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


def robots_agrees_with_sitemap() -> list[str]:
    """Disallow rules that contradict the sitemap, and a mismatched origin."""
    robots, sitemap = DIST / "robots.txt", DIST / "sitemap.xml"
    if not robots.exists():
        return ["robots.txt was not generated"]
    if not sitemap.exists():
        return ["sitemap.xml was not generated"]
    text = robots.read_text(encoding="utf-8")
    locs = re.findall(r"<loc>([^<]+)</loc>", sitemap.read_text(encoding="utf-8"))
    problems: list[str] = []

    declared = re.findall(r"(?im)^\s*Sitemap:\s*(\S+)", text)
    if not declared:
        problems.append("robots.txt names no Sitemap")
    for url in declared:
        if locs and url.rsplit("/", 1)[0] != locs[0].rstrip("/").rsplit("/", 1)[0] \
                and not url.startswith(re.match(r"https?://[^/]+", locs[0]).group(0)):
            problems.append(f"robots.txt Sitemap {url} is not on the origin the sitemap uses "
                            f"({re.match(r'https?://[^/]+', locs[0]).group(0)})")

    # Only the wildcard group can affect Googlebot's view of a sitemap URL here;
    # a rule for a named agent is deliberate and not this check's business.
    rules: list[str] = []
    in_star = False
    for line in text.splitlines():
        line = line.split("#")[0].strip()
        if not line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip().lower(), value.strip()
        if key == "user-agent":
            in_star = value == "*"
        elif key == "disallow" and in_star and value:
            rules.append(value)

    for loc in locs:
        path = re.sub(r"^https?://[^/]+", "", loc) or "/"
        for rule in rules:
            pattern = re.escape(rule).replace(r"\*", ".*")
            if re.match(pattern, path):
                problems.append(f"sitemap lists {path} but robots.txt disallows {rule}")
                break
    return problems


def main() -> int:
    if not DIST.exists():
        print("dist/ not found: run npm run build first", file=sys.stderr)
        return 2
    pages = sorted(DIST.rglob("index.html"))
    broken: Counter[str] = Counter()
    dead_anchor: Counter[str] = Counter()
    follows: Counter[str] = Counter()
    bad_card: Counter[str] = Counter()
    dupe_h2: Counter[str] = Counter()
    leaked_status: Counter[str] = Counter()
    robots_bad: Counter[str] = Counter()
    internal = outbound = cards = 0

    for page in pages:
        html = page.read_text(encoding="utf-8", errors="ignore")
        ids = set(IDS.findall(html))
        where = page.parent.relative_to(DIST).as_posix() or "/"

        for word in STATUS_CODE.findall(html):
            leaked_status[f"{where} -> <code>{word}</code>"] += 1

        seen_h2: Counter[str] = Counter()
        for raw in H2.findall(html):
            text = unescape(TAGS.sub("", raw)).strip()
            if text:
                seen_h2[text] += 1
        for text, count in seen_h2.items():
            if count > 1:
                dupe_h2[f"{where} -> {text!r} x{count}"] += 1

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

        for tag in LINK_ASSET.finditer(html):
            href = LINK_HREF.search(tag.group(0))
            if not href:
                continue
            cards += 1
            rel = href.group(1).split("?")[0].lstrip("/")
            asset = DIST / rel
            if not asset.is_file():
                bad_card[f"{where} -> {tag.group(1)} missing: /{rel}"] += 1
                continue
            dim = LINK_SIZES.search(tag.group(0))
            if dim and asset.suffix.lower() == ".png":
                want_px = (int(dim.group(1)), int(dim.group(2)))
                size = image_size(asset)
                if size and size != want_px:
                    bad_card[f"{where} -> /{rel} is {size[0]}x{size[1]},"
                             f" declared {want_px[0]}x{want_px[1]}"] += 1
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

    # The manifest's icons are named in JSON, not in any page's markup.
    for mf in sorted(DIST.rglob("*.webmanifest")) + sorted(DIST.glob("manifest.json")):
        where = mf.relative_to(DIST).as_posix()
        try:
            icons = json.loads(mf.read_text(encoding="utf-8")).get("icons") or []
        except (ValueError, OSError) as exc:
            bad_card[f"{where} -> unreadable: {exc}"] += 1
            continue
        for icon in icons:
            src = (icon.get("src") or "").split("?")[0].lstrip("/")
            if not src:
                continue
            cards += 1
            asset = DIST / src
            if not asset.is_file():
                bad_card[f"{where} -> icons[] missing: /{src}"] += 1
                continue
            declared = re.fullmatch(r"(\d+)x(\d+)", (icon.get("sizes") or "").strip())
            size = image_size(asset)
            if declared and size and size != (int(declared.group(1)), int(declared.group(2))):
                bad_card[f"{where} -> /{src} is {size[0]}x{size[1]},"
                         f" declared {declared.group(0)}"] += 1

    for problem in robots_agrees_with_sitemap():
        robots_bad[problem] += 1

    print(f"{len(pages)} pages | {internal} internal links | "
          f"{outbound} outbound links | {cards} asset refs")
    failed = False
    for label, counter in (("broken internal links", broken),
                           ("same-page anchors with no matching id", dead_anchor),
                           ("outbound links missing rel=nofollow", follows),
                           ("card, icon or manifest assets missing or mis-sized", bad_card),
                           ("pages rendering the same H2 twice", dupe_h2),
                           ("pages printing an internal record status", leaked_status),
                           ("robots.txt disagreeing with the sitemap", robots_bad)):
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
