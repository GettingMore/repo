# Target Shape

Default scaffold shape:

```text
agents/<agent_name>/
  agent.py
  README.md
  tests/
```

Recommended `agent.py` responsibilities:

- expose one top-level ADK agent object
- keep the external contract narrow
- wrap deterministic integrations as tools
- place internal workflow composition behind the same boundary
- leave TODO business logic explicit

When A2A is required, add a protocol note or adapter file that describes the remote agent interaction. Do not fake a working remote call without configuration.
