# Skill Composition Protocol

## Package Structure
- `SKILL.md` — lightweight router and high-level index
- `composition-protocol.md` — universal rules for selecting and combining mini-skills
- `self-diagnostic-protocol.md` — self-diagnostic rules for this domain package
- `resources/skill-catalog.md` — full catalog of extracted mini-skills
- `resources/routing-guide.md` — navigation and composition rules
- `resources/asset-link-index.md` — complete link map for every auxiliary folder and file
- `resources/manifest.json` — machine-readable package manifest
- `references/skills/*.md` — full extracted guidance per mini-skill
- `examples/skills/*.md` — extracted code snippets, command examples, prompt patterns, and usage samples

## Domain Coverage

This package represents a single professional domain, not a single isolated task.

A domain is a connected area of work made up of multiple related capabilities, workflows, decision patterns, and validation methods. Real tasks in this domain rarely depend on one skill alone. They usually require a combination of primary, adjacent, and validation-oriented knowledge.

To keep this package maintainable, navigable, and effective for automatic activation, the domain is split into smaller units called mini-skills.

A mini-skill is a focused capability within the broader domain. Each mini-skill covers a narrower problem space, method, toolset, or execution pattern. Mini-skills are separated so the agent can load only the most relevant materials instead of treating the entire domain as one large undifferentiated block.

This structure is intentional:
- the package defines the domain,
- mini-skills define the specialized parts inside that domain,
- references provide deeper guidance,
- examples provide concrete implementation patterns,
- resources provide shared routing, support files, and package-wide context.

Mini-skills should not be treated as fully isolated unless the task is unusually narrow. In most real tasks, one mini-skill acts as the primary driver, while other mini-skills provide adjacent knowledge, constraints, validation, implementation support, or cross-functional context.

Use this package as a routed domain system:
- identify the domain-level fit,
- select the best primary mini-skill,
- add adjacent and validation mini-skills when the task is not trivially narrow,
- open only the files needed for the current task.

## Universal Skill Composition Rule

Do not use a mini-skill in isolation unless the task is trivially narrow.

For every non-trivial task, apply this protocol:

1. Identify the single best primary mini-skill.
   - Choose the mini-skill that most directly matches the user's main objective.
   - If multiple mini-skills seem relevant, choose the one that is most action-driving.

2. Identify at least two adjacent mini-skills.
   - Select mini-skills that are likely to affect correctness, completeness, implementation quality, or downstream outcomes.
   - Prefer adjacent mini-skills from different perspectives, such as:
     - implementation
     - validation
     - observability
     - optimization
     - deployment
     - business impact
     - safety or reliability

3. Identify one validation mini-skill.
   - Select at least one mini-skill whose role is to verify, measure, test, monitor, or challenge the output.
   - If a dedicated validation mini-skill exists, use it.
   - Otherwise choose the best available mini-skill for evaluation, review, monitoring, benchmarking, or error checking.

4. Open all selected files together before producing the final answer when the task has multiple moving parts.

5. Escalate if needed.
   - If the task touches architecture, production risk, cost, scale, or quality, expand the working set beyond the minimum.
   - If the task is ambiguous, choose the most plausible adjacent mini-skills rather than staying too narrow.

Minimum composition:
- 1 primary mini-skill
- 2 adjacent mini-skills
- 1 validation mini-skill

Use more when needed, but never default to a single mini-skill for a complex task.

## Mini-Skill Selection Criteria

When selecting mini-skills, use these criteria:

- Relevance: which mini-skill is most directly tied to the user's main goal?
- Dependency: which mini-skills provide knowledge required for the primary one to work well?
- Risk: which mini-skills reduce the chance of wrong, incomplete, unsafe, or shallow output?
- Validation: which mini-skills can test, measure, review, or monitor the result?
- Scale: which mini-skills become necessary if the task affects production, cost, performance, rollout, or multiple stakeholders?

## Practical Workflow Recipes

### 1) Campaign Visual Production and Delivery
- Primary: `raster-retouch-pipeline`
- Adjacent: `ad-creative`, `content-creator`
- Validation/Delivery: `creative-asset-handoff`
- Use when campaign images need cleanup plus launch-ready messaging and package delivery.

### 2) Icon System Cleanup to Engineering Handoff
- Primary: `vector-workflow-automation`
- Adjacent: `content-creator` (usage labeling), `ad-creative` (campaign consistency when icons are promotional)
- Validation/Delivery: `creative-asset-handoff`
- Use when mixed-source icon assets must be normalized and shipped to a design system or front-end team.

### 3) Document-Heavy Creative Release
- Primary: `pdf-processing`
- Adjacent: `content-creator`, `raster-retouch-pipeline`
- Validation/Delivery: `creative-asset-handoff`
- Use when creative and document assets are shipped together with approval constraints.

### 4) Multi-Asset Campaign Release
- Primary: `creative-asset-handoff`
- Adjacent: `vector-workflow-automation`, `raster-retouch-pipeline`, `content-creator`
- Validation: `pdf-processing` when document artifacts are included.
- Use when final delivery must include complete manifests, provenance, and acceptance criteria.


### 5) Full Campaign Creative Release
- Primary: `creative-qa-gate-automation`
- Adjacent: `ad-creative`, `content-creator`, `raster-retouch-pipeline`, `vector-workflow-automation`
- Delivery: `creative-asset-handoff`

### 6) Ad Variation Review and Release
- Primary: `ad-creative`
- Adjacent: `creative-qa-gate-automation`, `content-creator`
- Delivery: `creative-asset-handoff`

### 7) Editorial Launch Package
- Primary: `content-creator`
- Adjacent: `creative-qa-gate-automation`, `ad-creative`
- Delivery: `creative-asset-handoff`

### 8) Icon/Vector Release to Engineering
- Primary: `vector-workflow-automation`
- Adjacent: `creative-qa-gate-automation`
- Delivery: `creative-asset-handoff`

### 9) Product Image Variant Release
- Primary: `raster-retouch-pipeline`
- Adjacent: `creative-qa-gate-automation`, `ad-creative`
- Delivery: `creative-asset-handoff`

### 10) Branded PDF/Document Delivery
- Primary: `pdf-processing`
- Adjacent: `creative-qa-gate-automation`, `content-creator`
- Delivery: `creative-asset-handoff`

### 11) Final Creative Asset Handoff with Late Revision Loop
- Primary: `creative-asset-handoff`
- Adjacent: `creative-qa-gate-automation`, owning production mini-skill
- Rule: reopen QA gate on any late content/spec/platform change before re-export.
