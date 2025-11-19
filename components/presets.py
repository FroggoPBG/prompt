import io, json
import streamlit as st

def export_preset_bytes(
    client_name=None,
    client_type=None,
    products_used=None,
    account_owner=None,
    practice_areas=None,
    region=None,
):
    """Export current sidebar client data as downloadable JSON."""
    payload = {
        "client_name": client_name,
        "client_type": client_type,
        "products_used": products_used,
        "account_owner": account_owner,
        "practice_areas": practice_areas,
        "region": region,
    }
    b = io.BytesIO(json.dumps(payload, indent=2, ensure_ascii=False).encode())
    b.seek(0)
    return b

def load_preset_into_state(uploaded_file):
    """Import preset from uploaded JSON and populate session_state."""
    try:
        data = json.load(uploaded_file)
        for k, v in data.items():
            st.session_state[k] = v
        st.success("Preset imported successfully.")
    except Exception as e:
        st.error(f"Error importing preset: {e}")
