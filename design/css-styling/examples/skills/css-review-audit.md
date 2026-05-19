# Examples — Review & Audit

## Example: review prompt

Review this CSS using the CSS Review & Audit skill.
Return:
- exact problematic snippet
- issue category
- severity
- concrete fix
- note whether the fix belongs in tokens, component styles, layout primitives, or page styles

## Example: findings shape

```text
Snippet:
.sidebar .menu li a:hover { margin-left: 6px; }

Issue:
Layout-shifting hover state

Severity:
Medium

Fix:
Replace margin movement with a color or transform-based hover treatment that does not reflow nearby content.
```

## Stage 3.5 Extension: Audit Report Example

### Severity Model

| Level | Meaning | Example |
|---|---|---|
| S0 blocker | release risk | broken focus visibility on primary form flow |
| S1 major risk | high UX/perf impact | hover margin shifts causing reflow in nav |
| S2 maintainability debt | accumulative complexity | repeated token aliases with conflicting names |
| S3 cosmetic drift | low-risk inconsistency | card radius differs by 2px from system |

### Anti-Pattern Taxonomy
- specificity
- duplication
- accessibility
- performance
- responsiveness

### Remediation Backlog

| Owner | Fix | Evidence | Due Date |
|---|---|---|---|
| FE Platform | remove `!important` in billing cards | PR #812 diff + screenshot | 2026-05-30 |
| Design Systems | unify focus ring token | contrast report + keyboard video | 2026-06-02 |
| Web Perf | split unused marketing CSS | coverage report + LCP delta | 2026-06-05 |
