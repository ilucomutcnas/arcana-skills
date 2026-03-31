# Domain Package, Router, and Mini-Skill Working Instructions

## Scope

These instructions define the required working rules for creating, updating, validating, and maintaining domain packages, routers, mini-skills, references, examples, manifests, and related package files.

These instructions apply globally across all domains. They are not specific to any one package or mini-skill.

---

## Core Principles

1. Treat every domain package as a routed system, not as a flat document collection.
2. Treat every mini-skill as part of a connected domain, not as an isolated unit.
3. Keep the main router lightweight and navigational.
4. Store deep guidance outside the main router.
5. Use selective loading and linked navigation instead of loading the entire package at once.
6. Preserve consistency, traceability, and structural integrity across all package files.
7. Keep the package fully usable in English.
8. Ensure that all declared files, paths, and links are valid.

---

## Language Rules

1. All package content must be in English.
2. If any content appears in a language other than English, translate it into English.
3. Do not leave mixed-language summaries, descriptions, comments, labels, or routing text.
4. Normalize obvious non-English fragments, broken phrases, or untranslated metadata.
5. If a source contains non-English content that must be preserved for technical reasons, add an English explanation or normalize the user-facing text to English.

---

## Structural Rules

1. Every file must follow its expected structure.
2. Do not invent arbitrary section orders.
3. Preserve the standard section sequence for each file type unless the package standard explicitly requires otherwise.
4. Keep naming stable and consistent across package files.
5. Use normalized file names and normalized skill names.
6. Do not leave raw source artifacts, placeholders, or accidental formatting remnants in final files.
7. Remove duplicate or redundant sections when they do not add routing or execution value.
8. Add missing required sections when they are necessary for package consistency.

---

## Router Rules

1. The main `SKILL.md` must remain concise.
2. The router must act as the entry point for the domain package.
3. The router must not become a monolithic knowledge dump.
4. The router should contain:
   - frontmatter,
   - purpose,
   - domain coverage,
   - how to use,
   - multi-skill activation guidance,
   - package structure,
   - mini-skills index,
   - validation,
   - output requirements.
5. The router must link to the deeper files instead of duplicating all details inline.
6. The router must support efficient routing across mini-skills without forcing the entire package to load at once.

---

## Mini-Skill Rules

1. Every mini-skill must have a clear and bounded purpose.
2. Every mini-skill must use the required mini-skill file structure.
3. Every mini-skill must be written in English.
4. Every mini-skill must have a usable description for activation and discovery.
5. Every mini-skill must preserve the package-level structure expectations where required by the package standard.
6. Every mini-skill must be connected to:
   - the main router,
   - its examples file,
   - any declared asset folders if they exist.
7. Mini-skills must not contain broken references to files that do not exist.
8. Mini-skills must not contain raw source debris such as:
   - unfinished lines,
   - truncated summaries,
   - placeholder text,
   - duplicated headings,
   - accidental markdown artifacts,
   - inline extraction debris,
   - mixed formatting styles that reduce usability.

---

## References and Examples Rules

1. Deep guidance belongs in `references/skills/*.md`.
2. Concrete commands, code, prompts, and operational patterns belong in `examples/skills/*.md`.
3. Do not overload the main router with long examples or long implementation details.
4. If a mini-skill contains substantial code, commands, or usage patterns, move them into the examples file.
5. If a mini-skill contains long conceptual or operational guidance, keep it in the reference file.
6. Use the reference file for explanation and the examples file for execution patterns.
7. Keep the split clean and deliberate.

---

## Linking Rules

1. Everything that is declared must be linked correctly.
2. Everything that is linked must exist.
3. Every declared path must point to a real file or folder.
4. Every package file must be reachable through the routing structure.
5. Check for:
   - broken links,
   - missing files,
   - wrong file names,
   - wrong folder names,
   - stale paths,
   - orphaned files,
   - references to deleted content.
6. All package links must be internally consistent across:
   - `SKILL.md`,
   - `resources/skill-catalog.md`,
   - `resources/routing-guide.md`,
   - `resources/asset-link-index.md`,
   - `resources/manifest.json`,
   - `references/skills/*.md`,
   - `examples/skills/*.md`.
7. If a file is referenced in one package control file, verify whether it should also be reflected in the other package control files.

---

## File Existence and Integrity Rules

1. Verify that all declared files exist.
2. Verify that all expected core package files exist.
3. Verify that all declared examples files exist.
4. Verify that all declared reference files exist.
5. Verify that all declared asset folders exist when referenced.
6. Do not keep references to non-existent files.
7. Do not keep file entries that cannot be resolved.
8. If a file is missing but required, either:
   - create it,
   - remove the broken reference,
   - or report the issue clearly.

---

## Consistency Rules

