# Example: Creative Asset Handoff

## Scenario
A cross-functional team is delivering assets for a spring campaign: social creatives, product hero imagery, icon updates, and a one-page PDF overview for partners.

## Final Folder Tree
```text
spring-campaign-delivery/
  source/
    vectors/
    raster-working/
    layout/
  exports/
    web/
    social/
    print/
    app/
  docs/
    delivery-manifest.md
    usage-notes.md
    provenance-and-licensing.md
  previews/
    contact-sheet.pdf
```

## Delivery Manifest (Sample)
| File | Purpose | Format | Version | Source link | Owner | Approval |
|---|---|---|---|---|---|---|
| `exports/app/spring-icons-nav-home-outline-v2.svg` | App navigation icon | SVG | v2 | `source/vectors/nav-icons.fig` | Design Systems | Approved |
| `exports/web/spring-hero-bottle-main-web-v3.webp` | Web hero image | WebP | v3 | `source/raster-working/hero-bottle.psd` | Brand Design | Approved |
| `exports/social/spring-launch-carousel-01-v1.jpg` | Social carousel panel | JPG | v1 | `source/layout/social-carousel.ai` | Social Team | Approved |
| `exports/print/spring-partner-onepager-v1.pdf` | Partner handout | PDF | v1 | `source/layout/partner-onepager.indd` | Marketing Ops | Approved |

## Acceptance Checklist
- [ ] Source folders contain editable masters for all exports.
- [ ] Export folders include only approved release artifacts.
- [ ] Manifest reconciles 1:1 with exported files.
- [ ] Licensing and usage constraints documented.
- [ ] Version numbers updated for changed assets.
- [ ] Stakeholder notes include engineering and marketing guidance.

## Handoff Note (Short)
"Attached is the approved spring campaign delivery package v3. All exports are reconciled in `docs/delivery-manifest.md`, source files are separated under `source/`, and usage constraints are documented in `docs/provenance-and-licensing.md`."

## Stage 3.8 Example: Final Campaign Package Governance

### Release Manifest Snapshot
| Asset Group | Source path | Export path | Status | Notes |
|---|---|---|---|---|
| Ad copy and channel text | `source/content/` | `exports/social/`, `exports/ad-platform/` | Approved | Includes legal-cleared copy IDs |
| Product imagery | `source/raster-working/` | `exports/web/`, `exports/marketplace/` | Approved | Non-destructive masters retained |
| Icon set | `source/vectors/` | `exports/app/` | Approved | Token-aligned SVG + PNG fallback |
| Partner PDF | `source/layout/` | `exports/print/` | Approved | Metadata and footer disclaimers validated |

### Ownership and Signoff Matrix
| Team | Owner | Signoff state | Evidence |
|---|---|---|---|
| Creative production | Creative ops lead | Approved | QA gate report v5 |
| Design systems | DS manager | Approved | SVG acceptance checklist |
| Marketing | Campaign manager | Approved | Channel usage instructions |
| Legal/compliance | Counsel reviewer | Approved | Claim/disclaimer review log |

### Source/Export Separation Notes
- `source/` contains editable PSD/AI/FIG/INDD and working markdown files only.
- `exports/` contains immutable release artifacts only.
- Every exported file maps to one source record in the manifest.

### Revision History
| Version | Change | Trigger |
|---|---|---|
| v3.0 | Initial approved delivery set | Launch freeze |
| v3.1 | Replaced one social image after crop fix | Late major issue from QA gate |
| v3.2 | Updated one partner PDF disclaimer line | Legal amendment |

### Rollback/Withdrawal Path
If post-release defect is found:
1. Mark impacted exports as withdrawn in manifest.
2. Move withdrawn assets to `/archive/withdrawn-v3.2/`.
3. Restore last approved version from `/archive/approved-v3.1/`.
4. Notify channel owners with replacement IDs.

### Late-Change Protocol
Any late change after signoff reopens `creative-qa-gate-automation`. No modified export is redistributed until blocker status is cleared and signoff matrix is re-stamped.
