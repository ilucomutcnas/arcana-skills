#!/usr/bin/env python3
"""
Validate Arcana skill package structure, content depth, routing integrity, assets,
and English-only user-facing package documentation.

This script is intentionally dependency-free so it can run in local shells,
Codex tasks, and GitHub Actions without installing extra packages.

Default mode is report-only to support the initial repository cleanup phase.
Use --strict to fail on structural errors.
Use --fail-on-warning to also fail on quality warnings.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_POLICY_PATH = REPO_ROOT / "validation" / "skill_validation_policy.json"

IGNORED_ROOT_DIRS = {
    ".git",
    ".github",
    ".vscode",
    ".idea",
    "node_modules",
    "dist",
    "build",
    "coverage",
    "__pycache__",
    "docs",
    "scripts",
    "tests",
    "validation",
}

CORE_PACKAGE_FILES = [
    "SKILL.md",
    "composition-protocol.md",
    "self-diagnostic-protocol.md",
    "resources/manifest.json",
    "resources/skill-catalog.md",
    "resources/routing-guide.md",
    "resources/asset-link-index.md",
]

REQUIRED_PACKAGE_DIRS = [
    "references/skills",
    "examples/skills",
]

USER_FACING_DIR_PARTS = {
    "resources",
    "references",
    "examples",
    "shared-rules",
}

USER_FACING_SUFFIXES = (
    "__resources",
    "__references",
)

TEXT_EXTENSIONS = {".md", ".json", ".txt", ".yml", ".yaml"}
BINARY_EXTENSIONS = {
    ".ttf",
    ".otf",
    ".woff",
    ".woff2",
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",
    ".zip",
    ".gz",
    ".tar",
    ".rar",
    ".7z",
    ".bin",
    ".exe",
    ".dll",
    ".dmg",
    ".mp4",
    ".mov",
    ".mp3",
    ".wav",
}

PLACEHOLDER_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"<[^>\n]+>",
    r"\{\{[^}\n]+\}\}",
    r"\bplaceholder\b",
    r"\bfill this in\b",
    r"\bcoming soon\b",
    r"\btemplate\b",
]

SECRET_PATTERNS = [
    r"(?i)\b(api[_-]?key|secret|token|password|private[_-]?key)\b\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}",
    r"sk-[A-Za-z0-9]{20,}",
    r"ghp_[A-Za-z0-9]{20,}",
    r"github_pat_[A-Za-z0-9_]{20,}",
    r"xox[baprs]-[A-Za-z0-9-]{20,}",
]

NON_ENGLISH_BLOCKS = [
    ("Cyrillic", r"[\u0400-\u04FF]"),
    ("Arabic", r"[\u0600-\u06FF]"),
    ("Hebrew", r"[\u0590-\u05FF]"),
    ("CJK", r"[\u4E00-\u9FFF]"),
    ("Hiragana", r"[\u3040-\u309F]"),
    ("Katakana", r"[\u30A0-\u30FF]"),
    ("Hangul", r"[\uAC00-\uD7AF]"),
    ("Thai", r"[\u0E00-\u0E7F]"),
    ("Devanagari", r"[\u0900-\u097F]"),
]


@dataclass
class Finding:
    severity: str
    code: str
    path: str
    message: str
    package: str | None = None
    domain: str | None = None


@dataclass
class PackageReport:
    domain: str
    slug: str
    path: str
    status: str
    maturity_candidate: str
    mini_skill_count: int
    user_facing_word_count: int
    has_scripts: bool
    has_assets: bool
    has_binary_assets: bool
    errors: int
    warnings: int
    score: int


def load_policy(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {
            "minimums": {
                "package_user_facing_words": 1200,
                "skill_reference_words": 180,
                "skill_example_words": 80,
                "mini_skills_per_professional_package": 6,
            },
            "allowed_statuses": ["draft", "usable", "ready", "deprecated", "needs-review"],
            "allowed_maturity": ["professional", "working", "amateur"],
            "report_only_ci": True,
        }
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def normalize_rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def is_probable_domain_dir(path: Path) -> bool:
    if not path.is_dir():
        return False
    if path.name in IGNORED_ROOT_DIRS:
        return False
    if path.name.startswith("."):
        return False
    return any(child.is_dir() for child in path.iterdir())


def is_probable_package_dir(path: Path) -> bool:
    if not path.is_dir():
        return False

    markers = [
        path / "SKILL.md",
        path / "SKILL.me",
        path / "composition-protocol.md",
        path / "self-diagnostic-protocol.md",
        path / "resources" / "manifest.json",
        path / "references" / "skills",
        path / "examples" / "skills",
    ]
    return any(marker.exists() for marker in markers)


def discover_packages(root: Path, package_filter: str | None = None) -> list[Path]:
    packages: list[Path] = []

    if package_filter:
        package_path = (root / package_filter).resolve()
        if not package_path.exists():
            raise SystemExit(f"Package path not found: {package_filter}")
        if not is_probable_package_dir(package_path):
            raise SystemExit(f"Path does not look like a skill package: {package_filter}")
        return [package_path]

    for domain_dir in sorted(root.iterdir()):
        if not is_probable_domain_dir(domain_dir):
            continue
        for candidate in sorted(domain_dir.iterdir()):
            if is_probable_package_dir(candidate):
                packages.append(candidate)

    return packages


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ""


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*", text))


def is_user_facing_text_file(path: Path, package_root: Path) -> bool:
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return False

    rel_parts = path.relative_to(package_root).parts
    if not rel_parts:
        return False

    if rel_parts[0] in {"SKILL.md", "composition-protocol.md", "self-diagnostic-protocol.md"}:
        return True

    if any(part in USER_FACING_DIR_PARTS for part in rel_parts):
        return True

    if any(part.endswith(USER_FACING_SUFFIXES) for part in rel_parts):
        return True

    return False


def iter_user_facing_files(package_root: Path) -> Iterable[Path]:
    for path in package_root.rglob("*"):
        if path.is_file() and is_user_facing_text_file(path, package_root):
            yield path


def iter_all_text_files(package_root: Path) -> Iterable[Path]:
    for path in package_root.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            yield path


def iter_binary_assets(package_root: Path) -> Iterable[Path]:
    for path in package_root.rglob("*"):
        if path.is_file() and path.suffix.lower() in BINARY_EXTENSIONS:
            yield path


def add_finding(findings: list[Finding], severity: str, code: str, path: Path | str, message: str, package_root: Path | None = None) -> None:
    rel_path = normalize_rel(path if isinstance(path, Path) else REPO_ROOT / path)
    package_rel = normalize_rel(package_root) if package_root else None
    domain = package_root.relative_to(REPO_ROOT).parts[0] if package_root and len(package_root.relative_to(REPO_ROOT).parts) >= 1 else None
    findings.append(
        Finding(
            severity=severity,
            code=code,
            path=rel_path,
            message=message,
            package=package_rel,
            domain=domain,
        )
    )


def validate_core_structure(package_root: Path, findings: list[Finding]) -> None:
    if (package_root / "SKILL.me").exists():
        add_finding(
            findings,
            "error",
            "wrong-skill-extension",
            package_root / "SKILL.me",
            "Package has SKILL.me. Rename it to SKILL.md so skill discovery works.",
            package_root,
        )

    for rel in CORE_PACKAGE_FILES:
        file_path = package_root / rel
        if not file_path.exists():
            add_finding(
                findings,
                "error",
                "missing-core-file",
                file_path,
                f"Missing required package file: {rel}",
                package_root,
            )
            continue
        if file_path.is_file() and file_path.stat().st_size == 0:
            add_finding(
                findings,
                "error",
                "empty-core-file",
                file_path,
                f"Required package file is empty: {rel}",
                package_root,
            )

    for rel in REQUIRED_PACKAGE_DIRS:
        dir_path = package_root / rel
        if not dir_path.exists() or not dir_path.is_dir():
            add_finding(
                findings,
                "error",
                "missing-core-directory",
                dir_path,
                f"Missing required package directory: {rel}",
                package_root,
            )


def validate_manifest(package_root: Path, findings: list[Finding], policy: dict[str, Any]) -> int:
    manifest_path = package_root / "resources" / "manifest.json"
    if not manifest_path.exists():
        return 0

    try:
        manifest = json.loads(read_text(manifest_path))
    except json.JSONDecodeError as exc:
        add_finding(
            findings,
            "error",
            "invalid-manifest-json",
            manifest_path,
            f"Manifest JSON is invalid: {exc}",
            package_root,
        )
        return 0

    if not isinstance(manifest, list):
        add_finding(
            findings,
            "error",
            "invalid-manifest-shape",
            manifest_path,
            "Manifest must be a list of mini-skill records.",
            package_root,
        )
        return 0

    seen_slugs: set[str] = set()
    for index, item in enumerate(manifest):
        item_path = f"{normalize_rel(manifest_path)}[{index}]"
        if not isinstance(item, dict):
            add_finding(findings, "error", "invalid-manifest-item", item_path, "Manifest item must be an object.", package_root)
            continue

        for field in ["title", "slug", "purpose", "when", "reference", "examples"]:
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                add_finding(findings, "error", "missing-manifest-field", item_path, f"Manifest item is missing required field: {field}", package_root)

        slug = item.get("slug")
        if isinstance(slug, str):
            if slug in seen_slugs:
                add_finding(findings, "error", "duplicate-manifest-slug", item_path, f"Duplicate manifest slug: {slug}", package_root)
            seen_slugs.add(slug)

        for field in ["reference", "examples"]:
            value = item.get(field)
            if isinstance(value, str) and value.strip():
                target = package_root / value
                if not target.exists():
                    add_finding(
                        findings,
                        "error",
                        "broken-manifest-link",
                        target,
                        f"Manifest field '{field}' points to a missing file: {value}",
                        package_root,
                    )

    reference_files = sorted((package_root / "references" / "skills").glob("*.md")) if (package_root / "references" / "skills").exists() else []
    example_files = sorted((package_root / "examples" / "skills").glob("*.md")) if (package_root / "examples" / "skills").exists() else []

    manifest_refs = {str(item.get("reference")) for item in manifest if isinstance(item, dict)}
    manifest_examples = {str(item.get("examples")) for item in manifest if isinstance(item, dict)}

    for ref in reference_files:
        rel = ref.relative_to(package_root).as_posix()
        if rel not in manifest_refs:
            add_finding(findings, "warning", "unlisted-reference", ref, "Reference file exists but is not listed in manifest.", package_root)

    for example in example_files:
        rel = example.relative_to(package_root).as_posix()
        if rel not in manifest_examples:
            add_finding(findings, "warning", "unlisted-example", example, "Example file exists but is not listed in manifest.", package_root)

    min_ref_words = int(policy["minimums"].get("skill_reference_words", 180))
    min_example_words = int(policy["minimums"].get("skill_example_words", 80))

    for ref in reference_files:
        count = word_count(read_text(ref))
        if count < min_ref_words:
            add_finding(
                findings,
                "warning",
                "thin-reference",
                ref,
                f"Reference file has {count} words; expected at least {min_ref_words}.",
                package_root,
            )

    for example in example_files:
        count = word_count(read_text(example))
        if count < min_example_words:
            add_finding(
                findings,
                "warning",
                "thin-example",
                example,
                f"Example file has {count} words; expected at least {min_example_words}.",
                package_root,
            )

    return len(manifest)


def validate_content_quality(package_root: Path, findings: list[Finding], policy: dict[str, Any]) -> int:
    total_words = 0
    min_package_words = int(policy["minimums"].get("package_user_facing_words", 1200))

    for path in iter_user_facing_files(package_root):
        text = read_text(path)
        total_words += word_count(text)

        for pattern in PLACEHOLDER_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                add_finding(
                    findings,
                    "warning",
                    "placeholder-content",
                    path,
                    f"Potential placeholder/template content matched pattern: {pattern}",
                    package_root,
                )
                break

        for block_name, block_pattern in NON_ENGLISH_BLOCKS:
            if re.search(block_pattern, text):
                add_finding(
                    findings,
                    "warning",
                    "non-english-user-facing-content",
                    path,
                    f"User-facing package content contains {block_name} characters. Repository package content should be English-only unless explicitly documented as test corpus data.",
                    package_root,
                )
                break

    if total_words < min_package_words:
        add_finding(
            findings,
            "warning",
            "thin-package",
            package_root,
            f"Package has {total_words} user-facing words; expected at least {min_package_words}.",
            package_root,
        )

    return total_words


def validate_security_and_assets(package_root: Path, findings: list[Finding]) -> tuple[bool, bool]:
    has_scripts = any((package_root / dirname).exists() for dirname in ["scripts"]) or any(
        part.endswith("__scripts") for path in package_root.rglob("*") for part in path.parts
    )

    binary_assets = list(iter_binary_assets(package_root))
    has_binary_assets = bool(binary_assets)

    has_assets = has_binary_assets or any((package_root / dirname).exists() for dirname in ["assets"]) or any(
        part.endswith(("__assets", "__canvas-fonts", "__themes")) for path in package_root.rglob("*") for part in path.parts
    )

    for asset in binary_assets:
        add_finding(
            findings,
            "warning",
            "binary-asset-review",
            asset,
            "Binary asset should be reviewed for legal, repository-size, and security hygiene. Prefer official links or installation instructions where possible.",
            package_root,
        )

    for path in iter_all_text_files(package_root):
        text = read_text(path)
        for pattern in SECRET_PATTERNS:
            if re.search(pattern, text):
                add_finding(
                    findings,
                    "error",
                    "possible-secret",
                    path,
                    "Possible secret/token pattern found in text content.",
                    package_root,
                )
                break

    return has_scripts, has_assets


def calculate_score(errors: int, warnings: int, mini_skill_count: int, word_total: int, policy: dict[str, Any]) -> tuple[int, str, str]:
    score = 100
    score -= errors * 25
    score -= min(warnings * 4, 45)

    min_words = int(policy["minimums"].get("package_user_facing_words", 1200))
    professional_skill_count = int(policy["minimums"].get("mini_skills_per_professional_package", 6))

    if word_total >= min_words and mini_skill_count >= professional_skill_count:
        score += 5

    score = max(0, min(100, score))

    if errors:
        status = "needs-review"
    elif warnings:
        status = "usable"
    else:
        status = "ready"

    if score >= 90 and mini_skill_count >= professional_skill_count and word_total >= min_words:
        maturity = "professional"
    elif score >= 65:
        maturity = "working"
    else:
        maturity = "amateur"

    return score, status, maturity


def validate_package(package_root: Path, policy: dict[str, Any]) -> tuple[PackageReport, list[Finding]]:
    findings: list[Finding] = []

    validate_core_structure(package_root, findings)
    mini_skill_count = validate_manifest(package_root, findings, policy)
    word_total = validate_content_quality(package_root, findings, policy)
    has_scripts, has_assets = validate_security_and_assets(package_root, findings)
    has_binary_assets = bool(list(iter_binary_assets(package_root)))

    errors = sum(1 for finding in findings if finding.severity == "error")
    warnings = sum(1 for finding in findings if finding.severity == "warning")
    score, status, maturity = calculate_score(errors, warnings, mini_skill_count, word_total, policy)

    rel_parts = package_root.relative_to(REPO_ROOT).parts
    domain = rel_parts[0] if rel_parts else ""
    slug = rel_parts[1] if len(rel_parts) > 1 else package_root.name

    report = PackageReport(
        domain=domain,
        slug=slug,
        path=normalize_rel(package_root),
        status=status,
        maturity_candidate=maturity,
        mini_skill_count=mini_skill_count,
        user_facing_word_count=word_total,
        has_scripts=has_scripts,
        has_assets=has_assets,
        has_binary_assets=has_binary_assets,
        errors=errors,
        warnings=warnings,
        score=score,
    )

    return report, findings


def build_domain_reports(package_reports: list[PackageReport]) -> dict[str, dict[str, Any]]:
    domains: dict[str, dict[str, Any]] = {}

    for report in package_reports:
        domain = domains.setdefault(
            report.domain,
            {
                "package_count": 0,
                "ready_package_count": 0,
                "needs_review_package_count": 0,
                "professional_package_count": 0,
                "average_score": 0.0,
                "status": "ready",
            },
        )
        domain["package_count"] += 1
        domain["ready_package_count"] += 1 if report.status == "ready" else 0
        domain["needs_review_package_count"] += 1 if report.status == "needs-review" else 0
        domain["professional_package_count"] += 1 if report.maturity_candidate == "professional" else 0
        domain["average_score"] += report.score

    for domain in domains.values():
        if domain["package_count"]:
            domain["average_score"] = round(domain["average_score"] / domain["package_count"], 2)
        if domain["needs_review_package_count"]:
            domain["status"] = "needs-review"
        elif domain["ready_package_count"] != domain["package_count"]:
            domain["status"] = "usable"
        else:
            domain["status"] = "ready"

    return domains


def emit_markdown_summary(package_reports: list[PackageReport], findings: list[Finding]) -> str:
    total_errors = sum(1 for finding in findings if finding.severity == "error")
    total_warnings = sum(1 for finding in findings if finding.severity == "warning")

    lines = [
        "# Skill Validation Report",
        "",
        f"- Packages checked: {len(package_reports)}",
        f"- Errors: {total_errors}",
        f"- Warnings: {total_warnings}",
        "",
        "## Packages",
        "",
        "| Package | Status | Maturity | Mini-skills | Words | Errors | Warnings | Score |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for report in sorted(package_reports, key=lambda item: item.path):
        lines.append(
            f"| `{report.path}` | {report.status} | {report.maturity_candidate} | "
            f"{report.mini_skill_count} | {report.user_facing_word_count} | "
            f"{report.errors} | {report.warnings} | {report.score} |"
        )

    lines.extend(["", "## Findings", ""])

    if not findings:
        lines.append("No findings.")
    else:
        for finding in sorted(findings, key=lambda item: (item.severity, item.path, item.code)):
            lines.append(f"- **{finding.severity.upper()}** `{finding.code}` `{finding.path}` - {finding.message}")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Arcana skill packages.")
    parser.add_argument("--root", default=str(REPO_ROOT), help="Repository root. Defaults to this script's repository root.")
    parser.add_argument("--package", help="Validate only one package path, for example design/content-writing.")
    parser.add_argument("--policy", default=str(DEFAULT_POLICY_PATH), help="Validation policy JSON path.")
    parser.add_argument("--output-json", help="Write machine-readable validation report to this path.")
    parser.add_argument("--output-md", help="Write Markdown validation report to this path.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when error findings are present.")
    parser.add_argument("--fail-on-warning", action="store_true", help="Exit non-zero when warning findings are present.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    policy = load_policy(Path(args.policy).resolve())

    packages = discover_packages(root, args.package)
    if not packages:
        print("No skill packages found.")
        return 1 if args.strict else 0

    package_reports: list[PackageReport] = []
    findings: list[Finding] = []

    for package in packages:
        report, package_findings = validate_package(package, policy)
        package_reports.append(report)
        findings.extend(package_findings)

    domain_reports = build_domain_reports(package_reports)

    result = {
        "schema_version": "1.0.0",
        "root": normalize_rel(root),
        "package_count": len(package_reports),
        "domain_reports": domain_reports,
        "packages": [asdict(report) for report in sorted(package_reports, key=lambda item: item.path)],
        "findings": [asdict(finding) for finding in sorted(findings, key=lambda item: (item.severity, item.path, item.code))],
        "summary": {
            "errors": sum(1 for finding in findings if finding.severity == "error"),
            "warnings": sum(1 for finding in findings if finding.severity == "warning"),
        },
    }

    if args.output_json:
        output_json = Path(args.output_json)
        output_json.parent.mkdir(parents=True, exist_ok=True)
        output_json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if args.output_md:
        output_md = Path(args.output_md)
        output_md.parent.mkdir(parents=True, exist_ok=True)
        output_md.write_text(emit_markdown_summary(package_reports, findings), encoding="utf-8")

    print(emit_markdown_summary(package_reports, findings))

    has_errors = bool(result["summary"]["errors"])
    has_warnings = bool(result["summary"]["warnings"])

    if args.strict and has_errors:
        return 1
    if args.fail_on_warning and (has_errors or has_warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
