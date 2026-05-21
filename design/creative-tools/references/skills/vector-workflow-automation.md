# Vector Workflow Automation

## Purpose
Use this mini-skill to run repeatable, semi-automated vector production workflows for icon sets, UI illustrations, and design-system assets. It focuses on SVG hygiene, normalization, naming consistency, complexity control, and export planning so assets are implementation-ready.

## When to Use
Use when at least one condition is true:
- You received inconsistent SVG files from multiple designers or tools.
- You must normalize an icon family to shared size, stroke, and alignment rules.
- You need design-token-aware vector output for product themes.
- Engineering needs predictable IDs, names, and export variants.
- You need a QA gate before handoff.

## Required Inputs
Collect these inputs before processing:
1. Source vectors (SVG, AI, Figma export package, or EPS converted to SVG).
2. Icon taxonomy (functional names, categories, state variants).
3. Grid and geometry rules (e.g., 24x24 viewport, 1.5px stroke baseline).
4. Design-token map (color tokens, stroke tokens, corner/shape rules).
5. Target outputs (inline SVG, sprite, PNG fallbacks, PDF spec sheet).
6. Consumption context (web app, mobile app, print system, docs site).

## SVG and Vector Hygiene Checklist
- Remove hidden layers, clipped leftovers, and off-canvas artifacts.
- Flatten unnecessary group nesting while preserving semantic grouping.
- Expand text to paths only when runtime fonts are not guaranteed.
- Remove editor metadata not required downstream.
- Ensure a consistent `viewBox` and no width/height mismatch.
- Replace hard-coded colors with token aliases where supported.
- Normalize stroke caps, joins, and miter limits to package standard.
- Avoid redundant points and zero-length path segments.

## Naming and Layer Conventions
Use stable kebab-case naming:
- Icon master: `icon-{category}-{name}-v{major}`
- State variants: `icon-{name}--active`, `--disabled`, `--filled`
- Size variants (only if needed): `icon-{name}-16`, `-20`, `-24`

Layer/group conventions:
- `base` for primary geometry.
- `accent` for optional highlights.
- `mask` only when masking is essential.
- `decorative` for non-semantic embellishments.

Reject files where names are opaque (`Layer 14 copy 2`) or where layers imply behavior that is not documented.

## Path Complexity and Accessibility
### Complexity targets
- Simple UI icons: prefer <= 12 paths and <= 250 total points.
- Detailed illustrations: define per-family limit before production.
- Avoid boolean residue and overlapping duplicates.

### Accessibility and semantics
- Provide title/description metadata when SVG is delivered as standalone assets.
- Mark decorative icons as decorative in usage notes.
- Ensure contrast intent is documented for token-driven theming.
- Avoid encoding critical meaning in color alone.

## Batch Export Decision Tree
1. Need CSS styling or dynamic theme control? -> export clean inline SVG.
2. Need legacy email/client support? -> include PNG fallback.
3. Need icon-font compatibility? -> evaluate only if existing stack requires it; otherwise keep SVG-first.
4. Need design review packet? -> generate PDF contact sheet from normalized SVG set.
5. Need docs-site preview? -> export SVG + 1x/2x PNG preview thumbnails.

## Design-System Compatibility Checklist
- Geometry aligns to shared grid.
- Stroke and fill tokens map to existing design tokens.
- Naming aligns to component/library naming.
- Size variants match component API expectations.
- State variants correspond to product interaction states.
- Changelog documents modified/removed symbols.

## QA Checks Before Handoff
- Every file opens without renderer warnings.
- ViewBox and visual bounds are consistent across set.
- No clipped shapes or missing fills in target renderers.
- Tokenized colors resolve correctly in light/dark themes.
- Exports match requested formats and pixel dimensions.
- Manifest includes file name, variant, version, and owner.

## Failure Modes and Rejection Criteria
Reject and rework when:
- Source SVG includes destructive rasterized vector substitutes.
- Inconsistent viewport sizes break shared component rendering.
- Paths are overly complex without visual benefit.
- Colors remain hard-coded despite token requirement.
- Naming/versioning prevents deterministic imports.
- Export package omits required fallback formats.

## QA Gate Integration
Use with `creative-qa-gate-automation` for pre-release checks, revision loops, stakeholder signoff, and evidence-pack generation.
