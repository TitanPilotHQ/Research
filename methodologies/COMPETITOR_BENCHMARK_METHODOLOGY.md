# Competitor Evidence-Capability Benchmark Methodology

## Objective
Evaluate how well products support accountable AI-assisted trading decisions without reducing the comparison to broad feature checklists or unverifiable marketing claims.

## Systems in scope
Charting platforms, AI signal products, strategy builders, execution platforms, institutional terminals, enterprise AI-governance tools, and representative in-house workflows.

## Capability dimensions
1. Structured decision input.
2. Claim-to-evidence citations.
3. Machine validation.
4. Adversarial review.
5. Deterministic scoring/control math.
6. Human approval provenance.
7. Refusal and skip records.
8. Prompt/model/version provenance.
9. Cost and budget control.
10. Immutable event history.
11. State reconstruction/replay.
12. Export and audit usability.
13. Provider and execution neutrality.
14. Security/data-residency posture.

## Evidence sources
Official documentation, public product, authorized trial, vendor demo, published reports, and vendor-supplied correction. Third-party reviews may identify questions but do not establish capability alone.

## Scoring
For each dimension:
- 0: no evidence / unavailable.
- 1: manually documented or partial.
- 2: implemented but not independently provable.
- 3: implemented with reproducible evidence.
- 4: externally validated or customer-replicated.

Do not calculate a single overall winner unless weights are preregistered for a named buyer scenario.

## Test cases
Use one shared sanitized decision fixture where supported. Ask each system to preserve inputs, reasoning, challenge/validation, decision controls, human action, and final record. Record missing or transformed information.

## Fairness
Do not access private endpoints, bypass controls, violate terms, or infer absence from a missing UI alone. Mark not tested separately from unavailable. Give vendors a factual-correction period before public comparison.

## Reporting
Publish version/date, environment, evidence link, screenshots where licensed, test protocol, raw-result manifest, scores by dimension, concessions, limitations, and unresolved vendor disagreements.

## Claim constraints
Allowed: "No public or tested evidence was found for capability X as of date Y." Avoid: "Vendor cannot do X" unless the vendor confirms it.

## Update cadence
Quarterly or after a major release. Preserve historical scorecards so capability evolution remains visible.

## Definition of done
Every score is traceable to dated evidence, every asymmetry is disclosed, vendors have a correction route, and conclusions are limited to decision-governance capability rather than investment performance.