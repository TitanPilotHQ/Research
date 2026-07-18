# Public Evidence Fixture Contract v1

**Status:** Draft contract — no fixture has been certified or released yet.

**Owner:** Titan Pilot Research  
**Engineering source of truth:** Titan  
**Public consumer:** Portfolio / Evidence Explorer  
**Dataset registry entry:** DS-0002

## 1. Purpose

This contract defines the only public-safe shape that Titan may hand to the Research and Portfolio repositories for evidence demonstrations.

It is designed to show how a supervised AI decision was governed without publishing private strategy, raw model reasoning, credentials, account data, executable instructions, or internal security configuration.

A conforming fixture is evidence about decision governance. It is not evidence of profitability, market alpha, investment suitability, or future performance.

## 2. Release gate

A fixture is not public merely because it matches this schema. Publication additionally requires:

1. source-event authorization from Titan;
2. schema validation;
3. redaction review;
4. public-claims review;
5. dataset-card completion;
6. integrity hash generation;
7. independent adversarial review;
8. explicit release approval.

Until all eight gates pass, the artifact must remain marked `draft` or `internal_candidate` and must not be consumed by the production Evidence Explorer.

## 3. Allowed top-level content

The v1 fixture may contain only:

- fixture and schema identifiers;
- publication status;
- sanitized decision identity;
- bounded timestamps;
- decision state and terminal outcome;
- aggregate evidence counts;
- closed severity counts;
- bounded human-readable summaries;
- hash-pinned citations;
- provenance and component versions;
- replay and determinism assertions;
- governance-control assertions;
- explicit limitations;
- fixture integrity metadata.

Every field is allowlisted. Unknown fields are invalid.

## 4. Explicitly forbidden content

A fixture must not contain:

- credentials, tokens, secrets, DSNs, private keys or public-key material;
- raw WebAuthn credential identifiers, challenges, signatures, authenticator data or attestation;
- account identifiers, broker identifiers, order tickets or private infrastructure addresses;
- raw event payloads or unrestricted JSONB;
- raw analyst, debate-agent, validator or model prose;
- hidden prompts, chain-of-thought, private instructions or complete prompt templates;
- exact private strategy rules or proprietary thresholds;
- executable trade instructions, live entry instructions or automation commands;
- customer, operator or third-party PII;
- internal exception traces or security-control implementation details;
- claims of profit, win rate, expected return or market alpha unless separately governed by a later research protocol.

## 5. Bounded-summary rules

`summary` fields are public editorial artifacts, not copied model output.

They must:

- be written from allowlisted facts;
- remain within the schema length limit;
- avoid exact proprietary thresholds;
- avoid predictions and return claims;
- distinguish measured fact from interpretation;
- be independently reviewed;
- carry no instructions that could be executed as a trade.

## 6. Decision identity

Public fixtures use a release-specific pseudonymous `decision_ref`. Internal approval IDs, event IDs, account IDs and broker correlation IDs must not be published.

The public reference must not be reversible without a private mapping retained by Titan.

## 7. Evidence counts and severities

Counts must define their unit and denominator. Zero is a valid value and must not be omitted.

The v1 closed severity vocabulary is:

- `critical`
- `high`
- `medium`
- `low`
- `info`

The fixture may report aggregate objection, validation and control counts. It may not include raw objection prose.

## 8. Citations

Each citation is hash-pinned and contains:

- a closed `kind`;
- a SHA-256 digest;
- an optional public-safe label.

The digest proves reference stability; it does not make the underlying private artifact public.

Allowed v1 citation kinds:

- `candle_snapshot`
- `decision_dossier`
- `validation_report`
- `replay_record`
- `governance_event_chain`

## 9. Provenance and versions

The fixture records the versions needed to understand which governed components produced the decision evidence. Version strings are identifiers only; source code, prompts and private configuration are not embedded.

Required provenance includes:

- source system;
- market-data source class;
- weights version;
- validator version;
- dossier schema version;
- prompt-component version identifiers;
- replay implementation version;
- export-generator version.

## 10. Replay and governance assertions

Assertions must be boolean or closed-enum outputs generated from certified evidence, never marketing copy.

Permitted v1 assertions include:

- replay completed;
- rebuilt state equaled live state;
- deterministic fingerprint matched;
- human approval was required;
- risk gate remained required;
- synthetic fixture was non-executable;
- no execution event occurred for a non-executable fixture.

A false assertion must remain false. Failed or negative results must not be removed to make a fixture appear stronger.

## 11. Integrity

The published JSON is canonicalized using UTF-8 JSON with sorted keys and no insignificant whitespace before calculating `fixture_sha256`.

The release manifest must bind:

- schema ID and version;
- fixture SHA-256;
- generator version;
- publication timestamp;
- review decision;
- source authorization reference.

## 12. Consumer requirements

Portfolio must:

- reject unknown schema IDs or versions;
- reject additional properties;
- verify the fixture hash before rendering;
- render limitations alongside evidence;
- avoid translating counts into performance claims;
- avoid exposing hidden fields through debug output;
- fail closed on invalid or incomplete data;
- never substitute mock evidence in production.

## 13. Change control

Breaking changes require a new schema major version. Additive optional fields require:

- an updated specification;
- schema change;
- dataset-card review;
- consumer compatibility review;
- release-note entry.

The Research repository owns this public contract. Titan owns the factual correctness and authorization of every exported fixture. Portfolio owns presentation only.