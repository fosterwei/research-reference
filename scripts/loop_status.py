#!/usr/bin/env python3
"""Which SOP stages each written page has actually completed.

Usage:
    python3 scripts/loop_status.py            # table for every page with guide[]
    python3 scripts/loop_status.py --strict   # exit 1 if any page lacks a stage

Columns follow docs/content-sop.md and docs/content-automation.md:
  S1 vol    every mapped query carries a measured volume
  S2 comp   at least two scored competitors in the intent map
  S4 gain   an information_gain statement
  S5 outl   an outline
  S6 uniq   uniqueness_pct written to the record
  S6 fmt    docs/design.md 9.10 minimums met in the built page
  audit     research/audits/<slug>-*.md with a triage table
  exit      the audit file carries an exit run (Part 3)
The point is that skipping a stage shows up here rather than being remembered.
"""
import glob, json, os, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
TYPES = {'compounds': 'compounds', 'stacks': 'stacks', 'comparisons': 'compare'}

def status():
    rows = []
    for f in sorted(glob.glob(str(ROOT / 'data/*/*.json'))):
        if '/examples/' in f: continue
        d = json.load(open(f))
        if not d.get('guide'): continue
        t = TYPES[f.split('/')[-2]]; slug = d['slug']
        mp = ROOT / 'research/intents' / f'{slug}.json'
        m = json.load(mp.open()) if mp.exists() else {}
        qs = m.get('queries', [])
        vol = bool(qs) and all(((q.get('volume') or {}).get('clickstream') is not None) or ((q.get('volume') or {}).get('google_ads') is not None) for q in qs)
        audits = glob.glob(str(ROOT / f'research/audits/{slug}-*.md'))
        texts = [open(a).read() for a in audits]
        page = ROOT / 'dist' / t / slug / 'index.html'
        fmt = None
        if page.exists():
            main = re.search(r'<main.*?</main>', page.read_text(), re.S).group(0)
            fmt = main.count('<caption') >= 1 and main.count('<b>') >= 6 and main.count('<ol') >= 1 and main.count('<dl') >= 1 and main.count('<time') >= 1
        rows.append(dict(page=slug, type=t, S1=vol, S2=len(m.get('competitors', [])) >= 2, S3=bool(m), S4=bool(m.get('information_gain')),
                         S5=bool(m.get('outline')), S6u=d.get('uniqueness_pct') is not None, S6f=fmt, audit=any('## Part 2' in x for x in texts), exit=any('## Part 3' in x for x in texts)))
    return rows

if __name__ == '__main__':
    rows = status(); Y = lambda b: 'yes' if b else ('n/a' if b is None else '-')
    print(f"{'page':<28}{'S1 vol':>7}{'S2 comp':>8}{'S3 map':>7}{'S4 gain':>8}{'S5 outl':>8}{'S6 uniq':>8}{'S6 fmt':>7}{'audit':>7}{'exit':>6}")
    for r in rows: print(f"{r['page']:<28}{Y(r['S1']):>7}{Y(r['S2']):>8}{Y(r['S3']):>7}{Y(r['S4']):>8}{Y(r['S5']):>8}{Y(r['S6u']):>8}{Y(r['S6f']):>7}{Y(r['audit']):>7}{Y(r['exit']):>6}")
    incomplete = [r['page'] for r in rows if not all(r[k] for k in ('S1', 'S2', 'S3', 'S4', 'S5', 'S6u', 'audit', 'exit')) or r['S6f'] is False]
    print(f"\n{len(rows) - len(incomplete)}/{len(rows)} pages complete; incomplete: {incomplete or 'none'}")
    if '--strict' in sys.argv and incomplete: sys.exit(1)
