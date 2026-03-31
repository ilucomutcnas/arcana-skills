# Domain Package Construction Standard

## Purpose

This standard defines how to create, normalize, compress, and maintain a domain package.

A domain package is a structured folder that represents one professional or operational domain. It is not a single skill and not a random file collection. It is a routed package made of connected mini-skills, references, examples, resources, and package-level control files.

The package must remain:
- structurally consistent,
- internally linked,
- English-only,
- selectively loadable,
- usable at scale,
- small enough to remain maintainable.

---

## Definition of a Domain

A domain is a named folder representing one connected area of work.

A domain contains:
- one main router file,
- package-level control files,
- resource files,
- mini-skill reference files,
- mini-skill example files,
- optional linked asset folders.

The domain name is the canonical package name.  
All package files, routing records, manifests, and linked package references must remain consistent with that domain identity.

A domain is composed of multiple mini-skills.  
Mini-skills are focused sub-capabilities inside the broader domain. They are separated for routing, clarity, and selective loading, not because real work happens in isolation.

---

## Required Domain Package Structure

Each domain package must be a folder with a stable, normalized domain name.

At minimum, the package must include:

- `SKILL.md`
- `composition-protocol.md`
- `self-diagnostic-protocol.md`
- `resources/skill-catalog.md`
- `resources/routing-guide.md`
- `resources/asset-link-index.md`
- `resources/manifest.json`
- `references/skills/*.md`
- `examples/skills/*.md`

Optional additional folders may exist when needed, such as:
- asset folders,
- script folders,
- auxiliary references,
- templates,
- implementation notes.

Do not add optional folders unless they provide real routing or execution value.

---

## Hard File Count Limit

The total number of files in a single domain package must never exceed **199 files**.

This is a strict upper limit.

Count all files inside the domain package, including:
- root files,
- files inside `resources/`,
- files inside `references/skills/`,
- files inside `examples/skills/`,
- files inside any asset, reference, script, or support folders.

If the package would exceed 199 files, reduce the file count before finalizing the package.

---

## What To Do If File Count Exceeds 199

If the initial input, source package, or transformed package contains more than 199 files, reduce the package size by merging, consolidating, or removing low-value duplication.

Use the following reduction strategy:

### Preferred Reduction Targets
1. Merge weak, tiny, or highly overlapping example files.
2. Merge near-duplicate example files that describe the same operational pattern.
3. Merge small support files when they are only useful together.
4. Remove redundant duplicate files.
5. Remove stale or purely decorative files that add no routing or execution value.
6. Consolidate repeated dependency files when the package uses multiple near-identical small dependency manifests.
7. Remove low-value extraction debris or placeholder files that should not exist in the final package.

### Avoid Reducing First
Do not start by merging:
- `SKILL.md`
- `composition-protocol.md`
- `self-diagnostic-protocol.md`
- `resources/skill-catalog.md`
- `resources/routing-guide.md`
- `resources/asset-link-index.md`
- `resources/manifest.json`
- core mini-skill reference files in `references/skills/`

Treat `references/skills/*.md` as the source-of-truth layer whenever possible.

### Reduction Principle
Reduce duplication, not clarity.  
Do not merge files if the merge would damage routing quality, domain clarity, or execution usefulness.

---

## Required Actions After Merging or Removing Files

Whenever files are merged, renamed, removed, or replaced, update all affected package records immediately.

This includes:
- internal links,
- `SKILL.md`,
- `resources/skill-catalog.md`,
- `resources/routing-guide.md`,
- `resources/asset-link-index.md`,
- `resources/manifest.json`,
- linked package references inside mini-skills,
- references to example files,
- references to asset folders,
- file names and paths inside any package control file.

No stale references may remain.

Every package update that changes file structure must also update package linking.

---

## Linking Rules

Everything declared must be linked correctly.  
Everything linked must exist.

Check all of the following:
- every path resolves to a real file or folder,
- every example file reference is valid,
- every mini-skill reference file exists,
- every linked asset folder exists if declared,
- no file points to a deleted or renamed file,
- no package control file contains stale paths,
- no orphaned files remain undocumented if they still belong to the package.

All major package files must stay aligned:
- `SKILL.md`
- `resources/skill-catalog.md`
- `resources/routing-guide.md`
- `resources/asset-link-index.md`
- `resources/manifest.json`
- `references/skills/*.md`
- `examples/skills/*.md`

---

## English-Only Rule

All final package content must be in English.

If any content is not in English:
- translate it into English,
- normalize the user-facing text to English,
- remove mixed-language summaries, labels, or metadata,
- do not leave untranslated fragments in final files.

This applies to:
- titles,
- descriptions,
- summaries,
- purposes,
- when-to-use sections,
- labels,
- routing text,
- manifest fields,
- catalog entries,
- linked file descriptions.

If a technical string must remain unchanged, keep it only when required, and ensure surrounding explanatory text is in English.

---

## Naming Rules

### Domain Name
Each domain package must have one canonical domain name.  
The folder name must be stable, normalized, and machine-friendly.

### Mini-Skill Name
Each mini-skill must have its own canonical name.

Mini-skill names must be:
- stable,
- normalized,
- machine-friendly,
- consistent across all package files.

Do not use accidental source file names with unnecessary suffixes when normalizing.  
Prefer canonical package-safe naming.

### File Naming
Use descriptive, stable, normalized file names.

Examples:
- `references/skills/agent-memory-systems.md`
- `examples/skills/agent-memory-systems.md`

Avoid:
- random suffixes,
- broken file naming patterns,
- raw extraction names,
- temporary source names left in final output.

---

## Description Rules

Descriptions are written for discovery and auto-activation.

