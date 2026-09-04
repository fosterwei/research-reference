#!/usr/bin/env python3
"""Dependency-free content gate for JSON records under data/.

Usage:
    python3 scripts/validate_content.py            # validate data/ recursively
    python3 scripts/validate_content.py path ...   # validate specific files or folders

Exit status is 1 when any error is found. Errors are also emitted as GitHub
Actions annotations so they appear inline on pull requests.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import sys
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
EXAMPLES_DIR = "examples"

# ---- Canonical vocabularies (mirrored in docs/content-contract.md) ---------

STATUSES = (
    "discovered",
    "researched",
    "draft",
    "reviewed",
    "published",
    "stale",
    "retired",
)
GATED_STATUSES = ("reviewed", "published")

EVIDENCE_LABELS = (
    "approved-label",
    "human-clinical-trial",
    "observational-human",
    "animal-preclinical",
    "mechanistic-in-vitro",
    "community-reported",
)

SOURCE_KINDS = (
    "peer-reviewed",
    "regulatory",
    "preprint",
    "clinical-registry",
    "manufacturer",
    "community",
    "other",
)

# type -> (folder, url prefix, required fields)
TYPES = {
    "compound": ("compounds", "/compounds/", ("preferred_name", "slug", "status", "evidence_tier", "summary", "review")),
    "stack": ("stacks", "/stacks/", ("title", "slug", "status", "components", "summary", "review")),
    "comparison": ("comparisons", "/compare/", ("title", "slug", "status", "summary", "review")),
    "cycle": ("cycles", "/cycles/", ("title", "slug", "status", "summary", "review")),
    "tool": ("tools", "/tools/", ("title", "slug", "status", "formula", "summary", "review")),
    "post": ("posts", "/blog/", ("title", "slug", "status", "category", "excerpt", "body", "review")),
}
FOLDER_TO_TYPE = {folder: t for t, (folder, _, _) in TYPES.items()}

SLUG_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
URL_RE = re.compile(r"https?://[^\s]+")


def display(path: pathlib.Path) -> str:
    """Repo-relative path when possible, otherwise the path as given."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


class Report:
    def __init__(self) -> None:
        self.errors: list[tuple[str, str]] = []

    def error(self, path: pathlib.Path, message: str) -> None:
        self.errors.append((display(path), message))

    def emit(self) -> None:
        in_actions = os.environ.get("GITHUB_ACTIONS") == "true"
        for file, message in self.errors:
            if in_actions:
                print(f"::error file={file}::{message}")
            print(f"- {file}: {message}")


def load_json(path: pathlib.Path, report: Report) -> dict | None:
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - any parse failure is a content error
        report.error(path, f"invalid JSON ({exc})")
        return None
    if not isinstance(record, dict):
        report.error(path, "top-level value must be an object")
        return None
    return record


def is_iso_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def check_sources(record: dict, path: pathlib.Path, report: Report, gated: bool) -> set[str]:
    """Validate the source ledger and return the set of declared source ids."""
    sources = record.get("sources")
    ids: set[str] = set()
    if sources is None:
        report.error(path, "missing sources (use [] while drafting)")
        return ids
    if not isinstance(sources, list):
        report.error(path, "sources must be a list")
        return ids
    if gated and not sources:
        report.error(path, "reviewed/published record needs at least one source")
    for index, source in enumerate(sources):
        label = f"sources[{index}]"
        if not isinstance(source, dict):
            report.error(path, f"{label} must be an object")
            continue
        sid = source.get("id")
        if not sid or not isinstance(sid, str):
            report.error(path, f"{label} missing id")
        elif sid in ids:
            report.error(path, f"{label} duplicate source id {sid!r}")
        else:
            ids.add(sid)
        url = source.get("url")
        if not isinstance(url, str) or not URL_RE.fullmatch(url):
            report.error(path, f"{label} needs an http(s) url")
        if not is_iso_date(source.get("published")):
            report.error(path, f"{label} needs published as YYYY-MM-DD")
        if not source.get("title"):
            report.error(path, f"{label} missing title")
        kind = source.get("kind")
        if kind is not None and kind not in SOURCE_KINDS:
            report.error(path, f"{label} kind {kind!r} not in {list(SOURCE_KINDS)}")
    return ids


