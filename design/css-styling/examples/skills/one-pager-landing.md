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

## Stage 3.5 Extension: Launch Landing Section Plan

### Section Plan

| Section | Goal | Styling Priority | Risk |
|---|---|---|---|
| Hero | value proposition | strong heading contrast + primary CTA | oversized media pushes CTA below fold |
| Trust Block | credibility | logo rhythm + subtle separators | low contrast logos |
| Feature Band | explain benefits | alternating backgrounds + icon consistency | spacing drift |
| CTA | conversion | highest contrast action button | competing secondary actions |
| Footer | orientation | subdued hierarchy, legal links readable | cramped mobile columns |

### Mobile/Desktop QA

| Check | Mobile | Desktop |
|---|---|---|
| Hero CTA visible without scroll | pass | pass |
| Trust logos wrap cleanly | pass | pass |
| Feature cards equal rhythm | pass | pass |
| CTA contrast >= 4.5:1 | pass | pass |

### Performance-Sensitive Notes
- Above-the-fold CSS budget target: <= 45KB gzip.
- Avoid heavy animated background gradients in hero.
- Defer decorative section flourishes to non-critical CSS chunk.
