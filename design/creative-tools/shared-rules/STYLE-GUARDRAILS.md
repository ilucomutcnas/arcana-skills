# Creative Tools Style Guardrails

These shared rules standardize output quality across `design/creative-tools` mini-skills. Focus on tool-aware instructions, reproducible edits, and safe file handling rather than one-off artistry.

## 1) Make workflow steps tool-specific and explicit
- Name the target tool or tool class when behavior differs (vector editor, raster editor, PDF editor, layout suite).
- Describe action sequences in operational order: inspect -> duplicate -> adjust -> verify -> export.
- Avoid abstract directions that omit where in the tool the operation occurs.
- If multiple tools are viable, provide a preferred route plus one fallback.

## 2) Write prompts and edit instructions with measurable intent
- State desired output before method details.
- Include concrete constraints: dimensions, alignment, color mode, resolution, compression, and transparency.
- Separate non-negotiable requirements from optional refinements.
- Keep terminology consistent across steps so operators can execute without reinterpretation.

## 3) Default to non-destructive editing
- Duplicate source files or create versioned working copies before edits.
- Prefer adjustment layers, masks, linked objects, and reversible operations.
- Preserve source data for text, vector paths, and smart objects where supported.
- Document when destructive edits are unavoidable and why.

## 4) Handle PDF and image inputs safely
- Confirm whether PDF edits are structural (text/vector) or appearance-only (overlay/raster).
- For image operations, specify color space and bit depth expectations when relevant.
- Note OCR dependency when editable text may not exist.
- Avoid assumptions that every PDF or image is fully editable in place.

## 5) Preserve file provenance and revision trace
- Record source filename, revision stamp, and transformation intent in handoff notes.
- Distinguish original assets from generated derivatives.
- Use deterministic naming conventions for iterative exports.
- Keep references to imported assets explicit so replacements can be traced.

## 6) Define export settings by destination
- Specify output format per use case (print proof, web upload, social share, archival source).
- Include critical settings: DPI/PPI, compression level, color profile, bleed/crop marks, font embedding or outlining requirements.
- Provide quality-size tradeoff guidance when bandwidth/platform limits apply.
- Require a final preflight check before delivery.

## 7) Require output verification checkpoints
- Add visible checks: alignment, crop boundaries, clipping, artifacting, and text legibility.
- Add metadata checks: dimensions, profile, file size, page count, and font substitution warnings.
- Confirm that key objects remained editable when required by workflow.
- If automation is used, include manual spot checks for high-risk regions.

## Quick pre-delivery checklist
- [ ] Steps are tool-aware and operationally ordered.
- [ ] Instructions include measurable output constraints.
- [ ] Non-destructive workflow was used by default.
- [ ] PDF/image editability assumptions were validated.
- [ ] File provenance and revisions are traceable.
- [ ] Export settings match destination requirements.
- [ ] Visual and metadata verification checks are complete.
