#!/usr/bin/env python3
"""Measure built pages against the template spec and write uniqueness into records.

Usage:
    python3 scripts/measure_pages.py            # report only
    python3 scripts/measure_pages.py --write    # also set uniqueness_pct on records

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


if __name__ == "__main__":
    sys.exit(run("--write" in sys.argv))
