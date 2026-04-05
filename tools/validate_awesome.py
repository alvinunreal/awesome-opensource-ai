#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import unicodedata
import urllib.error
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
EMERGING_PATH = ROOT / "EMERGING.md"
GITHUB_API = "https://api.github.com/graphql"
ENTRY_RE = re.compile(
    r"\*\*\[(?P<label>[^\]]+)\]\((?P<url>https?://[^)]+)\)\*\*(?:\s+(?P<badge>!\[GitHub stars\]\(https://img\.shields\.io/github/stars/(?P<badge_repo>[^?)+]+)\?style=social\)))?"
)
SECTION_RE = re.compile(r"^###\s+(?P<title>.+)$")
SUBSECTION_RE = re.compile(r"^####\s+(?P<title>.+)$")
INLINE_ANCHOR_RE = re.compile(r'^<a\s+id="(?P<id>[^"]+)"\s*></a>$')
TOC_LINK_RE = re.compile(r"^- \[(?P<label>[^\]]+)\]\(#(?P<anchor>[^)]+)\)$")
GITHUB_REPO_URL_RE = re.compile(
    r"^https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/)?#]+)(?:[/?#].*)?$"
)
ALLOWED_BETWEEN_LINKS_RE = re.compile(r"^\s*(?:\+\s*)?$")
ALLOWED_TRAILING_META_RE = re.compile(r"^\s*(?:\([^)]*\)\s*)*$")


@dataclass(frozen=True)
class Problem:
    severity: str
    file: str
    line: int
    message: str


@dataclass(frozen=True)
class RepoRef:
    owner: str
    repo: str

    @property
    def full_name(self) -> str:
        return f"{self.owner}/{self.repo}"


@dataclass
class ParsedLink:
    label: str
    url: str
    badge_repo: str | None
    repo_ref: RepoRef | None


@dataclass
class ParsedEntry:
    file: Path
    line_number: int
    section: str | None
    raw: str
    description: str
    links: list[ParsedLink]


def github_anchor_slug(title: str) -> str:
    text = (
        unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    )
    text = text.lower()
    text = re.sub(r"[^a-z0-9\- ]", "", text)
    text = text.replace(" ", "-")
    return text


def parse_repo_ref(url: str) -> RepoRef | None:
    match = GITHUB_REPO_URL_RE.match(url.strip())
    if not match:
        return None
    return RepoRef(owner=match.group("owner"), repo=match.group("repo"))


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def parse_entries(path: Path) -> tuple[list[ParsedEntry], list[Problem]]:
    entries: list[ParsedEntry] = []
    problems: list[Problem] = []
    current_section: str | None = None

    for line_number, line in enumerate(read_lines(path), start=1):
        stripped = line.strip()
        section_match = SECTION_RE.match(stripped)
        if section_match:
            current_section = section_match.group("title")
            continue

        subsection_match = SUBSECTION_RE.match(stripped)
        if subsection_match:
            current_section = subsection_match.group("title")
            continue

        if not stripped.startswith("- ") or "**[" not in stripped:
            continue

        content = stripped[2:]
        matches = list(ENTRY_RE.finditer(content))
        if not matches:
            problems.append(
                Problem(
                    "error",
                    path.name,
                    line_number,
                    "entry link markup could not be parsed",
                )
            )
            continue

        description_index = content.find(" - ", matches[-1].end())
        if description_index == -1:
            problems.append(
                Problem(
                    "error",
                    path.name,
                    line_number,
                    "entry is missing ` - description` separator after project links",
                )
            )
            continue

        head = content[:description_index]
        description = content[description_index + 3 :]

        parsed_links: list[ParsedLink] = []
        if head[: matches[0].start()].strip():
            problems.append(
                Problem(
                    "error",
                    path.name,
                    line_number,
                    "entry contains unexpected text before the first project link",
                )
            )

        previous_end = 0
        for index, match in enumerate(matches):
            gap = head[previous_end : match.start()]
            if index > 0 and not ALLOWED_BETWEEN_LINKS_RE.fullmatch(gap):
                problems.append(
                    Problem(
                        "error",
                        path.name,
                        line_number,
                        "entry contains malformed text between project links",
                    )
                )

            repo_ref = parse_repo_ref(match.group("url"))
            parsed_links.append(
                ParsedLink(
                    label=match.group("label"),
                    url=match.group("url"),
                    badge_repo=match.group("badge_repo"),
                    repo_ref=repo_ref,
                )
            )

            if repo_ref and not match.group("badge"):
                problems.append(
                    Problem(
                        "error",
                        path.name,
                        line_number,
                        f"missing GitHub stars badge for {repo_ref.full_name}",
                    )
                )
            if (
                repo_ref
                and match.group("badge_repo")
                and match.group("badge_repo") != repo_ref.full_name
            ):
                problems.append(
                    Problem(
                        "error",
                        path.name,
                        line_number,
                        f"badge repo `{match.group('badge_repo')}` does not match link repo `{repo_ref.full_name}`",
                    )
                )
            previous_end = match.end()

        trailing_meta = head[previous_end:]
        if trailing_meta and not ALLOWED_TRAILING_META_RE.fullmatch(trailing_meta):
            problems.append(
                Problem(
                    "error",
                    path.name,
                    line_number,
                    "entry contains malformed markdown or unexpected text after project links",
                )
            )

        if not description.strip():
            problems.append(
                Problem("error", path.name, line_number, "entry description is empty")
            )

        entries.append(
            ParsedEntry(
                file=path,
                line_number=line_number,
                section=current_section,
                raw=line,
                description=description.strip(),
                links=parsed_links,
            )
        )

    return entries, problems


