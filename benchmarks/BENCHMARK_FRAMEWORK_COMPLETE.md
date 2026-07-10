# Titan Pilot Benchmark Framework

## Objective
Compare decision-governance capabilities with reproducible protocols rather than marketing feature tables.

## Benchmark families
1. Contract compliance.
2. Citation accuracy and fabrication containment.
3. Decision completeness.
4. Deterministic reproducibility.
5. Replay and auditability.
6. Provider resilience.
7. Human-approval safety.
8. Budget enforcement.
9. Operational recovery.
10. Cost and latency.

## Benchmark unit
A benchmark case contains a fixed input fixture, expected contract, system configuration, allowed retries/fallbacks, terminal outcome set, evidence capture requirements, and scoring rubric.

## Fairness rules
Use the same disclosed task, data, time allowance, and outcome definition. Separate unavailable features from failed features. Do not infer internal architecture from UI alone. Allow vendors to correct factual errors before public release.

## Metrics
Pass rate with counts, false-accept rate, false-reject rate, evidence coverage, replay success, deterministic match, latency distribution, cost, missing outcomes, and operator effort.

## Model benchmarks
Pin provider/model/version where possible. Run enough cases to expose variance. Preserve raw outputs privately and publish sanitized examples.

## Competitor benchmarks
Use public product behavior, documentation, trial accounts, or vendor-supplied evidence. Never test in ways that violate terms or access controls.

## Repetition
Run each stochastic case multiple times. Report median and range; publish all terminal outcomes, not the best run.

## Reproducibility bundle
Protocol, fixtures or fixture hashes, environment, versions, scripts, raw-result manifest, analysis notebook/script, and claim register.

## Stop conditions
Secret exposure, unsafe real-money action, terms violation, corrupted fixture, undocumented config drift, or inability to identify the tested version.

## Definition of done
A benchmark is complete when its protocol is frozen before final analysis, all runs are accounted for, failures remain visible, and conclusions do not exceed the measured capability.