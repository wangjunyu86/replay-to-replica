# Parity testing

## Compare contracts, not pixels by default

Prefer semantic observables:

- state reached;
- record created or updated;
- validation outcome;
- permission enforced;
- file or message produced;
- ordering and count;
- persistence after restart;
- timing band when timing is part of the experience.

Pixel comparison is appropriate only when visual fidelity is explicitly in scope and lawful assets are available. Brand imitation is not a default parity target.

## Normalize unstable values

Declare normalization before comparing:

- timestamps to relative offsets or ranges;
- generated identifiers to stable aliases;
- unordered collections to sorted canonical form;
- localized formatting to semantic values;
- network latency to an approved interval;
- random output to invariant properties or seeded runs.

Never normalize away a difference that changes user value, permissions, money, data integrity, or failure behavior.

## Scenario gate

A parity scenario should state:

- prerequisites and reset method;
- normalized actions;
- required observables;
- allowed tolerance;
- original evidence;
- replica evidence;
- status and rationale.

Release-blocking scenarios may end only as `match` or approved `acceptable-difference`. `Unverified` is not a pass.

## Structured trace format

`compare_traces.py` expects a JSON array, or an object with an `events` array. Each event should have:

```json
{
  "step_id": "S1.2",
  "action": "submit_form",
  "observable": "validation_error",
  "value": {"field": "email", "code": "invalid"}
}
```

The comparison canonicalizes object key order but otherwise compares values exactly. Normalize timestamps, IDs, ordering, and approved tolerances before invoking it.