def validate_toc(path: Path) -> list[Problem]:
    problems: list[Problem] = []
    lines = read_lines(path)
    headings: set[str] = set()
    pending_anchor: str | None = None

    for line in lines:
        stripped = line.strip()
        anchor_match = INLINE_ANCHOR_RE.match(stripped)
        if anchor_match:
            pending_anchor = anchor_match.group("id")
            continue

        section_match = SECTION_RE.match(stripped)
        if section_match:
            headings.add(github_anchor_slug(section_match.group("title")))
            if pending_anchor:
                headings.add(pending_anchor)
                pending_anchor = None

    for line_number, line in enumerate(lines, start=1):
        match = TOC_LINK_RE.match(line.strip())
        if not match:
            continue
        anchor = match.group("anchor")
        if anchor not in headings:
            problems.append(
                Problem(
                    "error",
                    path.name,
                    line_number,
                    f"TOC anchor `#{anchor}` does not match any section anchor",
                )
            )

    return problems


def validate_duplicates(entries: list[ParsedEntry]) -> list[Problem]:
    problems: list[Problem] = []
    repos: dict[tuple[str, str, str], list[ParsedEntry]] = defaultdict(list)
    raws: dict[tuple[str, str, str], list[ParsedEntry]] = defaultdict(list)

    for entry in entries:
        section = entry.section or "(unknown section)"
        raws[(entry.file.name, section, entry.raw.strip())].append(entry)
        for link in entry.links:
            if link.repo_ref:
                repos[
                    (entry.file.name, section, link.repo_ref.full_name.lower())
                ].append(entry)

    for (file_name, section, repo_name), repo_entries in sorted(repos.items()):
        if len(repo_entries) <= 1:
            continue
        refs = ", ".join(
            f"{entry.file.name}:{entry.line_number}" for entry in repo_entries
        )
        first = repo_entries[0]
        problems.append(
            Problem(
                "warning",
                file_name,
                first.line_number,
                f"repo `{repo_name}` appears multiple times in `{section}` ({refs})",
            )
        )

    for (file_name, section, raw_line), raw_entries in sorted(raws.items()):
        if len(raw_entries) <= 1:
            continue
        refs = ", ".join(
            f"{entry.file.name}:{entry.line_number}" for entry in raw_entries
        )
        first = raw_entries[0]
        problems.append(
            Problem(
                "warning",
                file_name,
                first.line_number,
                f"identical entry appears multiple times in `{section}` ({refs})",
            )
        )

    return problems


def collect_repos(entries: list[ParsedEntry]) -> list[RepoRef]:
    seen: dict[str, RepoRef] = {}
    for entry in entries:
        for link in entry.links:
            if link.repo_ref:
                seen.setdefault(link.repo_ref.full_name.lower(), link.repo_ref)
    return list(seen.values())


def graphql_literal(value: str) -> str:
    return json.dumps(value)


