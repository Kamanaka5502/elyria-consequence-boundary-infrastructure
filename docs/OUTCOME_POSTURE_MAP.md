# Outcome Posture Map

## Purpose

Outcome labels are not enough.

For consequence-boundary infrastructure, every outcome must map to physical posture.

The proof is not that the boundary returned a word.

The proof is that the word controlled whether consequence could bind.

## Core rule

```text
Every outcome must determine effect posture.
```

## Standard outcome map

| Outcome | Physical posture | Meaning |
|---|---|---|
| EXECUTE | ALLOW_EFFECT | Action may bind. |
| NARROW | ALLOW_ONLY_NARROWED_EFFECT | Only constrained action may bind. |
| ESCALATE | PREVENT_EFFECT_PENDING_AUTHORIZED_REVIEW | Effect is held until authorized review resolves ambiguity. |
| REFUSE | PREVENT_EFFECT | Effect is blocked. |
| HALT | STOP_CORRIDOR | Corridor stops because safety, integrity, or authority has failed. |
| REBOUND | RETURN_TO_PRIOR_STABLE_STATE | System returns to the last valid support point. |
| QUARANTINE | ISOLATE_CONTAMINATED_FORMATION | Contaminated formation is isolated and cannot bind. |
| OBSERVE | OBSERVE_WITHOUT_BINDING | Formation may be inspected but not persisted or acted on. |
| BIND | ALLOW_SPECIFIC_BINDING | Specific admitted formation may bind to its permitted target. |

## Why this matters

Many systems produce labels such as approved, denied, flagged, risky, or compliant.

Those labels do not necessarily control consequence.

A consequence-boundary outcome must control physical posture:

```text
allowed
narrowed
held
blocked
stopped
rebounded
quarantined
observed only
bound only when admitted
```

## Corridor examples

### Privacy Action Custody

```text
EXECUTE  → data action may proceed
NARROW   → only reduced data scope may proceed
ESCALATE → prevent data effect pending authorized review
REFUSE   → prevent data effect
```

### AI Output-to-Action

```text
EXECUTE  → output may become action
NARROW   → constrained action only
ESCALATE → hold pending authority/risk review
REFUSE   → no action
HALT     → stop corridor
```

### Mission Control

```text
ADMIT      → stage advancement permitted
HOLD       → no advancement pending missing support
REBOUND    → return to prior valid stage
REFUSE     → no advancement
HALT       → stop corridor
QUARANTINE → isolate contaminated formation
CERTIFY    → bounded proof packet may advance to controlled review
```

### Consciousness Boundary

```text
OBSERVE       → internal formation may be inspected but not persisted
BIND_MEMORY   → memory may persist
BIND_IDENTITY → identity reference may persist
REBOUND       → return to prior continuity state
REFUSE_SELF   → self/agency claim cannot bind
QUARANTINE    → isolate contaminated formation
HALT          → stop corridor
```

## Acceptance condition

```text
If an outcome does not control physical posture, it is not a consequence-boundary outcome.
```

## Clean line

```text
The outcome is only real if it controls what can happen next.
```
