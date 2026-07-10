# Titan Pilot Evidence Standard

## Evidence levels
- **E0 — Assertion:** unsupported statement; not publishable as fact.
- **E1 — Documented observation:** timestamped observation with source context.
- **E2 — Reproducible measurement:** method, denominator, versions, and repeat instructions.
- **E3 — Independently checked result:** reviewed by a second person/process or replicated.
- **E4 — External evidence:** third-party audit, customer replication, or peer-reviewed validation.

## Claim classes
Engineering correctness, operational performance, model behavior, safety/control effectiveness, commercial/market, and trading performance. Evidence from one class cannot automatically support another.

## Mandatory claim fields
Claim ID, exact wording, evidence level, scope, denominator, period, environment, versions, source artifact, owner, public-safe form, limitations, expiry/review date.

## Statistical discipline
Always report n, missing observations, exclusions, distribution where useful, and uncertainty. Never promote a small sample into a population claim. Avoid percentages without counts.

## Performance boundaries
Backtest, shadow, paper, demo, and live-real-money results must never be merged. Hypothetical outcomes are labeled and separated from executed outcomes.

## Model evidence
Record provider, model identifier, prompt version/hash, configuration hash, input/output tokens, validation result, latency, and cost when relevant.

## Operational evidence
Record host/environment, commit, command/procedure, time window, raw result location, and any intervention.

## Public-safety review
Remove secrets, account identifiers, infrastructure details that create attack value, customer data, and copyrighted inputs not licensed for publication.

## Invalid evidence patterns
Cherry-picked decisions, screenshots without provenance, self-reported win rates, undocumented denominator changes, current-code recomputation of historical results, and claims copied from another repository without source linkage.

## Review outcome
Approved, approved with qualification, internal-only, revise, or rejected. Rejected claims remain in the register with reason.

## Definition of publishable
A technically competent skeptical reader can determine what was measured, how, when, on what system, with what limitations, and which conclusion is justified.