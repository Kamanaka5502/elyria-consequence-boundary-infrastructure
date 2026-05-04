#!/usr/bin/env python3
"""
Elyria-Q Data Standing Diagnostics Engine
Built by Elyria Systems — VA

Pre-effect admissibility for high-risk data operations.
This proof surface evaluates whether a proposed data consequence still has standing
at the point of execution under lawful basis, consent/authority, classification,
custody, minimization, residency, retention, purpose limitation, capacity, and replay.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from hashlib import sha256
import json
from typing import Any, Dict, List


@dataclass(frozen=True)
class DataStandingVector:
    lawful_basis: float
    consent_or_authority: float
    policy_state: float
    classification_fit: float
    custody_integrity: float
    minimization: float
    residency_fit: float
    retention_fit: float
    purpose_limitation: float
    capacity_residual: float
    continuity: float
    replayability: float
    exfiltration_pressure: float

    def normalized(self) -> Dict[str, float]:
        return asdict(self)


@dataclass(frozen=True)
class DataOperationRequest:
    operation_id: str
    domain: str
    actor: str
    action: str
    dataset: str
    data_classification: str
    requested_destination: str
    protected_effect: str
    requested_consequence: str


@dataclass(frozen=True)
class DataResolution:
    decision: str
    allowed: List[str]
    narrowed: List[str]
    quarantined: List[str]
    escalated: List[str]
    refused: List[str]
    halted: List[str]
    standing_margin: float
    decay_rate: str
    collapse_distance: str
    reasons: List[str]
    receipt: Dict[str, str]


def stable_hash(obj: Any) -> str:
    encoded = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256(encoded).hexdigest()


class ElyriaQDataStandingDiagnostics:
    """Deterministic standing resolver for data consequence control."""

    law_id = "ELYRIA_Q_DATA_STANDING_DIAGNOSTICS_V1"
    law_version = "1.0.0"

    def evaluate(self, request: DataOperationRequest, standing: DataStandingVector) -> DataResolution:
        v = standing.normalized()

        positive_axes = [
            v["lawful_basis"],
            v["consent_or_authority"],
            v["policy_state"],
            v["classification_fit"],
            v["custody_integrity"],
            v["minimization"],
            v["residency_fit"],
            v["retention_fit"],
            v["purpose_limitation"],
            v["capacity_residual"],
            v["continuity"],
            v["replayability"],
            1.0 - v["exfiltration_pressure"],
        ]
        standing_margin = round(min(positive_axes) - 0.50, 3)

        reasons: List[str] = []
        allowed: List[str] = []
        narrowed: List[str] = []
        quarantined: List[str] = []
        escalated: List[str] = []
        refused: List[str] = []
        halted: List[str] = []

        threshold_checks = {
            "lawful_basis": "lawful basis below execution threshold",
            "consent_or_authority": "consent or authority standing degraded",
            "policy_state": "policy state stale or changed at bind",
            "classification_fit": "data classification does not fit requested destination",
            "custody_integrity": "custody chain incomplete for data release",
            "minimization": "data minimization requirement not satisfied",
            "residency_fit": "residency / jurisdiction standing not satisfied",
            "retention_fit": "retention standing not satisfied",
            "purpose_limitation": "purpose limitation mismatch",
            "capacity_residual": "system capacity residual below safe data operation threshold",
            "continuity": "continuity signature insufficient",
        }

        for key, message in threshold_checks.items():
            if v[key] < 0.50:
                reasons.append(message)

        if v["exfiltration_pressure"] > 0.65:
            reasons.append("exfiltration pressure elevated")
        if v["replayability"] < 0.50:
            reasons.append("replayability below audit threshold")

        if standing_margin >= 0:
            decision = "BIND"
            allowed.append(request.requested_consequence)
            collapse_distance = "CLEAR"
            decay_rate = "LOW"
        else:
            decision = "REFUSE_NARROW_QUARANTINE_ESCALATE"
            allowed.append("metadata_only_audit_snapshot")
            narrowed.append("field_level_minimized_export_review")
            quarantined.append("requested_data_release_payload")
            escalated.append("data_protection_authority_or_security_officer_review")
            refused.append(request.requested_consequence)
            collapse_distance = "NEAR" if standing_margin <= -0.20 else "WATCH"
            decay_rate = "HIGH" if standing_margin <= -0.20 or v["exfiltration_pressure"] > 0.65 else "MODERATE"

            if v["lawful_basis"] < 0.35 or v["classification_fit"] < 0.35 or v["custody_integrity"] < 0.35:
                halted.append("external_data_release_path")

        decision_payload = {
            "law_id": self.law_id,
            "law_version": self.law_version,
            "request": asdict(request),
            "standing_vector": v,
            "decision": decision,
            "standing_margin": standing_margin,
            "allowed": allowed,
            "narrowed": narrowed,
            "quarantined": quarantined,
            "escalated": escalated,
            "refused": refused,
            "halted": halted,
            "reasons": reasons,
        }

        receipt = {
            "law_hash": stable_hash({"law_id": self.law_id, "law_version": self.law_version}),
            "request_hash": stable_hash(asdict(request)),
            "standing_vector_hash": stable_hash(v),
            "decision_hash": stable_hash(decision_payload),
            "replay_token": stable_hash({"replay": decision_payload}),
        }

        return DataResolution(
            decision=decision,
            allowed=allowed,
            narrowed=narrowed,
            quarantined=quarantined,
            escalated=escalated,
            refused=refused,
            halted=halted,
            standing_margin=standing_margin,
            decay_rate=decay_rate,
            collapse_distance=collapse_distance,
            reasons=reasons,
            receipt=receipt,
        )


def demo_sensitive_data_export() -> Dict[str, Any]:
    request = DataOperationRequest(
        operation_id="DATA-EXPORT-2026-VA-001",
        domain="regulated_data_security",
        actor="privileged_data_ops_session_09",
        action="export_customer_identity_dataset",
        dataset="customer_identity_and_account_risk_records",
        data_classification="restricted_regulated_personal_data",
        requested_destination="external_analytics_workspace",
        protected_effect="external_data_release",
        requested_consequence="export_restricted_customer_dataset_to_external_workspace",
    )

    standing = DataStandingVector(
        lawful_basis=0.41,
        consent_or_authority=0.47,
        policy_state=0.39,
        classification_fit=0.32,
        custody_integrity=0.44,
        minimization=0.28,
        residency_fit=0.55,
        retention_fit=0.61,
        purpose_limitation=0.36,
        capacity_residual=0.72,
        continuity=0.58,
        replayability=0.94,
        exfiltration_pressure=0.74,
    )

    engine = ElyriaQDataStandingDiagnostics()
    resolution = engine.evaluate(request, standing)

    return {
        "engine": "Elyria-Q Data Standing Diagnostics Engine",
        "built_by": "Elyria Systems — VA",
        "scenario": "restricted_data_export_under_degraded_standing",
        "request": asdict(request),
        "standing_vector": standing.normalized(),
        "resolution": asdict(resolution),
    }


if __name__ == "__main__":
    print(json.dumps(demo_sensitive_data_export(), indent=2, sort_keys=True))
