# WP-0001 — Supervised AI Trading: Evidence Before Action

**Status:** Working paper · **Evidence level:** E3 for system behavior, E0 for commercial adoption · **Performance claim:** None

## Abstract

AI is already entering discretionary trading workflows through general-purpose assistants, private prompts and ad hoc scripts. The practical governance problem is therefore not whether traders will use AI, but whether a firm can reconstruct what the AI observed, claimed, cost, and influenced. This paper defines *Supervised AI Trading* as a system in which model output is treated as testimony rather than authority; deterministic software owns validation, scoring, risk and execution; and every material decision is preserved as replayable evidence.

## Core proposition

A trustworthy AI trading system must answer six questions for every cycle:

1. What market state was available at the decision timestamp?
2. What did each model claim?
3. Which claims were checked against source data?
4. How was the final score or refusal computed?
5. Who approved or rejected the action?
6. Can the resulting state be reconstructed from immutable records?

A prompt/response log answers only question two. A supervised decision record answers all six.

## Reference architecture

`market snapshot → deterministic pre-gate → versioned dossier → analyst → adversarial reviewer → machine validation → deterministic score → human/risk gates → execution or deliberate pass → immutable event record`

The model is denied authority over:

- arithmetic that code can perform;
- risk limits;
- position sizing beyond allowed proposals;
- broker reconciliation;
- state recovery;
- approval provenance.

## Design principles

### Evidence or it did not happen

Every model claim must cite a stored input path and value. A citation is accepted only when machine validation resolves it against the exact historical dossier.

### Failure reduces activity

Provider outage, malformed output, stale data, budget exhaustion, model disagreement or validation failure must result in no new action. Failure never widens risk.

### Inaction is a valid output

A system that frequently concludes “none” or “skip” is not incomplete. It demonstrates that action is conditional rather than the product's engagement target.

### Reconstructable past

Historical views must use the versions, hashes and inputs stored at the time. Re-rendering old decisions with current prompts or weights corrupts the record.

## Evidence from the TITAN reference implementation

The reference implementation demonstrated, during a defined 48-hour shadow window:

- all eligible hourly closes accounted for;
- no invalid model output reaching deterministic scoring;
- exact budget-ledger reconciliation;
- repeated replay verification with identical rebuilt state;
- fail-closed behavior during pauses, budget limits, stale data and a deliberate process kill;
- zero path from shadow analysis to execution.

These observations validate the control architecture over that window. They do not demonstrate profitability, market-beating performance, or generalization to other instruments and regimes.

## Research agenda

- Measure whether adversarial review improves calibration or merely adds cost.
- Compare human approval quality with and without visible counterarguments.
- Evaluate evidence-citation accuracy across model providers and prompt versions.
- Study operator fatigue and rubber-stamping risk.
- Define an open decision-evidence schema and conformance suite.

## Conclusion

The durable product opportunity in AI-assisted trading may not be another source of signals. It may be the accountability layer that makes every signal, refusal and approval inspectable. Supervised AI Trading treats evidence, not autonomy, as the unit of trust.
