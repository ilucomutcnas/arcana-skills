# 3D Animation Anti-Patterns

Use this list to catch common failure modes in `design/3d-animation` outputs before they reach production. These anti-patterns reduce clarity, inflate render cost, and create avoidable revision loops.

## 1) Vague cinematic language with no operational detail
**Pattern:** “Make it epic,” “more cinematic,” or “film-like” without shot, lens, timing, or mood constraints.

**Why it fails:** Team members interpret broad style language differently, so blocking, lighting, and camera choices diverge.

**Better approach:** Translate adjectives into actionable parameters: framing, camera path, beat timing, lighting contrast, and intended emotional read.

## 2) Impossible physics without declared intent
**Pattern:** Objects hover, characters accelerate instantly, or collisions have no weight response, but stylization is never stated.

**Why it fails:** Viewers read the result as broken simulation instead of deliberate direction.

**Better approach:** Either preserve believable inertia/contact behavior or explicitly label the stylization model and apply it consistently.

## 3) Excessive camera movement that fights subject motion
**Pattern:** Constant orbiting, rolling, and push-pull camera moves stacked in short shots.

**Why it fails:** The viewer loses spatial orientation and misses key animation beats.

**Better approach:** Limit each shot to a dominant camera idea and ensure camera motion supports, not competes with, subject action.

## 4) Unbounded render complexity
**Pattern:** Adding high-sample GI, dense particles, volumetric fog, cloth, hair, and depth-of-field blur simultaneously with no quality tiers.

**Why it fails:** Render time explodes, iteration slows, and deadlines slip.

**Better approach:** Define cost-aware priorities and staged quality levels (blocking preview, lighting preview, final render).

## 5) Missing frame and timing specifics
**Pattern:** Notes like “faster intro,” “linger at the end,” or “snappier transition” without frame rate or durations.

**Why it fails:** Animators and editors cannot align pacing decisions, causing subjective back-and-forth.

**Better approach:** Specify fps, total duration, and beat boundaries in frames or seconds for each shot segment.

## 6) Continuity drift across sequence shots
**Pattern:** Light direction flips, props teleport, character facing changes, or scale shifts unintentionally.

**Why it fails:** Sequence coherence breaks and compositing/edit teams must patch inconsistencies.

**Better approach:** Maintain a continuity ledger for orientation, lighting, prop states, and transition logic.

## 7) Unclear asset ownership and source assumptions
**Pattern:** Referring to “the model pack,” “studio textures,” or “downloaded rig” without source and status.

**Why it fails:** Teams cannot confirm what is approved, replaceable, or missing at handoff time.

**Better approach:** Tag every required asset with source, status (approved/stand-in), and handoff dependency.

## 8) Delivering animation notes without production handoff metadata
**Pattern:** Creative direction is present, but no frame ranges, naming rules, pass requirements, or dependency list.

**Why it fails:** Downstream teams reinterpret intent and introduce technical mismatches.

**Better approach:** Attach a short technical handoff block with scene version, render settings tier, output naming, and known risks.

## Anti-pattern rejection checklist
- [ ] No purely subjective style phrases without measurable translation.
- [ ] No accidental physics breaks.
- [ ] No camera choreography that obscures action.
- [ ] No unlimited simulation/render asks.
- [ ] No timing notes lacking fps or durations.
- [ ] No undocumented continuity changes.
- [ ] No ambiguous asset provenance or ownership.
- [ ] No delivery packet missing technical handoff details.
