# ADK A2A Agent Generation

This note captures the design thinking behind the skill.

## The Problem

Agent projects often over-split early. A multi-step workflow gets turned into many remote agents before the boundary is clear. That creates extra contracts, latency, authentication, failure modes, and operational work.

The skill uses a narrower default:

- start with one specialist agent
- reuse local tools or local sub-agents when possible
- add internal ADK workflow composition when deterministic control flow is needed
- use A2A only when another agent is independently owned, deployed, discovered, and invoked through a remote contract

## Public Technical Basis

Google ADK describes agents as self-contained execution units. It distinguishes LLM agents, workflow agents such as `SequentialAgent`, `ParallelAgent`, and `LoopAgent`, and custom agents built from `BaseAgent`.

A2A describes interoperability between independent agents. The protocol centers on discoverable Agent Cards, JSON-RPC request/response structures, message sending, streaming, task state, artifacts, and security considerations.

The skill treats these as different design layers:

- ADK decides how an agent is built internally.
- A2A decides how independent agents communicate across a remote boundary.

## Decision Model

Use a specialist boundary when the requirement has a narrow responsibility and a clear input/output contract.

Use a shared agent when multiple specialists need the same higher-level capability and the capability deserves its own policy, lifecycle, or ownership.

Use a tool adapter when the reusable unit is a deterministic API call, data lookup, transformation, or service binding.

Use a metadata registry when the reusable unit is mostly declarative routing, schema, policy, or capability metadata.

Use internal ADK workflow when the same boundary needs deterministic sequencing, parallel fan-out/fan-in, or bounded retry loops.

Use A2A when the dependency is an independently hosted or independently governed agent and the interaction must cross a remote protocol boundary.

## Why Evidence Comes First

The skill asks for evidence before classification because sparse requirements are normal. Evidence makes assumptions visible:

- what the user actually asked for
- what the candidate agent owns
- what it explicitly does not own
- what reusable boundaries already exist
- what remains speculative

This keeps the handoff honest. The output can be useful even when business logic remains TODO.
