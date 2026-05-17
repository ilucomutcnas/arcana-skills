# Example: Vector Workflow Automation

## Scenario
A product design team provides 18 navigation icons exported from mixed tools. Engineering reports inconsistent viewports, random names, and oversized path complexity. The request is to clean and export the set for a React icon package.

## Realistic Request
"Normalize this icon set to a 24x24 grid, align strokes to our token rules, simplify excessive paths, and produce SVG + PNG fallback exports with a manifest for handoff."

## Expected Output Plan
1. Intake and map source files to canonical names.
2. Normalize viewport/grid/stroke settings.
3. Run path simplification pass with manual spot checks.
4. Apply token-compatible color strategy.
5. Export delivery variants and manifest.
6. Perform QA checks in browser and design tool preview.

## Execution Checklist
- [ ] All icons mapped to canonical slug list.
- [ ] Every icon uses `viewBox="0 0 24 24"`.
- [ ] Stroke width normalized to approved token value.
- [ ] Decorative fragments removed.
- [ ] Filled/outlined state variants named consistently.
- [ ] SVG and PNG exports generated for each icon.
- [ ] Handoff manifest includes owner, date, version, and notes.

## Sample Naming and Export Table
| Icon intent | Canonical file name | Variant | Export formats | Notes |
|---|---|---|---|---|
| Dashboard home | `icon-nav-home-v1.svg` | outline | SVG, PNG 24, PNG 48 | Primary nav icon |
| Dashboard home active | `icon-nav-home--active-v1.svg` | filled | SVG, PNG 24, PNG 48 | Selected state |
| Search | `icon-nav-search-v1.svg` | outline | SVG, PNG 24, PNG 48 | Includes 1.5px stroke |
| Notifications | `icon-nav-bell-v1.svg` | outline | SVG, PNG 24, PNG 48 | Bell clapper simplified |

## QA Gate
- [ ] No icon exceeds defined path/point complexity threshold.
- [ ] SVG renders match PNG previews.
- [ ] Tokenized color assignment verified in light/dark preview.
- [ ] File naming is deterministic and import-safe.
