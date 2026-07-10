# Titan Pilot Evidence Standard

## Purpose

Define the minimum proof required before a result becomes a Titan Pilot public claim.

## Evidence Levels

### E0 — Assertion

Unsupported statement or working hypothesis.

May appear only in drafts and must be labeled.

### E1 — Internal Observation

Observed in logs, code, or an operator report, but not independently reproduced.

May guide engineering. Not suitable for headline marketing.

### E2 — Reproduced Internal Evidence

Observed and reproduced using a documented method, known version, and retained evidence.

Suitable for technical documentation with limitations.

### E3 — Publicly Reproducible Evidence

Method, fixtures/data, configuration, and reproduction steps are public or independently accessible.

Suitable for public technical claims.

### E4 — Independent Verification

A qualified external party reproduced or audited the result.

Suitable for strong enterprise and diligence claims, with exact scope stated.

## Claim Record

Every measurable claim must include:

- claim id
- exact wording
- evidence level
- source artifact
- source commit/version
- observation window
- population/sample size
- numerator
- denominator
- exclusions
- method
- owner
- reviewer
- limitations
- approval date
- expiry/review date
- public-safe wording

## Metric Rules

### Rates

Always provide numerator and denominator.

Bad:

> Validation was highly reliable.

Good:

> 0 of 51 completed calls were rejected during the stated 48-hour window.

### Latency

Provide:

- population
- clock boundary
- median
- p95 where sample allows
- maximum
- timeout

### Cost

Provide:

- pricing basis
- provider/model
- input/output tokens
- estimated vs actual
- currency
- ledger reconciliation status

### Coverage

Define what counts as eligible, terminal, explained, and excluded.

A killed drill bar cannot be silently removed; it must be separately classified.

### Performance

Any trading-performance claim must state:

- demo, paper, or live
- gross or net
- fees/spread/slippage assumptions
- starting capital
- position sizing
- period
- number of trades
- max drawdown
- benchmark
- forward vs historical

No annualization from statistically meaningless samples.

## Source Hierarchy

Preferred order:

1. immutable event record
2. deterministic projection/replay output
3. system status artifact
4. provider invoice/API usage record
5. broker statement
6. controlled experiment output
7. operator note
8. model-generated summary

A model-generated summary is never the primary evidence.

## Reproducibility Package

Where possible, include:

- README
- protocol
- fixture or dataset
- code/notebook/script
- environment versions
- configuration hashes
- expected outputs
- actual outputs
- checksum manifest
- limitations

## Redaction Rules

Redaction must not change the conclusion.

Document:

- what was removed
- why
- whether removed fields affect reproducibility
- how an authorized reviewer could inspect originals

Never publish:

- credentials
- broker account identifiers
- customer strategy data
- private prompts without approval
- personal data
- infrastructure addresses that increase attack surface

## Negative Evidence

Retain and report:

- rejected calls
- failed experiments
- unexpected restarts
- unexplained gaps
- metric regressions
- adverse model/version behavior

A result cannot be promoted by deleting inconvenient observations.

## Backtest Standard

A backtest publication must include:

- hypothesis written before result interpretation
- data source and licensing
- full date range
- splits
- leakage controls
- parameter search space
- transaction costs
- survivorship treatment
- missing-data handling
- baseline strategies
- all tested variants or multiplicity disclosure

Backtests may prove implementation mechanics. They do not prove deployable alpha.

## Forward Study Standard

Define before start:

- start/end
- eligibility rules
- intervention policy
- model/prompt/config versions
- cap/timeout rules
- outcome metric
- stop conditions
- allowed fixes

Any in-window change creates a new cohort unless protocol explicitly allows it.

## Benchmark Fairness

When comparing competitors/models:

- use equivalent tasks
- disclose prompts/configs where permitted
- avoid vendor-specific tuning unless all receive equal tuning budget
- show failures
- report cost and latency alongside quality
- distinguish missing capability from untested capability

## Corrections and Retractions

Corrections must preserve:

- original wording
- corrected wording
- reason
- date
- impact on dependent claims

Retractions remain visible. Do not silently delete published evidence.

## Publication Gate

A publication passes only when:

- claim records are complete
- sample and exclusions are explicit
- source evidence is retained
- public disclosure is authorized
- reproduction was attempted
- limitations are prominent
- no title or summary overstates the body

## Fast Checklist

Before citing any number, ask:

1. Where did it come from?
2. Can we reproduce it?
3. What exactly is the denominator?
4. What was excluded?
5. Did anything change during the window?
6. Is this forward evidence or retrospective evidence?
7. Could a skeptical reviewer reach the same conclusion?
8. Does the public wording say less than or equal to what the evidence proves?