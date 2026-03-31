# Self-Diagnostic Protocol

## Purpose

Define the mandatory (tiered) self-diagnostic procedure that protects package integrity and must be performed before using any mini-skill from this domain package, without forcing the agent to load the entire domain package for every task.
The purpose of self-diagnostic is to verify that the package is structurally usable, internally consistent, and safe to rely on before any substantive work begins.
This protocol exists to confirm that the package is usable, internally coherent, and safe to rely on before substantive work begins, while preserving the efficiency benefits of router-based domain packages.

## Core Principle

- Self-diagnostic must be proportional to task scope.
- Do not audit the entire package by default.  
- Start with a lightweight package-level check, then validate only the activated working set for the current task. 
- Expand the diagnostic scope only when necessary.

## When to Apply

Apply this protocol before starting any non-trivial task in this domain package.

Self-diagnostic must be performed before:
- selecting mini-skills,
- opening references or examples,
- using package assets,
- producing a substantive answer based on this package.

Use the tiered model:
1. Quick Integrity Check
2. Activated Scope Check
3. Full Package Audit only if needed

## Core Rule

Do not begin substantive domain work until self-diagnostic has been completed.

Self-diagnostic must be proportional to the active task scope.

If the package passes self-diagnostic, proceed with normal routing and task execution.

If the package fails self-diagnostic, report the issue before continuing.

## Diagnostic Modes

## 1. Quick Integrity Check

### Purpose
Confirm that the package router and core control files are present and usable.

### When to Use
Run this check at the start of every non-trivial task.

### Scope
Check only the package-level entry and routing structure.

### Verify
- `SKILL.md` exists and is readable
- `composition-protocol.md` exists and is readable
- `resources/skill-catalog.md` exists and is readable
- `resources/routing-guide.md` exists and is readable
- `resources/asset-link-index.md` exists and is readable
- `resources/manifest.json` exists and is readable
- `resources/composition-protocol.md` exists and is readable if referenced
- this self-diagnostic file exists and is readable if referenced
- the main router structure is intact
- the package is readable enough to continue routing

### Goal
Determine whether the package is alive and usable as a router.

### If This Check Passes
Proceed to mini-skill selection.

### If This Check Fails
Report the issue before continuing.

A failure here may be:
- Critical, if the router or core files are missing or unusable
- Major, if the package is still partly usable but routing quality is reduced

## 2. Activated Scope Check

### Purpose
Validate only the mini-skills and linked files selected for the current task.

### When to Use
Run this after selecting the working set for the task.

### Minimum Working Set
For any non-trivial task, the working set should normally include:
- 1 primary mini-skill
- at least 2 adjacent mini-skills
- 1 validation mini-skill

Use fewer only if the task is clearly narrow and self-contained.

### Scope
Check only:
- the selected mini-skills
- their reference files
- their example files
- their linked asset folders
- any directly required supporting files

Do not load unrelated mini-skills just to perform this check.

### Verify
For the activated working set, check:

#### File existence
- each referenced file exists
- each examples file exists if declared
- each linked asset folder exists if declared
- each directly required support file exists if referenced

#### Link validity
- links point to real package files or folders
- there are no broken paths in the activated chain
- there are no references to missing or renamed files in the activated chain

#### Local consistency
- the selected mini-skill names are consistent across router, catalog, and manifest where applicable
- summary, purpose, and when-to-use fields are usable if present
- the selected working set is readable enough to support the current task

#### Readiness for execution
- the primary mini-skill is usable
- adjacent mini-skills are usable
- the validation mini-skill is usable
- there is enough structural integrity to continue responsibly

### Goal
Confirm that the current task can proceed using the selected working set without requiring a full-package audit.

### If This Check Passes
Proceed with task execution.

### If This Check Fails
Report the issue before continuing.

## 3. Full Package Audit

### Purpose
Perform a comprehensive package-wide structural audit.

### When to Use
Run a full package audit only when:
- the user explicitly asks for a package audit
- the task is about package quality, repair, governance, or refactoring
- quick or activated-scope checks reveal signs of broader systemic issues
- multiple unrelated failures suggest the package may be structurally unsound
- a recent package rebuild or migration may have introduced widespread inconsistencies

### Scope
Check the full package, including:
- all listed mini-skills
- all references
- all examples
- all package asset folders
- all control files
- cross-file consistency across router, catalog, manifest, references, and examples

### Verify
- all declared files exist
- all declared links resolve
- all cross-file references are consistent
- there are no orphaned or stale declared entries
- summaries, purpose fields, and when-to-use fields are materially usable
- the package remains structurally coherent as a whole

### Goal
Assess overall package integrity, not just task-level usability.

## Severity Levels

If any issue is found, classify it by severity.

## Critical
A problem is critical if it materially blocks safe or reliable use of the package or active working set.

Examples:
- missing `SKILL.md`
- missing routing files required for navigation
- missing reference file for the selected primary mini-skill
- missing validation file required to assess output reliability
- broken routing that prevents responsible file selection
- structural corruption that makes the active working set unusable
- widespread package failure during a full audit

## Major
A problem is major if the package remains usable, but quality, completeness, or confidence is significantly reduced.

Examples:
- broken links inside the activated working set
- missing adjacent or example files
- stale manifest entries for selected mini-skills
- inconsistent summaries or routing information
- partial package drift across catalog, manifest, and router

## Minor
A problem is minor if it does not block responsible work but should still be reported.

Examples:
- formatting inconsistencies
- small metadata gaps
- minor wording issues
- optional fields missing
- non-blocking readability issues

## Response Rules

## If No Material Issues Are Found
Proceed with normal package use.

Suggested internal conclusion:
- self-diagnostic completed
- no blocking issues found
- package is usable for the current task

## If Issues Are Found
Do not silently ignore them.

You must report:
1. which diagnostic mode was used
2. what was checked
3. what issue was found
4. where it was found
5. the severity level
6. how it affects quality, completeness, routing, or reliability
7. whether work can continue safely

## If the Issue Is Critical
State clearly that the issue is critical and that reliable execution cannot be guaranteed.

If the issue blocks responsible work, say so explicitly.

Do not imply full confidence when the structure does not support it.

## If the Issue Is Major or Minor
Inform the user before continuing.

State:
- what was found
- how serious it is
- how it may affect output quality
- whether work can continue with limitations

Then ask whether to continue if the limitation is material to the task.

## Communication Template

Use a response like this when issues are found:

- Self-diagnostic completed.
- Diagnostic mode: [Quick Integrity Check / Activated Scope Check / Full Package Audit].
- I checked: [brief scope].
- I found the following issue(s): [brief description].
- Severity: [Critical / Major / Minor].
- Impact: [how this affects routing, completeness, accuracy, reliability, or execution quality].
- I can continue with limitations / I should not continue without repair.
- Please confirm whether you want me to proceed.

## Operating Rules

- Do not default to a full-package audit for normal task execution.
- Always begin with Quick Integrity Check for non-trivial tasks.
- After selecting the working set, run Activated Scope Check.
- Expand diagnostic scope only when the task, the evidence, or the user request justifies it.
- Treat self-diagnostic as mandatory package hygiene, but keep it router-aware, lazy, and proportional to scope.
