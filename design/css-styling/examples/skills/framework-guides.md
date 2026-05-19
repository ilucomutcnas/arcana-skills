# Examples — Framework Guides

## Example: Tailwind discipline

Good:
- utilities used consistently
- tokens mapped through theme
- repeated patterns extracted into components or class abstractions

Bad:
- massive unreadable class chains
- arbitrary values everywhere
- color usage detached from theme

## Example: CSS Modules fit

Good for:
- card component variants
- form field shells
- isolated dashboard widgets

Less good for:
- platform-wide token governance
- typography rules that should remain global

## Stage 3.5 Extension: Framework Selection and Migration Matrix

| Approach | Best Fit | Tradeoff | Migration Note |
|---|---|---|---|
| Vanilla CSS | small/static pages | global collision risk | introduce layers before scaling |
| SCSS | complex shared mixins | nesting bloat risk | cap nesting depth at 2 |
| Tailwind | rapid product UI | class sprawl risk | enforce semantic tokens in config |
| CSS Modules | isolated widgets | cross-page reuse friction | keep tokens global |
| CSS-in-JS | dynamic theme logic | runtime overhead | restrict to truly dynamic cases |

Decision example: dashboard widgets use CSS Modules, tokens remain global, Tailwind only for shadcn/ui shell.

### Mixing Rejection Criteria
Reject if raw Tailwind arbitrary values, SCSS globals, and inline styles are combined without ownership model and token contract.
