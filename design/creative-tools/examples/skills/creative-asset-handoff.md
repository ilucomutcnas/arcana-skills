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
