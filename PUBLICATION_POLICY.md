# Titan Pilot Publication Policy

## Purpose

Govern how research moves from internal evidence to public release.

## Publication Types

### Technical Report

Detailed method, system context, results, limitations, and reproduction path.

### Benchmark

Structured comparison across models, providers, versions, systems, or operating conditions.

### Research Note

Focused analysis that may combine public sources, internal observations, and clearly labeled interpretation.

### Incident Study

Timeline and analysis of a real failure, near miss, or control activation.

### Specification

Normative schema, protocol, or evidence requirement intended for implementation or interoperability.

### Dataset/Fixture Release

Sanitized data with provenance, license, schema, checksums, and known limitations.

## Required Front Matter

Every publication includes:

- title
- publication class
- status: draft/reviewed/published/corrected/retracted
- version
- date
- authors
- reviewers
- evidence level
- source commit(s)
- disclosure scope
- conflicts of interest
- review date

## Review Stages

1. Method review
2. Evidence review
3. Security/privacy review
4. Commercial-claims review
5. Editorial review
6. Reproduction attempt
7. Publication approval

One person may fill multiple roles initially, but the document must disclose that limitation.

## Public-Safe Rule

A publication must not expose:

- credentials or tokens
- customer identities without permission
- proprietary strategy details
- personal information
- attack-enabling infrastructure detail
- copyrighted datasets without license
- provider content beyond allowed quotation and disclosure limits

## Title and Abstract Discipline

The title and abstract may not claim more than the strongest supported conclusion.

Avoid:

- “proves” when evidence only suggests
- “institutional-grade” without exact scope
- “zero hallucinations” when only observed validation failures are zero
- “fully autonomous” when human or risk gates remain
- “profitable” from hypothetical or demo outcomes

## Use of AI in Research

AI may assist with:

- drafting
- code review
- literature categorization
- formatting
- hypothesis generation

AI may not be treated as:

- a factual source
- an independent reviewer
- a reproduction attempt
- proof that an interpretation is correct

Material AI assistance should be disclosed where relevant.

## Source Citation

Prefer primary sources:

- official documentation
- research papers
- standards
- regulatory publications
- direct system evidence

Secondary sources may provide context but should not carry load-bearing technical or legal claims.

## Commercial Separation

Marketing may summarize a published result only using approved wording from its claim record.

Marketing may not:

- remove limitations
- combine incompatible cohorts
- convert demo results into live claims
- present a benchmark as a customer result
- cite a draft as final

## Embargoes

Embargoes may protect:

- coordinated security disclosure
- customer confidentiality
- partner announcement timing
- patent/trademark review

Embargoes may not be used to hide negative results while positive summaries are marketed.

## Versioning

Publications use semantic or date-based versions.

Any change affecting interpretation requires a new version and changelog entry.

Minor typography corrections may retain version if meaning is unchanged.

## Corrections

A correction notice states:

- what was wrong
- when discovered
- corrected content
- whether conclusions changed
- which dependent claims were updated

## Retractions

Retract when:

- source evidence is unreliable
- privacy/security was breached
- method contains a conclusion-invalidating flaw
- key claims cannot be reproduced
- disclosure authorization was invalid

Retractions remain discoverable with the reason.

## Release Checklist

- [ ] Front matter complete
- [ ] Evidence Standard satisfied
- [ ] Raw/source evidence retained
- [ ] Reproduction attempted
- [ ] Limitations prominent
- [ ] Security/privacy approved
- [ ] Licenses verified
- [ ] Links and checksums tested
- [ ] Public claims registered
- [ ] Website summary matches approved wording
- [ ] Research index updated

## Definition of Published

A document is published only when:

- committed to the public repository
- tagged or versioned
- status marked published
- claim records approved
- source links resolve
- website or index points to the exact version

A document merely pushed to a branch is not a published result.