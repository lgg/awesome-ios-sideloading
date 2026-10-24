#!/usr/bin/env python3
"""Validate the curated Markdown catalog (stdlib only, no CI required).

Usage:
    python3 scripts/validate_catalog.py
    python3 scripts/validate_catalog.py --online --max-online 100
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = ("README.md", "COMPATIBILITY.md", "RESEARCH_NOTES.md", "CONTRIBUTING.md")
LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^\s)]+)(?:\s+[^)]*)?\)")
HEADER = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
PROJECT = re.compile(r"^\s*-\s+\*\*\[[^\]]+\]\((https?://[^)]+)\)\*\*", re.MULTILINE)


def slugify(text: str) -> str:
    """Match common GitHub heading anchors for the headings used here."""
    text = re.sub(r"<[^>]*>", "", text).lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text.strip())


def anchors(document: str) -> set[str]:
    seen: Counter[str] = Counter()
    result: set[str] = set()
    for match in HEADER.finditer(document):
        value = slugify(match.group(1).replace("`", ""))
        suffix = seen[value]
        result.add(value if not suffix else f"{value}-{suffix}")
        seen[value] += 1
    return result


def verify_internal(path: Path, target: str, cache: dict[Path, str]) -> str | None:
    resolved_url = urllib.parse.unquote(target).split("#", 1)
    filename = resolved_url[0]
    fragment = resolved_url[1] if len(resolved_url) == 2 else ""
    resolved = (path.parent / filename).resolve() if filename else path
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        return f"relative link leaves repository: {target}"
    if not resolved.is_file():
        return f"missing local target: {target}"
    if fragment:
        if resolved.suffix.lower() != ".md":
            return None
        try:
            body = cache.setdefault(resolved, resolved.read_text(encoding="utf-8"))
        except UnicodeError:
            return f"cannot decode local target: {target}"
        if fragment not in anchors(body):
            return f"unknown Markdown heading: {target}"
    return None


def verify_online(url: str, timeout: float) -> tuple[bool, str]:
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(
            url,
            method=method,
            headers={"User-Agent": "awesome-ios-sideloading-link-check/1.0"},
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return True, f"HTTP {response.status}"
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in (403, 405, 429, 501):
                continue
            if exc.code in (401, 403, 429):
                return True, f"HTTP {exc.code} (manual review / rate limit)"
            return False, f"HTTP {exc.code}"
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            if method == "HEAD":
                continue
            return False, str(exc)
    return False, "no HTTP response"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", action="store_true", help="Check external links via HTTP")
    parser.add_argument("--timeout", type=float, default=8, help="Seconds per HTTP request")
    parser.add_argument(
        "--max-online",
        type=int,
        default=100,
        help="Maximum unique external links to inspect",
    )
    args = parser.parse_args()
    failures: list[str] = []
    warnings: list[str] = []
    cache: dict[Path, str] = {}
    external: set[str] = set()
    project_targets: list[str] = []
    total_links = 0

    for name in FILES:
        path = ROOT / name
        if not path.exists():
            failures.append(f"Required file missing: {name}")
            continue
        data = path.read_text(encoding="utf-8")
        cache[path] = data
        for match in LINK.finditer(data):
            target = match.group(2)
            total_links += 1
            lineno = data.count("\n", 0, match.start()) + 1
            if target.startswith(("https://", "http://")):
                external.add(target)
            elif target.startswith(("mailto:", "tel:")):
                continue
            else:
                problem = verify_internal(path, target, cache)
                if problem:
                    failures.append(f"{name}:{lineno}: {problem}")
        if name == "README.md":
            # Count actual catalog projects, not regional marketplace links or
            # discussion communities. Those are useful links but not tools.
            start_marker = "\n## Projects\n"
            end_marker = "\n## Region-specific marketplaces\n"
            if start_marker not in data or end_marker not in data:
                failures.append("README.md catalog section markers missing")
                catalog = ""
            else:
                catalog = data.split(start_marker, 1)[1].split(end_marker, 1)[0]
            project_targets = PROJECT.findall(catalog)
            duplicates = [
                name for name, count in Counter(project_targets).items() if count > 1
            ]
            for url in duplicates:
                failures.append(f"Duplicate primary project entry: {url}")
            if len(project_targets) < 20:
                failures.append("README.md should have at least 20 primary project entries")

    if args.online:
        unique = sorted(external)
        if len(unique) > args.max_online:
            warnings.append(
                f"Online check limited to first {args.max_online} of {len(unique)} URLs"
            )
        for url in unique[: args.max_online]:
            ok, note = verify_online(url, args.timeout)
            if not ok:
                failures.append(f"External link: {url}: {note}")
            elif "manual review" in note:
                warnings.append(f"{url}: {note}")
            time.sleep(0.1)

    for item in warnings:
        print(f"WARNING: {item}", file=sys.stderr)
    for item in failures:
        print(f"FAIL: {item}", file=sys.stderr)
    print(
        f"Checked {len(FILES)} documents, {len(project_targets)} project entries, "
        f"{total_links} Markdown links, {len(external)} distinct external URLs."
    )
    if failures:
        print(f"{len(failures)} validation issue(s).", file=sys.stderr)
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
