# Anti-Patterns

## Structural failures
- A "design systems" file that actually contains dashboards, email infrastructure, and backend architecture.
- Tokens defined after components are already shipping.
- Separate design names and code names for the same concept.
- Theme overrides that bypass semantic tokens.
- Components with dozens of boolean props instead of clear variants or slots.
- One team using primitives while another ships custom snowflakes.

## Token failures
- `blue-500` used as a product meaning instead of a semantic role.
- spacing scales that mix arbitrary pixels and semantic sizes without logic.
- typography styles named after pages instead of roles.
- duplicate tokens with slightly different values and no documented intent.

## Component failures
- components that own layout, content, and business logic all at once
- no disabled or focus-visible state
- interactive elements with only color differences
- too many variants created to patch bad defaults

## Governance failures
- no contribution model
- no versioning policy
- no deprecation path
- no review gate for additions to tokens or components
