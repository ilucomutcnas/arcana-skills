# Skill Composition Protocol

## Universal Composition Rule

For non-trivial work, do not run a single mini-skill in isolation.
Minimum working set: 1 primary + 2 adjacent + 1 validation mini-skill.

## Composition Workflow

1. Identify user outcome (API change, mismatch, perf, corpus, release, roadmap).
2. Select primary mini-skill that owns acceptance criteria.
3. Add adjacent mini-skills that provide constraints and evidence.
4. Add validation mini-skill that can reject weak claims.
5. Collect evidence artifacts (tables, command outputs, risks, decision log).

## Practical Recipes

### 1) Layout engine API change
- Primary: `library-architecture`
- Adjacent: `corpus-diagnostics`, `browser-accuracy`
- Validation: `architecture-review`
- Required evidence: API impact table, migration notes, width sweep diff, browser deltas, risk sign-off.

### 2) Cross-browser accuracy investigation
- Primary: `browser-accuracy`
- Adjacent: `library-architecture`, `development-workflow`
- Validation: `corpus-diagnostics`
- Required evidence: mismatch taxonomy table, sweep commands, reproducible case in pages/, triage result (fix/accept/refresh).

### 3) Performance regression triage
- Primary: `benchmarks-profiling`
- Adjacent: `library-architecture`, `browser-accuracy`
- Validation: `architecture-review`
- Required evidence: before/after benchmark table, CPU profile notes, allocation/retained memory interpretation, threshold decision.

### 4) Corpus mismatch diagnosis
- Primary: `corpus-diagnostics`
- Adjacent: `browser-accuracy`, `research-log`
- Validation: `priorities-roadmap`
- Required evidence: script/font matrix, width sweep probes, mismatch taxonomy assignment, canary keep/drop decision.

### 5) Release readiness review
- Primary: `packaging-release`
- Adjacent: `demo-dogfooding`, `development-workflow`
- Validation: `browser-accuracy`
- Required evidence: export/entrypoint checklist, smoke test results, demo QA notes, rollback vs fix-forward call.

### 6) Roadmap decision review
- Primary: `priorities-roadmap`
- Adjacent: `research-log`, `architecture-review`
- Validation: `corpus-diagnostics`
- Required evidence: priority matrix, rejected-work guardrail, dependency order, communication note.
