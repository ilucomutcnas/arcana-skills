# Raster Retouch Pipeline

## Purpose
Use this mini-skill for structured, non-destructive raster editing across product photos, social visuals, and campaign imagery. It prioritizes source preservation, controlled retouch boundaries, quality review, and export variants for downstream channels.

## When to Use
Use when you need to:
- Clean backgrounds or distractions in product photos.
- Correct exposure, white balance, or color cast safely.
- Resize or crop assets for multiple channels.
- Create platform-ready web/social/thumbnail derivatives.
- Deliver assets with provenance and quality traceability.

## Required Inputs
- Original source files (RAW/TIFF/PSD preferred; highest-quality JPG if constrained).
- Retouch brief with explicit allowed and disallowed edits.
- Target channel matrix (website, marketplace, social placements).
- Color/profile requirements (sRGB, Adobe RGB, CMYK for print).
- Output dimension and compression targets.

## Source Preservation Rules
- Never overwrite originals.
- Store immutable source under `/source/original/`.
- Perform edits in layered working files (`.psd`, `.xcf`, or equivalent).
- Maintain versioned milestones (`v1`, `v2`, `v3`) with edit logs.
- Keep retouch notes: operator, date, operations applied.

## Non-Destructive Editing Rules
- Use adjustment layers, masks, and smart objects.
- Keep healing/clone operations on separate retouch layers.
- Avoid flattening until final export stage.
- Preserve alpha channel when transparency is required.
- Keep crop decisions reversible until approval.

## Retouching Boundaries
Allowed (if requested):
- Dust/scratch cleanup.
- Background isolation and edge refinement.
- Exposure, white balance, and contrast correction.
- Minor perspective correction.

Disallowed unless explicitly approved:
- Altering product shape/functionality.
- Removing legally required marks/labels.
- Over-smoothing that misrepresents texture.
- Compositing misleading contextual elements.

## Resolution and Aspect-Ratio Handling
- Define a master aspect ratio first.
- Produce channel-specific crops from master non-destructively.
- Upscaling beyond 125% requires explicit approval.
- Keep key subject safe area within platform crop zones.

## Color and Profile Considerations
- Default web/social exports to sRGB unless otherwise required.
- Convert only at export boundary; keep working space documented.
- Check skin/product critical colors against reference swatches.
- Confirm black levels and highlight clipping using scopes/histograms.

## Export Variant Strategy
Create a variant matrix with:
- channel/platform,
- dimensions,
- file format,
- target file size,
- compression quality,
- transparency requirement.

Typical set:
- Web hero: WebP + JPG fallback.
- Social feed: JPG or PNG depending on transparency/text edges.
- Thumbnail: aggressively optimized JPG/WebP.
- Marketplace: platform-compliant JPG/PNG with required background rules.

## Review Checklist
- [ ] Original source preserved and unchanged.
- [ ] Retouch operations traceable by layer/log.
- [ ] No destructive flattening in working master.
- [ ] Color/profile conversion validated.
- [ ] Exports meet size and resolution targets.
- [ ] Subject edges clean at 100% and 200% zoom.
- [ ] Metadata/provenance fields populated.

## Failure Modes
- Flattened master without editable layers.
- Aggressive compression introducing artifacts.
- Color shifts caused by profile mismatch.
- Haloing or masking artifacts around subjects.
- Crops that remove critical product detail.
- Missing provenance notes for edited assets.


## Stage 3.8 Extension: QA Gates, Revision Loops, and Release Evidence

### QA Gates
- Require non-destructive edit logs tied to source IDs and working file versions.
- Validate color/profile conversions per target channel (sRGB/CMYK as specified).
- Validate crop safety zones and subject framing for each channel variant.
- Validate channel-specific dimensions and compression thresholds.
- Require metadata/provenance fields (editor, edit date, source lineage).
- Capture visual diff notes for each revision round.

### Revision-Loop Rules
- Track defects by type: artifacting, color shift, framing, profile mismatch, size overflow.
- Each fix must reference affected layer/export and include recheck status.
- Late visual changes reopen final gate checks for all downstream variants.

### Evidence Requirements
- Edit log table, export matrix, and compression audit results.
- Visual diff/revision ledger with severity and owner.
- Final acceptance signatures from creative and channel owners.

### Acceptance/Rejection Gates
Accept when originals are preserved, edits are traceable, exports satisfy channel specs, and visual QA is approved.
Reject when masters are flattened destructively, profile mismatches remain, or channel constraints fail.

### Integration and Handoff
Provide revision ledger and final export evidence to `creative-qa-gate-automation`.
After approval, package source/export sets and usage notes through `creative-asset-handoff`.

