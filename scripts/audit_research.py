#!/usr/bin/env python3
"""Read-only quality audit for the TitanPilot Research repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = [
    "README.md",
    "RESEARCH_CHARTER.md",
    "EVIDENCE_STANDARD.md",
    "PUBLICATION_POLICY.md",
    "governance/PUBLICATION_MANIFEST.md",
    "governance/REPRODUCIBILITY_CHECKLIST.md",
    "templates/DATASET_CARD_TEMPLATE.md",
]

PLACEHOLDERS = [
    re.compile(r"\blorem ipsum\b", re.I),
    re.compile(r"\bcoming soon\b", re.I),
    re.compile(r"\bTBD\b"),
]

REPORT_ID = re.compile(r"\bTR-\d{4}\b")


def audit(root: Path) -> list[str]:
    errors: list[str] = []

    for item in REQUIRED:
        if not (root / item).is_file():
            errors.append(f"missing required artifact: {item}")

    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        relative = path.relative_to(root)
        if len(text.strip()) < 120:
            errors.append(f"insufficient substantive content: {relative}")
        for pattern in PLACEHOLDERS:
            if pattern.search(text):
                errors.append(f"placeholder language '{pattern.pattern}' in {relative}")

        if path.parent.name in {"reports", "studies"} and path.name.startswith("TR-"):
            if not REPORT_ID.search(text):
                errors.append(f"report file does not contain a report ID: {relative}")
            required_headings = ["Limitations", "Status"]
            for heading in required_headings:
                if heading.casefold() not in text.casefold():
                    errors.append(f"report missing {heading} section: {relative}")

    report_files = sorted(
        p for p in root.rglob("TR-*.md") if p.is_file()
    )
    ids: dict[str, list[Path]] = {}
    for path in report_files:
        match = REPORT_ID.search(path.name)
        if match:
            ids.setdefault(match.group(0), []).append(path)

    for report_id, paths in ids.items():
        if len(paths) > 1:
            joined = ", ".join(str(p.relative_to(root)) for p in paths)
            errors.append(f"duplicate report ID {report_id}: {joined}")

    return errors


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors = audit(root)
    if errors:
        print("Research audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    reports = sum(1 for _ in root.rglob("TR-*.md"))
    markdown = sum(1 for _ in root.rglob("*.md"))
    print(f"Research audit PASSED: {reports} report/protocol files, {markdown} markdown artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
