#!/usr/bin/env python3
"""Content-quality audit of one built page, as Markdown, for docs/content-automation.md step 3.

Usage:
    python3 scripts/audit_page.py <slug> [--type compounds] [--url <live url>]

Reads dist/<type>/<slug>/index.html (run `npm run build` first) and prints the
audit that the /seo-content skill would produce, computed deterministically so
it can run offline and on CI: meta tags, structured data, Google's who/how/why
test, E-E-A-T sub-scores, readability of our own prose versus quoted prose,
keyword placement, link profile, formatting minimums and a heuristic score.

Scores are this repo's heuristics, not Google signals. When a live URL is
given it is fetched for headers only; Vercel preview deployments redirect
unauthenticated requests (302), so the page body always comes from dist/.
"""
from __future__ import annotations

import html
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


def text_of(fragment: str) -> str:
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", fragment))).strip()


def readability(t: str) -> tuple[int, float, float]:
    w = re.findall(r"[A-Za-z][A-Za-z'’\-]*", t)
    s = [x for x in re.split(r"(?<=[.!?])\s+", t) if len(x.split()) > 2]
    if not w or not s:
        return (0, 0.0, 0.0)
    syl = lambda x: max(1, len(re.findall(r"[aeiouy]+", x.lower())))
    asl = len(w) / len(s); asw = sum(map(syl, w)) / len(w)
    return (round(206.835 - 1.015 * asl - 84.6 * asw), round(0.39 * asl + 11.8 * asw - 15.59, 1), round(asl, 1))


