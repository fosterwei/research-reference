"""Notify IndexNow about sitemap changes after a successful production deploy."""

import argparse
import json
import os
import re
import subprocess
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

ORIGIN = "https://www.dashnaiv.com"
HOST = urlsplit(ORIGIN).netloc
ENDPOINT = "https://api.indexnow.org/indexnow"
ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "research/lastmod.json"


def read_url(url):
    with urlopen(Request(url, headers={"Cache-Control": "no-cache"}), timeout=15) as response:
        if response.geturl() != url or response.status != 200:
            raise ValueError("Expected a direct HTTP 200 from the production host.")
        return response.read()


def sitemap():
    xml = ET.fromstring(read_url(f"{ORIGIN}/sitemap.xml"))
    return {
        item.findtext("{*}loc"): item.findtext("{*}lastmod")
        for item in xml.findall("{*}url")
    }


def hosted_key():
    keys = [(file, file.stem) for file in (ROOT / "public").glob("*.txt")
            if re.fullmatch(r"[A-Za-z0-9-]{8,128}", file.stem)
            and file.read_text(encoding="utf-8") == file.stem]
    if len(keys) != 1:
        raise ValueError("Expected one IndexNow key file in public/.")
    _, key = keys[0]
    location = f"{ORIGIN}/{key}.txt"
    if read_url(location).decode("utf-8") != key:
        raise ValueError("Production key file does not match the deployed key.")
    return key, location


def submit(urls):
    if not urls:
        print("No indexable URLs changed.")
        return
    key, location = hosted_key()
    for start in range(0, len(urls), 10_000):
        data = json.dumps({
            "host": HOST, "key": key, "keyLocation": location,
            "urlList": urls[start:start + 10_000],
        }).encode("utf-8")
        request = Request(ENDPOINT, data=data, headers={"Content-Type": "application/json; charset=utf-8"})
        with urlopen(request, timeout=20) as response:
            if response.status not in (200, 202):
                raise ValueError(f"Unexpected IndexNow response: HTTP {response.status}")
            print(f"IndexNow HTTP {response.status} for {min(10_000, len(urls) - start)} URLs.")


def github_api(path):
    repo = os.environ["GITHUB_REPOSITORY"]
    return json.loads(subprocess.check_output(["gh", "api", f"repos/{repo}/{path}"]))


def manifest(revision):
    data = subprocess.check_output(["git", "show", f"{revision}:{MANIFEST}"], cwd=ROOT)
    pages = json.loads(data)["pages"]
    return {urljoin(ORIGIN, path): entry for path, entry in pages.items()}


def deployment_urls():
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
    current = event["deployment"]
    deployments = github_api("deployments?environment=Production&per_page=100")
    baseline = None
    for deploy in sorted(deployments, key=lambda deploy: deploy["id"], reverse=True):
        if deploy["id"] == current["id"] or deploy["creator"]["login"] != "vercel[bot]":
            continue
        statuses = github_api(f"deployments/{deploy['id']}/statuses")
        if not any(status["state"] == "success" for status in statuses):
            continue
        if deploy["id"] > current["id"]:
            print("A newer production deployment already succeeded.")
            return []
        baseline = deploy["sha"]
        break
    if baseline is None:
        print("First successful production deployment establishes the IndexNow baseline.")
        return []

    previous, latest = manifest(baseline), manifest(current["sha"])
    changes = {url: latest[url]["lastmod"] if url in latest else None
               for url in previous.keys() | latest.keys()
               if previous.get(url) != latest.get(url)}
    if not changes:
        return []
    for attempt in range(4):
        live = sitemap()
        if all((url not in live if date is None else live.get(url) == date)
               for url, date in changes.items()):
            return sorted(changes)
        if attempt < 3:
            time.sleep(5)
    raise ValueError("The public sitemap does not match the deployment's URL changes.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--verify-only", action="store_true")
    mode.add_argument("--deployment", action="store_true")
    mode.add_argument("--urls", nargs="+")
    args = parser.parse_args()
    if args.verify_only:
        hosted_key()
        print("Verified the IndexNow key on production (HTTP 200).")
    elif args.deployment:
        submit(deployment_urls())
    else:
        live = sitemap()
        if any(url not in live for url in args.urls):
            parser.error("Explicit submissions must be canonical URLs in the production sitemap.")
        submit(list(dict.fromkeys(args.urls)))


if __name__ == "__main__":
    main()
