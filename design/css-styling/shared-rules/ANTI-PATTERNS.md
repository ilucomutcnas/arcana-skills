# CSS Anti-Patterns

## Architectural anti-patterns

- Giant global stylesheet with unrelated concerns mixed together
- Component styling overridden from page files without clear contract
- Styling coupled to DOM depth instead of component API
- Deep selector chains used as dependency management

## Code anti-patterns

- `!important` as a routine tool
- Magic numbers with no rationale
- Arbitrary z-index escalation
- Unbounded nesting in SCSS
- Duplicated media queries across random files
- Multiple conflicting transition declarations
- Random utility sprawl without naming strategy
- Mixing presentational and semantic class naming inconsistently

## UX anti-patterns

- Hover-only affordances on critical interactions
- Invisible focus states
- Tiny hit targets
- Layout shifts on hover
- Decorative animation that slows reading or task completion
- Color contrast that depends on “modern aesthetic” rather than readability

## Performance anti-patterns

- Animating width, height, top, left when transform would do
- Excessive box-shadow layering on large lists
- Backdrop blur used everywhere
- Heavy filters on scrolling surfaces
- Loading large custom fonts without fallback strategy

## Team anti-patterns

- No token governance
- No spacing scale
- No breakpoint policy
- No styling review checklist
- No examples of preferred patterns
