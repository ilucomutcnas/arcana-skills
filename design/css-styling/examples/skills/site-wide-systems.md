# Examples — Site-Wide Systems

## Example: page shell rules

```css
.page-shell {
  min-height: 100dvh;
  background: var(--color-bg);
  color: var(--color-fg);
}

.page-section {
  padding-block: clamp(3rem, 6vw, 6rem);
}

.content-measure {
  width: min(100%, 68ch);
}
```

## Example: semantic text roles

```css
.text-display { font-size: clamp(2.25rem, 5vw, 4.5rem); line-height: 0.98; }
.text-heading { font-size: clamp(1.5rem, 2.8vw, 2.5rem); line-height: 1.08; }
.text-body { font-size: 1rem; line-height: 1.6; }
.text-meta { font-size: 0.875rem; line-height: 1.4; color: var(--color-muted); }
```
