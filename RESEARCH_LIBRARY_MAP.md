# Titan Pilot Research Library Map

## Mission

Build a public, reproducible body of evidence about supervised AI decision systems in trading. This repository does **not** market returns. It studies provenance, validation, replay, governance, operational safety, cost, latency, and human oversight.

## Library

| Area | Purpose | First deliverable |
|---|---|---|
| Whitepapers | Synthesize load-bearing ideas | Supervised AI Trading: Evidence Before Action |
| Benchmarks | Compare systems under pre-registered protocols | Evidence Capability Benchmark v1 |
| Datasets | Describe source material and limitations | Phase C Decision Record dataset card |
| Evaluations | Measure contracts and failure containment | Validator effectiveness evaluation |
| Provider comparisons | Compare model/provider behavior fairly | Dual-provider reliability protocol |
| Trading AI studies | Study decision quality without returns hype | No-trade behavior study |
| Governance papers | Human and organizational controls | Human Approval as an Auditable Control |
| Replay papers | Reconstruction and determinism | Replayable Decisions vs Logs |
| Risk papers | Fail-closed and budget controls | Failure Reduces Activity to Zero |
| Conference papers | Prepare peer-reviewed submissions | Workshop paper package |
| Academic references | Maintain source quality | Annotated bibliography |
| Public datasets | Release safe research artifacts | Redacted decision evidence sample |
| Reproducibility kits | Make claims independently checkable | TR-0001 reproduction bundle |
| Charts and figures | Visualize measured evidence only | Figure catalog and data manifest |
| Statistical analysis | Prevent misleading inference | Statistical analysis standard |
| Peer review | Record criticism and response | Review form and decision log |
| Errata | Correct the public record | Permanent errata register |
| Version history | Preserve publication lineage | Research release ledger |

## Evidence ladder

- **E0 — Hypothesis:** reasoned but untested.
- **E1 — Test evidence:** controlled automated tests.
- **E2 — Drill evidence:** deliberately induced failure or recovery exercise.
- **E3 — Forward operational evidence:** observed on a running system over a defined window.
- **E4 — Independent replication:** reproduced by a separate reviewer or environment.

Every abstract and chart must state its highest evidence level. E1–E3 validate system behavior; they do not establish market alpha.

## Publication flow

1. Register the question and protocol.
2. Freeze definitions, exclusions and metrics.
3. Create a dataset card before analysis.
4. Run analysis from a clean environment.
5. Generate tables/charts from data, never by hand.
6. Complete internal adversarial review.
7. Publish manuscript, artifact manifest and limitations.
8. Record corrections in `errata/` and releases in `versions/`.
