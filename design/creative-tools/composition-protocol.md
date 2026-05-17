# Skill Composition Protocol

## Universal Rule
For non-trivial tasks, activate:
- 1 primary mini-skill,
- at least 2 adjacent mini-skills,
- 1 validation-oriented mini-skill.

## Composition Patterns

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
