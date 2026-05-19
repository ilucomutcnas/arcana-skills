# Examples — Animation & Motion

## Example: subtle interaction lift

```css
.interactive-card {
  transition:
    transform var(--duration-fast) var(--ease-standard),
    box-shadow var(--duration-fast) var(--ease-standard);
}

.interactive-card:hover {
  transform: translateY(-2px);
}
```

## Example: reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 1ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 1ms !important;
    scroll-behavior: auto !important;
  }
}
```

## Example: dismiss / reveal panel

```css
.panel {
  opacity: 0;
  transform: translateY(0.5rem);
  transition:
    opacity var(--duration-base) var(--ease-standard),
    transform var(--duration-base) var(--ease-standard);
}

.panel[data-open="true"] {
  opacity: 1;
  transform: translateY(0);
}
```

## Stage 3.5 Extension: Panel, Tooltip, and Loading Motion

### Motion Budget Table

| Element | Property Animated | Duration | Easing | Reduced-Motion Fallback | Performance Risk |
|---|---|---:|---|---|---|
| Filter Panel | transform + opacity | 180ms | `cubic-bezier(.2,.8,.2,1)` | instant show/hide | low |
| Tooltip | opacity + translateY | 120ms | ease-out | opacity only (80ms) | low |
| Loading Bars | transformX | 700ms loop | linear | static shimmer disabled | medium |

### Before

```css
.panel[data-open="true"] {
  top: 0;
  height: 100%;
  transition: top 220ms ease, height 220ms ease;
}
```

### After

```css
.panel {
  transform: translateY(0.5rem);
  opacity: 0;
  transition: transform 180ms var(--ease-standard), opacity 180ms var(--ease-standard);
}
.panel[data-open="true"] { transform: translateY(0); opacity: 1; }
```

### Acceptance Criteria
- No width/height/top/left animation unless justified and measured.
- Reduced-motion path is fully functional (not hidden content).
- Mid-tier mobile trace shows no noticeable jank during panel + tooltip interactions.
