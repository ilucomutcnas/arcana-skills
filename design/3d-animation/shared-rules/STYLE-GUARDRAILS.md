# 3D Animation Style Guardrails

These guardrails align all mini-skills in `design/3d-animation` around clear motion direction, feasible production constraints, and reliable handoff quality. Use them for concepting, shot planning, polish notes, and execution prompts.

## 1) Prioritize animation readability over spectacle
- State the **primary action** of every shot in one sentence.
- Keep one clear focal intent at a time: subject reveal, motion beat, or environment context.
- If multiple actions happen, define visual hierarchy (primary, secondary, background).
- Specify what the viewer should understand by the end of the shot.

## 2) Keep camera language controlled and intentional
- Define lens feel (wide, normal, telephoto) and camera behavior (locked, dolly, handheld-style).
- Avoid combining aggressive pan + tilt + roll + push unless the sequence explicitly requires disorientation.
- Use camera moves to support subject motion, not to replace it.
- Include start and end framing notes (for example: medium profile to close-up detail).

## 3) Preserve scene continuity across shots
- Track continuity anchors: light direction, character orientation, prop state, and environment condition.
- Maintain world scale and spatial relationships unless a transformation is intentional.
- Document transitions between shots (cut, match cut, wipe, dissolve) with purpose.
- Call out any continuity break as intentional stylization.

## 4) Specify timing and frame-level expectations
- Always include frame rate and target duration.
- Define beat timing in seconds or frame ranges (anticipation, impact, settle).
- For loops, specify loop boundaries and seamless requirements.
- If timing is exploratory, provide bounded alternatives rather than open-ended “play with speed.”

## 5) Ground motion in plausible behavior (or explicit stylization)
- Default to believable weight, acceleration, and deceleration.
- If physics are exaggerated, label the style (cartoony squash/stretch, dreamlike float, etc.).
- Ensure contact events (foot plants, collisions, object grabs) have clear timing and follow-through.
- Clarify whether simulation is physically based, art-directed, or hybrid.

## 6) Constrain render and simulation scope
- Provide quality targets that fit delivery needs (preview, social clip, hero render).
- Bound expensive effects: particles, volumetrics, hair, cloth, fluid, motion blur, GI bounces.
- Prefer tiered output specs (draft vs final) when heavy compute is involved.
- Flag assumptions that impact render feasibility: resolution, samples, hardware class, deadline.

## 7) Define asset inputs and ownership clarity
- List required assets: models, rigs, textures, HDRIs, caches, audio cues.
- Mark each asset state: provided, to-be-created, or stand-in.
- Distinguish reusable library assets from project-specific assets.
- Do not imply rights transfer; record provenance expectations and source location metadata.

## 8) Improve production handoff quality
- End each output with a concise handoff checklist:
  - scene file version and dependencies
  - frame range and naming convention
  - color pipeline notes (linear/sRGB, LUT usage)
  - render passes/AOV requirements
  - known risks and fallback options
- Keep language execution-ready: specific, measurable, and tool-agnostic where possible.

## Quick pre-delivery checklist
- [ ] Primary visual intent is explicit per shot.
- [ ] Camera motion is readable and justified.
- [ ] Continuity anchors are documented.
- [ ] Timing includes frame rate and beat structure.
- [ ] Physics behavior is plausible or intentionally stylized.
- [ ] Render complexity is bounded to feasible targets.
- [ ] Asset states and provenance expectations are clear.
- [ ] Handoff notes enable downstream production without guesswork.
