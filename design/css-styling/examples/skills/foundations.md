# Examples — Foundations

## Example: token structure

```css
:root {
  --color-bg: #ffffff;
  --color-fg: #101418;
  --color-muted: #6b7280;
  --color-border: #d9dee5;

  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;

  --radius-sm: 0.375rem;
  --radius-md: 0.75rem;
  --radius-lg: 1rem;

  --duration-fast: 120ms;
  --duration-base: 180ms;
  --duration-slow: 280ms;
  --ease-standard: cubic-bezier(.2,.8,.2,1);
}
```

## Example: layer ownership

```css
@layer reset, tokens, base, layout, components, utilities;

@layer tokens {
  :root { --container-max: 72rem; }
}

@layer layout {
  .container {
    width: min(100% - 2rem, var(--container-max));
    margin-inline: auto;
  }
}
```

## Example: bad pattern

```css
.homepage .hero .content .card .title span {
  color: #1458ff !important;
}
```

Why bad:
- too specific
- page-dependent
- hardcoded color
- override debt
