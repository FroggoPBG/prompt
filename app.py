import streamlit as st
from datetime import datetime, date
from components.recipes import (
    SCAFFOLDS, LN_CONTEXT, PROMPT_RECIPES,
    fill_recipe, shape_output
)
from components.presets import export_preset_bytes, load_preset_into_state

# ---------- Page setup ----------
st.set_page_config(page_title="LexisNexis Prompt Builder (no APIs)", page_icon="🧠", layout="wide")
st.title("🧠 LexisNexis Prompt Builder (no APIs)")
st.caption("Multilingual, guided workflows (Renewal, QBR, Client Snapshot, Objection Coach) — no external APIs.")

# ---------- Language & output format ----------
col_lang, col_format = st.columns([1, 1])
with col_lang:
    lang_code = st.selectbox(
        "Target language",
        options=list(SCAFFOLDS.keys()),  # en / zh / ko / ja
        format_func=lambda k: SCAFFOLDS[k]["name"],
        index=0
    )
with col_format:
    output_format = st.selectbox(
        "Output format",
        ["plain text", "email", "CRM note", "slide outline"],
        index=0
    )

# ---------- Sidebar: Client & context ----------
with st.sidebar:
    st.header("Client Profile")
    client_name = st.text_input("Client name")
    client_type = st.selectbox("Client type", ["law firm", "in-house legal", "government", "corporate"], index=0)
    products_used = st.multiselect("Products in use", LN_CONTEXT["products"])
    region = st.selectbox("Region", ["Global", "Hong Kong"], index=0)
    include_highlights = st.checkbox("Auto-include product highlights", value=True)

    primary_role = st.selectbox("Your role", LN_CONTEXT["roles"])
    audience_role = st.selectbox("Primary audience", LN_CONTEXT["audiences"])
    key_metrics = st.multiselect("Metrics to emphasise", LN_CONTEXT["metrics"])

    wins_or_metrics = st.text_area("Recent wins / metrics (free text)")
    objection = st.text_input("Top renewal objection (optional)")
    meeting_notes = st.text_area("Paste meeting notes (optional)")
    signal_snippets = st.text_area("Paste client communication snippets (optional)")

    st.markdown("---")
    st.subheader("Presets")
    preset_bytes = export_preset_bytes(
        client_name, client_type, products_used, primary_role, audience_role, key_metrics
    )
    st.download_button(
        "💾 Export client preset (.json)",
        preset_bytes,
        file_name="client_preset.json",
        mime="application/json"
    )
    uploaded = st.file_uploader("📂 Import client preset (.json)", type="json")
    if uploaded:
        import json
        data = json.load(uploaded)
        load_preset_into_state(data)
        st.success("✅ Preset loaded. Update fields as needed.")

# ---------- Main controls ----------
col_left, col_right = st.columns([2, 3])

with col_left:
    recipe = st.selectbox("Function / Use-case", list(PROMPT_RECIPES.keys()), index=0)

    # Global style sliders
    tone = st.select_slider(
        "Tone",
        options=["neutral", "friendly", "formal", "persuasive", "technical", "concise"],
        value="neutral"
    )
    depth = st.select_slider("Depth/rigor", options=["brief", "standard", "in-depth"], value="standard")
    length = st.select_slider("Target length", options=["very short", "short", "medium", "long"], value="medium")
    add_critique = st.checkbox("Add self-critique + revision step", value=True)

with col_right:
    st.subheader("Additional Inputs (optional)")
    user_goal = st.text_area("Goal / problem statement", height=120, placeholder="Describe what you want the model to do.")
    inputs = st.text_area("Key inputs (paste any text/data/instructions)", height=120, placeholder="Optional: source text, facts, requirements…")
    ex_col1, ex_col2 = st.columns(2)
    with ex_col1:
        ex_input = st.text_area("Few-shot: Example input", height=100, placeholder="Short example input")
    with ex_col2:
        ex_output = st.text_area("Few-shot: Example output", height=100, placeholder="Desired example output")

# ---------- Dynamic guided workflow (forms change by function) ----------
st.markdown("---")
st.markdown("### 🧩 Guided options (change by function)")

guided_ctx = {}

