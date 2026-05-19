# wcag-audit-reporting

## When to use
Use after (or during) audit discovery to deliver governance-ready outputs to engineering, product, legal, and procurement.

## Required inputs
- WCAG issue inventory from `wcag-audit-patterns`
- Keyboard and AT evidence from `screen-reader-testing`
- Visual evidence from `ui-visual-validator`
- Candidate remediation actions from `fixing-accessibility`

## Reporting workflow
1. Normalize issue taxonomy (content, structure, interaction, announcement, visual, motion).
2. Assign severity (`critical`, `high`, `medium`, `low`) using user-impact and task-blocking rules.
3. Map every issue to WCAG 2.2 criterion.
4. Build evidence pack: visual notes, DOM snippet, keyboard path, SR notes, browser/AT matrix.
5. Build remediation backlog with owner, due date, dependency, and acceptance criteria.
6. Mark VPAT/ACR-supportable findings and out-of-scope legal interpretations.
7. Publish retest workflow with pass gates and rejection triggers.

## Failure modes / rejection
Reject reports that omit severity, owner assignment, retest plan, or evidence references.
