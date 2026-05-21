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

## Stage 3.8 Example: Icon Set QA and Release

### Before/After SVG Snippet
```svg
<!-- Before -->
<svg width="31" height="30"><path d="M1.2 0.9 ... (420 points)" fill="#2A2A2A"/></svg>

<!-- After -->
<svg viewBox="0 0 24 24" role="img" aria-label="Home" data-token-fill="icon.primary">
  <path d="M4 11.5 12 4l8 7.5V20a1 1 0 0 1-1 1h-4v-5H9v5H5a1 1 0 0 1-1-1z"/>
</svg>
```

### Issue Taxonomy
| Category | Check | Result | Action |
|---|---|---|---|
| viewBox consistency | 24x24 required | 3 files failed | Reframed to `0 0 24 24` |
| Path complexity | <=250 points | 2 files exceeded | Simplified with manual node cleanup |
| Stroke/fill rules | token-based styling | 5 files had hard-coded hex | Replaced with token attrs |
| Naming/versioning | deterministic slug + version | 4 files had “Layer copy” names | Renamed to canonical scheme |
| Token alignment | fill/stroke maps | 1 icon used wrong accent token | Remapped to `icon.accent` |
| Accessibility labels | title/aria for semantic icons | 6 icons missing labels | Added `aria-label` and title metadata |

### Export Variants
| Variant | Output | Purpose | Gate |
|---|---|---|---|
| Source normalized | SVG | Engineering import | Must pass lint and render diff |
| Raster fallback | PNG 24/48 | Legacy clients/docs | Must match SVG silhouette |
| Sprite bundle | SVG sprite | Web performance path | Must preserve IDs/names |

### Signoff Gates
- Design system lead: approves geometry, naming, and token alignment.
- Engineering owner: approves import safety, sprite compatibility, and runtime rendering.
- Release ops: confirms manifest and evidence package forwarded to `creative-qa-gate-automation`.
