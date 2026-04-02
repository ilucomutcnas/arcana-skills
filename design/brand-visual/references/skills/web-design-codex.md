---
name: "web-design-codex"
title: "Web Design Codex"
description: "Use for reviewing web interface files for compliance with Vercel's Web Interface Guidelines, outputting findings in terse file:line format."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/web-design-codex.md`
- Examples: `examples/skills/web-design-codex.md`

## Linked Package Files

- Adjacent: `references/skills/brand-bible.md` — for brand voice alignment in UI copy
- Adjacent: `references/skills/design-orchestration.md` — for review pipeline integration
- Validation: `references/skills/brand-guidelines-anthropic.md` — for brand compliance checks

## Purpose

Review web interface files for compliance with Vercel's Web Interface Guidelines. Fetch the latest guidelines from the source, read specified files, check against all rules, and output findings in terse `file:line` format.

## When to Use

- When reviewing web UI files for design guideline compliance
- When checking frontend code against Vercel's Web Interface Guidelines
- When auditing frontend components for design consistency
- When performing design code review

## Workflow

1. Fetch the latest guidelines from the source URL: `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`
2. Read the specified files (or prompt the user for files or a glob pattern).
3. Apply all rules from the fetched guidelines to the files.
4. Output findings using the format specified in the guidelines (terse `file:line` format).

If no files are specified, ask the user which files to review.

## Quality Standards

- Fetch fresh guidelines before each review — do not rely on cached versions.
- Apply all rules from the fetched content, not a subset.
- Output must follow the terse `file:line` format specified in the guidelines.
- Cover every file in the specified scope.

## Technical Rules

- Guidelines source: `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`
- Use WebFetch to retrieve the latest rules before each review.
- The fetched content contains all rules and output format instructions.
- Apply rules as defined in the fetched document — do not add or remove rules.

## Validation

- Verify guidelines were fetched successfully before starting review.
- Confirm all specified files were checked.
- Check that output format matches the terse `file:line` specification.

## Restrictions

- Do not review files without first fetching the latest guidelines.
- Do not invent rules not present in the fetched guidelines.
- Do not reformat findings outside the specified output format.

## Output Requirements

- Findings in terse `file:line` format as specified by the guidelines.
- All specified files covered.
- Summary of total findings count.
