---
name: adk-a2a-agent-generate
description: Plan one Google ADK-based specialist-agent scaffold from a requirement, classify shared reuse and A2A boundaries, and produce evidence, classification, commonization notes, and an implementation handoff with TODO business logic. Use when Codex should help design agent boundaries, ADK internal workflow composition, shared agent/tool reuse, or A2A interactions without assuming private deployment infrastructure.
---

# ADK A2A Agent Generate

## Overview

Use this skill when the user wants Codex to prepare one agent implementation step inside a larger incremental agent buildout.

The skill is a unit workflow. It handles one request at a time and produces planning artifacts for a future implementation. It does not default to finished business logic, deployment, or publication.

The important work is:

- collect compact evidence before designing code
- classify the requested boundary as `Specialist Agent`, `Shared Agent`, `Tool/Adapter`, or `Metadata Registry`
- decide whether local same-runtime reuse is enough
- decide whether internal ADK workflow composition is needed
- mark A2A only when a remote independent agent boundary is required
- produce a handoff and scaffold shape with explicit TODOs

## Required Inputs

- Default `repo_path` to the current git repository root.
- Collect a `specialist_agent_request` with `goal` or `spec_path`.
- Accept sparse first-pass inputs:
  - `goal`
  - optional `domain_key`
  - optional `agent_name`
  - optional `specialist_role`
  - optional `specialist_input_contract`
  - optional `specialist_output_contract`
  - optional `specialist_parent_context`
  - optional `additional_context_paths`
- Accept optional reuse-analysis inputs:
  - `prior_delta_paths`
  - `shared_boundary_catalog_paths`
  - `incremental_context_template_id`

Do not require JSONL files as direct skill input. An external orchestrator may invoke this skill once per request.

## Workflow

1. Resolve the request context.
   Infer `agent_name` from the requirement when it is missing. Keep it as a stable ASCII package identifier. If the request identity is still unknown after reading the requirement text, ask for the smallest missing identifier.

2. Load the standards that control the decision.
   Read only the references needed for the request:
   - `references/spec-driven-execution.md`
   - `references/minimal-input-contract.md`
   - `references/incremental-commonization.md`
   - `references/boundary-decision-rules.md`
   - `references/internal-workflow-composition.md`
   - `references/a2a-boundary-rules.md`
   - `references/implementation-handoff.md`
   - `references/question-rules.md`
   - `references/target-shape.md`
   - `references/specialist-agent-template.md`

3. Build evidence first.
   Summarize the requirement, inputs, outputs, ownership hints, existing shared candidates, and any prior decisions. Keep the evidence compact enough to review in one screen.

4. Build incremental shared context.
   Summarize prior commonization notes and shared boundary catalogs. Distinguish confirmed reuse from speculative reuse.

5. Classify with the main model.
   Capture structured classification JSON with:
   - `recommended_shape`
   - `reuse_bindings`
   - `shared_registration_proposals`
   - `retrofit_actions`
   - `a2a_required`
   - `a2a_interactions`
   - `internal_workflow`
   - `reasoning_summary`
   - `todo`

6. Build commonization notes.
   Record which shared tools, shared agents, or metadata registries should be reused, added, updated, or revisited later.

7. Generate the implementation handoff.
   Produce one markdown handoff that explains the selected boundary, ADK composition pattern, A2A interactions, TODO business logic, and testing notes.

8. Materialize only when requested.
   If the user asks for files, create a minimal ADK-oriented scaffold under `agents/<agent_name>`. Keep incomplete business logic as explicit TODOs.

## Ask The User Only When Required

- The request lacks a stable identity after reading the requirement.
- The owner or domain boundary is required for a safe A2A/shared-boundary decision and cannot be inferred.
- The user asks for runnable code but the target runtime, language, or model configuration is unspecified.

Do not ask for prior delta paths when the user intentionally wants a cold-start run.

## Output Contract

Start with the resolved `repo_path`, `request_unit`, and `agent_name`.

Produce:

- evidence summary JSON
- incremental shared-context summary JSON
- classification JSON
- commonization notes JSON
- implementation handoff markdown
- optional scaffold files only when requested

When A2A is required, show the remote interaction boundary explicitly. When internal workflow is required, keep it inside the selected ADK agent boundary and do not automatically promote it to remote A2A.

## Defaults

- Default to a candidate `Specialist Agent`.
- Default to local tool or local sub-agent reuse when the dependency is in the same runtime.
- Default to A2A only for independent remote agents with their own capability boundary.
- Default to ADK `SequentialAgent`, `ParallelAgent`, or `LoopAgent` only when deterministic internal control flow is needed.
- Default to TODO business logic rather than pretending an incomplete scaffold is production-ready.
