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
