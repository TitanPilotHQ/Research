# DS-0002 — Redacted Decision Evidence Examples

**Status:** Planned public dataset; no records released.  
**Version:** 0.1-draft  
**Contract:** `specifications/PUBLIC_EVIDENCE_FIXTURE_V1.md`  
**Schema:** `schemas/public-evidence-fixture-v1.schema.json`

## Purpose

DS-0002 is intended to provide a small, public-safe set of examples for:

- the Titan Pilot Evidence Explorer;
- reproducibility demonstrations;
- governance-control education;
- schema and consumer validation;
- public claims that can be traced to approved evidence.

It is not a trading-signal feed, backtest dataset, performance dataset, or source of investment advice.

## Source systems

The only authorized source is Titan through an explicit sanitized-export process. Research does not scrape or reconstruct private Titan events independently.

Potential source classes:

- certified synthetic ceremony evidence;
- certified replay/determinism records;
- approved forward operational decision evidence;
- deliberately redacted negative or refusal cases.

## Unit of observation

One JSON object represents one governed decision-evidence fixture.

A fixture may describe a requested, armed, confirmed, rejected, expired, cancelled or failed decision state. Inclusion does not imply execution.

## Inclusion rules

A record may be included only when:

- Titan authorizes the source evidence;
- the export matches the v1 schema exactly;
- the decision reference is pseudonymous and release-specific;
- all summaries are public editorial summaries rather than copied model prose;
- the fixture includes limitations;
- integrity verification passes;
- an adversarial reviewer approves publication.

## Exclusion rules

Exclude any record containing or enabling reconstruction of:

- credentials, secrets, tokens, DSNs or cryptographic material;
- private accounts, orders, broker tickets or infrastructure identifiers;
- personal or customer data;
- raw event payloads;
- raw model, analyst, validator or debate-agent prose;
- private prompts or complete prompt templates;
- proprietary strategy thresholds;
- executable trading instructions;
- unsupported profit, win-rate, return or alpha claims;
- an unresolved security or legal concern.

## Transformations

Required transformations include:

- replace internal identifiers with release-specific public references;
- aggregate objection, validation and severity information into counts;
- replace raw prose with bounded independently reviewed summaries;
- retain only allowlisted provenance versions;
- convert citations to approved kind + SHA-256 pairs;
- canonicalize JSON before integrity hashing;
- validate with `additionalProperties=false`.

## Missingness

Missing required fields invalidate the fixture.

Optional fields must not be inferred. An absent optional value means it was not approved for release or did not exist; consumers must not guess it.

## Known bias and limitations

- Public-safe examples may overrepresent decisions that are easiest to sanitize.
- Synthetic and drill evidence validates controls but does not establish live market performance.
- A small curated dataset cannot estimate system-wide error rates.
- Counts omit the semantic detail of private evidence by design.
- Published examples may lag current production versions.
- The dataset cannot establish profitability, suitability or expected returns.

## License and redistribution

Release license is **undecided** pending legal review. Until a release manifest names a license, redistribution is not authorized beyond normal repository viewing.

Third-party source data is not redistributed. Hash citations do not grant access to private source artifacts.

## Security classification

Current classification: **internal candidate**.

A record becomes **public** only after the full release gate in the fixture contract passes.

## Integrity

Each released record requires:

- schema validation result;
- canonical fixture SHA-256;
- release-manifest entry;
- source authorization reference;
- reviewer decision;
- publication timestamp.

## Permitted uses

- Evidence Explorer rendering;
- schema conformance tests;
- governance and replay research;
- reproducibility demonstrations;
- factual public claims directly supported by the fixture.

## Prohibited uses

- live trading or signal generation;
- reverse engineering private strategy;
- training a model to imitate Titan decisions without separate approval;
- profitability or marketing claims not explicitly supported;
- deanonymization;
- security testing against production infrastructure;
- joining with external data to recover private identifiers.

## Retention and withdrawal

A released record is versioned rather than silently overwritten.

Withdrawal may occur for security, legal, privacy or factual-integrity reasons. The release ledger and errata register must retain a public notice of the withdrawal without retaining the unsafe payload.

## Release readiness checklist

- [ ] At least one Titan-generated candidate fixture exists.
- [ ] Titan source authorization recorded.
- [ ] Schema validation passes.
- [ ] Redaction review passes.
- [ ] Public-claims review passes.
- [ ] Integrity hash independently recomputed.
- [ ] License approved.
- [ ] Adversarial review passes.
- [ ] Portfolio consumer rejects invalid/unknown fields.
- [ ] Release manifest completed.

No box is currently checked. DS-0002 remains unreleased.