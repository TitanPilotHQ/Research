# TR-0004 — A Governance Model for Supervised AI Trading Decisions

**Status:** Conceptual and architecture paper

## Abstract
This paper describes a governance pattern for using language models in professional trading workflows without granting them direct authority over risk or execution. The pattern combines structured inputs, bounded model roles, machine validation, deterministic scoring, human approval, immutable evidence, cost controls, and replay.

## Governance layers
1. **Eligibility:** deterministic checks decide whether analysis may begin.
2. **Evidence:** a versioned dossier defines the model's factual boundary.
3. **Reasoning:** the analyst proposes a bounded thesis.
4. **Challenge:** an adversarial role records objections and fatal concerns.
5. **Validation:** code checks schema, citations, quality, and price rules.
6. **Scoring:** deterministic code produces the score and veto behavior.
7. **Budget:** spend is authorized before a provider call.
8. **Human authority:** proposals expire unless explicitly approved in copilot mode.
9. **Risk authority:** existing deterministic risk and kill-switch controls remain structurally unbypassable.
10. **Evidence:** every material step becomes an immutable, replayable record.

## Design principles
The default action is nothing. Unknown states reduce activity rather than expand authority. Model text is testimony, not truth. Numbers that can be computed deterministically are not delegated to a model. Approval must be easier to refuse than to grant.

## Separation of responsibilities
Models interpret and challenge. Deterministic software computes, validates, budgets, gates, and reconciles. Humans approve or refuse. The broker remains the external source of execution truth.

## Governance outcomes
A committee should be able to answer: what the model saw, what it claimed, what evidence supported it, who challenged it, how the score was calculated, what controls applied, who approved or refused, what it cost, and what happened next.

## Risks
Rubber-stamping, model drift, data-quality errors, approval fatigue, false confidence from replay, prompt injection, provider concentration, and governance theater.

## Controls against theater
Measure review time, refusal reasons, validator failures, veto impact, prompt-version outcomes, approval conversion, control exceptions, and incident response. Publish negative findings.

## Limitations
Governance does not create alpha, remove human responsibility, or guarantee compliant use in every jurisdiction. Legal and organizational controls remain necessary.

## Research agenda
Human-factors testing of approval design, review-time thresholds, model/provider comparisons, outcome-independent certification semantics, and independent conformance testing against an open decision-evidence schema.