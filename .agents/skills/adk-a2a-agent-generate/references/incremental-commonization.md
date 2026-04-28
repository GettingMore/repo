# Incremental Commonization

Each run may discover reusable elements.

Classify them as:

- confirmed reuse binding
- proposed shared registration
- update to an existing shared item
- retrofit action for earlier agents
- rejected or deferred reuse

Keep the notes incremental. Do not rewrite the whole architecture for every request.

## Commonization Notes Shape

```json
{
  "current_agent": "agent-name",
  "reused_items": [],
  "new_shared_agents": [],
  "new_tools": [],
  "updated_shared_items": [],
  "retrofit_actions": [],
  "a2a_interactions": [],
  "todo": []
}
```
