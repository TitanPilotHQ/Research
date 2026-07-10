# First 12 Studies Roadmap

## Selection Rule

Early research must strengthen product truth, buyer trust, or methodology. It must not optimize for attention alone.

## Study 1 — Prompt Contract Reliability

Question: How reliably do approved models satisfy the Analyst, Devil's Advocate, and Sentinel contracts?

Primary metrics:

- valid response rate
- rejection reasons
- retry rate
- latency
- tokens/cost

Evidence requirement: model/prompt/config versions and full denominator.

## Study 2 — Citation Containment

Question: Does machine validation correctly reject fabricated or mismatched dossier citations?

Design:

- controlled adversarial fixtures
- scalar, nested, missing, degraded, and fabricated fields
- false-accept and false-reject analysis

## Study 3 — “None” as a Valid Decision

Question: How often does the analyst choose direction=none, and what market conditions surround those decisions?

Purpose: establish that inaction is normal, not pipeline failure.

## Study 4 — Devil's Advocate Contribution

Question: Do serious/fatal objections improve calibration or reduce poor proposals?

Requirements:

- sufficient forward sample
- analyst-only counterfactual computed without altering live decisions
- cost and latency overhead
- no claim before statistical power is reasonable

## Study 5 — Deterministic Score Reproduction

Question: Can every historical score be independently reproduced from its stored bundle?

Expected: exact equality.

Any mismatch is an engineering defect, not a statistical result.

## Study 6 — Budget Enforcement Economics

Question: How do hard caps alter cycle coverage, cost predictability, and decision availability?

Metrics:

- refused calls
- eligible bars lost to caps
- actual vs estimated spend
- cost per completed outcome

## Study 7 — Provider Reliability

Question: What are real latency, failure, and fallback characteristics across approved providers/models?

Separate controlled fault tests from naturally observed production behavior.

## Study 8 — Calendar and Data Freshness Impact

Question: How many eligible bars are skipped due to stale calendar/candles, and what operational changes reduce those losses?

Purpose: distinguish safety-preserving refusal from avoidable operational debt.

## Study 9 — Replay and Recovery Reliability

Question: Across repeated verify/restore/PITR drills, how often does rebuilt state exactly equal live state and how long does recovery take?

Metrics:

- pass rate
- event count
- rebuild time
- RPO/RTO
- unexplained divergence

## Study 10 — Human Approval Behavior

Question: When Copilot launches, how do operators use evidence before approving or rejecting?

Prerequisites:

- consent and privacy design
- minimum sample
- clear separation between workflow research and employee surveillance

Metrics:

- review time
- evidence stages opened
- approval/rejection
- reason codes
- TTL expiry
- later outcome

## Study 11 — AI Governance Market Map

Question: What controls do professional trading desks currently use for AI-assisted decisions?

Method:

- interviews
- public policy review
- DDQ/regulatory source analysis
- no fabricated market-size precision

Deliverable: pain taxonomy and control maturity model.

## Study 12 — Competitor Evidence Capability

Question: Which competitors can preserve and reconstruct a complete AI-assisted decision?

Evaluate public evidence only:

- input provenance
- model output record
- citation checking
- counter-argument
- deterministic score
- human approval
- execution link
- replay
- audit export

Untested is not absent. Mark it honestly.

## Priority Sequence

### Immediate

- Study 1
- Study 2
- Study 5
- Study 7
- Study 9

These use existing system evidence and create the public trust foundation.

### After More Forward Data

- Study 3
- Study 4
- Study 6
- Study 8

### After Customers / Phase D

- Study 10
- Study 11
- Study 12

## Standard Deliverables Per Study

- protocol
- evidence classification
- dataset/fixture manifest
- reproducible analysis
- result report
- limitations
- claim records
- correction policy
- public-safe summary

## Stop Rule

Do not start a new study merely because the previous result is uninteresting. Complete, review, and retain negative or null results first.