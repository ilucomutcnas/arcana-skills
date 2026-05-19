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

## Stage 3.5 Extension: Concrete Scenario

Naming cleanup scenario with before/after class names and comment policy decisions.

- Include before/after snippets for changed selectors or component classes.
- Include acceptance checklist with responsive, accessibility, and regression-safe styling criteria.
- Include handoff note format for frontend + design reviewers.
