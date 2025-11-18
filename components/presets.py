import io, json
import streamlit as st

def export_preset_bytes(client_name, client_type, products_used, primary_role, audience_role, key_metrics):
    payload = {
        "client_name": client_name,
        "client_type": client_type,
        "products_used": products_used,
        "primary_role": primary_role,
        "audience_role": audience_role,
        "key_metrics": key_metrics
    }
    b = io.BytesIO(json.dumps(payload, indent=2).encode())
    b.seek(0)
    return b

def load_preset_into_state(data: dict):
    for k, v in data.items():
        st.session_state[k] = v
