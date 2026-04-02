---
name: "language-handling"
title: "Language Handling for Writing"
description: "Controls multilingual input, translation fidelity, code-switching, and target-language consistency across writing tasks."
version: "1.0.0"
category: "Writing"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/language-handling.md`
- Examples: `examples/skills/language-handling.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — cross-skill style guardrails
- Adjacent: see `resources/routing-guide.md` for recommended combinations

# Language Handling for Writing

## Purpose
Handle multilingual input safely and intentionally.  
When a request contains more than one language, do not improvise. Detect the language setup, preserve meaning, and control the output language deliberately.

## Use This Skill Alongside Other Writing Skills
Apply it whenever:
- the input contains multiple languages
- the user asks for bilingual output
- part of the source text must remain untranslated
- cultural or tone fidelity matters
- a translated draft must keep the function of the original

## Step 1 — Detect the Language Architecture
Identify:
1. primary source language
2. secondary source language(s)
3. requested output language
4. fixed terms that must remain unchanged
5. whether the user wants:
   - translation
   - rewrite
   - localization
   - parallel bilingual text
   - tone-preserving adaptation

## Step 2 — Decide the Output Regime

### Single-Language Output
Use one target language consistently.  
Translate embedded fragments unless:
- they are names
- they are legal/company/product terms
- they are quoted material the user wants preserved
- they are culturally better left in original form

### Bilingual Output
Use parallel structure:
- original + translation
- or section-by-section bilingual blocks
Keep alignment clear. Do not mix languages unpredictably inside the same sentence unless code-switching is explicitly desired.

### Mixed-Language Source Cleanup
If the user's source text jumps between languages unintentionally:
- normalize it
- preserve meaning
- remove accidental mixing
- flag ambiguous phrases internally

## Tone Preservation Rules
When translating or adapting:
- preserve purpose before syntax
- preserve legal effect before elegance
- preserve marketing intent before literal wording
- preserve emotional tone without over-literal phrasing
- preserve journalistic caution and attribution markers

## Term Handling
Protect:
- names
- brands
- product names
- legal terms that should stay in source language if translation may distort meaning
- technical abbreviations
- quoted text when accuracy matters

When a term can be translated in more than one way, prefer:
1. the user's established terminology
2. the industry-standard equivalent
3. the clearer option for the target audience

## Language Quality Rules
- Avoid partial translation unless requested.
- Avoid hybrid grammar caused by literal transfer.
- Do not let one language leak its syntax into another.
- Make punctuation and date format appropriate to the target language when relevant.
- Keep register consistent.

## Special Cases

### Legal Writing + Translation
Preserve legal structure and flag when exact enforceability may depend on local drafting conventions.

### Journalistic Writing + Translation
Preserve attribution verbs, uncertainty markers, and factual distinctions.

### Marketing Writing + Translation
Localize for persuasion; do not cling to literal word order when it harms impact.

### Business Writing + Translation
Favor clarity, politeness norms, and local professional expectations.

### General Writing + Translation
Keep relationship tone natural. A literal translation that sounds stiff is a failed translation.

## Final Check
Ask internally:
- What is the main language of the final output?
- Is code-switching deliberate or accidental?
- Were key terms preserved correctly?
- Did the text keep the same job after translation?
