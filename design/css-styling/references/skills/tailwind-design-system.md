---
name: "tailwind-design-system"
title: "Tailwind Design System"
description: "Use for building production-ready design systems with Tailwind CSS including tokens, component variants, semantic colors, shadcn/ui patterns, dark mode, and accessibility."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/tailwind-design-system.md`
- Examples: `examples/skills/tailwind-design-system.md`
- Implementation playbook: `tailwind-design-system__resources/implementation-playbook.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Adjacent: `references/skills/framework-guides.md` — for Tailwind within broader CSS strategy
- Adjacent: `references/skills/foundations.md` — for token architecture
- Adjacent: `references/skills/general-ui-styling.md` — for component state styling
- Validation: `references/skills/css-review-audit.md` — for review workflow

## Purpose

Build production-ready design systems with Tailwind CSS, including design tokens, component variants, responsive patterns, accessibility, shadcn/ui integration, dark mode, and semantic color systems.

For detailed implementation patterns, see `tailwind-design-system__resources/implementation-playbook.md`.

## When to Use

- When creating a component library with Tailwind
- When implementing design tokens and theming
- When building responsive and accessible components
- When standardizing UI patterns across a codebase
- When migrating to or extending Tailwind CSS
- When setting up dark mode and color schemes
- When using shadcn/ui components

## Workflow

1. Clarify goals, constraints, and design token requirements.
2. Define semantic color system with CSS variables.
3. Implement component variants using built-in variant props.
4. Apply Tailwind utility classes for layout only.
5. Use `cn()` for conditional class composition.
6. Validate against the rules below.

## Quality Standards

### Semantic Colors
Use semantic tokens, not raw color values: `bg-primary text-primary-foreground` not `bg-blue-500 text-white`. For status indicators, use Badge variants or semantic tokens like `text-destructive`.

### Built-in Variants First
Use component variant props before className overrides: `<Button variant="outline">` not manual border styling.

### className for Layout Only
Use className for positioning and spacing (`max-w-md`, `mx-auto`, `mt-4`), not for overriding component colors or typography.

### Utility Preferences
- `gap-*` instead of `space-x-*` / `space-y-*`
- `size-*` instead of `w-* h-*` when dimensions are equal
- `truncate` instead of `overflow-hidden text-ellipsis whitespace-nowrap`

### Dark Mode
Use semantic tokens — they handle light/dark via CSS variables. `bg-background text-foreground` not `bg-white dark:bg-gray-950`.

### Conditional Classes
Use the `cn()` utility for conditional or merged class names, not manual ternaries.

### Overlay Components
Never add manual z-index on Dialog, Sheet, Drawer, AlertDialog, DropdownMenu, Popover, Tooltip, HoverCard.

## Technical Rules

Customization hierarchy (in order of preference):
1. Built-in variants
2. Semantic color tokens
3. CSS variables in global CSS

For detailed patterns, tokens, and component examples, see `tailwind-design-system__resources/implementation-playbook.md`.

## Validation

- Verify semantic colors are used instead of raw values.
- Confirm built-in variants are preferred over className overrides.
- Check that className is used for layout only.
- Test dark mode and themed rendering.

## Restrictions

- Do not use raw Tailwind colors for status indicators.
- Do not override component styles with className when variants exist.
- Do not add manual z-index on overlay components.
- Do not use `dark:` color overrides when semantic tokens handle it.

## Output Requirements

- Tailwind-based components following semantic color system.
- Consistent use of variants and `cn()`.
- Dark mode support through CSS variables.