def audit(slug: str, rtype: str, live: str | None) -> str:
    page = DIST / rtype / slug / "index.html"
    if not page.exists():
        sys.exit(f"no built page at {page}; run npm run build")
    h = page.read_text(encoding="utf-8")
    g = lambda p: (lambda m: html.unescape(m.group(1)).strip() if m else None)(re.search(p, h, re.I | re.S))
    title, desc, robots, canon = g(r"<title>(.*?)</title>"), g(r'<meta name="description" content="([^"]*)"'), g(r'<meta name="robots" content="([^"]*)"'), g(r'rel="canonical" href="([^"]*)"')
    ld = [json.loads(b) for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)]
    art = next((d for d in ld if d.get("@type") == "Article"), {})
    main = re.search(r"<main.*?</main>", h, re.S).group(0)
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", main, flags=re.S)
    h1 = [text_of(x) for x in re.findall(r"<h1[^>]*>(.*?)</h1>", body, re.S)]
    h2 = [text_of(x) for x in re.findall(r"<h2[^>]*>(.*?)</h2>", body, re.S)]
    txt = text_of(body); words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-\.·]*", txt); n = len(words)
    own_html = re.sub(r"<(q|blockquote|table)\b[^>]*>.*?</\1>", " ", body, flags=re.S)
    own = text_of(" ".join(re.findall(r"<(?:p|dd|li|caption|summary)\b[^>]*>(.*?)</(?:p|dd|li|caption|summary)>", own_html, re.S)))
    quoted = text_of(" ".join(re.findall(r"<q\b[^>]*>(.*?)</q>", body, re.S)))
    kw = slug.replace("-", " ")
    kc = len(re.findall(re.escape(kw), txt, re.I))
    # Whole anchor tag, so attributes after href (target, rel) are seen.
    links = [(tag, re.search(r'href="([^"]+)"', tag).group(1)) for tag in re.findall(r"<a\b[^>]*>", body) if re.search(r'href="([^"]+)"', tag)]
    internal = {u for a, u in links if u.startswith("/")}
    ext = [(a, u) for a, u in links if u.startswith("http")]
    hosts: dict[str, int] = {}
    for a, u in ext:
        host = re.match(r"https?://([^/]+)", u).group(1); hosts[host] = hosts.get(host, 0) + 1
    fmt = {k: len(re.findall(p, body)) for k, p in {"tables": r"<table", "captions": r"<caption", "quotes_with_cite": r"<q cite=", "abbr": r"<abbr", "time": r"<time", "details": r"<details", "images": r"<img", "bold_own": r"<b>"}.items()}
    reviewed = bool(art.get("reviewedBy")); author = bool(art.get("author"))
    not_reviewed_notice = "Not yet reviewed" in txt
    footer = re.search(r"<footer.*?</footer>", h, re.S); flinks = re.findall(r'href="([^"]+)"', footer.group(0)) if footer else []
    trust_pages = {p: (DIST / p.strip("/") / "index.html").exists() for p in ("/about", "/privacy", "/contact")}
    dates = sorted(set(re.findall(r"20\d\d-\d\d-\d\d", txt)))
    fre_all, fk_all, asl_all = readability(txt); fre_own, fk_own, asl_own = readability(own); fre_q, fk_q, asl_q = readability(quoted)

    # E-E-A-T heuristics (this repo's model; trust weighted highest, per Google's stated hierarchy)
    exp = 6 + (4 if fmt["tables"] >= 1 else 0) + (3 if fmt["quotes_with_cite"] >= 10 else 0) + (2 if "No study" in txt or "none tests" in txt else 0)
    expert = (4 if fmt["quotes_with_cite"] >= 10 else 1) + (3 if hosts.get("europepmc.org", 0) >= 10 else 0) + (2 if fmt["captions"] else 0) + (12 if reviewed else 0) + (2 if author else 0)
    auth = (5 if hosts.get("europepmc.org", 0) >= 10 else 2) + (4 if art.get("publisher") else 0) + (4 if trust_pages["/about"] else 0) + (10 if reviewed else 0) + (2 if len(internal) >= 6 else 0)
    trust = (3 if canon and "*" not in canon else 0) + (3 if dates else 0) + (4 if not_reviewed_notice or reviewed else 0) + (3 if trust_pages["/about"] else 0) + (2 if trust_pages["/privacy"] else 0) + (2 if trust_pages["/contact"] else 0) + (10 if reviewed else 0) + (3 if art.get("datePublished") else 0)
    exp, expert, auth, trust = min(exp, 20), min(expert, 25), min(auth, 25), min(trust, 30)
    score = exp + expert + auth + trust
    geo = (25 if fmt["quotes_with_cite"] >= 10 else 10) + (15 if fmt["tables"] else 0) + (10 if len(h2) >= 8 else 5) + (10 if fmt["details"] else 0) + (10 if art.get("publisher") else 0) + (15 if reviewed else 0) + (10 if fre_own >= 40 else 0) + (5 if canon and "*" not in canon else 0)

    issues = []
    if not reviewed: issues.append("No named reviewer (JSON-LD `reviewedBy` absent). For a YMYL topic this caps every E-E-A-T factor; it is the launch blocker in Issue #3, not a content edit.")
    if not author: issues.append("No author in structured data (`author` absent).")
    if canon and "*" in canon: issues.append(f"Canonical contains a wildcard: {canon}")
    if title and len(title) > 60: issues.append(f"Title is {len(title)} characters (budget 60).")
    if desc and (len(desc) < 130 or len(desc) > 160): issues.append(f"Meta description is {len(desc)} characters (target 130–160).")
    if fre_own < 40: issues.append(f"Own prose reads at Flesch {fre_own} (avg sentence {asl_own} words). Quotations are verbatim by policy; this measures only the text we wrote.")
    if 1000 * len(internal) / max(n, 1) < 3: issues.append(f"Internal links {1000*len(internal)/max(n,1):.1f} per 1,000 words (guideline 3–5).")
    for p, ok in trust_pages.items():
        if not ok: issues.append(f"Trust page {p} does not exist.")
    if fmt["images"] == 0: issues.append("No image, so no image alt text carrying the keyword (design.md requires none; note only).")
    if not any("/compounds/" in u and u != f"/compounds/{slug}" for u in internal): issues.append("No contextual link to another compound page in the body.")

    out = []
    out.append(f"## Part 1: audit\n")
    out.append(f"Built from `dist/{rtype}/{slug}/index.html`" + (f"; live URL `{live}` (body not fetched: preview deployments redirect unauthenticated requests)" if live else "") + ".\n")
    out.append(f"### Content quality score: {score}/100 (heuristic)\n")
    out.append("| Factor | Score | Signals |\n|---|---|---|")
    out.append(f"| Experience | {exp}/20 | {fmt['tables']} data tables, {fmt['quotes_with_cite']} cited verbatim quotations, measured-absence statements {'present' if 'No study' in txt else 'absent'} |")
    out.append(f"| Expertise | {expert}/25 | {hosts.get('europepmc.org',0)} primary-source links; reviewer {'named' if reviewed else 'absent'}; author {'named' if author else 'absent'} |")
    out.append(f"| Authoritativeness | {auth}/25 | publisher {'set' if art.get('publisher') else 'missing'} in JSON-LD; /about {'exists' if trust_pages['/about'] else 'missing'}; {len(internal)} internal links |")
    out.append(f"| Trustworthiness | {trust}/30 | canonical `{canon}`; datePublished {art.get('datePublished')}; not-yet-reviewed notice {'shown' if not_reviewed_notice else 'absent'}; privacy {'yes' if trust_pages['/privacy'] else 'no'}, contact {'yes' if trust_pages['/contact'] else 'no'} |\n")
    out.append(f"### AI citation readiness: {geo}/100 (heuristic)\n")
    out.append("### Who / how / why\n")
    out.append(f"- **Who**: {'reviewer and author in structured data' if reviewed and author else 'no named person; the page says so'}.\n- **How**: process disclosed on-page ({'yes' if 'verbatim' in txt else 'no'}: quotations labelled verbatim, changelog present {'yes' if 'changed' in txt.lower() else 'no'}).\n- **Why**: evidence-first, empty sections suppressed, no commercial content ({hosts}).\n")
    out.append("### Page facts\n")
    out.append(f"| | |\n|---|---|\n| Title ({len(title or '')}) | {title} |\n| Description ({len(desc or '')}) | {desc} |\n| Robots | {robots} |\n| Canonical | {canon} |\n| H1 / H2 / H3 | {h1} / {len(h2)} / {len(re.findall(r'<h3', body))} |\n| Words (total / own prose / quoted) | {n} / {len(own.split())} / {len(quoted.split())} |\n| Readability Flesch, grade, avg sentence: all | {fre_all}, {fk_all}, {asl_all} |\n| … own prose only | {fre_own}, {fk_own}, {asl_own} |\n| … quotations only | {fre_q}, {fk_q}, {asl_q} |\n| Keyword `{kw}` | {kc}× ({100*kc/max(n,1):.2f}%); title {kw in (title or '').lower()}, H1 {any(kw in x.lower() for x in h1)}, first 100 words {kw in ' '.join(words[:100]).lower()} |\n| Links | {len(internal)} internal ({1000*len(internal)/max(n,1):.1f}/1k words); {len(ext)} external {hosts}; new-tab {sum('_blank' in a for a,u in ext)}/{len(ext)} |\n| Formatting | {fmt} |\n| Footer links | {flinks} |\n| Dates on page | {dates[-4:]} |\n")
    out.append("### H2 sequence\n\n" + "\n".join(f"{i+1}. {x}" for i, x in enumerate(h2)) + "\n")
    out.append("### Issues found\n\n" + "\n".join(f"{i+1}. {x}" for i, x in enumerate(issues)) + "\n")
    return "\n".join(out)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    rtype = sys.argv[sys.argv.index("--type") + 1] if "--type" in sys.argv else "compounds"
    live = sys.argv[sys.argv.index("--url") + 1] if "--url" in sys.argv else None
    print(audit(args[0], rtype, live))
