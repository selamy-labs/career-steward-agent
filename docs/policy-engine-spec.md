# Policy Engine Spec

## Default

External side effects are denied unless explicitly allowed by policy and, when required, approved by the current user.

## Exact-Text Approval

Approval-gated actions require:

- channel
- recipient
- exact text or artifact URL
- current user approval in the current interaction context

The approval must include the exact recipient, channel, and text/artifact being sent or shared. Approval expires after the current turn unless reconfirmed.

## Escalation

If the agent is uncertain whether an action is external, public, irreversible, or privacy-sensitive, it must escalate to the user and treat the action as approval-required.

## Forbidden Actions

The v1 forbidden list includes:

- publish raw private transcripts
- publish raw third-party chat text
- commit secret values
- mutate repo-owned runtime files inside a running pod
- bypass OAuth or counterparty controls
- send WhatsApp messages from read-only intake workflows
- publish public content without explicit approval

## Non-Removable Capability

Approval gating and privacy validation are required capabilities. A manifest that omits them is invalid.

