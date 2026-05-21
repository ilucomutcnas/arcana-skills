# Example: Raster Retouch Pipeline

## Scenario
An ecommerce team needs updated product images for a reusable bottle launch. The current photos have uneven lighting, visible dust, and inconsistent crop framing across channels.

## Before/After Requirements (Text)
### Before
- Gray backdrop has wrinkles and tone variation.
- Bottle cap has dust specks and small glare hotspots.
- Framing differs between SKU color variants.

### After
- Clean neutral background (#F5F5F5 equivalent visual target).
- Dust and hotspot cleanup without changing material realism.
- Standardized framing with consistent headroom and centering.
- Export variants for web PDP, Instagram feed, and thumbnails.

## Workflow Plan
1. Preserve original files in `/source/original/`.
2. Create layered working masters per SKU in `/source/working/`.
3. Perform retouch on separate cleanup layers.
4. Normalize exposure and white balance using adjustment layers.
5. Produce channel-specific crops from approved master.
6. Export variant matrix and run QA review.

## Export Variant Table
| Channel | Dimensions | Format | Target size | Notes |
|---|---:|---|---:|---|
| Product detail page | 2000x2000 | WebP + JPG fallback | <= 450 KB (WebP) | Keep edge detail for zoom |
| Instagram feed | 1080x1350 | JPG | <= 350 KB | 4:5 crop, preserve label center |
| Thumbnail grid | 400x400 | WebP | <= 80 KB | Sharp silhouette at small size |

## QA Checklist
- [ ] Originals untouched and archived.
- [ ] Working files retain masks/adjustments.
- [ ] No clipping in highlights on metallic cap.
- [ ] Background edges free from halo artifacts.
- [ ] Exports meet file-size and dimension constraints.
- [ ] Metadata includes editor, edit date, and source ID.

## Stage 3.8 Example: Product Image Cleanup Release

### Source Image and Edit Log
| Source ID | Working file | Non-destructive edits | Editor | Status |
|---|---|---|---|---|
| SKU-BTL-001 | `bottle-blue-v3.psd` | Dust cleanup layer, WB curve, mask refinement | Retoucher A | Approved |
| SKU-BTL-002 | `bottle-black-v2.psd` | Background neutralization, glare reduction | Retoucher B | Approved after R2 |
| SKU-BTL-003 | `bottle-green-v2.psd` | Crop realignment + exposure correction | Retoucher A | Approved |

### Variant Matrix (Web / Social / Marketplace)
| Channel | Size | Format | Compression target | Result |
|---|---|---|---|---|
| Web PDP | 2000x2000 | WebP + JPG | WebP <=450 KB | Pass |
| Instagram | 1080x1350 | JPG | <=350 KB | Pass after recompression |
| Marketplace | 1600x1600 | JPG | <=500 KB, white background | Pass |

### Crop/Color/Profile/Compression Checks
- [x] Crop safety overlays preserve logo and product cap in all aspect ratios.
- [x] Color profile standardized to sRGB for all exports.
- [x] Histogram check confirms no clipped highlights.
- [x] Compression artifacts reviewed at 100% and 200% zoom.

### Visual Diff and Revision Log
| Round | Diff finding | Severity | Owner | Resolution |
|---|---|---|---|---|
| R1 | Halo artifact on right bottle edge | Major | Retoucher B | Refined mask feather and re-exported |
| R2 | Instagram variant exceeded file size by 42 KB | Major | Production designer | Adjusted quality from 88 to 82 |
| R3 | Minor color warmth mismatch on SKU-BTL-003 | Minor | Retoucher A | White balance tweak + approved |

### Acceptance Gates and Final Approval
- Creative lead: approved visual quality and brand consistency.
- Channel ops: approved dimension/compression constraints.
- QA gate owner: confirmed revision log + evidence pack complete.
- Final state: **Approved for handoff** to `creative-asset-handoff` after `creative-qa-gate-automation` release gate pass.
