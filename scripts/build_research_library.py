#!/usr/bin/env python3
"""Create Titan Pilot's research-library structure and starter artifacts.

Idempotent by default: existing files are preserved. Use --force only after
reviewing the diff. The script writes no experimental results and makes no
performance claims; it creates governance, protocols, templates, and indexes.
"""
from __future__ import annotations

import argparse
from pathlib import Path

SECTIONS = {
    "whitepapers": "Long-form technical and governance papers.",
    "benchmarks": "Pre-registered, versioned benchmark protocols and results.",
    "datasets": "Internal dataset cards, schemas, provenance and licenses.",
    "evaluations": "Model, prompt, validator and system evaluation plans.",
    "provider-comparisons": "Fair cross-provider comparison protocols.",
    "trading-ai-studies": "Studies of supervised AI decision systems; not returns marketing.",
    "governance-papers": "Human oversight, auditability and accountability research.",
    "replay-papers": "Event replay, reconstruction and determinism research.",
    "risk-papers": "Fail-closed controls, gates, budgets and operational risk.",
    "conference": "Submission targets, abstracts, reviewer responses and camera-ready assets.",
    "references": "Academic reference register and annotated bibliography.",
    "public-datasets": "Public-safe, licensed, redacted research datasets.",
    "reproducibility": "Environment manifests, commands and artifact verification.",
    "charts": "Data-backed chart specifications and source manifests.",
    "figures": "Architecture and research figure catalog.",
    "statistics": "Statistical analysis standards and notebooks policy.",
    "peer-review": "Internal and external review records.",
    "errata": "Corrections, withdrawals and retractions.",
    "versions": "Repository and publication version history.",
}

README_TEMPLATE = """# {title}\n\n{purpose}\n\n## Rules\n\n- Separate measured results from hypotheses.\n- Link every quantitative claim to a versioned artifact.\n- State sample size, date range, exclusions and limitations.\n- Never present system validation as evidence of trading profitability.\n- Record corrections in `../errata/`.\n"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    written = 0
    for name, purpose in SECTIONS.items():
        folder = args.root / name
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / "README.md"
        if path.exists() and not args.force:
            continue
        path.write_text(
            README_TEMPLATE.format(title=name.replace("-", " ").title(), purpose=purpose),
            encoding="utf-8",
        )
        written += 1

    print(f"Research library scaffold ready; files written: {written}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
