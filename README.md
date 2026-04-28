# ADK A2A Agent Skill Notes

This repository is a public extract of a Codex skill for planning Google ADK-based agent scaffolds and A2A interaction boundaries.

It is intentionally documentation-focused. It does not include private runner datasets, company deployment scripts, or organization-specific runtime code.

## What Is Included

- `.agents/skills/adk-a2a-agent-generate/`: a concise Codex skill contract
- `references/`: decision rules for specialist boundaries, shared reuse, ADK internal workflow, and A2A interaction boundaries
- `assets/`: small prompt and scaffold-shape templates
- `docs/`: human-facing notes about the design tradeoffs behind the skill

## Core Idea

The skill handles one agent request at a time:

1. Read a requirement or short specialist-agent request.
2. Extract compact evidence before designing code.
3. Decide whether the request should be a specialist agent, shared agent, tool adapter, or metadata registry.
4. Decide whether internal ADK workflow composition is needed inside the same boundary.
5. Decide whether remote A2A interaction is actually required.
6. Produce a handoff with TODO business logic instead of pretending the agent is complete.

The default is specialist-first. Use A2A only when there is an independent remote agent boundary, not merely because a workflow has multiple steps.

## Public Scope

This extract keeps only public, portable ADK/A2A design material. It excludes:

- private deployment environments
- private datasets and regression fixtures
- organization-specific naming

## Useful Links

- [Docs index](./docs/README.md)
- [Agent generation concept](./docs/concepts/adk-a2a-agent-generation.md)
- [Target agent architecture](./docs/reference/target-agent-architecture/README.md)
- [Skill contract](./.agents/skills/adk-a2a-agent-generate/SKILL.md)
