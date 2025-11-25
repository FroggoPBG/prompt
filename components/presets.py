import io, json
import streamlit as st

def export_preset_bytes(
    client_name=None,
    client_type=None,
    products_used=None,
    account_owner=None,
    practice_areas=None,
    region=None
):
    """Export client preset as downloadable JSON."""
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
    """Load preset JSON back into Streamlit session_state."""
    for k, v in data.items():
        st.session_state[k] = v
    st.success("Preset imported successfully.")
