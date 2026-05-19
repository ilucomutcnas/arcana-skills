# packaging-release Reference

## When to Use
Use this mini-skill for Pretext tasks where **packaging-release** is the main decision driver.

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
- Verify package shape: dist files, entrypoints, exports map, and type declarations.
- Build correctness requires clean build + package smoke tests from consumer perspective.
- Release confidence checks include browser/perf/corpus evidence links, not build-only pass.
- Rollback vs fix-forward: rollback for API breakage, fix-forward for minor docs/demo gaps.