def check_claims(record: dict, path: pathlib.Path, report: Report, source_ids: set[str], gated: bool) -> None:
    """Every attribute claim must carry an evidence label and cite declared sources."""
    attributes = record.get("attributes")
    if attributes is None:
        return
    if not isinstance(attributes, dict):
        report.error(path, "attributes must be an object of field -> list of claims")
        return
    for field, claims in attributes.items():
        if not isinstance(claims, list):
            report.error(path, f"attributes.{field} must be a list of claim objects")
            continue
        for index, claim in enumerate(claims):
            label = f"attributes.{field}[{index}]"
            if not isinstance(claim, dict):
                report.error(path, f"{label} must be an object with value, evidence_label, source_ids")
                continue
            if claim.get("value") in (None, ""):
                report.error(path, f"{label} missing value")
            if claim.get("evidence_label") not in EVIDENCE_LABELS:
                report.error(path, f"{label} evidence_label must be one of {list(EVIDENCE_LABELS)}")
            refs = claim.get("source_ids")
            if not isinstance(refs, list):
                report.error(path, f"{label} source_ids must be a list")
                continue
            unknown = [r for r in refs if r not in source_ids]
            if unknown:
                report.error(path, f"{label} cites unknown source ids {unknown}")
            if gated and not refs:
                report.error(path, f"{label} must cite at least one source on reviewed/published records")


def check_review(record: dict, path: pathlib.Path, report: Report, gated: bool) -> None:
    review = record.get("review")
    if not isinstance(review, dict):
        report.error(path, "review must be an object with author, reviewer, reviewed_at")
        return
    for key in ("author", "reviewer", "reviewed_at"):
        if key not in review:
            report.error(path, f"review.{key} missing")
    if gated:
        if not review.get("author"):
            report.error(path, "reviewed/published record needs a named review.author")
        if not review.get("reviewer"):
            report.error(path, "reviewed/published record needs a named review.reviewer")
        if not is_iso_date(review.get("reviewed_at")):
            report.error(path, "reviewed/published record needs review.reviewed_at as YYYY-MM-DD")
        if review.get("author") and review.get("author") == review.get("reviewer"):
            report.error(path, "review.reviewer must differ from review.author")


def validate_record(path: pathlib.Path, report: Report) -> tuple[str, str] | None:
    """Validate one file. Return (url_prefix, slug) for slug-uniqueness tracking."""
    record = load_json(path, report)
    if record is None:
        return None

    rtype = record.get("type")
    if rtype not in TYPES:
        report.error(path, f"type must be one of {list(TYPES)} (got {rtype!r})")
        return None
    folder, url_prefix, required = TYPES[rtype]

    parent = path.parent.name
    if parent in FOLDER_TO_TYPE and FOLDER_TO_TYPE[parent] != rtype:
        report.error(path, f"type {rtype!r} does not belong in data/{parent}/ (expected data/{folder}/)")

    for key in required:
        if record.get(key) in (None, "", [], {}):
            report.error(path, f"missing {key}")

    status = record.get("status")
    if status not in STATUSES:
        report.error(path, f"status must be one of {list(STATUSES)} (got {status!r})")
    gated = status in GATED_STATUSES

    slug = record.get("slug")
    if isinstance(slug, str) and slug and not SLUG_RE.fullmatch(slug):
        report.error(path, f"invalid slug {slug!r} (lowercase words joined by single hyphens)")

    if rtype == "compound" and record.get("evidence_tier") not in EVIDENCE_LABELS:
        report.error(path, f"evidence_tier must be one of {list(EVIDENCE_LABELS)}")

    source_ids = check_sources(record, path, report, gated)
    check_claims(record, path, report, source_ids, gated)
    check_review(record, path, report, gated)

    if parent == EXAMPLES_DIR and status != "draft":
        report.error(path, "example records must stay in status 'draft'")

    return (url_prefix, slug) if isinstance(slug, str) and slug else None


def collect(paths: list[str]) -> list[pathlib.Path]:
    if not paths:
        return sorted(DATA.rglob("*.json"))
    files: list[pathlib.Path] = []
    for raw in paths:
        p = pathlib.Path(raw).resolve()
        files.extend(sorted(p.rglob("*.json")) if p.is_dir() else [p])
    return files


def main(argv: list[str]) -> int:
    report = Report()
    files = collect(argv)
    seen: dict[tuple[str, str], pathlib.Path] = {}
    scanned = 0
    for path in files:
        scanned += 1
        key = validate_record(path, report)
        if key is None or path.parent.name == EXAMPLES_DIR:
            continue
        if key in seen:
            report.error(path, f"duplicate slug {key[0]}{key[1]} also used by {display(seen[key])}")
        else:
            seen[key] = path

    if report.errors:
        print("CONTENT VALIDATION FAILED")
        report.emit()
        return 1
    print(f"Content validation passed ({scanned} records scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
