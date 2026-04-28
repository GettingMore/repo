# Internal Workflow Composition

Use internal ADK workflow when the selected boundary needs deterministic control flow.

Patterns:

- `sequential`: ordered steps where each step depends on previous output
- `parallel`: independent branches that can run concurrently and be joined
- `loop`: bounded retry, review, revision, or convergence pattern

Rules:

- Keep internal workflow inside the selected agent boundary.
- Do not convert internal workflow into remote A2A unless the dependency is independently owned or hosted.
- Record the workflow in `classification.internal_workflow`.
- Preserve TODOs for business logic that is not implemented yet.
