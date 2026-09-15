#!/usr/bin/env python3
"""Measure built pages against the template spec and write uniqueness into records.

Usage:
    python3 scripts/measure_pages.py            # report only
    python3 scripts/measure_pages.py --write    # also set uniqueness_pct on records
    python3 scripts/measure_pages.py --formatting [slug]   # docs/design.md section 9.10 minimums

Reads dist/ (run `npm run build` first). For every record page it counts words
inside <main>, lists rendered sections, and computes uniqueness the same way
docs/competitive-baseline.md measured the incumbent: 6-word shingles, header,
footer and navigation excluded, boilerplate defined as any shingle present on
at least 80% of the pages of the same type. Uniqueness is the share of a page's
shingles that are not boilerplate.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
TYPES = {"compounds": "compounds", "stacks": "stacks", "compare": "comparisons"}


def main_text(html: str) -> str:
    m = re.search(r"<main.*?</main>", html, re.S)
    body = m.group(0) if m else html
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body)).strip()


def shingles(words: list[str], n: int = 6) -> set[tuple[str, ...]]:
    return {tuple(words[i : i + n]) for i in range(len(words) - n + 1)}


def run(write: bool) -> int:
    if not DIST.exists():
        print("dist/ missing; run npm run build first"); return 1
    report = []
    for url_dir, data_dir in TYPES.items():
        pages = {}
        for html in sorted((DIST / url_dir).glob("*/index.html")):
            slug = html.parent.name
            text = main_text(html.read_text(encoding="utf-8"))
            words = re.findall(r"[a-z0-9][a-z0-9'’\-\.]*", text.lower())
            sections = re.findall(r"<h2>([^<]*)</h2>", html.read_text(encoding="utf-8"))
            pages[slug] = (words, shingles(words), sections)
        if not pages:
            continue
        counts: Counter = Counter()
        for _, sh, _ in pages.values():
            counts.update(sh)
        thresh = max(2, int(0.8 * len(pages)))
        boiler = {s for s, c in counts.items() if c >= thresh}
        print(f"\n== /{url_dir}/  ({len(pages)} pages, boilerplate shingles shared by >={thresh}: {len(boiler)})")
        print(f"{'page':<30}{'words':>7}{'sections':>10}{'unique%':>9}")
        for slug, (words, sh, sections) in sorted(pages.items(), key=lambda kv: len(kv[1][0])):
            uniq = 100.0 * (1 - len(sh & boiler) / len(sh)) if sh else 0.0
            flag = "!" if uniq < 40 else " "
            print(f"{flag}{slug:<29}{len(words):>7}{len(sections):>10}{uniq:>8.1f}")
            report.append((data_dir, slug, len(words), len(sections), round(uniq, 1)))
            if write:
                p = ROOT / "data" / data_dir / f"{slug}.json"
                if p.exists():
                    rec = json.loads(p.read_text(encoding="utf-8"))
                    if rec.get("status") in ("researched", "draft"):
                        rec["uniqueness_pct"] = round(uniq, 1)
                        p.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if report:
        ws = sorted(r[2] for r in report); us = sorted(r[4] for r in report)
        print(f"\nall pages: n={len(report)}  words median={ws[len(ws)//2]} min={ws[0]} max={ws[-1]}  "
              f"uniqueness median={us[len(us)//2]:.1f}% min={us[0]:.1f}%  below40={sum(1 for u in us if u < 40)}")
    return 0



def own_prose(main_html: str) -> str:
    """The text we wrote: paragraph and list-item content, minus quotations.

    Table cells, claim meta rows and source lines are structured data, not
    prose, and are excluded so the sentence-length figure measures writing."""
    body = re.sub(r"<(script|style|table)[^>]*>.*?</\1>", " ", main_html, flags=re.S)
    body = re.sub(r"<(q|blockquote)\b[^>]*>.*?</\1>", " ", body, flags=re.S)
    parts = re.findall(r"<(?:p|dd|caption|summary)\b[^>]*>(.*?)</(?:p|dd|caption|summary)>", body, flags=re.S)
    parts += re.findall(r"<(?:ul|ol) class=\"(?:list|changelog)\"[^>]*>(.*?)</(?:ul|ol)>", body, flags=re.S)
    return " ".join(parts)


def own_prose_bold(main_html: str) -> str:
    """Prose containers only, quotations removed, for counting <b> emphasis."""
    body = re.sub(r"<(script|style|table)[^>]*>.*?</\1>", " ", main_html, flags=re.S)
    body = re.sub(r"<(q|blockquote)\b[^>]*>.*?</\1>", " ", body, flags=re.S)
    return " ".join(re.findall(r"<(?:p|dd|caption|summary)\b[^>]*>(.*?)</(?:p|dd|caption|summary)>", body, flags=re.S))


def formatting(slug_filter):
    """Report the per-page formatting minimums from docs/design.md section 9.10."""
    pages = sorted((DIST / "compounds").glob("*/index.html"))
    if slug_filter:
        pages = [p for p in pages if p.parent.name == slug_filter]
    if not pages:
        print("no built pages matched"); return 1
    cols = ["tables", "captions", "bold(own)", "ol", "ul", "q+cite", "dl", "time", "abbr", "int/1k", "sent.len", "ext_blank"]
    print(f"{'page':<26}" + "".join(f"{c:>10}" for c in cols))
    for html_path in pages:
        h = html_path.read_text(encoding="utf-8")
        main = re.search(r"<main.*?</main>", h, re.S).group(0)
        own = own_prose(main)
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", own))
        words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-\.]*", text))
        sents = [s for s in re.split(r"(?<=[.!?])\s+", text) if len(s.split()) > 2]
        avg = words / len(sents) if sents else 0
        page_words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-\.]*", re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", main, flags=re.S)))))
        internal = {u for u in re.findall(r'href="(/[^"#?]*)"', main)}
        ext = re.findall(r'<a\b[^>]*href="https?://[^"]+"[^>]*>', main)
        vals = [
            len(re.findall(r"<table", main)), len(re.findall(r"<caption", main)),
            len(re.findall(r"<b>", own_prose_bold(main))), len(re.findall(r"<ol\b", main)), len(re.findall(r"<ul\b", main)),
            len(re.findall(r'<(?:q|blockquote)\b[^>]*\bcite="', main)), len(re.findall(r"<dl\b", main)),
            len(re.findall(r"<time\b", main)), len(re.findall(r"<abbr\b", main)),
            f"{1000 * len(internal) / max(page_words, 1):.1f}", f"{avg:.1f}",
            f"{sum('_blank' in e for e in ext)}/{len(ext)}",
        ]
        print(f"{html_path.parent.name:<26}" + "".join(f"{str(v):>10}" for v in vals))
    print("\nminimums (compound page): tables>=1 captions>=1 bold(own)>=6 ol>=1 ul>=1 q+cite=all dl>=1 time>=1 int/1k 3-5 sent.len<=~22 (own prose only)")
    return 0


if __name__ == "__main__":
    if "--formatting" in sys.argv:
        args = [a for a in sys.argv[1:] if not a.startswith("--")]
        sys.exit(formatting(args[0] if args else None))
    sys.exit(run("--write" in sys.argv))
