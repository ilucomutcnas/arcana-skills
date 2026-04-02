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
