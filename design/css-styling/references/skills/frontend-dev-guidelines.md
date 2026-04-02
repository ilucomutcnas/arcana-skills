---
name: "frontend-dev-guidelines"
title: "Frontend Development Guidelines"
description: "Use for production-grade React/TypeScript development with Suspense-first data fetching, feature-based organization, strict TypeScript, and performance-safe defaults."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/frontend-dev-guidelines.md`
- Examples: `examples/skills/frontend-dev-guidelines.md`
- Deep references: `frontend-dev-guidelines__resources/` (9 files)
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`

## Linked Package Files

- Adjacent: `references/skills/frontend-alchemy.md` — for visual design systems
- Adjacent: `references/skills/tailwind-design-system.md` — for Tailwind styling
- Validation: `references/skills/css-review-audit.md` — for code review

Deep reference guides:
- `frontend-dev-guidelines__resources/common-patterns.md`
- `frontend-dev-guidelines__resources/complete-examples.md`
- `frontend-dev-guidelines__resources/component-patterns.md`
- `frontend-dev-guidelines__resources/data-fetching.md`
- `frontend-dev-guidelines__resources/file-organization.md`
- `frontend-dev-guidelines__resources/loading-and-error-states.md`
- `frontend-dev-guidelines__resources/performance.md`
- `frontend-dev-guidelines__resources/routing-guide.md`
- `frontend-dev-guidelines__resources/styling-guide.md`
- `frontend-dev-guidelines__resources/typescript-standards.md`

## Purpose

Build scalable, predictable, and maintainable React applications using Suspense-first data fetching, feature-based code organization, strict TypeScript discipline, and performance-safe defaults. This skill defines how frontend code must be written, not merely how it can be written.

## When to Use

- When creating React components or pages
- When adding new features to a React application
- When fetching or mutating data
- When setting up routing
- When addressing performance issues
- When reviewing or refactoring frontend code

## Core Architectural Doctrine (Non-Negotiable)

1. **Suspense is the default**: `useSuspenseQuery` is the primary data-fetching hook. No `isLoading` conditionals. No early-return spinners.
2. **Lazy load anything heavy**: routes, feature entry components, data grids, charts, editors, large dialogs.
3. **Feature-based organization**: domain logic in `features/`, reusable primitives in `components/`, cross-feature coupling forbidden.
4. **TypeScript is strict**: no `any`, explicit return types, `import type` always, types are first-class design artifacts.

## Workflow

### Frontend Feasibility & Complexity Index (FFCI)

Before implementing, assess:

| Dimension | Question |
|-----------|----------|
| Architectural Fit | Aligns with feature-based structure and Suspense model? |
| Complexity Load | How complex is state, data, and interaction logic? |
| Performance Risk | Introduces rendering, bundle, or CLS risk? |
| Reusability | Can be reused without modification? |
| Maintenance Cost | Hard to reason about in 6 months? |

```
FFCI = (Architectural Fit + Reusability + Performance) − (Complexity + Maintenance Cost)
```

Range: -5 to +15. Proceed if ≥ 6.

## Quality Standards

- Components use `React.FC<Props>` with explicit props interface.
- Non-trivial components are lazy loaded.
- Data fetched with `useSuspenseQuery`, wrapped in `<SuspenseLoader>`.
- No early returns for loading states.
- Handlers wrapped in `useCallback`.
- Default export at bottom of file.

## Technical Rules

- `useMemo` for expensive derivations.
- `useCallback` for passed handlers.
- `React.memo` for heavy pure components.
- Debounce search inputs (300-500ms).
- Cleanup effects to avoid leaks.
- Performance regressions are bugs.
- TypeScript strict mode enabled, no implicit `any`, explicit return types, JSDoc on public interfaces.

## Validation

Before finalizing code:
- FFCI ≥ 6
- Suspense used correctly
- Feature boundaries respected
- No early returns for loading
- Types explicit and correct
- Lazy loading applied
- Performance safe

## Restrictions

- No early loading returns — use Suspense boundaries.
- No feature logic in `components/` — keep in `features/`.
- No shared state via prop drilling — use hooks.
- No inline API calls — use dedicated API layer.
- No untyped responses.
- No multiple responsibilities in one component.

## Output Requirements

- Production-ready React/TypeScript code.
- Feature-based file organization.
- Suspense-first data fetching.
- Strict TypeScript throughout.
