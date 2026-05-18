# components Example

## Scenario: Primary Button contract for commerce checkout

A checkout flow currently has 5 custom button implementations. The design-system team standardizes on one `Button` component for web and admin with clear API, accessibility states, and implementation handoff.

## Anatomy
- Container
- Label
- Optional leading icon
- Optional trailing icon
- Focus ring layer
- Loading spinner slot

## Variant Matrix
| Variant | Intent | Supported tones | Disabled behavior |
|---|---|---|---|
| `solid` | Primary action | brand, danger | Reduced contrast + no hover |
| `outline` | Secondary action | neutral, brand | Border reduced; text muted |
| `ghost` | Tertiary action | neutral | Background stays transparent |

## Sizes
- `sm` (32px min height)
- `md` (40px min height)
- `lg` (48px min height)

## States
- Default, hover, pressed, focus-visible, disabled, loading
- Controlled: `isLoading`, `isDisabled`
- Uncontrolled: internal pressed/hover visuals only

## Component API Contract
- Required: `children`
- Optional: `variant`, `tone`, `size`, `leadingIcon`, `trailingIcon`, `fullWidth`, `isLoading`, `isDisabled`, `onClick`
- Rule: icon-only usage requires `aria-label`

## Accessibility Notes
- Keyboard: Enter/Space activate
- Focus visibility: 3:1 ring contrast on all themes
- Touch targets: minimum 44x44 for mobile contexts
- Busy state: `aria-busy="true"` and loading text announced

## Anti-Patterns
- Button used as navigation link without `href`
- Spinner with no text change or announcement
- Brand-only color overrides bypassing semantic tokens

## Acceptance Criteria
- No custom CSS button classes in checkout pages
- All states pass visual + keyboard tests in light/dark themes
- Screen reader announces loading and disabled correctly

## Implementation Handoff Checklist
- Figma spec with anatomy and spacing tokens
- Variant matrix mapped to token names
- Storybook stories for all states + interaction tests
- QA test cases attached for keyboard, focus, and contrast
