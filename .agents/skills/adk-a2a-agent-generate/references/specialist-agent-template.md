# Specialist Agent Template

A specialist agent should have:

- stable `agent_name`
- short responsibility statement
- input contract
- output contract
- owned decisions
- non-owned upstream or downstream responsibilities
- local tools or local sub-agents
- optional internal ADK workflow
- optional A2A interactions

Template:

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="agent_name",
    model="model-name",
    description="Single responsibility.",
    instruction="TODO: implement the specialist policy and response contract.",
    tools=[],
)
```
