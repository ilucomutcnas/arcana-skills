# Skill Package — Template Structure

```
skill-domain-name/
│
├── SKILL.md                          # Main router and mini-skills index (< 500 lines)
├── composition-protocol.md           # Rules for selecting and combining mini-skills
├── self-diagnostic-protocol.md       # Tiered integrity check rules
│
├── resources/                        # Shared package-wide navigation files
│   ├── skill-catalog.md              # Full index: all mini-skills with summaries
│   ├── routing-guide.md              # Which file to open for which task
│   ├── asset-link-index.md           # Complete map of all auxiliary folders and files
│   └── manifest.json                 # Machine-readable package manifest
│
├── references/
│   └── skills/                       # One file per mini-skill — full methodology
│       ├── mini-skill-one.md
│       ├── mini-skill-two.md
│       └── mini-skill-three.md
│
├── examples/
│   └── skills/                       # One file per mini-skill — code, prompts, commands
│       ├── mini-skill-one.md
│       ├── mini-skill-two.md
│       └── mini-skill-three.md
│
│   [For mini-skills that need additional assets, scripts, or deep references,
│    create a dedicated folder at the package root using the naming convention
│    <mini-skill-name>__<type>/ — see patterns below]
│
├── mini-skill-one__references/       # Deep reference files for mini-skill-one
│   ├── topic-a.md
│   └── topic-b.md
│
├── mini-skill-one__scripts/          # Executable scripts for mini-skill-one
│   ├── main.py
│   ├── helpers.py
│   └── requirements.txt
│
├── mini-skill-two__assets/           # Static assets for mini-skill-two
│   ├── template-library.md
│   └── examples.json
│
└── mini-skill-two__scripts/          # Executable scripts for mini-skill-two
    ├── run.py
    └── requirements.txt
```

---

## File responsibilities

| File | Role |
|---|---|
| `SKILL.md` | Entry point and router. Lists all mini-skills with one-line summaries and file paths. Never contains deep guidance. |
| `composition-protocol.md` | Universal rules: always use 1 primary + 2 adjacent + 1 validation mini-skill for non-trivial tasks. |
| `self-diagnostic-protocol.md` | Three-tier check: Quick Integrity → Activated Scope → Full Audit. Run before any substantive work. |
| `resources/skill-catalog.md` | Full catalog with summaries, file paths, and related asset links for every mini-skill. |
| `resources/routing-guide.md` | Decision guide: for task type X, open file Y. Quick navigation index. |
| `resources/asset-link-index.md` | Every auxiliary folder and file in the package, with clickable links. |
| `resources/manifest.json` | Machine-readable: slug, purpose, when-to-use, file paths for every mini-skill. |
| `references/skills/<slug>.md` | Full methodology, guardrails, validation rules for one mini-skill. |
| `examples/skills/<slug>.md` | Code snippets, CLI commands, prompt patterns, usage samples for one mini-skill. |
| `<slug>__references/` | Deep domain references tied to a specific mini-skill (taxonomies, playbooks, schemas). |
| `<slug>__scripts/` | Executable scripts tied to a specific mini-skill. Always include `requirements.txt`. |
| `<slug>__assets/` | Static data files tied to a specific mini-skill (JSON templates, example libraries). |
| `<slug>__resources/` | Mixed supporting materials for a specific mini-skill. |

---

## Naming conventions

- Package root folder: `your-skill-name/` — lowercase, hyphen-separated
- Mini-skill file slugs: `mini-skill-name.md` — match the slug used in `manifest.json`
- Auxiliary folders: `<mini-skill-slug>__<type>/` — double underscore separates slug from type
- Folder types: `__references`, `__scripts`, `__assets`, `__resources`
- Scripts folder always contains `requirements.txt` if any dependencies exist

---

## Minimum viable package (1 mini-skill)

```
skill-domain-name/
├── SKILL.md
├── composition-protocol.md
├── self-diagnostic-protocol.md
├── resources/
│   ├── skill-catalog.md
│   ├── routing-guide.md
│   ├── asset-link-index.md
│   └── manifest.json
├── references/
│   └── skills/
│       └── mini-skill-one.md
└── examples/
    └── skills/
        └── mini-skill-one.md
```
