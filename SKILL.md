---
name: replay-to-replica
description: Turn authorized observation of an existing app, website, device workflow, or user demonstration into an evidence-linked behavioral specification, independent implementation handoff, executable acceptance scenarios, and parity report. Use when reproducing product behavior without copying source, branding, or protected assets; do not use to bypass access controls, extract secrets, or make an unlicensed near-identical clone.
---

# Replay to Replica

Translate observed product behavior into an implementable, independently expressed contract, then verify the new implementation by replaying the same user tasks. Optimize for behavioral clarity, not visual or code imitation.

## Boundary

This skill supports authorized black-box observation and clean-room-style handoff. It does not itself establish legal compliance. Respect licenses, terms, patents, privacy, and contractual restrictions. Do not:

- bypass authentication, payment, rate limits, encryption, or technical controls;
- access data or features the user is not authorized to access;
- copy source code, decompiled code, proprietary assets, trademarks, copywriting, hidden identifiers, or confidential data into the implementation pack;
- claim strict legal clean-room separation when the same person or agent saw protected implementation details.

If strict separation matters, divide the work: an observation role produces a normalized behavior pack, and a separate implementation role receives only that pack.

## Choose the requested outcome

Clarify which result is needed:

- **Behavior pack only** — specifications and acceptance scenarios.
- **Implementation handoff** — behavior pack plus build-ready tasks and interfaces.
- **Verified replica** — independent implementation plus replayed parity tests.

Do not expand “analyze this product” into building a clone unless the user requested implementation.

Initialize a working pack with:

```bash
python3 scripts/init_replica_pack.py <output-directory> --product "<observed product>" --replica "<new product>"
```

## Phase 1: Define scope and authorization

Record:

- authorized target and access method;
- intended independent product and user;
- behaviors to preserve;
- behaviors, branding, data, and assets to exclude;
- supported platform and test environment;
- whether runtime interaction or account actions require fresh consent;
- the parity threshold: exact contract, functionally equivalent, or intentionally changed.

Create task-based scope rather than “copy the whole app.” Start with the smallest valuable journeys.

## Phase 2: Observe as a user

For each journey, capture:

1. starting state and prerequisites;
2. user action;
3. immediately observable response;
4. resulting state and persisted data;
5. errors, delays, limits, and recovery paths;
6. evidence path and environment;
7. epistemic label: `observed`, `derived`, or `inferred`.

Reset the target between runs when state could affect behavior. Repeat variable or timing-sensitive behavior enough to identify ranges rather than treating one sample as a rule.

Observation evidence can include recordings, screenshots, accessibility trees, public network behavior, exported files, user-visible logs, and documented APIs. Use available inspection tools only within authorization. Internal implementation details are unnecessary for a behavioral contract.

Read [references/observation-and-spec.md](references/observation-and-spec.md) when writing the behavior pack.

## Phase 3: Normalize into a behavior contract

Describe behavior independently of the original interface and wording. The contract should define:

- actors and permissions;
- entities, identifiers, and relationships;
- states and valid transitions;
- actions, inputs, outputs, side effects, and invariants;
- validation and failure behavior;
- persistence, ordering, timing, and concurrency rules where visible;
- external integration boundaries;
- accessibility and platform expectations;
- intentional differences.

Every nontrivial rule needs an evidence reference or an explicit inference label. Conflicting observations remain unresolved until tested; do not silently choose the convenient interpretation.

## Phase 4: Produce a clean implementation handoff

The implementation handoff may include:

```text
behavior-spec.yaml
state-model.md
data-contracts.md
acceptance-scenarios.md
implementation-handoff.md
source-observations.csv
```

Rewrite names, text, visual identity, and domain examples for the new product. Exclude original assets and internal identifiers. Specify interfaces and outcomes, not presumed source architecture.

Read [references/clean-room-handoff.md](references/clean-room-handoff.md) before handing the pack to an implementation agent.

## Phase 5: Implement independently

Choose technology from the new product’s constraints, not from guesses about the original stack. Preserve behavior contracts while allowing different architecture, algorithms, visual design, and data structures.

Keep an implementation decision log for deliberate differences. Do not change the behavior spec merely to make a failing implementation appear compliant; update the spec only when new observation disproves it or the user approves a product change.

## Phase 6: Replay and compare

Turn acceptance scenarios into executable tests where practical. Run the same normalized actions against the original and replica, then compare user-observable results.

Classify each scenario:

- `match` — all required observables agree within the declared tolerance;
- `acceptable-difference` — differs intentionally and is approved/documented;
- `mismatch` — contradicts the behavior contract;
- `unverified` — one side could not be exercised or evidence is insufficient.

For structured event traces, use:

```bash
python3 scripts/compare_traces.py original.json replica.json --output parity-report.md
```

Read [references/parity-testing.md](references/parity-testing.md) when designing normalization, tolerances, or release gates.

## Completion gate

Do not call the replica complete unless:

- every release-blocking scenario is `match` or an approved `acceptable-difference`;
- unresolved inferred rules are disclosed;
- the new product contains no copied protected assets or identity;
- a user can execute the core journey in the intended environment;
- the parity report links to inspectable evidence.

A final report must state scope, authorization boundary, observed coverage, inferences, intentional differences, mismatches, unverified areas, and the exact implementation artifact tested.
