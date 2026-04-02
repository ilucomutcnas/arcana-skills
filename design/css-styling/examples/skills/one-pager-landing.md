# Examples — One-Pager & Landing

## Example: hero shell

```css
.hero {
  padding-block: clamp(5rem, 8vw, 8rem);
  background:
    radial-gradient(circle at top, color-mix(in srgb, var(--color-accent) 10%, transparent), transparent 45%),
    var(--color-bg);
}

.hero__inner {
  width: min(100% - 2rem, 74rem);
  margin-inline: auto;
  display: grid;
  gap: clamp(2rem, 5vw, 4rem);
  align-items: center;
}
```

## Example: CTA band

```css
.cta-band {
  padding: clamp(2rem, 4vw, 3rem);
  border-radius: var(--radius-lg);
  background: var(--color-surface-strong);
  color: var(--color-surface-strong-contrast);
}
```
