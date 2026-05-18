# foundations Example

## Scenario: Core token foundation for B2B dashboard suite

The team replaces ad-hoc values with a governed foundation model used by analytics, admin, and support products.

## Primitive Palette and Semantic Aliases
| Layer | Token | Value | Notes |
|---|---|---|---|
| Primitive | `color.blue.600` | `#1D4ED8` | Raw hue value |
| Primitive | `color.gray.900` | `#111827` | High-contrast text base |
| Semantic | `color.text.primary` | `{color.gray.900}` | Do not map directly to hex in UI code |
| Semantic | `color.action.primary` | `{color.blue.600}` | Action intent contract |

## Typography Roles
- `type.role.body.md`: default body copy
- `type.role.label.sm`: compact control label
- `type.role.heading.lg`: page section heading

## Spacing, Radius, Elevation, Breakpoints
- Spacing scale: 4, 8, 12, 16, 24, 32
- Radius scale: 2, 4, 8, 12
- Elevation: `elevation.100/200/300`
- Breakpoints: `sm=640`, `md=768`, `lg=1024`, `xl=1280`

## Primitive vs Semantic Distinction
- Primitives are implementation resources; semantic tokens are usage contracts.
- Components consume semantic tokens only.
- Theme overrides change semantic mappings, not component code.

## Foundation Review Checklist
- Naming follows namespace.category.role.state pattern
- Every semantic token maps to a primitive token
- No orphan primitives without known consumers
- Contrast checks pass for text/background combinations
- Breakpoints align with responsive layout system
