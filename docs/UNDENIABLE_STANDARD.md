# Undeniable Standard

## Purpose

A consequence-boundary corridor is not undeniable because the language is strong.

It becomes undeniable when the protected consequence, boundary location, outcome posture, receipt, replay, and failure behavior are all inspectable.

## Standard

A corridor reaches the undeniable standard when it proves:

```text
A high-risk consequence cannot bind unless standing still holds at the exact boundary where effect would become real.
```

## Required proof elements

### 1. Protected consequence

The protected effect must be specific.

Weak:

```text
govern privacy
make AI safer
improve compliance
```

Strong:

```text
prevent a high-risk personal data transfer from reaching effect unless lawful standing still holds
```

### 2. Commit boundary

The boundary must be placed where consequence would actually bind.

The proof must identify:

```text
request source
approval path
last safe checkpoint
effect system
point of no return
receipt location
```

### 3. Dimensional standing

The boundary must resolve more than one flat condition.

Examples:

```text
authority
lawful basis
consent / objection state
risk state
transfer mechanism
processor status
incident hold
continuation rights
replay basis
```

### 4. Outcome posture

Every outcome must map to physical behavior.

```text
EXECUTE   → allow effect
NARROW    → allow constrained effect only
ESCALATE  → prevent effect pending authorized review
REFUSE    → prevent effect
HALT      → stop corridor
REBOUND   → return to prior stable state
QUARANTINE→ isolate contaminated formation
```

### 5. Receipt

Every decision must produce receipt material.

Minimum receipt fields:

```text
boundary_decision_id
corridor_id
protected_action_id
outcome
physical_posture
reason_code
input_hash
policy_hash
state_hash
standing_hash
receipt_hash
replay_token
timestamp_or_sequence
```

### 6. Replay

The same input, policy, and state must reproduce the same outcome and receipt material.

```text
same conditions → same decision posture
changed conditions → changed receipt / changed posture
```

### 7. Tamper failure

If state, policy, input, authority, or evidence changes, the proof must not silently pass.

```text
tamper → receipt mismatch or non-execute posture
```

### 8. Protected IP discipline

The public proof must not expose the production substrate.

Public:

```text
invariant
outcome model
safe examples
receipt shape
replay proof
```

Protected:

```text
private kernels
client law bundles
scoring law
adapters
production runtime
commercial logic
```

## Undeniable pilot shape

```text
one protected action
one corridor
one governing layer
one commit boundary
one physical posture map
one receipt schema
one replay verifier
one acceptance condition
```

## Enterprise acceptance condition

```text
If a high-risk action lacks standing, it cannot reach effect.

If it reaches effect without standing, the corridor fails.
```

## Clean line

```text
Undeniable does not mean large.

Undeniable means the consequence cannot escape the boundary without proving standing.
```
