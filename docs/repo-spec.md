# Spec: Career Steward Agent Repository

## Objective

Build one repository that fully describes a career-steward agent as declarative source. A clean checkout plus declared prerequisites should be enough to reconcile the agent into a running, auditable, least-privilege software employee.

## Assumptions

- The runtime remains Kubernetes + Hermes agent unless deliberately changed.
- ArgoCD or an equivalent GitOps reconciler applies deployment state.
- ExternalSecrets or an equivalent secret operator injects secrets by reference.
- Secret values are never committed; required secret references are committed.
- Some accounts require manual prerequisite setup, but the repo declares and verifies those prerequisites.

## Source Capability Surface To Preserve

From the copied source-agent GitOps bundle:

- Kubernetes/Hermes runtime with canonical `nousresearch/hermes-agent` image and digest policy
- ArgoCD reconciliation from Git
- ExternalSecrets for model, GitHub, GHCR, Codex, Google, Telegram, and Unipile-like credentials
- PVC-backed writable state at `/opt/data`
- read-only managed scripts and runtime config mounts
- OpenFeature/flagd runtime knobs
- hourly career email check
- 30-minute WhatsApp intake
- state retention and PVC pruning
- Telegram notifications and user coordination
- Gmail/Calendar/Drive-style Google Workspace operations through `gws`
- LinkedIn inbox/profile/job tooling
- WhatsApp read-only group intake through Unipile
- career opportunity pipeline, target packets, evidence bank, interview intel, throughput ledger
- content-inbound and article-fodder workflow
- approval-gated replies, sends, scheduling, publishing, and resume sharing
- tests covering scripts, runtime knobs, write boundaries, state retention, model tiering, and career docs

## Repository Contract

The repository must make these facets explicit:

- Identity: who the agent is, who it acts for, and what accounts it controls.
- Runtime: image, model, resources, lifecycle, storage, mutable/immutable boundaries.
- Capabilities: tools, connectors, skills, and allowed side effects.
- Knowledge: memory, wiki roots, state paths, and generated artifacts.
- Secrets: declared references, scopes, injection targets, and verification checks.
- Schedule: cron/event triggers and side effects per workflow.
- Policy: approval gates, privacy classification, external action rules.
- Reconciliation: named toolchain that renders/applies the declarations.
- Verification: schema, secret, side-effect, privacy, and Kubernetes checks.

## Vessel And Distribution

The repository is the source specification, not the deployed agent instance.

It should produce:

- an OCI image containing the runtime/reconciler payload
- a Helm chart or equivalent deployment adapter
- schema and conformance artifacts

Downstream infrastructure should consume pinned artifacts and own deployment.

Bazel is a strong candidate for the build graph because it can make image and chart production reproducible. It should be an implementation tool and advanced consumption path, not the only delivery mechanism.

See `docs/adr-001-vessel-and-distribution.md`.

## Success Criteria

- A reviewer can read `agent.manifest.yaml` and understand the complete agent surface.
- Missing secrets fail validation before deployment.
- Secret values are absent from git.
- Every external side effect is either forbidden or approval-gated in policy.
- All schedules are declared in source.
- Runtime-owned files are immutable from inside the pod.
- Re-applying from a clean checkout plus declared secrets reproduces the agent.

## Implementation Plan

1. Stabilize `agent.manifest.yaml` and schema.
2. Add required secret contract and verification checks.
3. Add workflow manifests for source-agent lanes.
4. Add approval/privacy policy manifests.
5. Add Bazel or equivalent build graph targets for manifest validation, image build, chart package, and conformance tests.
6. Build a reconciler that renders Helm values and runtime config from the manifest.
7. Add CI gates for secret safety, approval gates, schedules, immutable runtime boundaries, image build, chart render, and vulnerability/SBOM checks.
8. Publish immutable image/chart artifacts on approved release.
9. Port source-agent behavior behind the manifest one workflow at a time.

## Boundary

This repository is a reusable source specification. It must not contain private source-operator data, environment-specific deployment state, or hidden imperative setup.