A description must:
- be in English,
- be concise,
- be high-signal,
- describe what the file is used for,
- support automatic activation or discovery,
- avoid decorative wording,
- avoid low-signal phrases,
- avoid trying to describe the entire package in excessive detail.

Descriptions should act as trigger text, not as a full specification.

### Domain Router Description
A domain router description should describe the domain and its adjacent activation scope.

Example pattern:
- "Use for [domain], [connected area], and adjacent tasks involving [key capabilities]."

### Mini-Skill Description
A mini-skill description should describe the focused capability of that mini-skill.

Example pattern:
- "Use for [specific task], including [core methods], [important execution features], and [relevant adjacent usage]."

---

## Required File Types and Their Required Content

## 1. Main Router File — `SKILL.md`

This is the main router for the domain package.

### Required Frontmatter Fields
The router must include:
- `name`
- `title`
- `description`
- `risk`
- `source`
- `date_added`

Optional fields may be included only if the package standard explicitly requires them.

### Required Sections
The main router should include:
- `## Purpose`
- `## Domain Coverage`
- `## How to Use`
- `## Multi-Skill Activation Guide`
- `## Package Structure`
- `## Mini-Skills Index`
- `## Validation`
- `## Output Requirements`

The router must remain concise.  
Do not turn it into a monolithic knowledge dump.

---

## 2. Composition Protocol — `composition-protocol.md`

This file defines the universal rules for selecting and combining mini-skills.

### Required Function
It must explain:
- how to identify the primary mini-skill,
- how to identify adjacent mini-skills,
- how to identify a validation mini-skill,
- how to combine them without loading the whole package.

### Scope Rule
This file is package-level and must remain reusable.

---

## 3. Self-Diagnostic Protocol — `self-diagnostic-protocol.md`

This file defines the tiered self-diagnostic procedure.

### Required Function
It must explain:
- quick integrity check,
- activated scope check,
- full package audit only when needed,
- how to classify severity,
- how to respond when issues are found.

### Important Rule
The self-diagnostic must not force full-package loading by default.

---

## 4. Skill Catalog — `resources/skill-catalog.md`

This file is the normalized catalog view of the package.

### Required Content
Each mini-skill entry should contain:
- numbering,
- canonical mini-skill name,
- summary,
- reference file path,
- examples file path,
- asset group paths if applicable.

### Summary Rules
Summaries must be:
- in English,
- complete,
- readable,
- plain,
- non-truncated,
- free from raw markdown debris,
- aligned with the actual mini-skill.

---

## 5. Routing Guide — `resources/routing-guide.md`

This file explains routing and composition behavior.

### Required Function
It must help the system navigate the package without loading the entire domain at once.

It should explain:
- how to choose the primary mini-skill,
- how to add adjacent mini-skills,
- how to bring in validation support,
- how to work selectively.

---

## 6. Asset Link Index — `resources/asset-link-index.md`

This file provides the complete link map for auxiliary folders and files.

### Required Function
It must describe where all non-core linked files live and how they are related to mini-skills.

Use it to prevent orphaned support files.

---

## 7. Manifest — `resources/manifest.json`

This is the machine-readable record of the package.

### Required Content
Each mini-skill record should include, where applicable:
- canonical name,
- title,
- description or summary,
- purpose,
- when-to-use,
- reference path,
- examples path,
- linked asset folders,
- status or structural metadata if required by the package design.

### Manifest Rules
The manifest must reflect the real package state.  
Do not leave stale records, broken paths, or dirty source text.

---

## 8. Mini-Skill Reference Files — `references/skills/*.md`

These are the source-of-truth files for each mini-skill.

### Required Frontmatter Fields
Each mini-skill reference file must include:
- `name`
- `title`
- `description`
- `risk`
- `source`
- `date_added`

### Required Sections
Each mini-skill reference file should include:
- `## Package Structure`
- `## Linked Package Files`
- `## Purpose`
- `## When to Use`
- `## Workflow`
- `## Quality Standards`
- `## Technical Rules`
- `## Validation`
- `## Restrictions`
- `## Output Requirements`

Additional sections may be included when truly useful, such as:
- capabilities,
- patterns,
- anti-patterns,
- sharp edges,
- related mini-skills.

Do not keep raw extraction artifacts or redundant source debris.

---

## 9. Mini-Skill Example Files — `examples/skills/*.md`

These files contain concrete execution material.

### Required Function
Use them for:
- commands,
- code examples,
- operational prompts,
- templates,
- structured checklists,
- execution patterns.

### Rules
- keep them practical,
- keep them readable,
- keep them directly usable,
- merge overlapping example files when file-count reduction is required.

---

## Cleanup Rules

When normalizing a domain package:
- remove duplicates,
- remove broken extraction artifacts,
- remove stale links,
- remove invalid paths,
- remove decorative low-value redundancy,
- add missing required structure,
- add missing required fields,
- rewrite incomplete or unusable descriptions and summaries,
- rewrite mixed-language text into English,
- preserve practical execution value.

Do not preserve bad source text just because it came from the source.

---

## Validation Rules

Before finalizing a domain package, verify all of the following:

- the domain package contains no more than 199 files,
- all required control files exist,
- all required file structures are correct,
- all user-facing content is in English,
- all links resolve,
- all referenced files exist,
- all naming is normalized,
- all summaries are usable,
- all descriptions are activation-ready,
- all package records are aligned,
- all merged or removed files are reflected in updated linking,
- no stale or orphaned records remain.

---

## Final Operating Standard

A domain package is not just a folder of markdown files.

It is a routed domain system with:
- a stable domain identity,
- a lightweight router,
- connected mini-skills,
- normalized references,
- executable examples,
- package-level control files,
- strict file-count discipline,
- enforced linking integrity,
- English-only usability,
- and scalable selective loading.

Build and maintain it accordingly.
