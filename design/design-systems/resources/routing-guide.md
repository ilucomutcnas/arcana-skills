# Routing Guide

## Rules

- Open `references/skills/{slug}.md` for full methodology and validation rules.
- Open `examples/skills/{slug}.md` for concrete examples.
- Always apply `shared-rules/STYLE-GUARDRAILS.md` across all design system work.

## Quick Navigation

### Foundation Layer
- **foundations** -> `references/skills/foundations.md`
- **components** -> `references/skills/components.md`
- **theming** -> `references/skills/theming.md`
- **design-token-governance** -> `references/skills/design-token-governance.md`

### Quality Layer
- **accessibility** -> `references/skills/accessibility.md`
- **review-audit** -> `references/skills/review-audit.md`

### Organizational Layer
- **documentation** -> `references/skills/documentation.md`
- **governance** -> `references/skills/governance.md`
- **system-adoption-playbook** -> `references/skills/system-adoption-playbook.md`

### Implementation Layer
- **framework-mapping** -> `references/skills/framework-mapping.md`

## Routing by Task Type

- **New design system** -> foundations + components + theming + accessibility + documentation
- **Component library** -> components + foundations + accessibility + framework-mapping
- **Theming / dark mode** -> theming + foundations + accessibility
- **System audit** -> review-audit + foundations + components + governance
- **Implementation** -> framework-mapping + foundations + components
- **Governance setup** -> governance + documentation + review-audit
- **Accessibility review** -> accessibility + components + theming + review-audit
- **Token system setup** -> foundations + design-token-governance
- **Component implementation** -> components + accessibility + framework-mapping
- **Dark or multi-brand rollout** -> theming + design-token-governance
- **Organizational rollout** -> governance + system-adoption-playbook
- **Remediation program** -> review-audit + system-adoption-playbook
- **Enablement push** -> documentation + system-adoption-playbook

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md)
- [`manifest.json`](manifest.json)
