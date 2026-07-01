# ADR 002: Chart Boundary

## Status

Accepted for v1.

## Decision

Use a generic Helm chart that consumes the manifest-derived values and mounts the selected manifest/policy/workflow bundle. Do not generate a bespoke chart per agent.

## Rationale

A generic chart keeps the deployment adapter stable while the agent declaration evolves. The manifest remains the semantic source of truth; Helm handles Kubernetes packaging.

## Consequences

- The chart can be versioned independently.
- Multiple Reeve-class agents can share one chart.
- Chart templates must be validated against the manifest-derived values.
- Agent behavior changes happen in manifests/workflows/policies, not bespoke chart forks.

