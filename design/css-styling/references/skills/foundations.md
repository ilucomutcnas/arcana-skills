# foundations

## Core Governance
- Separate primitive tokens (`--space-4`, `--gray-900`) from semantic tokens (`--surface-card`, `--text-muted`).
- Maintain explicit cascade layers: `reset`, `base`, `components`, `utilities`, `overrides`.
- Keep reset rules minimal and accessibility-safe (font inheritance, list semantics, form controls).

## Naming and Token Constraints
- Primitive names are scale-based; semantic names are role-based.
- Disallow component names in primitive token namespace.
- Theme variables must map semantic tokens, not raw colors in components.

## Layering Boundaries
- `base` defines typographic rhythm and global spacing defaults.
- `components` owns reusable UI blocks only.
- `utilities` are low-specificity single-purpose helpers.
- `overrides` are temporary and ticket-linked with expiry owner.

## Workflow
1. Audit current token collisions and specificity hotspots.
2. Create migration table old token -> semantic token.
3. Move rules into layer boundaries with visual regression snapshots.
4. Run dark/light theme and high contrast checks.
5. Record adoption progress and deprecated token cutoff date.

## Diagnostics and Compatibility
- Validate `@layer` fallback strategy for older browsers (progressive enhancement).
- Use computed-style checks for token resolution across themes.
- Verify focus outline contrast after reset updates.

## Anti-Patterns
- Global `!important` utilities.
- Component files redefining global typography tokens.
- Mixing brand-specific color literals directly in page CSS.
