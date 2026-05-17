# design-token-governance Example

## Token Change Request
Request: rename `color.brand.primary` to `color.action.primary` and add `color.action.primary.hover` for accessibility consistency.

## Token Decision Record
- Classification: major (consumer updates required)
- Board decision: approved with compatibility alias for one major cycle
- Owners: Design system lead, frontend platform lead

## Migration Plan
1. Release new semantic tokens and temporary aliases.
2. Update consuming libraries and product apps in two waves.
3. Enforce lint error on deprecated token usage after two sprints.

## Release Notes Snippet
"Introduced `color.action.primary` token family. `color.brand.primary` is deprecated and will be removed in v5.0.0. Use migration map in docs."

## QA Checklist
- Contrast checks for default/hover/disabled states
- Visual regression on top 20 components
- Token diff report reviewed by board
- Deprecated usage report trend decreasing weekly

## Rollback Plan
If regression rate exceeds 2% or contrast failures appear in production, revert alias removal and freeze deprecation enforcement until defects are resolved.
