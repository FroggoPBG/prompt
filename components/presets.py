"""Preset management for Legal Tech Sales Prospecting."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Any

import streamlit as st


@dataclass
class ProspectPreset:
    """Represents a saved prospect configuration."""
    company_name: str
    company_url: str
    practice_area: str
    buyer_persona: str
    industry: str = ""
    notes: str = ""
    version: str = "1.0"
    tool: str = "LegalTech Sales Prospecting - OUS Framework"
    
    def to_json_bytes(self) -> bytes:
        """Export preset as JSON bytes."""
        data = asdict(self)
        return json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
    
    @classmethod
    def from_json(cls, json_data: dict[str, Any]) -> ProspectPreset:
        """Create preset from JSON data."""
        # Filter only known fields
        known_fields = {
            'company_name', 'company_url', 'practice_area', 
            'buyer_persona', 'industry', 'notes', 'version', 'tool'
        }
        filtered = {k: v for k, v in json_data.items() if k in known_fields}
        return cls(**filtered)
    
    def load_into_session_state(self) -> None:
        """Load this preset into Streamlit session state."""
        st.session_state["company_name"] = self.company_name
        st.session_state["company_url"] = self.company_url
        st.session_state["practice_area"] = self.practice_area
        st.session_state["buyer_persona"] = self.buyer_persona
        st.session_state["industry"] = self.industry
        st.session_state["notes"] = self.notes


def export_preset_bytes(
    *,
    company_name: str,
    company_url: str,
    practice_area: str,
    buyer_persona: str,
    industry: str = "",
    notes: str = "",
) -> bytes:
    """Export prospect research as a JSON preset for reuse."""
    preset = ProspectPreset(
        company_name=company_name,
        company_url=company_url,
        practice_area=practice_area,
        buyer_persona=buyer_persona,
        industry=industry,
        notes=notes
    )
    return preset.to_json_bytes()


def load_preset_into_state(uploaded_file) -> None:
    """Load a saved prospect preset into session state."""
    try:
        raw = uploaded_file.read()
        data = json.loads(raw.decode("utf-8"))
        preset = ProspectPreset.from_json(data)
        preset.load_into_session_state()
        st.success("✅ Preset loaded successfully!")
    except json.JSONDecodeError as e:
        st.error(f"Invalid JSON format: {str(e)}")
    except Exception as e:
        st.error(f"Could not read preset file: {str(e)}")
