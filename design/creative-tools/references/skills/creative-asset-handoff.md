# Creative Asset Handoff

## Purpose
Use this mini-skill to deliver final creative packages to designers, engineers, marketers, or clients with predictable structure, naming, provenance notes, and acceptance criteria.

## When to Use
Use when project output is ready for review, implementation, publication, or archiving and stakeholders need a clear handoff package instead of informal file drops.

## Handoff Package Structure
Recommended baseline:
- `/source/` -> editable originals and working files.
- `/exports/` -> final distribution formats only.
- `/docs/` -> usage guidance, licensing/provenance, manifest.
- `/previews/` -> lightweight review previews if needed.

Within `/exports/`, separate by channel or medium:
- `/exports/web/`
- `/exports/social/`
- `/exports/print/`
- `/exports/app/`

## Source vs Export Rules
- Source files must remain editable and versioned.
- Export files must be immutable release artifacts.
- Never mix source and export files in one folder.
- Each export should map back to exactly one source record.

## Naming and Versioning Conventions
Use deterministic naming:
`{project}-{asset-group}-{asset-name}-{variant}-v{major}.{ext}`

Examples:
- `spring-launch-icons-nav-home-outline-v2.svg`
- `spring-launch-hero-bottle-main-web-v3.webp`
- `spring-launch-onepager-client-print-v1.pdf`

Versioning rules:
- Increase major version on approved content changes.
- Keep deprecated exports in `/archive/` with replacement note.
- Do not overwrite approved release assets.

## Usage Constraints and Provenance Fields
For each release bundle include:
- asset owner,
- creation/edit date,
- source tool,
- license/usage rights,
- restricted use notes,
- dependency notes (fonts, plugins, linked media),
- approval status and approver.

## Review and Approval Checklist
- [ ] Folder structure matches package standard.
- [ ] Source and export files are clearly separated.
- [ ] Naming/versioning is consistent and sortable.
- [ ] Usage/licensing constraints documented.
- [ ] Provenance fields complete.
- [ ] Delivery manifest covers every exported file.
- [ ] Acceptance criteria and sign-off status included.

## Delivery Manifest Pattern
Include a machine-readable table (CSV/Markdown/JSON) with:
- file path,
- asset purpose,
- format,
- dimensions or duration,
- version,
- source link,
- owner,
- approval status,
- usage constraints.

## Stakeholder-Specific Notes
- Engineering: include implementation notes (token mapping, file naming imports).
- Marketing: include channel usage matrix and expiry windows.
- Legal/compliance: include rights and attribution obligations.
- Clients: include quick-start folder + approved-only subset.

## Failure Modes
Reject handoff when:
- Source files are missing or merged with exports.
- Naming lacks versioning or contains ambiguous labels.
- Provenance/licensing fields are absent.
- Manifest does not reconcile to delivered files.
- Acceptance criteria are missing or unsigned.


## Stage 3.8 Extension: QA Gates, Revision Loops, and Release Evidence

### QA Gates
- Require a release manifest that reconciles every export to one source record.
- Require ownership matrix and explicit approval status per asset group.
- Enforce strict source/export separation and immutable approved exports.
- Require usage instructions, constraints, and provenance/licensing notes.
- Define rollback/withdrawal paths before distribution.

### Revision-Loop Rules
- Any post-signoff file change creates a new version and reopens QA gate review.
- Maintain revision history with change reason, owner, and affected channels.
- Late-change protocol must identify impacted stakeholders and replacement instructions.

### Evidence Requirements
- Delivery manifest with versions and approval states.
- Signoff matrix across creative, engineering, marketing, and compliance.
- Rollback instructions and archive map for previous approved sets.

### Acceptance/Rejection Gates
Accept when manifest reconciliation, owner approvals, and source/export integrity are complete.
Reject when assets are missing provenance, ownership is undefined, or late changes bypassed re-approval.

### Integration and Downstream Expectations
Handoff should only proceed after `creative-qa-gate-automation` returns release-go status.
Downstream teams receive approved-only exports, source lineage references, usage guidance, and rollback contacts.

