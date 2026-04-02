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
