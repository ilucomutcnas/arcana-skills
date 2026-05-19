# Examples — General UI Styling

## Example: button states

```css
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  min-height: 2.75rem;
  padding-inline: var(--space-4);
  border: 1px solid transparent;
  border-radius: var(--radius-md);
  background: var(--color-accent);
  color: var(--color-accent-contrast);
  transition:
    background-color var(--duration-fast) var(--ease-standard),
    transform var(--duration-fast) var(--ease-standard),
    box-shadow var(--duration-fast) var(--ease-standard);
}

.button:hover { transform: translateY(-1px); }
.button:active { transform: translateY(0); }
.button:focus-visible { outline: 2px solid var(--color-focus); outline-offset: 2px; }
.button:disabled { opacity: 0.55; cursor: not-allowed; }
```

## Example: form field shell

```css
.field {
  display: grid;
  gap: var(--space-2);
}

.field__label {
  font-weight: 600;
}

.field__input {
  min-height: 2.75rem;
  padding: 0.75rem 0.875rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
}
```

## Stage 3.5 Extension: Settings Dashboard Styling Pass

### Component State Matrix

| Component | default | hover | active | focus-visible | disabled | error | loading |
|---|---|---|---|---|---|---|---|
| Button | solid primary | raise shadow-1 | shadow-0 | ring + offset | opacity + cursor | n/a | spinner reserved slot |
| TextInput | neutral border | border emphasis | subtle inset | ring + border accent | muted bg + icon | red border + message | skeleton overlay |
| Select | neutral shell | chevron tint | pressed bg | ring + label tint | muted shell | red border + helper | width preserved |
| DataCard | clean panel | border accent | n/a | focus-within ring | muted text/icon | status badge | pulse placeholder |

### Corrected State Pattern

```css
.field__input[data-state="error"] {
  border-color: var(--border-danger);
  background: color-mix(in srgb, var(--surface-default) 92%, var(--danger-50));
}

.field__input:focus-visible {
  outline: 2px solid var(--focus-ring);
  outline-offset: 2px;
}
```

### Acceptance Criteria
- Focus-visible states remain clearly visible on all controls.
- Disabled states include cursor + icon/opacity cues (not color alone).
- Error states include icon or text helper plus border change.
- Loading state reserves component height; no layout shift in forms.
