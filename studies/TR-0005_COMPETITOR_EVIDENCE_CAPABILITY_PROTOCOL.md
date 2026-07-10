# TR-0005 — Competitor Evidence-Capability Benchmark Protocol

## Status

Protocol only. No competitor has been scored by this document yet.

## Research Question

What publicly documented capabilities do major trading and AI-decision products provide for reconstructing, validating, governing, and auditing an AI-assisted trading decision?

This benchmark does not rank profitability, signal accuracy, chart quality, asset coverage, or general product quality.

## Candidate Products

Initial set:

- TradingView
- TrendSpider
- MetaTrader 5
- Capitalise.ai
- Tickeron
- Composer
- LuxAlgo
- Bloomberg Terminal
- selected trading-platform and model-governance vendors where relevant

A product may be added only when the same public-evidence method can be applied.

## Evidence Sources

Allowed:

- official product documentation
- official product pages
- official security/compliance documentation
- official API documentation
- official release notes
- reproducible observations from a legally accessed public or trial product

Secondary reviews may identify a capability but cannot establish a positive score without primary confirmation.

No score may rely on marketing inference, private access, leaked information, or absence of evidence treated as proof of absence.

## Benchmark Dimensions

Score each 0–3.

### D1 — Input Provenance

0: no public evidence
1: inputs can be viewed broadly
2: exact source inputs or structured features retained
3: exact decision-time input snapshot is immutable/versioned

### D2 — Model/Rule Provenance

0: no public evidence
1: model or rule identity visible
2: version/configuration visible
3: model, prompt/rule, and configuration hashes or immutable versions retained

### D3 — Claim-to-Evidence Linking

0: no public evidence
1: rationale text shown
2: rationale references source data
3: references are machine-validated against decision-time input

### D4 — Adversarial Review

0: none documented
1: generic risk warnings
2: structured counter-argument or challenge
3: challenge is stored, bounded, and capable of deterministic veto or scoring impact

### D5 — Deterministic Decision Boundary

0: decision logic undisclosed or fully model-driven
1: some fixed rules
2: material score/risk logic implemented in code
3: all money/risk/score boundaries are versioned, deterministic, and reproducible

### D6 — Human Approval Provenance

0: no approval record
1: manual approval exists
2: identity/time/decision context retained
3: what the operator saw, action, reason, TTL, and resulting state are auditable

### D7 — Replay/Reconstruction

0: no decision reconstruction
1: historical logs
2: complete decision timeline
3: state/decision can be rebuilt from immutable records and checked for equality

### D8 — Refusal and No-Trade Evidence

0: only positive signals shown
1: some rejected/expired items visible
2: structured refusal reasons retained
3: every eligible decision window has an accounted terminal outcome

### D9 — AI Cost Governance

0: no public evidence
1: usage visible after spend
2: budgets or limits available
3: hard pre-spend caps with event/ledger reconciliation

### D10 — Operational Verification

0: no public evidence
1: uptime/status information
2: backups/monitoring/audit controls documented
3: restore, replay, drift, or failure controls are actively verified and evidenced

Maximum score: 30.

## Scoring Rules

- `0` means no qualifying public evidence found, not proof the capability is absent.
- Every score above 0 must cite a primary source and access date.
- Ambiguous evidence receives the lower score.
- Vendor terminology is preserved; TITAN terminology is not imposed on competitors.
- Products are allowed to excel on different axes.
- The report must include an unscored “what they do better” section.

## Review Process

1. Two-pass source collection.
2. Independent scoring by two reviewers where possible.
3. Resolve disagreements by evidence, not averaging.
4. Offer vendors a correction channel before a public comparative article.
5. Preserve prior scores and correction history.

## Output

For each product:

- evidence table
- scores with citations
- unknowns
- limitations
- strongest capabilities
- areas not publicly evidenced
- date/version context

Aggregate output:

- dimension matrix
- methodology notes
- no single “winner” headline unless the evidence supports the stated scope

## Limitations

Public documentation favors vendors that disclose more. A low score may mean weak capability, weak documentation, or inaccessible enterprise functionality. The study must state this prominently.

The benchmark measures evidence capability only. It must not be used to imply investment performance, safety certification, legal compliance, or overall product superiority.