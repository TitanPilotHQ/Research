# TR-0003 — Replay as a Proof Mechanism for AI Decision Systems

**Status:** Architecture evidence draft

## Thesis
Audit logs are not enough. A trustworthy decision system should be able to reconstruct derived state from an immutable record and demonstrate that the reconstructed state matches the live state.

## Architecture
TITAN records typed immutable events and maintains projections in the same transaction. Replay copies events into a scratch schema and applies the same production fold used by live writes. It does not maintain a second projection implementation. Live and rebuilt projection rows are compared directly; two independent rebuilds must also produce an identical canonical state hash.

## Why the same fold matters
A separate replay implementation can agree by accident, drift independently, or encode the same mistake differently. Reusing the production fold turns replay from a second opinion into a direct test of the claim `state = fold(events)`.

## AI decision bundle
A replayable AI decision retains the dossier identifier/hash, candle snapshot hash, thesis, adversarial review, score components, prompt versions and hashes, configuration, validator and scorer versions, provider/model metadata, terminal result, and approval/execution lineage where applicable.

## Verification classes
- Event immutability.
- Taxonomy completeness.
- Orphan detection.
- Projection equality.
- Deterministic double rebuild.
- Journal/source consistency.
- Aggregate story rendering.

## Operational role
Replay runs as a scheduled production integrity check and as an operator forensic tool. A mismatch is an incident, not a dashboard warning to ignore.

## What replay proves
That stored derived state is reproducible from the stored event history under the recorded projection code and data.

## What replay does not prove
That external data was correct, that the strategy was profitable, that a model conclusion was wise, or that broker state currently agrees without reconciliation.

## Limitations
Schema/code compatibility must be preserved; external market data referenced by hash needs retention or a reproducible source; event corruption before durable storage remains outside the fold proof; independent external replication is still required for the strongest evidence level.

## Research agenda
Benchmark replay performance with larger histories, formalize event-schema evolution, compare same-fold replay against dual-implementation audit designs, and publish a sanitized reproducibility fixture.