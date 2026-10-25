#!/usr/bin/env python3
"""Check the curated GitHub project links for archival, disappearance, and inactivity.

This checks repository metadata only. It does not download IPAs, inspect code, or
certify compatibility/security. 404/410 are 'missing'; network/auth/rate-limit
errors are 'unknown', not evidence of a deleted project.

Usage: python3 scripts/audit_github_projects.py --output-dir reports
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = re.compile(
    r"^\s*-\s+\*\*\[([^\]]+)\]\((https?://[^)]+)\)\*\*", re.MULTILINE
)
API = "https://api.github.com/repos/"


def projects(readme: str) -> list[tuple[str, str, str]]:
    """Return unique (name, owner, repo) entries from the primary catalog only."""
    start, end = "\n## Projects\n", "\n## Region-specific marketplaces\n"
    if start not in readme or end not in readme:
        raise ValueError("Required catalog section delimiters are missing")
    section = readme.split(start, 1)[1].split(end, 1)[0]
    found: dict[str, tuple[str, str, str]] = {}
    for name, url in CATALOG.findall(section):
        parsed = urllib.parse.urlparse(url)
        if parsed.hostname != "github.com" or parsed.username or parsed.password:
            continue
        pieces = [x for x in parsed.path.split("/") if x]
        if len(pieces) < 2:
            continue
        owner, repository = pieces[0], pieces[1].removesuffix(".git")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", owner):
            continue
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", repository):
            continue
        key = f"{owner}/{repository}".lower()
        found.setdefault(key, (name, owner, repository))
    return list(found.values())


def fetch_repository(owner: str, repository: str, token: str, timeout: float) -> dict:
    safe_owner = urllib.parse.quote(owner, safe="")
    safe_repo = urllib.parse.quote(repository, safe="")
    request = urllib.request.Request(
        API + safe_owner + "/" + safe_repo,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-ios-sideloading-upstream-audit",
            "X-GitHub-Api-Version": "2022-11-28",
            **({"Authorization": "Bearer " + token} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.load(response)
        if not isinstance(data, dict) or not data.get("full_name"):
            return {"status": "unknown", "reason": "Unexpected GitHub API response"}
        return {"status": "found", "data": data}
    except urllib.error.HTTPError as error:
        if error.code in (404, 410):
            return {"status": "missing", "reason": f"HTTP {error.code}"}
        return {"status": "unknown", "reason": f"HTTP {error.code}"}
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as error:
        return {"status": "unknown", "reason": type(error).__name__}


def assess(name: str, owner: str, repo: str, lookup: dict, now: dt.datetime, stale_days: int) -> dict:
    item = {
        "catalog_name": name,
        "catalog_repo": f"{owner}/{repo}",
        "status": lookup["status"],
    }
    if lookup["status"] != "found":
        item["reason"] = lookup.get("reason", "")
        return item

    data = lookup["data"]
    item["canonical_repo"] = data["full_name"]
    item["archived"] = bool(data.get("archived"))
    item["disabled"] = bool(data.get("disabled"))
    item["pushed_at"] = data.get("pushed_at")
    item["renamed_or_transferred"] = item["catalog_repo"].lower() != data["full_name"].lower()
    item["stale"] = False
    if item["pushed_at"]:
        try:
            pushed = dt.datetime.fromisoformat(item["pushed_at"].replace("Z", "+00:00"))
            item["stale"] = (now - pushed).days >= stale_days
        except ValueError:
            item["status"] = "unknown"
            item["reason"] = "Invalid pushed_at timestamp"
    return item


def render_markdown(items: list[dict], now: dt.datetime, stale_days: int) -> str:
    flagged = [
        x for x in items
        if x["status"] != "found"
        or x.get("archived")
        or x.get("disabled")
        or x.get("stale")
        or x.get("renamed_or_transferred")
    ]
    lines = [
        "# GitHub upstream metadata audit",
        "",
        f"Run: {now.strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"Projects checked: {len(items)}  ",
        f"Stale threshold: {stale_days} days without a push",
        "",
        "> Metadata check only: inactivity does not imply a broken project, and",
        "> a 200 response does not prove that a sideloader is safe or functional.",
        "> HTTP 403/429/timeouts are unknown, not missing.",
        "",
        "## Items for human review",
        "",
        "| Catalog entry | Result | Detail |",
        "| --- | --- | --- |",
    ]
    for x in flagged:
        flags = []
        if x.get("archived"):
            flags.append("archived")
        if x.get("disabled"):
            flags.append("disabled")
        if x.get("stale"):
            flags.append("inactive")
        if x.get("renamed_or_transferred"):
            flags.append("renamed/transferred")
        detail = ", ".join(flags) or x.get("reason", "check manually")
        if x.get("canonical_repo") and x.get("renamed_or_transferred"):
            detail += " — " + x["canonical_repo"]
        lines.append(f"| {x['catalog_name']} ({x['catalog_repo']}) | {x['status']} | {detail} |")
    if not flagged:
        lines.append("| None | — | No items flagged |")
    lines.append("")
    lines.append("No catalog entries were changed automatically.")
    return "\n".join(lines) + "\n"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output-dir", default="reports")
    p.add_argument("--stale-days", type=int, default=365)
    p.add_argument("--timeout", type=float, default=12)
    args = p.parse_args()
    if args.stale_days < 1 or args.timeout <= 0:
        p.error("stale-days and timeout must be positive")

    now = dt.datetime.now(dt.timezone.utc)
    items = []
    token = os.environ.get("GITHUB_TOKEN", "")
    try:
        upstreams = projects((ROOT / "README.md").read_text(encoding="utf-8"))
    except (ValueError, OSError) as error:
        print(f"Cannot read primary catalog: {error}", file=sys.stderr)
        return 2

    for name, owner, repo in upstreams:
        status = fetch_repository(owner, repo, token, args.timeout)
        items.append(assess(name, owner, repo, status, now, args.stale_days))

    destination = Path(args.output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "github-upstreams.json").write_text(
        json.dumps({"checked_at": now.isoformat(), "items": items}, indent=2) + "\n",
        encoding="utf-8",
    )
    report = render_markdown(items, now, args.stale_days)
    (destination / "github-upstreams.md").write_text(report, encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as output:
            output.write(report)
    flagged = sum(
        1 for x in items
        if x["status"] != "found" or x.get("archived") or x.get("disabled")
        or x.get("stale") or x.get("renamed_or_transferred")
    )
    print(f"Checked {len(items)} distinct GitHub upstreams; {flagged} need manual review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
