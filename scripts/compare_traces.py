#!/usr/bin/env python3
"""Compare normalized original and replica event traces and write a parity report."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_events(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("events")
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError(f"{path} must contain an event array or an object with an events array")
    return data


def canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def label(event: dict[str, Any], index: int) -> str:
    return str(event.get("step_id") or f"index-{index}")


def escape_md(value: str) -> str:
    return value.replace("|", "\\|")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("original", type=Path)
    parser.add_argument("replica", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    original = load_events(args.original)
    replica = load_events(args.replica)
    rows: list[tuple[str, str, str]] = []
    mismatches = 0
    total = max(len(original), len(replica))

    for index in range(total):
        if index >= len(original):
            rows.append((label(replica[index], index), "mismatch", "extra replica event"))
            mismatches += 1
            continue
        if index >= len(replica):
            rows.append((label(original[index], index), "mismatch", "missing replica event"))
            mismatches += 1
            continue
        left, right = original[index], replica[index]
        step = label(left, index)
        if label(right, index) != step:
            rows.append((step, "mismatch", f"step id differs: replica={label(right, index)}"))
            mismatches += 1
        elif canonical(left) == canonical(right):
            rows.append((step, "match", "normalized events are equal"))
        else:
            changed = sorted(set(left) | set(right))
            changed = [key for key in changed if canonical(left.get(key)) != canonical(right.get(key))]
            rows.append((step, "mismatch", "different fields: " + ", ".join(changed)))
            mismatches += 1

    status = "MATCH" if mismatches == 0 else "MISMATCH"
    report = [
        "# Trace parity report",
        "",
        f"**Result:** {status}",
        f"**Original events:** {len(original)}",
        f"**Replica events:** {len(replica)}",
        f"**Mismatches:** {mismatches}",
        "",
        "| Step | Status | Detail |",
        "|---|---|---|",
    ]
    for step, row_status, detail in rows:
        report.append(f"| {escape_md(step)} | {row_status} | {escape_md(detail)} |")
    text = "\n".join(report) + "\n"

    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(args.output)
    else:
        print(text, end="")
    return 0 if mismatches == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
