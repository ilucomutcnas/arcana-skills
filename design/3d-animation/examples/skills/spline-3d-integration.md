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

## React/Next Spline Hero Integration Example

### Lazy-Load + Fallback Poster Flow
1. Render static poster image immediately.
2. Lazy import Spline component on client intersection.
3. Swap poster to live scene after `onLoad` event and keep poster for reduced-motion mode.

### Event Listener Lifecycle Cleanup
- Register Spline events (`mouseDown`, `mouseHover`) inside `useEffect`.
- Remove listeners on unmount and when scene instance changes.

### SSR Boundary Note
- Wrap Spline import with `dynamic(..., { ssr: false })` in Next.js.
- Keep text content server-rendered to avoid hydration mismatch.

### Mobile Performance Check Table

| Device Class | Target FPS | Fallback Trigger |
|---|---:|---|
| High-end mobile | >= 45 | none |
| Mid-range mobile | >= 30 | disable heavy autoplay camera |
| Low-end mobile | >= 24 | static poster only |

### Accessibility Alternative Content
- Provide semantic heading + summary outside canvas.
- Add keyboard-accessible CTA independent from Spline interaction.

