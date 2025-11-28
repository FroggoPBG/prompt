# components/presets.py
# Preset management for Legal Tech Sales Prospecting
from __future__ import annotations

import json
from typing import Any, Dict

import streamlit as st


def export_preset_bytes(
    *,
    company_name: str,
    company_url: str,
    practice_area: str,
    buyer_persona: str,
    industry: str = "",
    notes: str = "",
) -> bytes:
    """
    Export prospect research as a JSON preset for reuse.
    """
    payload: Dict[str, Any] = {
        "company_name": company_name,
        "company_url": company_url,
        "practice_area": practice_area,
        "buyer_persona": buyer_persona,
        "industry": industry,
        "notes": notes,
        "version": "1.0",
        "tool": "LegalTech Sales Prospecting - OUS Framework",
    }
    return json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")


def load_preset_into_state(uploaded_file) -> None:
    """
    Load a saved prospect preset into session state.
    """
    try:
        raw = uploaded_file.read()
        data = json.loads(raw.decode("utf-8"))
    except Exception as e:
        st.error(f"Could not read preset file: {str(e)}")
        return

    # Safely load values into session state
    st.session_state["company_name"] = data.get("company_name", "")
    st.session_state["company_url"] = data.get("company_url", "")
    st.session_state["practice_area"] = data.get("practice_area", "General/Multiple")
    st.session_state["buyer_persona"] = data.get("buyer_persona", "General Counsel")
    st.session_state["industry"] = data.get("industry", "")
    st.session_state["notes"] = data.get("notes", "")

    st.success("✅ Preset loaded successfully!")
