# Spline 3D Integration — Examples

## Scene URL Format

```
https://prod.spline.design/XXXXXXXXXXXXXXXX/scene.splinecode
```

## Integration Guides

For detailed integration code, see the dedicated guide files:

- Vanilla HTML/JS: `spline-3d-integration__guides/VANILLA_INTEGRATION.md`
- React / Next.js / Vue: `spline-3d-integration__guides/REACT_INTEGRATION.md`
- Performance optimization: `spline-3d-integration__guides/PERFORMANCE.md`
- Debugging common problems: `spline-3d-integration__guides/COMMON_PROBLEMS.md`

## Code Examples

For working code examples, see the dedicated example files:

- Vanilla embed: `spline-3d-integration__examples/vanilla-embed.html`
- React wrapper component: `spline-3d-integration__examples/react-spline-wrapper.tsx`
- Interactive scene with events: `spline-3d-integration__examples/interactive-scene.tsx`

## Production Evidence Addendum

### Constraints
- Frame budget target: <= 16.6ms on desktop baseline, <= 25ms on mid-range mobile fallback path.
- Regression threshold: reject if draw calls or GPU memory increase > 15% without approval.
- Accessibility gate: reduced-motion path and non-pointer interaction fallback must be validated.

### Release Checks
1. Deterministic reproduction steps documented with exact parameter/state values.
2. Browser matrix logged (Chrome + Safari + Firefox + one mobile browser).
3. Before/after screenshots or metric notes recorded in PR description (no binary assets required in repository).
4. Rollback switch documented (feature flag, material fallback, or effect disable path).

