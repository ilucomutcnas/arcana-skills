# Examples — Layout & Responsive

## Example: fluid section spacing

```css
.section {
  padding-block: clamp(3rem, 5vw, 6rem);
}
```

## Example: auto-fit card grid

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(18rem, 100%), 1fr));
  gap: clamp(1rem, 2vw, 1.5rem);
}
```

## Example: content container

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

## Stage 3.5 Extension: Responsive Dashboard Card-Grid Refactor

### Width-State QA Table

| Width | Expected Columns | Title Behavior | Overflow | Sticky Header |
|---:|---:|---|---|---|
| 320 | 1 | 2-line clamp | none | working |
| 375 | 1 | 2-line clamp | none | working |
| 768 | 2 | wrap allowed | none | working |
| 1024 | 3 | single-line truncate | none | working |
| 1440 | 4 | single-line truncate | none | working |

### Before

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}
```

### After

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(18rem, 100%), 1fr));
  gap: clamp(0.75rem, 1.8vw, 1.25rem);
}

@container cards (min-width: 48rem) {
  .card__title { white-space: nowrap; text-overflow: ellipsis; overflow: hidden; }
}
```

### Overflow QA Gates
- No horizontal scroll at 320-1440 widths.
- Sticky header remains pinned during vertical scroll.
- Long card titles clamp or truncate intentionally per width state.
- iOS Safari safe-area verified (`padding-top: env(safe-area-inset-top)`).
