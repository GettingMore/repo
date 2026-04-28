# Agent Working Index

## Repository Role

- This is a public skill-source extract, not a runnable multi-agent application.
- Keep the repository focused on Codex skill instructions, reference notes, and small templates.
- Do not add private datasets, deployment scripts, or organization-specific runtime code.

## Read First

- Human overview: `README.md`
- Documentation index: `docs/README.md`
- Skill contract: `.agents/skills/adk-a2a-agent-generate/SKILL.md`
- Target architecture notes: `docs/reference/target-agent-architecture/README.md`

## Source Of Truth Map

- `AGENTS.md`: model-facing repository index and working rules.
- `.agents/skills/adk-a2a-agent-generate/SKILL.md`: executable workflow contract.
- `.agents/skills/adk-a2a-agent-generate/references/`: detailed skill-local rules.
- `.agents/skills/adk-a2a-agent-generate/assets/`: prompt and scaffold shape assets.
- `docs/`: human-facing concept and architecture notes.

## Editing Rules

- Keep `SKILL.md` concise.
- Put detailed decision rules in `references/`.
- Keep public examples generic and domain-neutral.
- Use Google ADK and A2A terminology only when it maps to public documentation.
- Do not introduce private environment names, private endpoints, or vendor-specific internal tooling.
