# components/presets.py
import io
import json
import streamlit as st

def export_preset_bytes(
    client_name: str = "",
    client_type: str = "",
    products_used=None,
    account_owner: str = "",
    practice_areas=None,
    region: str = "",
):
    if products_used is None:
        products_used = []
    if practice_areas is None:
        practice_areas = []

    payload = {
        "client_name": client_name,
        "client_type": client_type,
        "products_used": products_used,
        "account_owner": account_owner,
        "practice_areas": practice_areas,
        "region": region,
    }
    b = io.BytesIO(json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8"))
    b.seek(0)
    return b

def load_preset_into_state(data: dict):
    # Update Streamlit session_state with keys from the preset JSON
    for k, v in data.items():
        st.session_state[k] = v
