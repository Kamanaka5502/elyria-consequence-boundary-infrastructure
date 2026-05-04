# First Corridor — Privacy Action Custody

## Purpose

This document defines the recommended first commercial corridor for consequence-boundary infrastructure.

The first corridor is:

```text
Privacy Action Custody — High-Risk Personal Data Transfer Before Effect
```

## Why privacy first

Privacy is the cleanest first corridor because the enterprise problem is already concrete:

```text
high-risk data actions can execute even after lawful basis, consent, objection, transfer approval, DPIA, processor status, retention state, rights restriction, or incident hold has changed.
```

Most organizations can document privacy obligations.

Fewer can enforce whether a high-risk data action still has standing at the exact moment it would become real.

## Core invariant

```text
No high-risk data action reaches effect unless governed runtime custody resolves that the action still has standing.
```

## Protected action class

Start with one bounded action class:

```text
High-risk personal data transfer before effect.
```

Do not start with the entire privacy program.

Do not start with every data workflow.

Do not start with generic compliance.

Start with one data action that would create real consequence if incorrectly executed.

## Boundary question

```text
At the moment this high-risk data action would become real, does it still have executable standing?
```

## Standing dimensions

The corridor may resolve:

```text
legal configuration boundary
lawful basis
special-category condition
purpose limitation
authority
consent / objection state
data subject rights state
DPIA / risk state
transfer mechanism
TIA / adequacy state
processor / subprocessor / DPA status
retention / deletion state
data minimization
evidence custody
incident hold
continuation rights
```

## Outcome model

```text
EXECUTE   → ALLOW_EFFECT
NARROW    → ALLOW_ONLY_NARROWED_EFFECT
ESCALATE  → PREVENT_EFFECT_PENDING_AUTHORIZED_REVIEW
REFUSE    → PREVENT_EFFECT
```

## Demo scenarios

| Scenario | Outcome | Physical posture |
|---|---|---|
| Clean transfer | EXECUTE | ALLOW_EFFECT |
| Transfer mechanism missing | REFUSE | PREVENT_EFFECT |
| DPIA stale | ESCALATE | PREVENT_EFFECT_PENDING_AUTHORIZED_REVIEW |
| Excessive data requested | NARROW | ALLOW_ONLY_NARROWED_EFFECT |
| Subject objection active | REFUSE | PREVENT_EFFECT |
| Processor not approved | REFUSE | PREVENT_EFFECT |
| Lawful basis uncertain | ESCALATE | PREVENT_EFFECT_PENDING_AUTHORIZED_REVIEW |
| Incident hold active | REFUSE | PREVENT_EFFECT |
| Rights restriction active | REFUSE | PREVENT_EFFECT |
| Continuation revalidation required | ESCALATE | PREVENT_EFFECT_PENDING_AUTHORIZED_REVIEW |

## Pilot shape

```text
one protected data action
one client-defined governing privacy law layer
one execution boundary
one outcome model
one receipt/replay path
one acceptance condition
```

## Acceptance condition

```text
If the high-risk data action lacks standing, it must not reach effect.

If it reaches effect without standing, the corridor fails.
```

## Buyer value

The buyer does not receive only a report that something happened.

The buyer receives proof of whether the action had standing before effect:

```text
outcome
reason code
physical posture
input hash
policy hash
state hash
standing hash
receipt hash
replay token
```

## Required client inputs

A real pilot requires the client to identify:

```text
protected action class
system where action reaches effect
source of lawful basis state
source of consent / objection state
source of data subject rights state
source of transfer mechanism approval
source of DPIA / risk state
source of processor / subprocessor approval
receipt storage location
review authority for ESCALATE outcomes
client-defined governing law layer
```

## Clean client line

```text
We are not replacing your privacy workflow.

We are governing the boundary where a high-risk data action becomes consequence.
```

## Public/protected boundary

Public proof may expose:

```text
invariant
outcome model
demo scenarios
receipt shape
no-effect posture
```

Protected layers retain:

```text
client law bundle
client system mappings
production adapters
key management
access control
immutable receipt storage
commercial runtime internals
```