def fetch_repo_metadata(
    repos: list[RepoRef], token: str
) -> tuple[dict[str, dict], list[str]]:
    metadata: dict[str, dict] = {}
    failures: list[str] = []
    batch_size = 20

    for batch_start in range(0, len(repos), batch_size):
        batch = repos[batch_start : batch_start + batch_size]
        query_parts = ["query RepoBatch {"]
        alias_map: dict[str, RepoRef] = {}
        for index, repo in enumerate(batch):
            alias = f"r{index}"
            alias_map[alias] = repo
            query_parts.append(
                f"{alias}: repository(owner: {graphql_literal(repo.owner)}, name: {graphql_literal(repo.repo)}) "
                "{ nameWithOwner stargazerCount pushedAt isArchived isDisabled url licenseInfo { spdxId } }"
            )
        query_parts.append("}")
        payload = json.dumps({"query": "\n".join(query_parts)}).encode("utf-8")
        request = urllib.request.Request(
            GITHUB_API,
            data=payload,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Accept": "application/vnd.github+json",
                "User-Agent": "awesome-open-source-ai-validator",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(request) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            failures.append(f"GitHub API request failed with HTTP {exc.code}")
            continue
        except urllib.error.URLError as exc:
            failures.append(f"GitHub API request failed: {exc.reason}")
            continue

        for error in body.get("errors", []):
            failures.append(error.get("message", "unknown GitHub API error"))

        data = body.get("data", {})
        for alias, repo in alias_map.items():
            metadata[repo.full_name.lower()] = data.get(alias)

    return metadata, failures


def validate_remote_requirements(
    entries: list[ParsedEntry],
    metadata: dict[str, dict],
    *,
    min_stars: int | None,
    max_stars: int | None,
    require_recent_push_days: int | None,
) -> list[Problem]:
    problems: list[Problem] = []
    entry_by_repo: dict[str, list[ParsedEntry]] = defaultdict(list)
    for entry in entries:
        for link in entry.links:
            if link.repo_ref:
                entry_by_repo[link.repo_ref.full_name.lower()].append(entry)

    now = dt.datetime.now(dt.timezone.utc)
    for repo_name, repo_entries in entry_by_repo.items():
        info = metadata.get(repo_name)
        first_entry = repo_entries[0]
        if info is None:
            problems.append(
                Problem(
                    "error",
                    first_entry.file.name,
                    first_entry.line_number,
                    f"GitHub repo `{repo_name}` was not returned by the API",
                )
            )
            continue
        if not info:
            problems.append(
                Problem(
                    "error",
                    first_entry.file.name,
                    first_entry.line_number,
                    f"GitHub repo `{repo_name}` was not found",
                )
            )
            continue

        stars = info.get("stargazerCount")
        pushed_at = info.get("pushedAt")
        is_archived = bool(info.get("isArchived"))
        is_disabled = bool(info.get("isDisabled"))

        if isinstance(stars, int):
            if min_stars is not None and stars < min_stars:
                problems.append(
                    Problem(
                        "error",
                        first_entry.file.name,
                        first_entry.line_number,
                        f"repo `{repo_name}` has {stars} stars, below required minimum of {min_stars}",
                    )
                )
            if max_stars is not None and stars >= max_stars:
                problems.append(
                    Problem(
                        "error",
                        first_entry.file.name,
                        first_entry.line_number,
                        f"repo `{repo_name}` has {stars} stars, expected fewer than {max_stars}",
                    )
                )

        if pushed_at and require_recent_push_days is not None:
            pushed = dt.datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
            age_days = (now - pushed).days
            if age_days > require_recent_push_days:
                problems.append(
                    Problem(
                        "error",
                        first_entry.file.name,
                        first_entry.line_number,
                        f"repo `{repo_name}` was last pushed {age_days} days ago, over {require_recent_push_days}-day limit",
                    )
                )

        if is_archived:
            problems.append(
                Problem(
                    "warning",
                    first_entry.file.name,
                    first_entry.line_number,
                    f"repo `{repo_name}` is archived",
                )
            )
        if is_disabled:
            problems.append(
                Problem(
                    "warning",
                    first_entry.file.name,
                    first_entry.line_number,
                    f"repo `{repo_name}` is disabled",
                )
            )

    return problems


def print_report(title: str, problems: list[Problem]) -> None:
    print(f"\n== {title} ==")
    if not problems:
        print("ok")
        return
    for problem in sorted(
        problems,
        key=lambda item: (item.severity != "error", item.file, item.line, item.message),
    ):
        print(
            f"{problem.severity.upper():7} {problem.file}:{problem.line} {problem.message}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Awesome Open Source AI structure and GitHub thresholds."
    )
    parser.add_argument(
        "--skip-remote",
        action="store_true",
        help="skip GitHub API validation even if GITHUB_TOKEN is set",
    )
    args = parser.parse_args()

    readme_entries, readme_entry_problems = parse_entries(README_PATH)
    emerging_entries, emerging_entry_problems = parse_entries(EMERGING_PATH)

    structure_problems = [
        *validate_toc(README_PATH),
        *validate_toc(EMERGING_PATH),
        *readme_entry_problems,
        *emerging_entry_problems,
        *validate_duplicates(readme_entries + emerging_entries),
    ]

    remote_problems: list[Problem] = []
    remote_notes: list[str] = []
    token = os.environ.get("GITHUB_TOKEN")
    if args.skip_remote:
        remote_notes.append("remote validation skipped via --skip-remote")
    elif not token:
        remote_notes.append(
            "set GITHUB_TOKEN to validate star count and last-push thresholds via GitHub GraphQL API"
        )
    else:
        readme_repos = collect_repos(readme_entries)
        emerging_repos = collect_repos(emerging_entries)
        metadata, api_failures = fetch_repo_metadata(
            readme_repos + emerging_repos, token
        )
        remote_notes.extend(api_failures)
        remote_problems.extend(
            validate_remote_requirements(
                readme_entries,
                metadata,
                min_stars=1000,
                max_stars=None,
                require_recent_push_days=183,
            )
        )
        remote_problems.extend(
            validate_remote_requirements(
                emerging_entries,
                metadata,
                min_stars=None,
                max_stars=1000,
                require_recent_push_days=183,
            )
        )

    print_report("Structural checks", structure_problems)
    print_report("Remote GitHub checks", remote_problems)
    if remote_notes:
        print("\n== Notes ==")
        for note in remote_notes:
            print(f"- {note}")

    error_count = sum(
        problem.severity == "error" for problem in structure_problems + remote_problems
    )
    warning_count = sum(
        problem.severity == "warning"
        for problem in structure_problems + remote_problems
    )
    print(f"\nSummary: {error_count} error(s), {warning_count} warning(s)")
    return 1 if error_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
