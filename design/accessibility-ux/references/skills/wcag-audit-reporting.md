# wcag-audit-reporting

## Purpose
Produce production-grade accessibility audit deliverables that convert findings into remediation governance, legal/compliance support artifacts, and release-ready retest gates.

## When to Use
Use this mini-skill when WCAG findings must be communicated beyond engineering notes: program management, procurement, legal, compliance, security review boards, and executive reporting.

## Required Inputs
- Issue inventory and criterion mapping from `wcag-audit-patterns`.
- Component-level technical remediation notes from `fixing-accessibility`.
- Keyboard and screen reader evidence from `screen-reader-testing`.
- Visual/focus/contrast evidence from `ui-visual-validator`.
- Scope statement identifying in-scope page-types, user journeys, and known exclusions.

## Issue Taxonomy and Severity Model
Classify each issue by taxonomy (navigation, form validation, dynamic announcements, visual contrast, focus handling, motion side effects, metadata context). Score severity with two dimensions: user impact and task criticality.
- Critical: blocks core task completion or legal access obligations.
- High: major friction with substantial error risk or abandonment.
- Medium: partial friction with workaround.
- Low: polish-level issue without major task impact.

## Evidence Requirements
For each issue include:
- visual note or screenshot reference identifier;
- affected DOM/code snippet;
- keyboard reproduction path;
- screen reader output notes;
- browser/assistive-technology matrix;
- affected route/component ID;
- WCAG criterion and conformance level.

## Remediation Backlog Structure
Each backlog row must include issue ID, severity, user impact, engineering owner, product owner, due date, dependency, remediation status, acceptance criteria, and retest owner.

## Compliance Notes, VPAT/ACR Boundaries
This mini-skill supports VPAT/ACR evidence preparation but does not issue legal determinations. Mark evidence confidence, in-scope platforms, and unresolved caveats explicitly.

## Retest Workflow and Acceptance
Require evidence-linked retest per issue. Exit criteria: criterion re-check passed, keyboard path verified, AT matrix rerun for impacted flows, visual validation completed, and no regression in adjacent features.

## Failure Modes and Rejection Criteria
Reject reports that omit severity rationale, owner assignment, due date, WCAG mapping, evidence references, retest gates, or stakeholder summary language.
