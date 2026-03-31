# Domain-Routed Skill Package Architecture

## What It Is

A structured system for organizing professional knowledge into routable, interconnected packages — where a skill is not a single document but a navigable graph of related capabilities.

Each package represents one professional domain. Inside that domain, knowledge is split into focused mini-skills. A lightweight router directs the agent to the right files based on task type, while cross-links between files preserve the natural adjacency of professional knowledge.

## The Core Problem It Solves

Most skill files try to be everything at once: a trigger, a guide, an instruction set, and a reference — all in one block. This creates files that are too large to scan, too general to route, and too flat to reflect how real professional work actually flows. Real tasks rarely depend on one capability alone. They require a primary skill, adjacent context, and a way to verify output quality.

## Three-Layer Architecture

1. Trigger layer. A short frontmatter description written as a high-signal classifier, not a human-readable summary. Its only job is to tell the model when to enter this package at all.
2. Routing layer. A concise SKILL.md that does not try to contain all knowledge — it maps task types to files. If the task is about X, open reference A. If implementation is needed, open example B. If the task is adjacent, check related file C. Hard limit: under 500 lines.
3. Knowledge graph layer. Reference and example files that are cross-linked to each other. Each file declares what it relates to, when to open the next file, and what to use alongside it. This turns passive documentation into an active adjacency engine.

## Key Principles

** Description as classifier.** The description field is written for the model, not the reader. It contains: primary domain, top use cases, adjacency hints, and disambiguation triggers — nothing else.

** Composition over isolation.**  Mini-skills are never used alone on non-trivial tasks. Every task activates a working set: one primary skill that drives the main objective, at least two adjacent skills that provide implementation context or constraint, and one validation skill that checks quality, risk, or correctness.

** Manifest as topology.**  The manifest.json is not for discovery — it is for package integrity. It holds the canonical file list, skill-to-file map, adjacency map, and asset groups. It makes the graph machine-readable and auditable.

** Self-diagnostic before execution.**  Before any substantive work begins, the agent runs a proportional integrity check: quick check for simple tasks, activated-scope check for working set validation, full audit only when explicitly needed or when systemic failures are detected.

## Goals

- Separate trigger logic, routing logic, and knowledge depth into distinct layers
- Reflect the natural adjacency of professional capabilities rather than treating skills as isolated atoms
- Keep the entry point lightweight so activation is fast and precise
- Enable deep, multi-file reasoning without bloating the router
- Make package structure auditable, maintainable, and consistent across domains

## What This Is Not

It is not a documentation wiki. It is not a flat collection of markdown files. It is not designed to be read by humans top to bottom. It is an architectural pattern for how an agent should navigate, select, and compose professional knowledge — domain-aware, graph-structured, and routing-first.
