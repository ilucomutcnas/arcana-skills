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
