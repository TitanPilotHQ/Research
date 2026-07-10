#!/usr/bin/env python3
"""Create the canonical Titan Pilot research-program files idempotently."""
from __future__ import annotations

import argparse
from pathlib import Path

FILES = [
    "RESEARCH_CHARTER_EXPANDED.md",
    "EVIDENCE_STANDARD_COMPLETE.md",
    "benchmarks/BENCHMARK_FRAMEWORK_COMPLETE.md",
    "templates/RESEARCH_REPORT_TEMPLATE.md",
    "templates/BENCHMARK_REPORT_TEMPLATE.md",
    "papers/TR-0001_PHASE_C_VALIDATION.md",
    "papers/TR-0002_HALLUCINATION_CONTAINMENT.md",
    "papers/TR-0003_REPLAY_ARCHITECTURE.md",
    "papers/TR-0004_AI_GOVERNANCE.md",
    "methodologies/COMPETITOR_BENCHMARK_METHODOLOGY.md",
]

STUB = """# {title}\n\nThis file is part of the Titan Pilot evidence and publication system. Replace only through a reviewed revision; preserve scope, methods, limitations, and provenance.\n"""

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--force", action="store_true")
    args = p.parse_args()
    root = Path(__file__).resolve().parents[1]
    for relative in FILES:
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not args.force:
            print(f"skip {relative}")
            continue
        title = Path(relative).stem.replace("_", " ").title()
        target.write_text(STUB.format(title=title), encoding="utf-8")
        print(f"write {relative}")

if __name__ == "__main__":
    main()
