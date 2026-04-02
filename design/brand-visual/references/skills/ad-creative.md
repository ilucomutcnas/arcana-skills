---
name: "ad-creative"
title: "Ad Creative"
description: "Use for generating high-performing ad copy at scale — headlines, descriptions, and primary text with character-count validation, angle-based organization, and performance iteration."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/ad-creative.md`
- Examples: `examples/skills/ad-creative.md`
- Platform specs: `ad-creative__references/platform-specs.md`
- Generative tools guide: `ad-creative__references/generative-tools.md`
- Evaluation data: `ad-creative__evals/evals.json`

## Linked Package Files

- Adjacent: `references/skills/brand-bible.md` — for brand voice consistency in ad copy
- Adjacent: `references/skills/brand-guidelines-anthropic.md` — for brand-compliant creative
- Validation: `references/skills/design-orchestration.md` — for pipeline review flow

## Purpose

Generate high-performing ad creative at scale. Produce headlines, descriptions, and primary text that drive clicks and conversions. Organize output by angles with character counts. Use performance data to iterate and improve.

## When to Use

- When generating or iterating paid ad copy at scale
- When producing headlines, descriptions, primary text, or structured ad variation sets
- When performance data should inform the next round of creative
- When validating ad copy against platform character limits

## Workflow

1. Pull performance data from previous campaigns (if available).
2. Identify winning patterns (hooks, angles, proof points).
3. Generate new variations organized by angle, with character counts.
4. Validate against platform specs (see `ad-creative__references/platform-specs.md`).
5. Deliver organized output with iteration log.

For AI-assisted creative generation workflows, see `ad-creative__references/generative-tools.md`.

## Quality Standards

- Descriptions should complement headlines, not repeat them.
- Use descriptions to add proof points, handle objections, reinforce CTAs, or add genuine urgency.
- Always include character counts next to each copy variant.
- Flag any line that exceeds platform character limits.
- Organize output by angle for easy scanning.

## Technical Rules

- Google RSA headlines: 30 characters max. Descriptions: 90 characters max.
- Facebook primary text: 125 characters recommended (up to 63,206 allowed). Headlines: 40 characters.
- LinkedIn headlines: 70 characters. Descriptions: 100 characters.
- Always check `ad-creative__references/platform-specs.md` for the latest platform limits.
- For AI+Remotion batch workflows, see `ad-creative__references/generative-tools.md`.

## Validation

- Verify every headline and description has a character count.
- Flag any line exceeding platform limits.
- Check that angles are varied and non-overlapping.
- Confirm descriptions complement (not repeat) headlines.

## Restrictions

- Do not generate copy without character counts.
- Do not exceed platform character limits without explicit flagging.
- Do not produce duplicate angles disguised as variation.

## Output Requirements

- Organize by angle, with character counts per line.
- Include an iteration log when iterating on previous rounds.
- Flag over-limit lines with suggested trims.
