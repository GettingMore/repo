# Boundary Decision Rules

## Specialist Agent

Choose `Specialist Agent` when the request has one narrow responsibility, a bounded input/output contract, and can hide internal tools or workflow behind one external interface.

## Shared Agent

Choose `Shared Agent` when a capability is reusable across multiple specialists and needs its own policy, lifecycle, memory, or ownership.

## Tool/Adapter

Choose `Tool/Adapter` when the reusable unit is deterministic integration: API call, search, retrieval, validation, parsing, transformation, or storage.

## Metadata Registry

Choose `Metadata Registry` when the reusable unit is mostly declarative: routing tables, capability catalogs, schemas, policy metadata, or configuration.

## Default

Start specialist-first. Promote only when evidence shows reuse, ownership, or lifecycle pressure.
