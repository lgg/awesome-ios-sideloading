#!/usr/bin/env python3
"""Offline tests for the GitHub upstream audit. No network or tokens required."""

import datetime as dt
import importlib.util
import io
import json
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

FILE = Path(__file__).resolve().parents[1] / "scripts" / "audit_github_projects.py"
spec = importlib.util.spec_from_file_location("upstream_audit", FILE)
audit = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = audit
spec.loader.exec_module(audit)
NOW = dt.datetime(2026, 10, 25, tzinfo=dt.timezone.utc)


class UpstreamAuditTests(unittest.TestCase):
    def test_catalog_scope_and_deduplicate_case_insensitive(self):
        readme = """
# Title
[External](https://github.com/ignored/outside)
## Projects
### Tools
- **[Alpha](https://github.com/Example/Repo)** — Test
- **[Alpha duplicate](https://github.com/example/repo)** — Test
- **[Deep](https://github.com/example/another/tree/main)** — Test
- **[Outside](https://example.com/not-github)** — Test
## Region-specific marketplaces
- **[Other](https://github.com/ignored/region)** — Test
"""
        self.assertEqual(
            audit.projects(readme),
            [("Alpha", "Example", "Repo"), ("Deep", "example", "another")],
        )

    def test_missing_catalog_markers_is_error(self):
        with self.assertRaises(ValueError):
            audit.projects("# nothing here")

    def test_assess_archived_renamed_and_stale(self):
        data = {
            "status": "found",
            "data": {
                "full_name": "new-org/repo",
                "archived": True,
                "disabled": False,
                "pushed_at": "2025-01-01T00:00:00Z",
            },
        }
        item = audit.assess("Example", "old-org", "repo", data, NOW, 365)
        self.assertTrue(item["archived"])
        self.assertTrue(item["stale"])
        self.assertTrue(item["renamed_or_transferred"])
        self.assertEqual(item["status"], "found")

    def test_assess_recent_project_is_not_stale(self):
        data = {
            "status": "found",
            "data": {
                "full_name": "owner/repo",
                "archived": False,
                "disabled": False,
                "pushed_at": "2026-10-24T10:00:00Z",
            },
        }
        item = audit.assess("Example", "owner", "repo", data, NOW, 365)
        self.assertFalse(item["stale"])
        self.assertFalse(item["renamed_or_transferred"])

    def test_http_404_distinct_from_rate_limit(self):
        def raise_code(code):
            raise urllib.error.HTTPError(
                "https://api.github.com/repos/test/test", code, "failure", {}, None
            )
        with patch.object(audit.urllib.request, "urlopen", side_effect=lambda *a, **kw: raise_code(404)):
            missing = audit.fetch_repository("test", "test", "", 1)
        with patch.object(audit.urllib.request, "urlopen", side_effect=lambda *a, **kw: raise_code(429)):
            rate_limited = audit.fetch_repository("test", "test", "", 1)
        self.assertEqual(missing["status"], "missing")
        self.assertEqual(rate_limited["status"], "unknown")

    def test_api_json_is_recognized(self):
        payload = io.BytesIO(json.dumps({
            "full_name": "owner/repo", "archived": False, "pushed_at": "2026-10-01T00:00:00Z"
        }).encode())
        class Response:
            def __enter__(self): return payload
            def __exit__(self, *args): return False
        with patch.object(audit.urllib.request, "urlopen", return_value=Response()):
            result = audit.fetch_repository("owner", "repo", "fake", 1)
        self.assertEqual(result["status"], "found")
        self.assertEqual(result["data"]["full_name"], "owner/repo")

    def test_report_does_not_claim_auto_removals(self):
        report = audit.render_markdown(
            [{"catalog_name": "A", "catalog_repo": "x/y", "status": "unknown", "reason": "HTTP 429"}],
            NOW, 365,
        )
        self.assertIn("unknown", report)
        self.assertIn("No catalog entries were changed automatically", report)


if __name__ == "__main__":
    unittest.main()
