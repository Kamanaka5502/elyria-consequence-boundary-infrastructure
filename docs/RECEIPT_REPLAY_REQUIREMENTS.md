# Receipt and Replay Requirements

## Purpose

Consequence-boundary infrastructure is not credible unless decisions are receipted and replayable.

A receipt proves what the boundary resolved.

Replay proves that the same conditions reproduce the same posture.

## Core rule

```text
No high-risk consequence should bind without a decision receipt and replay basis.
```

## Minimum receipt fields

Every corridor should define a receipt carrying at least:

```text
boundary_decision_id
corridor_id
protected_action_id
actor_or_requester_id
outcome
physical_posture
reason_code
input_hash
policy_hash
state_hash
standing_hash
evidence_hash
receipt_hash
replay_token
timestamp_or_sequence
```

## Optional corridor-specific fields

### Privacy Action Custody

```text
lawful_basis_hash
consent_objection_hash
rights_state_hash
transfer_mechanism_hash
processor_status_hash
dpia_risk_hash
incident_hold_hash
minimization_hash
```

### AI Output-to-Action

```text
model_output_hash
authority_hash
workflow_state_hash
risk_state_hash
tool_call_hash
continuation_hash
```

### Mission Control

```text
candidate_hash
stage_from
stage_to
witness_hash
safety_hash
monotonicity_hash
simulation_admission_hash
```

### Privileged Operations

```text
authentication_hash
authority_hash
revocation_hash
risk_context_hash
operation_scope_hash
production_state_hash
```

### Consciousness Boundary

```text
formation_hash
continuity_hash
coherence_hash
standing_hash
contamination_hash
target_legitimacy_hash
```

## Replay requirement

Replay must verify:

```text
same inputs + same policy + same state + same evidence → same outcome + same posture
```

If any governing material changes, the receipt must change.

```text
changed input, policy, state, authority, or evidence → changed receipt or non-execute posture
```

## Tamper requirement

Tampering must not silently pass.

If a receipt, input hash, policy hash, state hash, evidence hash, or standing hash is altered, verification must fail or produce a different posture.

```text
tamper → mismatch / refusal / escalation / halt
```

## Why receipts matter

Logs show that something happened.

Receipts show why a boundary allowed, narrowed, held, refused, halted, rebounded, quarantined, observed, or bound a consequence.

## Why replay matters

Audit without replay is only historical description.

Replayable proof shows whether the decision was deterministic under the same governing conditions.

## Acceptance condition

```text
If the decision cannot be receipted and replayed, the consequence should not be treated as governed.
```

## Clean line

```text
A boundary decision is not enterprise-grade until it can be receipted, replayed, and fail under tamper.
```
