---
name: "brand-bible"
title: "Brand Bible"
description: "Use for writing user-facing copy following brand voice guidelines with empathetic tone, concise style, active voice, and context-appropriate personality."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/brand-bible.md`
- Examples: `examples/skills/brand-bible.md`

## Linked Package Files

- Adjacent: `references/skills/brand-guidelines-anthropic.md` — for visual identity alignment
- Adjacent: `references/skills/ad-creative.md` — for ad copy that matches brand voice
- Validation: `references/skills/design-orchestration.md` — for review pipeline

## Purpose

Write user-facing copy that follows brand voice guidelines. Covers error messages, settings pages, documentation, billing flows, onboarding text, loading states, empty states, and any user-facing string that must follow the brand personality.

## When to Use

- When writing error messages (users are frustrated — be empathetic)
- When writing settings pages (users are focused — be clear)
- When writing documentation (users need information — be precise)
- When writing billing/payment flows (users need trust — be reassuring)
- When writing onboarding or empty states (users are exploring — be encouraging)

## Workflow

1. Identify the context and user emotional state.
2. Choose the appropriate tone: empathetic, direct, playful, or reassuring.
3. Write concise, active-voice copy.
4. Validate against the quality standards below.
5. Test the copy in context for readability and clarity.

## Quality Standards

- Be concise — use the fewest words needed.
- Be direct — tell users what to do, not what they can do.
- Use active voice — "Save your changes" not "Your changes will be saved."
- Avoid jargon — use simple words users understand.
- Be specific — "3 errors found" not "Some errors found."

Brand personality traits:
- Empathetic snark — direct frustration at the situation, never the user.
- Self-aware — acknowledge the absurdity of software when appropriate.
- Fun but functional — personality enhances, never obscures meaning.
- Earned moments — only use personality when users have time to appreciate it.

## Technical Rules

- Error messages: state what happened, why, and what to do next.
- Loading states: short, optionally playful.
- Empty states: guide toward the first action.
- Settings: labels should be self-explanatory without help text.
- Billing: precise, no ambiguity about charges or dates.

## Validation

- Verify copy is concise and uses active voice.
- Check that tone matches the user context.
- Confirm personality does not obscure meaning.
- Test for clarity with someone unfamiliar with the feature.

## Restrictions

- Do not use personality in high-stress contexts (billing errors, data loss).
- Do not direct humor at the user.
- Do not use jargon without explanation.

## Output Requirements

- Provide copy strings ready for implementation.
- Include context notes (where this string appears, user state).
- Keep variants minimal — one recommended string plus one alternative.
