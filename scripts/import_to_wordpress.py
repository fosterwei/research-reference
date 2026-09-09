#!/usr/bin/env python3
"""Idempotent importer: JSON records under data/ to WordPress via the REST API.

Usage:
    python3 scripts/import_to_wordpress.py --dry-run      # plan only, no writes
    python3 scripts/import_to_wordpress.py                # import everything
    python3 scripts/import_to_wordpress.py data/compounds # import a subset

Credentials come from the environment, never from the repository:

    WP_URL             https://staging.example.com
    WP_USER            WordPress username
    WP_APP_PASSWORD    Application password (Users -> Profile -> Application Passwords)

Records are matched on their slug within a post type, so re-running updates the
existing post instead of creating a second one. A content hash is stored on each
post, so a re-run with no source change reports "unchanged" and writes nothing.

The record's lifecycle state drives the WordPress post status: only `published`
records become WordPress `publish`. Everything else is imported as a WordPress
draft, which keeps it out of the sitemap and out of the index regardless of what
the Research Database plugin does.

Exit status is 1 if validation fails or any record fails to import.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

import validate_content as vc

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TIMEOUT = 30

# record type -> REST base. Mirrors research_db_post_types() in the plugin,
# and the URL column in docs/content-contract.md.
REST_BASE = {
    "compound": "compounds",
    "stack": "stacks",
    "comparison": "compare",
    "cycle": "cycles",
    "tool": "tools",
    "post": "posts",
}

PUBLISHED_STATE = "published"


class ImportError_(RuntimeError):
    """Raised when one record cannot be imported."""


# ---- HTTP -----------------------------------------------------------------


class Client:
    def __init__(self, base_url: str, user: str, password: str, allow_http: bool) -> None:
        parsed = urllib.parse.urlparse(base_url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise SystemExit(f"WP_URL must be an absolute http(s) URL (got {base_url!r})")
        if parsed.scheme == "http" and not allow_http:
            raise SystemExit(
                "WP_URL uses plain http, which would send the application password "
                "in the clear. Use https, or pass --allow-insecure-http for a local host."
            )
        self.api = f"{base_url.rstrip('/')}/wp-json/wp/v2"
        token = base64.b64encode(f"{user}:{password}".encode()).decode()
        self.auth = f"Basic {token}"

    def request(self, method: str, path: str, payload: dict | None = None) -> object:
        url = path if path.startswith("http") else f"{self.api}/{path.lstrip('/')}"
        body = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(url, data=body, method=method)
        req.add_header("Authorization", self.auth)
        req.add_header("Accept", "application/json")
        if body is not None:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:400]
            raise ImportError_(f"{method} {url} -> HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise ImportError_(f"{method} {url} -> {exc.reason}") from exc
        return json.loads(raw) if raw else None

    def find_by_slug(self, rest_base: str, slug: str) -> dict | None:
        query = urllib.parse.urlencode(
            {"slug": slug, "status": "any", "per_page": 1, "context": "edit"}
        )
        found = self.request("GET", f"{rest_base}?{query}")
        if isinstance(found, list) and found:
            return found[0]
        return None


# ---- Record -> post payload ----------------------------------------------


def post_title(record: dict) -> str:
    return str(record.get("preferred_name") or record.get("title") or record.get("slug") or "")


def post_content(record: dict) -> str:
    if record.get("type") == "post":
        return str(record.get("body") or "")
    return str(record.get("summary") or "")


def post_excerpt(record: dict) -> str:
    if record.get("type") == "post":
        return str(record.get("excerpt") or "")
    seo = record.get("seo") or {}
    return str(seo.get("description") or "") if isinstance(seo, dict) else ""


def build_meta(record: dict) -> dict:
    review = record.get("review") or {}
    seo = record.get("seo") or {}
    if not isinstance(review, dict):
        review = {}
    if not isinstance(seo, dict):
        seo = {}
    return {
        "record_status": str(record.get("status") or "draft"),
        "record_slug": str(record.get("slug") or ""),
        "evidence_tier": str(record.get("evidence_tier") or ""),
        "review_author": str(review.get("author") or ""),
        "review_reviewer": str(review.get("reviewer") or ""),
        "review_reviewer_credential": str(review.get("reviewer_credential") or ""),
        "reviewed_at": str(review.get("reviewed_at") or ""),
        "seo_title": str(seo.get("title") or ""),
        "seo_description": str(seo.get("description") or ""),
        "uniqueness_pct": record.get("uniqueness_pct") if isinstance(
            record.get("uniqueness_pct"), (int, float)
        ) and not isinstance(record.get("uniqueness_pct"), bool) else 0,
        "sources": record.get("sources") or [],
        "changelog": record.get("changelog") or [],
        "attributes_json": json.dumps(record.get("attributes") or {}, sort_keys=True),
    }


def build_payload(record: dict) -> dict:
    """The full post payload, minus the hash, which is added once it is known."""
    state = str(record.get("status") or "draft")
    return {
        "title": post_title(record),
        "slug": str(record.get("slug") or ""),
        "content": post_content(record),
        "excerpt": post_excerpt(record),
        # Only a fully published record becomes a published WordPress post.
        "status": "publish" if state == PUBLISHED_STATE else "draft",
        "meta": build_meta(record),
    }


def payload_hash(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()


# ---- Import ---------------------------------------------------------------


def import_record(client: Client, record: dict, path: pathlib.Path, dry_run: bool) -> str:
    rtype = record.get("type")
    rest_base = REST_BASE.get(str(rtype))
    if rest_base is None:
        raise ImportError_(f"unknown record type {rtype!r}")
    slug = str(record.get("slug") or "")
    if not slug:
        raise ImportError_("record has no slug")

    payload = build_payload(record)
    digest = payload_hash(payload)
    payload["meta"]["record_hash"] = digest

    if dry_run:
        return "would create or update"

    existing = client.find_by_slug(rest_base, slug)
    if existing is None:
        client.request("POST", rest_base, payload)
        return "created"

    post_id = existing.get("id")
    current = (existing.get("meta") or {}).get("record_hash")
    if current == digest:
        return "unchanged"
    client.request("POST", f"{rest_base}/{post_id}", payload)
    return "updated"


def collect_records(paths: list[str]) -> list[pathlib.Path]:
    """Every record file except the examples, which are templates, not content."""
    files = vc.collect(paths)
    return [f for f in files if f.parent.name != vc.EXAMPLES_DIR]


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="*", help="files or folders (default: data/)")
    parser.add_argument("--dry-run", action="store_true", help="plan only, write nothing")
    parser.add_argument(
        "--allow-insecure-http", action="store_true", help="permit a plain-http WP_URL"
    )
    args = parser.parse_args(argv)

    # The validator is the gate. Nothing reaches WordPress that CI would reject.
    report = vc.Report()
    for path in vc.collect(args.paths):
        vc.validate_record(path, report)
    if report.errors:
        print("VALIDATION FAILED, nothing imported")
        report.emit()
        return 1

    files = collect_records(args.paths)
    if not files:
        print("No records to import (data/examples/ is skipped by design).")
        return 0

    client = None
    if not args.dry_run:
        missing = [v for v in ("WP_URL", "WP_USER", "WP_APP_PASSWORD") if not os.environ.get(v)]
        if missing:
            print(f"Missing environment variables: {', '.join(missing)}")
            print("Set them, or use --dry-run to preview without connecting.")
            return 1
        client = Client(
            os.environ["WP_URL"],
            os.environ["WP_USER"],
            os.environ["WP_APP_PASSWORD"],
            args.allow_insecure_http,
        )

    tally: dict[str, int] = {}
    failures = 0
    for path in files:
        record = json.loads(path.read_text(encoding="utf-8"))
        rel = vc.display(path)
        try:
            outcome = import_record(client, record, path, args.dry_run)
        except ImportError_ as exc:
            failures += 1
            print(f"  FAILED    {rel}: {exc}")
            continue
        tally[outcome] = tally.get(outcome, 0) + 1
        print(f"  {outcome:9} {rel}")

    print()
    summary = ", ".join(f"{count} {name}" for name, count in sorted(tally.items()))
    print(f"{len(files)} records: {summary or 'none'}" + (f", {failures} failed" if failures else ""))
    if args.dry_run:
        print("Dry run: nothing was written.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
