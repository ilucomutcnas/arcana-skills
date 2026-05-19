# foundations Example

Token/layer refactor for account surfaces.

- Introduced primitive scale tokens and mapped semantic tokens per theme.
- Split stylesheet into `@layer reset, base, components, utilities`.
- Removed component-local color literals and migrated to semantic token map.

## Acceptance Checks
- No unresolved legacy tokens in changed files.
- Dark/light theme screenshots match contrast targets.
- Component overrides remain inside `overrides` layer with migration tickets.

## Migration Notes
- Introduced compatibility aliases for one release cycle to prevent runtime breakage.
- Added lint checks that fail on new hard-coded color literals in component styles.
- Documented rollback path for any theme contrast regressions detected in QA.
