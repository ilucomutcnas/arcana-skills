# Universal CSS Guardrails

These apply across all CSS-related skills in this pack.

## Core principles

1. Style systems before style fragments.
2. Tokens before literals.
3. Components before page-level overrides.
4. Composition before specificity wars.
5. Responsive intent before breakpoint patching.
6. Motion must clarify, not decorate blindly.
7. Accessibility is part of styling quality, not a separate concern.

## Always do

- Prefer design tokens for color, spacing, radius, shadows, and duration.
- Keep specificity low and predictable.
- Prefer class-driven styling over ID selectors.
- Use semantic naming where the codebase supports it.
- Define layout primitives once and reuse them.
- Ensure focus states are visible and intentional.
- Respect reduced motion preferences.
- Test hover, active, disabled, error, loading, empty, and dark-mode states where applicable.
- Document non-obvious styling constraints near the source.

## Never do

- Do not hardcode random hex values throughout the codebase.
- Do not create one-off spacing values without system justification.
- Do not use `!important` unless there is a documented escape hatch case.
- Do not stack selectors until maintenance becomes impossible.
- Do not animate layout-heavy properties when transform/opacity can do the job.
- Do not hide focus outlines without a real replacement.
- Do not solve architecture problems with selector tricks.
- Do not mix multiple styling systems carelessly in the same surface.

## Validation checklist

Before finalizing CSS:
- Is there a reusable pattern instead of a one-off patch?
- Is this aligned with the token system?
- Will another engineer understand why this exists in 6 months?
- Does it behave correctly across states and viewport ranges?
- Is performance acceptable on lower-end devices?
