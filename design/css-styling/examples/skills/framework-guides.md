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
