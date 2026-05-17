# Creative Tools Anti-Patterns

Use this anti-pattern guide to prevent common failures in `design/creative-tools` outputs. These issues often produce irreversible edits, unusable exports, or untraceable file history.

## 1) Destructive edits without backup or versioning
**Pattern:** Editing the only source file directly and flattening changes early.

**Why it fails:** Mistakes cannot be rolled back and future revisions become expensive.

**Better approach:** Start with a versioned duplicate and keep reversible layers/objects until final approval.

## 2) Tool hallucination in procedural guidance
**Pattern:** Referring to non-existent menu paths, unsupported features, or wrong tool capabilities.

**Why it fails:** Operators lose time, distrust instructions, and may execute risky workarounds.

**Better approach:** Keep steps grounded in known tool behaviors; when uncertain, state assumptions and offer a fallback method.

## 3) Unclear export settings
**Pattern:** “Export high quality” with no format, compression, profile, or resolution targets.

**Why it fails:** Deliverables vary unpredictably and may fail downstream platform or print requirements.

**Better approach:** Define exact export presets and acceptance thresholds for size and fidelity.

## 4) Hidden assumptions about file format editability
**Pattern:** Treating scanned PDFs as text-editable or assuming raster images contain vector shapes.

**Why it fails:** Workflows break midstream and deadlines slip.

**Better approach:** Validate editability first (OCR need, vector presence, layer availability) and choose the right process.

## 5) Overwriting source assets
**Pattern:** Saving derivative edits over originals without preserving provenance.

**Why it fails:** Original references are lost and legal/operational traceability weakens.

**Better approach:** Keep originals immutable and output derivatives with controlled naming conventions.

## 6) Skipping verification passes
**Pattern:** Delivering files without checking crop, profile, artifacts, substitutions, or page integrity.

**Why it fails:** Errors reach clients and rework multiplies.

**Better approach:** Run both visual and metadata checks before handoff.

## 7) Mixing manual and automated edits without audit trail
**Pattern:** Batch scripts and manual tweaks are combined with no record of what changed.

**Why it fails:** Results are hard to reproduce and defects are hard to isolate.

**Better approach:** Log automation inputs/outputs and summarize manual interventions in delivery notes.

## 8) One-size-fits-all instructions across tools
**Pattern:** Reusing the same editing recipe for Photoshop, Illustrator, Figma, PDF tools, and layout apps.

**Why it fails:** Tool differences cause inconsistent or impossible execution.

**Better approach:** Tailor steps to the tool class and call out equivalents when cross-tool adaptation is needed.

## Anti-pattern rejection checklist
- [ ] No destructive edits on sole originals.
- [ ] No unsupported or invented tool instructions.
- [ ] No ambiguous export directives.
- [ ] No unchecked format editability assumptions.
- [ ] No overwritten source assets.
- [ ] No skipped QA verification pass.
- [ ] No undocumented automation/manual hybrid edits.
- [ ] No tool-agnostic procedures where tool-specific steps are required.
