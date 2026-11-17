# Clean-room-style implementation handoff

This workflow reduces accidental copying; it is not legal advice and does not guarantee a jurisdiction’s formal clean-room standard.

## Observation side

May retain authorized evidence needed to establish user-visible behavior. The deliverable to implementation should contain normalized facts and tests, not:

- source or decompiled code;
- copied UI assets, icons, sounds, fonts, or text;
- trademarks, product names, or confusingly similar identity;
- internal class, endpoint, table, package, or variable names unless they are a documented interoperability requirement;
- secrets, private user data, or unauthorized exports.

## Implementation side

Build from the normalized contract. Choose independent:

- names and copy;
- visual system and assets;
- source structure and algorithms;
- storage schema, except where a public interoperability format is required;
- error wording, provided the behavior remains useful and testable.

Keep a decision log that explains the new architecture and intentional differences.

## Handoff checklist

Before transferring the pack:

- identify every evidence-backed rule;
- label every inference and unknown;
- remove protected identity and assets;
- replace screenshots in implementation-facing documents with abstract wireframes when screenshots are not needed for behavior;
- state public interoperability constraints separately;
- state what the implementer must not inspect;
- define release-blocking acceptance scenarios.

When stronger separation is required, use separate agents or people and give the implementation side only the scrubbed handoff pack.