if recipe == "Renewal Email":
    with st.expander("Renewal-specific options", expanded=True):
        pricing_concern_level = st.select_slider("Pricing concern level", options=["Mild","Moderate","High"], value="Moderate")
        meeting_options = st.text_input("2–3 date/time options (comma-separated)", placeholder="e.g., Tue 10am, Wed 2pm, Thu 4pm")
        guided_ctx.update({
            "pricing_concern_level": pricing_concern_level,
            "meeting_options": meeting_options,
        })

elif recipe == "QBR Brief":
    with st.expander("QBR-specific options", expanded=True):
        qbr_window = st.selectbox("Time window", ["Last Month","Last Quarter","Last 6 Months","Last 12 Months"], index=1)
        qbr_compare_benchmarks = st.checkbox("Include benchmarks comparison", value=False)
        qbr_sections = st.multiselect(
            "Sections to emphasize",
            ["Usage & Engagement","Business Impact","Wins","Underused Features","Recommendations"],
            default=["Usage & Engagement","Business Impact","Recommendations"]
        )
        guided_ctx.update({
            "qbr_window": qbr_window,
            "qbr_compare_benchmarks": qbr_compare_benchmarks,
            "qbr_sections": qbr_sections,
        })

elif recipe == "Client Snapshot & Risk Signals":
    with st.expander("Snapshot-specific options", expanded=True):
        prepared_by = st.selectbox("Prepared by", ["Sales","Pre-Sales","Customer Success"], index=0)
        last_engagement_date = st.text_input("Last engagement date (optional)", placeholder="e.g., 2025-02-05 or '2 weeks ago'")
        risk_level = st.select_slider("Risk level", options=["Low","Medium","High"], value="Medium")
        guided_ctx.update({
            "prepared_by": prepared_by,
            "last_engagement_date": last_engagement_date,
            "risk_level": risk_level,
        })

elif recipe == "Objection Coach":
    with st.expander("Objection-specific options", expanded=True):
        objection_type = st.selectbox("Client's reason for hesitation", ["Price","Usability","Prefer Competitor"], index=0)
        objection_severity = st.slider("Severity", 1, 5, 3)
        competitor_name = st.text_input("Competitor (optional)")
        supporting_data = st.multiselect("Supporting data available", ["Usage metrics","ROI","NPS quotes","Case studies","Benchmarks"])
        guided_ctx.update({
            "objection_type": objection_type,
            "objection_severity": objection_severity,
            "competitor_name": competitor_name,
            "supporting_data": supporting_data,
        })

# ---------- Quality checklist ----------
st.markdown("---")
st.markdown("### ✅ Quality Checklist")
checks = [
    "No confidential client data present",
    "Claims are accurate/verifiable (no legal advice)",
    "Outcome/ROI linked to client metrics",
    "Clear CTA / next steps included",
]
_ = [st.checkbox(c) for c in checks]

# ---------- Generate ----------
if st.button("✨ Generate Prompt"):
    ctx = dict(
        role=primary_role,
        client_name=client_name or "[Client Name]",
        client_type=client_type,
        products_used=products_used,
        audience_role=audience_role,
        key_metrics=key_metrics,
        wins_or_metrics=wins_or_metrics,
        objection=objection,
        meeting_notes=meeting_notes,
        signal_snippets=signal_snippets,
        tone=tone,
        depth=depth,
        length=length,
        add_critique=add_critique,
        user_goal=user_goal,
        inputs=inputs,
        ex_input=ex_input,
        ex_output=ex_output,
        region=region,
        include_highlights=include_highlights,
        # Guided, per function:
        **guided_ctx
    )

    final_prompt = fill_recipe(recipe, lang_code, ctx)
    shaped = shape_output(final_prompt, output_format, client_name, recipe)

    st.subheader("📝 Final Prompt")
    st.code(final_prompt, language="markdown")

    fname = f"ln_prompt_{lang_code}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.txt"
    st.download_button(
        "📥 Download prompt (.txt)",
        shaped.replace("{today}", str(date.today())),
        file_name=fname,
        mime="text/plain"
    )

st.caption("💡 Guided workflows + ‘prompt-as-a-brief’ = consistent, high-quality outputs in any supported language.")
