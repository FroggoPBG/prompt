# components/presets.py
from __future__ import annotations

import json
from typing import Any, Dict, List

import streamlit as st


def export_preset_bytes(
    *,
    client_name: str,
    client_type: str,
    products_used: List[str],
    account_owner: str,
    practice_areas: List[str],
    region: str,
    primary_role: str = "",
    primary_use_case: str = "",
    key_metrics: List[str] | None = None,
) -> bytes:
    """
    Build a JSON preset for export. Keep this in sync with how app.py calls it.
    """
    payload: Dict[str, Any] = {
        "client_name": client_name,
        "client_type": client_type,
        "products_used": products_used,
        "account_owner": account_owner,
        "practice_areas": practice_areas,
        "region": region,
        "primary_role": primary_role,
        "primary_use_case": primary_use_case,
        "key_metrics": key_metrics or [],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")


def load_preset_into_state(uploaded_file) -> None:
    """
    Read a .json preset and push values into st.session_state so UI fields update.
    Safe / defensive: ignore missing keys.
    """
    try:
        raw = uploaded_file.read()
        data = json.loads(raw.decode("utf-8"))
    except Exception:
        st.error("Could not read preset file. Please check the format.")
        return

    def _maybe_set(key: str, default: Any = ""):
        if key in data:
            st.session_state[key] = data.get(key, default)

    _maybe_set("client_name", "")
    _maybe_set("client_type", "")
    _maybe_set("products_used", [])
    _maybe_set("account_owner", "")
    _maybe_set("practice_areas", [])
    _maybe_set("region", "")
    _maybe_set("primary_role", "")
    _maybe_set("primary_use_case", "")
    _maybe_set("key_metrics", [])

    st.success("✅ Preset loaded. Fields updated from file.")
