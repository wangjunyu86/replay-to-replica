# Observation and behavioral specification

## Observation ledger

Use one row per observable step:

| Field | Meaning |
|---|---|
| `scenario_id` | Stable journey identifier |
| `step_id` | Ordered step identifier |
| `start_state` | Preconditions visible to the user |
| `action` | User action in normalized language |
| `observable` | What changed or appeared |
| `result_state` | State after the step |
| `persistence` | Whether the result survived reload/restart |
| `timing` | Measured delay or range, if relevant |
| `evidence` | Relative evidence path |
| `basis` | `observed`, `derived`, or `inferred` |
| `confidence` | `high`, `medium`, or `low` |
| `notes` | Ambiguity, environment, or reset details |

Avoid original marketing copy when a functional description is enough.

## Epistemic labels

- **Observed** — directly visible in a captured run.
- **Derived** — follows mechanically from multiple observations, such as a state transition table.
- **Inferred** — a plausible rule not yet directly established.

An inference never becomes observed merely because the implementation was built around it.

## Behavior-spec structure

A useful `behavior-spec.yaml` contains:

```yaml
schema_version: "1.0"
scope:
  product: "Observed product"
  replica: "Independent product"
  included_journeys: []
  excluded_identity: []
actors: []
entities: []
states: []
actions: []
invariants: []
integrations: []
scenarios: []
intentional_differences: []
unknowns: []
```

Each action should specify actor, preconditions, input, transition, observable output, side effects, failures, evidence, and basis. Each invariant should be testable.

## Resolve ambiguity

When two runs disagree:

1. record both observations;
2. identify variables that differed;
3. predict what a controlled rerun should show;
4. rerun only if authorized and proportionate;
5. retain the conflict as an unknown if it cannot be settled.

Do not hide nondeterminism behind an overly broad tolerance.
