# Titan Pilot Benchmark Program

## Objective

Create a reproducible benchmark suite for the parts of supervised AI trading that can be measured honestly without making performance promises.

## Benchmark Families

### B1 — Contract Compliance

Measures whether models produce outputs that satisfy required schemas and bounded contracts.

Metrics:

- valid response rate
- retry rate
- rejection reason distribution
- tokens
- latency
- cost

### B2 — Evidence Grounding

Measures whether cited fields and values match the provided dossier.

Test cases:

- exact scalar citation
- wrong field
- correct field/wrong value
- nested object misuse
- unavailable timeframe
- degraded source quality
- fabricated field
- price/invalidation violation

Metrics:

- true accept
- true reject
- false accept
- false reject
- reason-code accuracy

### B3 — Adversarial Review

Measures what Devil's Advocate review contributes.

Metrics:

- keep/kill rate
- objection severity distribution
- fatal-veto frequency
- downstream score delta
- outcome difference by objection class
- cost/latency overhead

This benchmark must not assume more objections are better.

### B4 — Deterministic Scoring

Measures exact reproducibility across:

- repeated execution
- replay
- database rebuild
- config versions
- Python/runtime versions

Expected result: identical components and final decisions for the same stored bundle.

### B5 — Provider Resilience

Fault matrix:

- DNS failure
- connect timeout
- read timeout
- TLS failure
- connection refused
- 429
- 5xx
- 401/403
- malformed body
- both providers unavailable

Metrics:

- fallback eligibility correctness
- fallback count
- duplicate-call risk
- fail-closed result
- event correctness
- budget correctness

### B6 — Operational Recovery

Scenarios:

- engine kill before call
- engine kill during call
- engine kill after provider response/before event commit
- database restart
- MT5 restart
- VPS rebuild
- backup restore
- PITR

Metrics:

- recovery time
- unexplained gaps
- duplicate decisions
- replay equality
- alert latency

### B7 — Human Approval

Future Phase D benchmark.

Metrics:

- review time
- approval/rejection rate
- reason-code distribution
- TTL expiry
- evidence panels opened before approval
- automation-bias indicators
- outcome by operator decision

Requires explicit privacy and workplace-monitoring review.

### B8 — Cost Efficiency

Metrics:

- cost per eligible bar
- cost per valid thesis
- cost per scored decision
- cost per proposed signal
- spend refused by caps
- estimate/actual ratio
- role/model breakdown

## Dataset Tiers

### Public Synthetic Fixtures

Designed to test contract and validator behavior. Must be clearly synthetic.

### Sanitized Production Fixtures

Derived from real certified decisions with sensitive data removed. Must retain semantic integrity.

### Private Evaluation Sets

Customer or proprietary data. Results may be published only in aggregate with authorization.

## Baselines

Where applicable compare:

- no AI
- analyst only
- analyst + deterministic validator
- analyst + DA
- full pipeline
- primary provider vs fallback provider
- current prompt vs prior prompt

## Anti-Gaming Rules

- evaluation fixtures cannot be included as prompt examples
- prompt changes after seeing results create a new benchmark version
- report all attempted models/configs
- separate development and evaluation sets
- do not remove difficult cases without a documented dataset-version change
- benchmark owners may not rewrite metric definitions after results arrive

## Benchmark Report Template

1. Question
2. Version
3. Dataset
4. Protocol
5. Models/configuration
6. Metrics
7. Results
8. Failures
9. Cost/latency
10. Limitations
11. Reproduction
12. Claim records

## Initial Release Sequence

1. B1 Contract Compliance v1
2. B2 Evidence Grounding v1
3. B5 Provider Resilience v1
4. B4 Deterministic Scoring v1
5. B6 Operational Recovery v1
6. B3 Adversarial Review after sufficient forward sample
7. B8 Cost Efficiency quarterly
8. B7 Human Approval only after Phase D deployment and consent design

## Definition of Done

A benchmark is complete when:

- protocol is frozen before final run
- dataset version is identified
- code/config hashes are recorded
- expected and actual outputs are retained
- failures are included
- reproduction succeeds on a clean environment
- claims satisfy the Evidence Standard
- result is versioned and indexed