1. Keep summaries, purpose fields, and usage guidance aligned across package files.
2. Do not allow router, catalog, and manifest data to drift apart.
3. If a mini-skill is renamed, update all linked package files.
4. If a file is merged, update all links and package records accordingly.
5. If a file is removed, remove or update all stale references.
6. Keep the same canonical skill name everywhere it is referenced.
7. Keep style, naming, and phrasing consistent across the package.

---

## Description Rules

1. The description should support discovery and auto-activation.
2. The description should be domain-relevant and concise.
3. The description should not try to explain the entire package in full detail.
4. The description should act as a high-signal trigger, not as a full specification.
5. Avoid vague, decorative, or low-signal descriptions.
6. Prefer descriptions that clearly state what the file is used for.

---

## Purpose Rules

1. The purpose should explain what the file is responsible for.
2. The purpose should be specific and operational.
3. The purpose should not be empty, generic, or decorative.
4. The purpose should reflect the real role of the file inside the package.
5. Use purpose to clarify function, not to repeat the file title.

---

## Summary Rules

1. Summaries must be complete and readable.
2. Summaries must be in English.
3. Summaries must not be truncated.
4. Summaries must not contain raw markdown debris.
5. Summaries should be plain, concise, and useful for routing.
6. Remove artifacts such as:
   - leading bullets,
   - stray blockquote markers,
   - raw bold markers,
   - unfinished sentences,
   - ellipses caused by extraction,
   - non-English fragments.
7. If a usable summary does not exist, write a new one.

---

## Domain Coverage Rules

1. Every domain package should explain what the domain covers.
2. Domain coverage should explain that a domain is made of connected mini-skills.
3. Domain coverage should explain that mini-skills are separated for routing and selective loading.
4. Domain coverage should explain that real tasks often require more than one mini-skill.
5. Keep domain coverage reusable, clear, and domain-agnostic where possible.

---

## Multi-Skill Activation Rules

1. Do not treat mini-skills as isolated when the task spans multiple concerns.
2. For non-trivial tasks, use the composition protocol.
3. Prefer:
   - 1 primary mini-skill,
   - at least 2 adjacent mini-skills,
   - 1 validation mini-skill.
4. Use broader combinations only when the task requires them.
5. Do not default to loading the whole package.
6. Use selective, scope-aware activation.

---

## Self-Diagnostic Rules

1. Always begin with tiered self-diagnostic for non-trivial tasks.
2. Do not perform a full package audit by default.
3. Use:
   - Quick Integrity Check,
   - Activated Scope Check,
   - Full Package Audit only when needed.
4. Verify package integrity before relying on the package.
5. If issues are found, classify severity and report them clearly.
6. If the issue is critical, do not imply full confidence in the result.
7. If the issue is non-critical but material, inform the user before continuing.

---

## Cleanup Rules

1. Remove duplicated content when it adds no value.
2. Remove redundant raw sections copied from source material when the same intent is already represented cleanly.
3. Remove extraction artifacts and malformed text.
4. Remove stale references to external structures that are no longer part of the current package design.
5. Keep the package lean, but do not remove functional information that supports real use.
6. If something is missing and necessary, add it.
7. If something is duplicated and unnecessary, remove it.

---

## Package Optimization Rules

1. Keep the number of files reasonable.
2. Prefer merging weak, tiny, highly overlapping example files when appropriate.
3. Do not merge files if doing so damages routing clarity or domain structure.
4. Do not optimize file count at the expense of package usability.
5. Preserve references as the source of truth when possible.
6. Reduce duplication, not clarity.

---

## Manifest Rules

1. The manifest must reflect the actual package.
2. Update the manifest when files are added, removed, merged, or renamed.
3. Keep manifest records aligned with the real reference and examples files.
4. Include purpose, when-to-use, and linked assets where applicable.
5. Do not leave stale or dirty manifest values.
6. Normalize manifest entries to the same English-only standard as the rest of the package.

---

## Catalog Rules

1. The skill catalog must stay aligned with the router and manifest.
2. Keep numbering, naming, summaries, references, examples, and assets accurate.
3. Normalize summaries to a consistent style.
4. Do not allow catalog entries to drift from actual package content.

---

## Output Rules

1. When generating or updating files, provide final content in a copy-paste-ready format.
2. When examples or references should be split, provide them as separate files.
3. When a file needs to be replaced, provide the final replacement file.
4. When a package file is updated, ensure all linked files remain consistent.
5. Prefer final, usable output over commentary-heavy output.

---

## Quality Standard

Every package update should satisfy the following:

- English-only user-facing content
- valid file structure
- correct linking
- existing referenced files
- clean and normalized summaries
- consistent naming
- proper routing
- no broken paths
- no stale package records
- no unnecessary duplication
- no unresolved placeholders
- no raw extraction artifacts
- efficient selective loading
- package-level integrity preserved

---

## Final Operating Rule

Do not treat package editing as simple text editing.

Treat it as structured domain-system maintenance:
- preserve routing,
- preserve integrity,
- preserve consistency,
- preserve selective loading,
- preserve usability,
- preserve real-world execution value.
