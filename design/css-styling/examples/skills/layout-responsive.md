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
