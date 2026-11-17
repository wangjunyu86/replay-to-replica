#!/usr/bin/env python3
"""Create a non-destructive Replay to Replica working pack."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--product", required=True, help="Observed product")
    parser.add_argument("--replica", required=True, help="Independent product")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    root = args.output.expanduser().resolve()
    if root.exists() and any(root.iterdir()) and not args.force:
        raise SystemExit(f"Refusing to write into non-empty directory: {root}")
    root.mkdir(parents=True, exist_ok=True)
    for path in ("evidence/original", "evidence/replica", "traces", "tests"):
        (root / path).mkdir(parents=True, exist_ok=True)

    with (root / "source-observations.csv").open("w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerow([
            "scenario_id", "step_id", "start_state", "action", "observable",
            "result_state", "persistence", "timing", "evidence", "basis",
            "confidence", "notes"
        ])

    (root / "behavior-spec.yaml").write_text(
        'schema_version: "1.0"\n'
        f'scope:\n  product: "{args.product.replace(chr(34), chr(39))}"\n'
        f'  replica: "{args.replica.replace(chr(34), chr(39))}"\n'
        '  included_journeys: []\n  excluded_identity: []\n'
        'actors: []\nentities: []\nstates: []\nactions: []\n'
        'invariants: []\nintegrations: []\nscenarios: []\n'
        'intentional_differences: []\nunknowns: []\n',
        encoding="utf-8",
    )

    (root / "state-model.md").write_text(
        f"# State model — {args.replica}\n\n## States\n\n## Transitions\n\n## Invariants\n",
        encoding="utf-8",
    )
    (root / "data-contracts.md").write_text(
        f"# Data contracts — {args.replica}\n\n## Entities\n\n## Inputs and outputs\n\n## Persistence\n",
        encoding="utf-8",
    )
    (root / "acceptance-scenarios.md").write_text(
        f"# Acceptance scenarios — {args.replica}\n\n"
        "Each release-blocking scenario must define prerequisites, normalized actions, required observables, tolerance, evidence, and status.\n",
        encoding="utf-8",
    )
    (root / "implementation-handoff.md").write_text(
        f"# Independent implementation handoff — {args.replica}\n\n"
        "## Scope\n\n## Prohibited source material\n\n## Architecture constraints\n\n"
        "## Build tasks\n\n## Intentional differences\n\n## Open unknowns\n",
        encoding="utf-8",
    )

    parity = {
        "schema_version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "observed_product": args.product,
        "replica": args.replica,
        "artifact_tested": "",
        "scenarios": [],
        "unknowns": [],
        "release_gate": "not-evaluated",
    }
    (root / "parity-manifest.json").write_text(
        json.dumps(parity, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
