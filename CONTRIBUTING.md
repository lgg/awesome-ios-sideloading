# Contributing to Awesome iOS Sideloading

Thank you for helping keep this list useful and trustworthy! Contributions are welcome for missing projects, corrections, broken links, changed requirements, and removals.

## Automated upstream health checks

The [weekly GitHub metadata audit](.github/workflows/upstream-audit.yml) checks **primary GitHub repository entries only**, using a read-only `GITHUB_TOKEN`. Its downloadable `github-upstream-report` artifact (JSON and Markdown, retained for 14 days) flags archived, disabled, renamed/transferred, missing and **365-day inactive** projects.

To run the same metadata review manually: `python3 scripts/audit_github_projects.py --output-dir reports`. To test the logic **offline**: `python3 -m unittest discover -s tests -p 'test_audit_github_projects.py' -v`. It can also be triggered via GitHub Actions → **Audit GitHub project metadata** → Run workflow.

**Do not automatically delete flagged projects.** Inactivity can be normal for stable software; HTTP 403/429, timeouts and GitHub API restrictions are **unknown**, not evidence that a project vanished. For moved repositories, update the canonical URL only after confirming the legitimate maintainer. The audit is not an IPA malware scan, link verification for all external websites, device test or endorsement of third-party signing services.

## What belongs here

A project should have a direct, meaningful role in at least one of these workflows:

- Installing, signing, refreshing, or managing apps outside the traditional App Store.
- Building/running a self-hosted signing or AltServer-compatible backend.
- Generating device pairing files or supporting modern iOS developer connections used by sideloading tools.
- Enabling JIT for sideloaded apps.
- Creating, validating, or browsing AltStore-compatible sources.
- Providing first-party documentation or a useful companion tool.

A great entry is **publicly discoverable**, has a **canonical maintainer URL**, explains its function, and discloses important restrictions.

Projects **do not need to be open source** (they must be clearly identified as proprietary where relevant).

## What does not belong here

- Collections of pirated apps, stolen signing certificates, cracked paid IPAs, or redistributed software without permission.
- Mirrors, impersonating repositories, or copycat download sites claiming to be official.
- Generic jailbreak tweak collections with no clear sideloading relevance.
- One-off support questions or unverified claims about "unlimited" signing.
- Link farms and referral-only signing/certificate storefronts.
- Archived or unmaintained projects masquerading as current solutions; historically important tools may be added in a clearly labeled legacy section if relevant.

## Submit or update an entry

1. **Search** the README and existing issues/PRs first. Avoid duplicates and list the upstream repository rather than an arbitrary fork.
2. Confirm that the URL opens, the project actually performs its stated function, and the maintainer controls that source.
3. Check recent releases, commits, issues and the current README. A recent commit is evidence of activity, **not proof** of iOS compatibility.
4. Add the link in the most relevant category, alphabetically by project name where practical. Format:
   `- **[Project](https://github.com/owner/repo)** — One-sentence description with the main distinguishing feature or requirement.`
5. If installation prerequisites, iOS ranges, signing, renewal, or JIT compatibility changes, update **[COMPATIBILITY.md](COMPATIBILITY.md)** as well.
6. For significant research, removals, disputed claims, or candidate decisions, update **[RESEARCH_NOTES.md](RESEARCH_NOTES.md)** with first-party evidence and a review date.
7. Check relative links and run the local validator (described below).
8. In the PR description, tell us what changed, why it belongs, and where the claims come from.

### Evidence checklist

Include when applicable:

- Canonical repository or maintainer's official website.
- Supported **platform(s)**: iOS, iPadOS, tvOS; Windows/macOS/Linux/on-device/server.
- **iOS version** and device architecture requirements.
- Whether a **computer** is needed for setup, renewal, or all operations.
- **Signing model**: free Apple Account, paid developer account, .p12 certificate, TrollStore/exploit, or region-specific marketplace.
- Expiration/automatic refresh behavior, device VPN or pairing-file prerequisites, and other meaningful limitations.
- Link to documentation, release notes, or a concrete test; identify any assertion that is **not independently verified**.
- Maintenance/experimental/archived status if uncertain.

**Do not include private Apple ID, pairing records, signing certificates, device IDs, passwords, or authorization tokens in issues or PRs.**

## Writing style

- Write in clear, neutral English.
- Keep the README skim-friendly: short link descriptions, not marketing copy.
- Avoid star counts, unsupported “best” claims, affiliate promotions, and stale version numbers in descriptions.
- Do not add decorative feature badge soups or a giant matrix to the README. Detailed compatibility belongs in `COMPATIBILITY.md`.
- Avoid presenting proprietary Apple-authorized marketplace distribution as equivalent to unrestricted IPA sideloading.
- Prefer authoritative first-party citations for compatibility claims.
- When deleting a dead entry, explain the status of the canonical project first.

## Local validation

From the repository root:

```bash
python3 scripts/validate_catalog.py
```

The stdlib-only script checks internal relative links, duplicate project targets, section formatting, and basic Markdown structure. GitHub Actions also runs this check on relevant pull requests and pushes to `master` via [catalog-validation.yml](.github/workflows/catalog-validation.yml). For optional live HTTP checks, use:

```bash
python3 scripts/validate_catalog.py --online
```

Online checks require network access and can report false positives for anti-bot protection or rate limits; confirm failures manually before deleting links. No GitHub Actions minutes are required to run locally.

## Pull requests

Keep PRs focused, preferably on one project or a group of related corrections. Link sources for changing version/support claims. Maintainers may decline unsafe links or reorganize an entry to avoid duplication.

Thanks for keeping the catalog accurate and useful.
