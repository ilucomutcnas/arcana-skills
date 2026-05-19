# Examples — Naming & Language Conventions

## Good

```css
.article-card {}
.article-card__title {}
.article-card__meta {}
.article-card--featured {}
```

## Bad

```css
.statya-kartochka {}
.blue-title-final {}
.knopka_new2 {}
```

## Good comment

```css
/* Safari clips the focus ring here unless the overflow stays visible. */
```

## Bad comment

```css
/* This sets the color to blue. */
color: blue;
```

## Stage 3.5 Extension: Naming Cleanup Scenario

### Before/After Table

| Before | After | Rationale |
|---|---|---|
| `.knopka_new2` | `.settings-saveButton` | English, component-purpose naming |
| `.blue-title-final` | `.profileHeader__title` | avoids color-only and "final" suffixes |
| `.statya-kartochka` | `.articleCard` | removes transliteration |
| `.final-2` | `.billingPlan__summary` | meaningful role-based name |

### Comment Policy

Acceptable:
```css
/* Safari clips focus outline unless overflow remains visible on card shell. */
```

Rejected:
```css
/* Makes text red. */
color: red;
```

### Acceptance Criteria
- English class names only.
- No `final-2`, `new2`, transliteration, or color-only semantic names.
- Reserved prefixes documented (`u-`, `is-`, `js-`, `t-`) and used consistently.
