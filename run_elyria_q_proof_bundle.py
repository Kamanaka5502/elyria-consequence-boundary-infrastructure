#!/usr/bin/env python3
"""
Elyria-Q Proof Bundle Runner
Built by Elyria Systems — VA

Runs the current Elyria-Q standing diagnostics proof surfaces as one deterministic
bundle and emits a combined bundle receipt. This is the front-door proof command
for banking, high-government security, and regulated data review.
"""
from __future__ import annotations

from hashlib import sha256
import json
from typing import Any, Dict

from elyria_q_standing_diagnostics import demo_high_value_wire_transfer
from elyria_q_data_standing_diagnostics import demo_sensitive_data_export


def stable_hash(obj: Any) -> str:
    encoded = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256(encoded).hexdigest()


def run_bundle() -> Dict[str, Any]:
    banking = demo_high_value_wire_transfer()
    data = demo_sensitive_data_export()

    proof_bundle = {
        "engine": "Elyria-Q Standing Diagnostics Proof Bundle",
        "built_by": "Elyria Systems — VA",
        "bundle_version": "1.0.0",
        "purpose": "pre-effect admissibility proof for high-risk operations and regulated data consequences",
        "principle": "Collapse is late. Standing decay is early.",
        "proof_surfaces": {
            "banking_high_value_transfer": banking,
            "regulated_data_export": data,
        },
    }

    proof_bundle["bundle_receipt"] = {
        "bundle_hash": stable_hash(proof_bundle),
        "banking_receipt_hash": stable_hash(banking["resolution"]["receipt"]),
        "data_receipt_hash": stable_hash(data["resolution"]["receipt"]),
        "replay_token": stable_hash({"elyria_q_replay_bundle": proof_bundle}),
    }

    return proof_bundle


if __name__ == "__main__":
    print(json.dumps(run_bundle(), indent=2, sort_keys=True))
