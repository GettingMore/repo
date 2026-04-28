# Target Agent Architecture

This reference describes the target shape assumed by the public skill.

## Boundary Layers

- `Specialist Agent`: narrow domain task with a clear input/output contract.
- `Shared Agent`: reusable higher-level agent capability used by multiple specialists.
- `Tool/Adapter`: deterministic API, service, data, or transformation binding.
- `Metadata Registry`: declarative capability, schema, policy, or routing metadata.
- `Internal Workflow`: ADK composition inside an agent boundary.
- `Remote A2A`: protocol interaction with an independent external agent boundary.

## Default Shape

Generated work should prefer:

```text
agents/<agent_name>/
  agent.py
  README.md
  tests/
```

The exact language and framework version can vary by target repository. The public skill describes the decision process and scaffold shape, not a private runtime.

## Important Distinction

Internal ADK workflow is not the same as A2A.

Use ADK workflow agents for deterministic control flow inside one runtime. Use A2A when an agent needs to discover and communicate with another independent agent over the protocol boundary.
