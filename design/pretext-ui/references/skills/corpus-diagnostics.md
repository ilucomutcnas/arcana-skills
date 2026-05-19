# corpus-diagnostics Reference

## When to Use
Use this mini-skill for Pretext tasks where **corpus-diagnostics** is the main decision driver.

## Operational Workflow
1. Confirm inputs, impacted files, and acceptance constraints.
2. Select commands/pages/scripts that produce verifiable evidence.
3. Record decision rules and blocking thresholds before implementation.
4. Capture QA checks, anti-patterns, and handoff expectations.

## Input Requirements
- Repro steps and affected script/font/width contexts where relevant.
- Expected output behavior and compatibility expectations.
- Evidence artifacts (tables, command logs, diff scope, risk notes).

## QA Checks and Constraints
- Validate against `shared-rules/ANTI-PATTERNS.md`.
- Reject ambiguous claims without measurable evidence.
- Ensure cross-skill handoff includes risks, unresolved questions, and rollback path.

## Failure Modes
- Narrowing scope too early and missing adjacent validation.
- Treating demo or benchmark evidence as optional for user-visible claims.
- Shipping behavior changes without documenting compatibility impact.

## Skill-Specific Notes

## Reference additions
- Maintain long-form canaries and width sweeps across representative script/font matrix.
- Probe design: isolate one hypothesis per run (line-break logic, measurement drift, bidi segmentation).
- Extractor questions: which token, width, script, or fallback font triggered mismatch?
- Script-sensitive handling: avoid cross-script generalization without corpus evidence.

