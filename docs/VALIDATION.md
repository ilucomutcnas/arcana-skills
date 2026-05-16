# Arcana Skill Validation

This repository uses a dependency-free validation script to check every skill package before content expansion, structural cleanup, registry generation, and release-quality work.

The validator is intentionally designed for two phases:

1. **Bootstrap phase**: generate reports without blocking CI while existing packages are being audited and cleaned.
2. **Strict phase**: fail Codex PRs when structural errors or quality regressions are introduced.

## Commands

Run a full repository report:

```bash
python scripts/validate_skills.py
```

Run a strict repository check that fails on structural errors:

```bash
python scripts/validate_skills.py --strict
```

Run a strict release-quality check that also fails on warnings:

```bash
python scripts/validate_skills.py --strict --fail-on-warning
```

Validate one package:

```bash
python scripts/validate_skills.py --package design/content-writing --strict
```

Write reports to files:

```bash
python scripts/validate_skills.py \
  --output-json reports/skill-validation.json \
  --output-md reports/skill-validation.md
```

## What the validator checks

### Package structure

Every detected package is checked for the required structure:

```text
<domain>/<package>/
  SKILL.md
  composition-protocol.md
  self-diagnostic-protocol.md
  resources/
    manifest.json
    skill-catalog.md
    routing-guide.md
    asset-link-index.md
  references/
    skills/
  examples/
    skills/
```

Technical packages may contain additional folders such as `src`, `scripts`, `pages`, `benchmarks`, `accuracy`, `corpora`, or `research-data`, but they still need the package-level routing files.

### Individual mini-skill validation

For every `resources/manifest.json`, the validator checks that:

- the manifest is valid JSON;
- the manifest is a list of mini-skill records;
- every mini-skill has `title`, `slug`, `purpose`, `when`, `reference`, and `examples`;
- every referenced file exists;
- every example file exists;
- no duplicate mini-skill slugs exist;
- reference files are not too thin;
- example files are not too thin;
- unlisted reference/example files are reported.

### Package depth

The validator checks the total user-facing word count across:

- `SKILL.md`;
- `composition-protocol.md`;
- `self-diagnostic-protocol.md`;
- `resources/*.md`;
- `resources/*.json`;
- `references/skills/*.md`;
- `examples/skills/*.md`;
- `shared-rules/*.md`;
- `*__resources/*.md`;
- `*__references/*.md`.

The default minimum package-level threshold is defined in:

```text
validation/skill_validation_policy.json
```

### English-only user-facing content

User-facing package documentation should be English-only. The validator flags visible non-English script blocks in user-facing package docs.

This rule intentionally avoids scanning corpus data, benchmark data, source code, and other technical test assets where multilingual content may be required.

### Placeholder and template-like content

The validator flags common unfinished content markers such as:

- `TODO`;
- `TBD`;
- `FIXME`;
- `<placeholder>`;
- `{{placeholder}}`;
- `fill this in`;
- `coming soon`;
- `template`.

### Binary and asset hygiene

The validator inventories common binary assets such as:

- fonts;
- PDFs;
- images;
- archives;
- videos;
- audio files;
- executable-like artifacts.

Binary assets are warnings by default because some packages may intentionally contain demo assets. They must be reviewed for legal, repository-size, and security hygiene.

### Secret scanning

The validator checks text files for common token and secret-like patterns. Possible secrets are treated as errors.

## Severity levels

### Error

Errors indicate structural or security problems that should block merge in strict mode.

Examples:

- missing `SKILL.md`;
- `SKILL.me` instead of `SKILL.md`;
- missing required package files;
- invalid manifest JSON;
- broken manifest links;
- possible secrets.

### Warning

Warnings indicate quality, maturity, legal hygiene, or readiness concerns.

Examples:

- thin package content;
- thin mini-skill references;
- thin examples;
- placeholder-like language;
- non-English user-facing documentation;
- binary assets requiring review;
- unlisted reference/example files.

## CI behavior

The initial GitHub Actions workflow runs the validator in report mode. This is intentional because the existing repository may already contain structural and quality findings.

After the structural cleanup phase is complete, update the workflow command to:

```bash
python scripts/validate_skills.py --strict
```

After all packages reach release-quality status, use:

```bash
python scripts/validate_skills.py --strict --fail-on-warning
```

## Codex task rule

Every Codex task that changes a skill package should include one of these commands:

```bash
python scripts/validate_skills.py --package <domain>/<package> --strict
```

For repository-wide structural work, use:

```bash
python scripts/validate_skills.py --strict
```

For final release readiness, use:

```bash
python scripts/validate_skills.py --strict --fail-on-warning
```

## Quality target

A package should be considered professional only when it has:

- a valid package structure;
- a valid manifest;
- meaningful mini-skill references;
- practical examples;
- enough user-facing depth;
- no placeholder content;
- no unresolved structural errors;
- no unexplained risky assets;
- English-only user-facing documentation;
- clear routing and self-diagnostic logic.
