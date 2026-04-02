---
name: "css-review-audit"
title: "CSS Review & Audit"
description: "Structured workflow for reviewing CSS, identifying anti-patterns by severity, and proposing concrete fixes."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/css-review-audit.md`
- Examples: `examples/skills/css-review-audit.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — universal CSS guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — CSS anti-patterns reference

# CSS Review & Audit

## Purpose
Audit existing CSS and return actionable findings instead of vague criticism.

## Review output format

For each issue:
1. quoted snippet
2. issue type
3. why it matters
4. severity
5. concrete fix

## Issue categories

- token violation
- architecture smell
- specificity risk
- responsiveness gap
- accessibility styling issue
- state inconsistency
- motion/performance issue
- maintainability problem
- dead or duplicated styling
- framework misuse

## Severity scale

- Critical — causes broken behavior, inaccessible UI, or unstable system behavior
- High — creates large maintenance or UX debt
- Medium — should be corrected during normal refactor
- Low — polish issue, but still worth tracking

## Review doctrine

- Quote exactly.
- Do not complain without proposing a fix.
- Distinguish symptom from root cause.
- Prefer system repairs over one-line patches.
- If a rule should move to tokens, say so explicitly.

## Output example

```text
Snippet:
.card--promo .widget .title span { color: #0057ff !important; }

Issue:
Specificity risk + token violation

Why it matters:
This is hard to override safely and bypasses the color system.

Severity:
High

Fix:
Replace the hardcoded color with a semantic token and move the title styling into the component contract.
```
