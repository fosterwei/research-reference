#!/usr/bin/env python3
"""Dependency-free content gate.

Enforces the release gates in agent/AGENT.md and the limits in
docs/page-template-spec.md. Standard library only, by design.

Exit 1 on any error. Warnings are reported but do not fail the build.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'

INDEXABLE = ('reviewed', 'published')
STATUSES = ('discovered', 'researched', 'draft', 'reviewed', 'published', 'stale', 'retired')

# Evidence labels defined in agent/AGENT.md. Every claim carries one.
LABELS = (
    'approved-label',
    'human-clinical-trial',
    'observational-human',
    'animal-preclinical',
    'mechanistic-in-vitro',
    'community-reported',
)

# Sections whose entries must each carry an evidence label.
LABELLED_COLLECTIONS = ('evidence', 'interactions', 'adverse_events', 'faq')

TITLE_MAX = 60
DESCRIPTION_MAX = 160
SLUG_MAX = 100
UNIQUENESS_HARD_STOP = 30.0   # below this, never publish
UNIQUENESS_FLOOR = 40.0       # release gate
UNIQUENESS_TARGET = 85.0      # competitive target, see docs/competitive-baseline.md

SLUG_RE = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')
ISO_DATE_RE = re.compile(r'\d{4}-\d{2}-\d{2}$')

errors = []
warnings = []
slugs = {}
names = {}


def check_metadata(name, record):
    seo = record.get('seo') or {}
    title = (seo.get('title') or '').strip()
    description = (seo.get('description') or '').strip()
    if len(title) > TITLE_MAX:
        errors.append(f'{name}: seo.title is {len(title)} chars, limit {TITLE_MAX}')
    if len(description) > DESCRIPTION_MAX:
        errors.append(f'{name}: seo.description is {len(description)} chars, limit {DESCRIPTION_MAX}')
    if record.get('status') in INDEXABLE:
        if not title:
            errors.append(f'{name}: indexable record needs seo.title')
        if not description:
            errors.append(f'{name}: indexable record needs seo.description')


def check_labels(name, record):
    for field in LABELLED_COLLECTIONS:
        entries = record.get(field)
        if not isinstance(entries, list):
            continue
        for i, entry in enumerate(entries):
            if not isinstance(entry, dict):
                errors.append(f'{name}: {field}[{i}] must be an object')
                continue
            label = entry.get('label')
            if not label:
                errors.append(f'{name}: {field}[{i}] is missing an evidence label')
            elif label not in LABELS:
                errors.append(f'{name}: {field}[{i}] has unknown label "{label}"')


def check_review(name, record):
    review = record.get('review') or {}
    if record.get('status') not in INDEXABLE:
        return
    # A named reviewer with a stated credential is the project's core
    # differentiator. See docs/competitive-baseline.md.
    for key in ('author', 'reviewer', 'reviewer_credential', 'reviewed_at'):
        if not (review.get(key) or '').strip():
            errors.append(f'{name}: indexable record needs review.{key}')
    reviewed_at = (review.get('reviewed_at') or '').strip()
    if reviewed_at and not ISO_DATE_RE.match(reviewed_at):
        errors.append(f'{name}: review.reviewed_at "{reviewed_at}" is not YYYY-MM-DD')


def check_sources(name, record):
    sources = record.get('sources')
    if record.get('status') in INDEXABLE and not sources:
        errors.append(f'{name}: reviewed/published record needs sources')
        return
    if not isinstance(sources, list):
        return
    for i, source in enumerate(sources):
        if not isinstance(source, dict):
            errors.append(f'{name}: sources[{i}] must be an object')
            continue
        if not source.get('url'):
            errors.append(f'{name}: sources[{i}] is missing url')
        if not source.get('date'):
            errors.append(f'{name}: sources[{i}] is missing publication date')


def check_uniqueness(name, record):
    value = record.get('uniqueness_pct')
    if value is None:
        if record.get('status') in INDEXABLE:
            errors.append(f'{name}: indexable record needs a measured uniqueness_pct')
        return
    if not isinstance(value, (int, float)):
        errors.append(f'{name}: uniqueness_pct must be a number')
        return
    if value < UNIQUENESS_HARD_STOP:
        errors.append(f'{name}: uniqueness {value}% is below the {UNIQUENESS_HARD_STOP}% hard stop')
    elif value < UNIQUENESS_FLOOR:
        errors.append(f'{name}: uniqueness {value}% is below the {UNIQUENESS_FLOOR}% release gate')
    elif value < UNIQUENESS_TARGET:
        warnings.append(
            f'{name}: uniqueness {value}% clears the gate but is under the '
            f'{UNIQUENESS_TARGET}% competitive target'
        )


def check_changelog(name, record):
    entries = record.get('changelog')
    if not isinstance(entries, list):
        return
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f'{name}: changelog[{i}] must be an object')
            continue
        date = (entry.get('date') or '').strip()
        if date and not ISO_DATE_RE.match(date):
            errors.append(f'{name}: changelog[{i}].date "{date}" is not YYYY-MM-DD')


paths = sorted(DATA.glob('*.json'))
for path in paths:
    name = path.name
    try:
        record = json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{name}: invalid JSON ({exc})')
        continue

    is_compound = record.get('type') == 'compound'
    required = (
        ('preferred_name', 'slug', 'status', 'evidence_tier', 'review')
        if is_compound else
        ('title', 'slug', 'status', 'body', 'review')
    )
    for key in required:
        if not record.get(key):
            errors.append(f'{name}: missing {key}')

    status = record.get('status')
    if status and status not in STATUSES:
        errors.append(f'{name}: unknown status "{status}"')

    slug = record.get('slug')
    if slug:
        if slug in slugs:
            errors.append(f'duplicate slug {slug}: {name} and {slugs[slug]}')
        else:
            slugs[slug] = name
        if not SLUG_RE.fullmatch(slug):
            errors.append(f'{name}: invalid slug')
        if len(slug) > SLUG_MAX:
            errors.append(f'{name}: slug is {len(slug)} chars, limit {SLUG_MAX}')

    identity = (record.get('preferred_name') or record.get('title') or '').strip().lower()
    if identity:
        if identity in names and names[identity] != name:
            errors.append(f'duplicate entity name "{identity}": {name} and {names[identity]}')
        else:
            names[identity] = name

    check_metadata(name, record)
    check_labels(name, record)
    check_review(name, record)
    check_sources(name, record)
    check_changelog(name, record)
    if is_compound:
        check_uniqueness(name, record)

if warnings:
    print('WARNINGS\n' + '\n'.join('- ' + w for w in warnings) + '\n')

if errors:
    print('CONTENT VALIDATION FAILED\n' + '\n'.join('- ' + e for e in errors))
    sys.exit(1)

print(f'Content validation passed ({len(paths)} records scanned).')
