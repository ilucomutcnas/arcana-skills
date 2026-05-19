# development-workflow Example

## Scenario: contributor fixes a line-wrap bug in editorial demo

Issue: at 640px, inline punctuation causes a premature wrap in `pages/demos/editorial-engine.html` for mixed Arabic/English paragraphs.

## Repo Analysis Routing
- Primary: `development-workflow`
- Adjacent: `library-architecture`, `browser-accuracy`
- Validation: `corpus-diagnostics`

## Core Command Quick Reference
- Install + baseline checks: `pnpm install`
- Targeted page workflow: run demo/build command used in current repo contributor docs
- Accuracy evidence: run browser accuracy script for impacted scenario
- Package checks before PR: `python scripts/validate_skills.py --package design/pretext-ui --strict`

## Workflow Stages
1. Reproduce bug on demo page with exact width/font context.
2. Trace to `line-break` and inline-flow metadata decision point.
3. Patch minimal fix in engine module.
4. Re-run targeted demo and browser/corpus checks.
5. Run package validator and prepare review notes.

## Command Checklist (before PR)
- [ ] Repro documented with paragraph sample and width.
- [ ] Targeted engine/test command output captured.
- [ ] Cross-browser sweep result attached for affected demo.
- [ ] Corpus diagnostic check confirms no new canary drift.
- [ ] Strict package validation passes.

## Expected Evidence Before PR
- Short root-cause note tied to exact module/function.
- Before/after behavior summary for demo page.
- Browser and corpus outputs proving no regression spread.
- Clear risk note if fix defers adjacent cleanup.
