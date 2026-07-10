# Reproducibility Checklist

Use this checklist before any TitanPilot research artifact is marked Published.

## Identity

- [ ] Report ID and version are present.
- [ ] Evidence window is exact and uses UTC.
- [ ] Source repository and commit are recorded.
- [ ] Environment and relevant configuration hashes are recorded.
- [ ] Model, provider, prompt, validator, and scoring versions are recorded when applicable.

## Data

- [ ] Dataset origin is documented.
- [ ] Inclusion and exclusion rules are explicit.
- [ ] Missing observations are counted and explained.
- [ ] Every transformation is documented.
- [ ] Sensitive data has been removed or access is controlled.
- [ ] Dataset checksum or immutable identifier is recorded.
- [ ] The dataset card is complete.

## Method

- [ ] Research question is stated before results.
- [ ] Primary metric is named.
- [ ] Secondary metrics are distinguished from primary metrics.
- [ ] Baseline or comparison condition is described.
- [ ] Randomness and seeds are controlled where applicable.
- [ ] Time boundaries prevent look-ahead.
- [ ] Operational failures are not silently excluded.
- [ ] Statistical uncertainty or small-sample limits are stated.

## Execution

- [ ] Commands or scripts required to reproduce results are listed.
- [ ] Dependencies and versions are pinned or captured.
- [ ] A clean-environment rerun has been attempted.
- [ ] Expected outputs and checksums are documented.
- [ ] Failed reruns are recorded rather than hidden.

## Claims

- [ ] Every numerical claim can be traced to an output table or query.
- [ ] System-validation evidence is not presented as profitability evidence.
- [ ] Backtests are labeled hypothetical.
- [ ] Forward observations are labeled with account type and execution mode.
- [ ] Causal language is avoided unless design supports causality.
- [ ] Negative and null results are included.
- [ ] Limitations are prominent, not buried.

## Independent Review

- [ ] A reviewer who did not author the analysis reran or inspected the method.
- [ ] Reviewer findings are recorded.
- [ ] Material disagreements are resolved or disclosed.
- [ ] Public wording matches the reviewed evidence.

## Publication Safety

- [ ] No secrets, account credentials, private endpoints, or personal data are present.
- [ ] No customer or partner is identifiable without authorization.
- [ ] No unsupported competitor accusation is present.
- [ ] External quotations and figures comply with licensing and citation requirements.
- [ ] Correction contact and version history are included.

## Sign-off

Author: ____________________  Date: __________

Technical reviewer: ____________________  Date: __________

Public-safety reviewer: ____________________  Date: __________

Decision: Draft / Approved / Published / Blocked

Blocking findings:

- 
