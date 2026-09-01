#!/usr/bin/env python3
import json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]; DATA = ROOT / 'data'; errors=[]; slugs={}
for path in DATA.glob('*.json'):
    try: record=json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc: errors.append(f'{path.name}: invalid JSON ({exc})'); continue
    required = ('preferred_name','slug','status','evidence_tier','review') if record.get('type')=='compound' else ('title','slug','status','body','review')
    for key in required:
        if not record.get(key): errors.append(f'{path.name}: missing {key}')
    slug=record.get('slug')
    if slug in slugs: errors.append(f'duplicate slug {slug}: {path.name} and {slugs[slug]}')
    elif slug: slugs[slug]=path.name
    if slug and not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug): errors.append(f'{path.name}: invalid slug')
    if record.get('status') in ('reviewed','published') and not record.get('sources'): errors.append(f'{path.name}: reviewed/published record needs sources')
if errors: print('CONTENT VALIDATION FAILED\n'+'\n'.join('- '+e for e in errors)); sys.exit(1)
print(f'Content validation passed ({len(list(DATA.glob("*.json")))} records scanned).')
