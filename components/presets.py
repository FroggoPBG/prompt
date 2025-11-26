# components/presets.py
import json
from typing import List, Dict, Any


def export_preset_bytes(
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
    Build a JSON preset for export. Must stay in sync with how app.py calls it.
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
