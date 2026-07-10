# TR-0002 — Containing Unsupported Model Claims in Financial Decision Workflows

**Status:** Method and evidence draft

## Problem
Language models can produce plausible claims that are absent from, inconsistent with, or structurally different from their supplied evidence. In a financial workflow, accepting those claims silently creates both decision risk and audit risk.

## TITAN control model
1. The model receives a versioned structured dossier.
2. Evidence citations must point to allowed scalar leaf fields.
3. The cited value must match the stored value under the contract's comparison rule.
4. Evidence from degraded-quality timeframes is rejected.
5. Invalidation prices are checked deterministically for direction and allowed range.
6. Cardinality, enums, lengths, and required fields are machine enforced.
7. Invalid output creates a closed reason code and no scoreable thesis.
8. Rejected content is redacted, bounded, and hash-stamped for forensics.

## Observed enablement findings
Early live regression exposed three contract mismatches: output truncation, evidence cardinality, and nested-object citation formatting. Each failure stopped progression, produced no signal, and led to a versioned contract correction rather than validator weakening.

## Phase C observation
After the scalar-leaf citation guidance was released, the reported 48-hour window completed 51 model calls with zero validator rejections. Pre-window invalid citations had already demonstrated that unsupported output was stopped before scoring.

## Evaluation metrics
- False acceptance: unsupported claims that pass validation.
- False rejection: supported claims rejected by contract mismatch.
- Contract pass rate with counts.
- Retry rate and cost.
- Reason-code distribution.
- Share of invalid output reaching scoring: target zero.

## Interpretation
The approach does not make model output true. It narrows a specific failure class: claims that cannot be traced verbatim to approved structured evidence. Feature correctness and market interpretation remain separate problems.

## Limitations
Exact-match rules can reject semantically equivalent expressions; structured dossiers can contain incorrect features; model behavior changes by version; small live samples do not establish long-term rates.

## Research agenda
Generate adversarial fixtures, measure false-accept and false-reject rates, compare scalar-only versus normalized comparisons, test prompt injection, and independently reproduce the validator with frozen fixtures.