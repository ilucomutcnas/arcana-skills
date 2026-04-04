# Library Architecture — Examples

## Example: System Design Task Routing

**Task:** "I need to change the core line-break behavior for a shaping-sensitive script."

**Route:**
1. library-architecture — core engine guardrails
2. browser-accuracy — fresh browser evidence
3. corpus-diagnostics — corpus canaries
4. research-log — earlier failed experiments

**Why:** The work touches core engine behavior, needs fresh browser evidence, needs corpus canaries, and should respect earlier failed experiments.

## Validation Checklist

- Does the change preserve the fast `layout()` path?
- Does it belong in preprocessing instead of line layout?
- Does it widen the public API only when a real consumer proves the need?
- Does it preserve browser-facing behavior for `white-space: normal` and explicit `pre-wrap` support?
