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

## Stage 3.5 Extension: Account Surface Token/Layer Refactor

Account settings surfaces were using hardcoded brand blues and one `!important` override in `.plan-card__price`.

### Primitive -> Semantic Mapping

| Primitive Token | Semantic Token | Usage |
|---|---|---|
| `--blue-600` | `--text-accent` | Link/action text in account notices |
| `--gray-100` | `--surface-subtle` | Secondary panel background |
| `--gray-900` | `--text-primary` | Body copy and headings |
| `--space-4` | `--control-padding-inline` | Input/button horizontal padding |

### Before

```css
.plan-card__price {
  color: #1458ff !important;
}
```

### After

```css
@layer components {
  .plan-card__price {
    color: var(--text-accent);
  }
}
```

### Acceptance Checks
- Zero raw hex additions in `components/**/*.css` for this change set.
- No new `!important` declarations.
- Theme fallback verified in Safari 17 and Firefox latest.
- Alias `--text-link: var(--text-accent);` retained for one release cycle.

### Handoff Notes
- Frontend: run token-lint and report any direct primitive usage in components.
- Design: approve semantic token mapping for billing, profile, and security account sections.
