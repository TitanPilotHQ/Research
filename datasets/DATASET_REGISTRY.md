# Dataset Registry

No dataset is public merely because this repository is public. Every release requires a dataset card, license review, redaction review and checksum manifest.

| ID | Dataset | Status | Sensitivity | Intended use | Contract/card |
|---|---|---|---|---|---|
| DS-0001 | Phase C decision records | Internal candidate | Contains operational payloads | Validation, cost and cycle-accounting research | Pending |
| DS-0002 | Redacted evidence examples | Contract drafted; no records released | Public-safe only after full review | Evidence Explorer demos and benchmark fixtures | [`PUBLIC_EVIDENCE_FIXTURE_V1`](../specifications/PUBLIC_EVIDENCE_FIXTURE_V1.md) · [`DS-0002 card`](DS-0002-DATASET-CARD.md) |
| DS-0003 | Prompt-contract failure cases | Internal candidate | Model output may contain unsafe strings | Validator evaluation | Pending |
| DS-0004 | Replay state fingerprints | Planned public | Aggregated hashes and counts | Determinism research | Pending |
| DS-0005 | Provider latency and token telemetry | Planned aggregate | Commercial/API metadata | Provider comparison | Pending |

## Required dataset-card fields

- identifier and version;
- owner and reviewer;
- collection purpose;
- source systems and date range;
- unit of observation;
- inclusion/exclusion rules;
- transformations and redactions;
- missingness and known bias;
- license and redistribution basis;
- security classification;
- integrity checksums;
- permitted and prohibited uses;
- retention and withdrawal procedure.

## Prohibited public content

Credentials, account identifiers, private IPs, unredacted model payloads, personal data, broker secrets, exact security configuration, private prompts unless separately approved, and any artifact whose release could weaken production controls.
