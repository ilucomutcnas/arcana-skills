# Design System Framework Mapping — Examples

## Plain CSS / SCSS
- Prefer CSS custom properties for tokens.
- Separate token layer from component layer.

## CSS Modules
- Use modules for local component styling.
- Do not redefine global token meaning in modules.

## Tailwind
- Extend the theme with semantic tokens.
- Avoid spraying raw utility values when a system token exists.
- Use component abstractions for repeated patterns.

## CSS-in-JS
- Keep token access centralized.
- Avoid ad hoc inline objects that drift from system naming.

## Validation Question

Can design decisions be traced from system token to rendered UI regardless of stack?
