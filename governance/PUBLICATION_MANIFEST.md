# Research Publication Manifest

## Purpose

This manifest is the authoritative index of TitanPilot research artifacts. A document is not considered published merely because it exists in Git. Publication requires evidence review, reproducibility review, public-safety review, and a stable identifier.

## Status Vocabulary

- Draft: incomplete and not citable
- Internal Review: methods and evidence under review
- Reproducibility Review: an independent rerun is required
- Approved: technically approved but not necessarily public
- Published: public, versioned, and citable
- Corrected: published with a documented correction
- Retracted: conclusions are no longer supported; artifact remains visible with notice

## Publication Record

Each artifact must record:

- report ID
- title
- version
- authorship and reviewer roles
- status
- publication date
- evidence window
- code/data commit identifiers
- method summary
- primary conclusion
- limitations
- conflict-of-interest statement
- public URL when available
- correction history

## Current Program

| ID | Title | Status | Evidence class | Primary purpose |
|---|---|---|---|---|
| TR-0001 | Phase C Shadow Validation | Approved draft | E3 operational evidence | certify system behavior during the production soak |
| TR-0002 | Hallucination Containment in Financial Decision Systems | Approved draft | E2–E3 | document contract rejection and containment behavior |
| TR-0003 | Replay Architecture for AI Trading Decisions | Approved draft | E2–E3 | explain and test decision reconstruction |
| TR-0004 | Supervised AI Governance for Trading Desks | Approved draft | mixed technical/position paper | define governance principles and decision evidence |
| TR-0005 | Competitor Evidence-Capability Benchmark | Planned | E1–E2 public evidence | compare documented evidence capabilities without unverifiable claims |
| TR-0006 | Prompt Contract Stability Study | Planned | E3 | measure validator outcomes across prompt versions |
| TR-0007 | Adversarial Review Contribution Study | Planned | E3 | quantify how DA objections affect deterministic decisions |
| TR-0008 | Budget Enforcement Reliability Study | Planned | E3 | test pre-token refusal and ledger reconciliation |

## Publication Gate

A report may move to Published only when:

1. Claims map to evidence.
2. Evidence classification is stated.
3. Methods can be rerun from the disclosed materials or limitations explain why not.
4. Sample size and observation window are visible.
5. Trading-performance implications are not inferred from system-validation evidence.
6. Sensitive production data is removed or intentionally approved.
7. External sources are cited accurately.
8. Negative and null results are retained.
9. A reviewer has completed the reproducibility checklist.
10. A public-safe abstract and correction contact exist.

## Citation Format

Recommended:

TitanPilot Research, “Title,” Report TR-XXXX, version X.Y, YYYY-MM-DD.

Every citation must refer to a stable tagged version or commit.

## Corrections

Corrections never overwrite history silently. A correction must state:

- what changed
- why it changed
- whether conclusions changed
- who approved the correction
- affected versions and channels

Materially unsupported conclusions require retraction, not quiet editing.