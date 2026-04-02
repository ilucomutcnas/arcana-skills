# Routing Guide

Use this guide to decide which extracted file to open.

## Rules

- Open `references/skills/<slug>.md` for full methodology and validation rules.
- Open `examples/skills/<slug>.md` for sample code and usage patterns.
- Always apply `shared-rules/STYLE-GUARDRAILS.md` across all CSS tasks.

## Quick Navigation

### CSS Architecture
- **foundations** -> `references/skills/foundations.md`
- **framework-guides** -> `references/skills/framework-guides.md`
- **language-conventions** -> `references/skills/language-conventions.md`

### Layout and Components
- **layout-responsive** -> `references/skills/layout-responsive.md`
- **general-ui-styling** -> `references/skills/general-ui-styling.md`
- **animation-motion** -> `references/skills/animation-motion.md`

### Page Types
- **one-pager-landing** -> `references/skills/one-pager-landing.md`
- **site-wide-systems** -> `references/skills/site-wide-systems.md`

### Review and Quality
- **css-review-audit** -> `references/skills/css-review-audit.md`

### Frontend Engineering
- **frontend-alchemy** -> `references/skills/frontend-alchemy.md`
- **tailwind-design-system** -> `references/skills/tailwind-design-system.md`
- **frontend-dev-guidelines** -> `references/skills/frontend-dev-guidelines.md`

## Routing by Task Type

- **New design system** -> foundations + framework-guides + tailwind-design-system
- **Component styling** -> general-ui-styling + foundations + animation-motion
- **Landing page** -> one-pager-landing + layout-responsive + animation-motion
- **CSS audit** -> css-review-audit + foundations + framework-guides
- **Tailwind project** -> tailwind-design-system + framework-guides + foundations
- **React app** -> frontend-dev-guidelines + frontend-alchemy + tailwind-design-system
- **Site consistency** -> site-wide-systems + foundations + layout-responsive

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md)
- [`manifest.json`](manifest.json)
