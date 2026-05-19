# library-architecture Reference

## When to Use
Use this mini-skill for Pretext tasks where **library-architecture** is the main decision driver.

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

- Public API boundaries: separate `prepare` input normalization, `layout` line construction, and `analyze` diagnostics outputs.
- Contract rules: text measurement and line-break behavior must remain deterministic for identical font/script/width inputs.
- Metadata: preserve bidi levels and inline-flow segment offsets in any new layout metadata extension.
- Architecture checklist: API surface delta, internal ownership map, migration impact, test updates, and rollback strategy.
- Compatibility risks: changed metadata naming, optional-to-required fields, or altered default width handling.
