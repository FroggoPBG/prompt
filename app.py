import streamlit as st
from datetime import datetime, date

# Local modules
from components.recipes import (
    SCAFFOLDS, LN_CONTEXT, PROMPT_RECIPES,
    fill_recipe, shape_output
)
from components.presets import export_preset_bytes, load_preset_into_state

# -------------------- Page --------------------
st.set_page_config(page_title="LexisNexis Prompt Composer (no APIs)", page_icon="🧠", layout="wide")
st.title("🧠 LexisNexis Prompt Composer (no APIs)")
st.caption("Generate high-quality, localized prompt briefs for any AI tool (ChatGPT, Copilot, Gemini) — no external APIs.")

# -------------------- Language & output --------------------
col_lang, col_out = st.columns([1, 1])
with col_lang:
    lang_code = st.selectbox(
        "Target language",
        options=list(SCAFFOLDS.keys()),  # en/zh/ko/ja
        format_func=lambda k: SCAFFOLDS[k]["name"],
        index=0,
    )
with col_out:
    output_format = st.selectbox("Output target", LN_CONTEXT["outputs"], index=0)  # "plain prompt" by default

# -------------------- Sidebar: global schema --------------------
with st.sidebar:
    st.header("Client identity")
    client_name = st.text_input("Client name")
    client_type = st.selectbox("Client type", LN_CONTEXT["client_types"], index=0)
    region = st.selectbox("Region / Country", LN_CONTEXT["regions"], index=0)
    practice_areas = st.multiselect("Industry / practice area(s)", LN_CONTEXT["practice_areas"])

    st.header("CS context")
    account_owner = st.text_input("Account owner / RM name")
    relationship_stage = st.selectbox("Relationship stage", LN_CONTEXT["stages"], index=1)
    products_used = st.multiselect("Primary LexisNexis products used", LN_CONTEXT["products"])

    st.header("Metrics (optional)")
    usage_metrics = st.text_area("Usage metrics (logins, searches, features, report)")
    time_saved = st.text_input("Time saved / efficiency data (e.g., 'avg. 4 hours/week')")
    nps_info = st.text_area("NPS score / feedback theme (paste)")

    st.header("Communication settings")
    # Tone “auto” = localized by Region + Stage (JP/KR more formal; Complaint -> apologetic)
    tone = st.selectbox("Tone", LN_CONTEXT["tones"], index=0)
    length = st.selectbox("Length preference", LN_CONTEXT["lengths"], index=2)
    include_highlights = st.checkbox("Auto-include product highlights (region-aware)", value=True)

    st.markdown("---")
    st.subheader("Presets")
    preset_bytes = export_preset_bytes(
        client_name=client_name,
        client_type=client_type,
        products_used=products_used,
        account_owner=account_owner,
        practice_areas=practice_areas,
        region=region,
    )
    st.download_button("💾 Export client preset (.json)", preset_bytes, file_name="client_preset.json", mime="application/json")
    uploaded = st.file_uploader("📂 Import client preset (.json)", type="json")
    if uploaded:
        load_preset_into_state(uploaded)
        st.success("✅ Preset loaded. Update fields as needed.")

# -------------------- Main: function selection --------------------
left, right = st.columns([2, 3])

with left:
    recipe = st.selectbox(
        "Function / Use-case",
        [
            "Renewal Email",
            "QBR Brief",
            "Client Follow-up",
            "Proposal / RFP Response",
            "Upsell / Cross-sell Outreach",
            "Client Risk Alert",
            "Client Snapshot & Risk Signals",
            "Objection Coach",
            "NPS Engagement",
        ],
        index=0
    )

with right:
    st.subheader("Few-shot examples (optional)")
    ex_col1, ex_col2 = st.columns(2)
    with ex_col1:
        ex_input = st.text_area("Example input", height=80, placeholder="Short example input")
    with ex_col2:
        ex_output = st.text_area("Example output", height=80, placeholder="Desired example output")

# -------------------- Guided forms by function --------------------
st.markdown("---")
st.markdown("### 🧩 Guided options")

guided = {}

if recipe == "Renewal Email":
    with st.expander("Renewal options", expanded=True):
        pricing_concern_level = st.select_slider("Pricing concern level", options=["Mild", "Moderate", "High"], value="Moderate")
        contract_details = st.text_input("Contract details (renewal date / price change)")
        meeting_options = st.text_input("2–3 date/time options (comma-separated)", placeholder="e.g., Tue 10am, Wed 2pm, Thu 4pm")
        guided.update({
            "pricing_concern_level": pricing_concern_level,
            "contract_details": contract_details,
            "meeting_options": meeting_options,
        })

elif recipe == "QBR Brief":
    with st.expander("QBR options", expanded=True):
        qbr_window = st.selectbox("Review period", ["Last Month", "Last Quarter", "H1", "FY"], index=1)
        qbr_include_benchmarks = st.checkbox("Include industry benchmarks", value=False)
        qbr_sections = st.multiselect(
            "Sections to emphasize",
            ["Usage & Engagement", "Business Impact", "Wins", "Underused Features", "Recommendations"],
            default=["Usage & Engagement", "Business Impact", "Recommendations"]
        )
        guided.update({
            "qbr_window": qbr_window,
            "qbr_include_benchmarks": qbr_include_benchmarks,
            "qbr_sections": qbr_sections,
        })

elif recipe == "Client Follow-up":
    with st.expander("Follow-up options", expanded=True):
        last_meeting_date = st.text_input("Date of last meeting")
        meeting_topics = st.text_input("Topics covered")
        guided.update({
            "last_meeting_date": last_meeting_date,
            "meeting_topics": meeting_topics,
        })

elif recipe == "Proposal / RFP Response":
    with st.expander("RFP options", expanded=True):
        rfp_sector = st.text_input("Client sector")
        rfp_scope = st.text_area("RFP scope / key requirements")
        rfp_differentiators = st.text_area("Differentiators to emphasize")
        rfp_deadline = st.text_input("Key deadline")
        guided.update({
            "rfp_sector": rfp_sector,
            "rfp_scope": rfp_scope,
            "rfp_differentiators": rfp_differentiators,
            "rfp_deadline": rfp_deadline,
        })

elif recipe == "Upsell / Cross-sell Outreach":
    with st.expander("Upsell options", expanded=True):
        pains = st.text_area("Client pain points")
        proposed_products = st.multiselect("Proposed LexisNexis products", LN_CONTEXT["products"])
        case_studies = st.text_area("Relevant case studies")
        guided.update({
            "pains": pains,
            "proposed_products": proposed_products,
            "case_studies": case_studies,
        })

elif recipe == "Client Risk Alert":
    with st.expander("Risk options", expanded=True):
        risk_trigger = st.selectbox("Risk trigger", ["Declining usage", "Delayed renewal", "Negative feedback", "Champion turnover", "Other"], index=0)
        risk_severity = st.select_slider("Severity", options=[1,2,3,4,5], value=3)
        risk_mitigations = st.text_area("Mitigation options (enablement plan, cadence, etc.)")
        guided.update({
            "risk_trigger": risk_trigger,
            "risk_severity": risk_severity,
            "risk_mitigations": risk_mitigations,
        })

elif recipe == "Client Snapshot & Risk Signals":
    with st.expander("Snapshot options", expanded=True):
        prepared_by = st.selectbox("Prepared by", ["Sales", "Pre-Sales", "Customer Success"], index=0)
        last_engagement_date = st.text_input("Last engagement date")
        risk_level = st.select_slider("Risk level", options=["Low","Medium","High"], value="Medium")
        guided.update({
            "prepared_by": prepared_by,
            "last_engagement_date": last_engagement_date,
            "risk_level": risk_level,
        })

elif recipe == "Objection Coach":
    with st.expander("Objection options", expanded=True):
        objection_type = st.selectbox("Objection type", ["Price", "Usability", "Prefer Competitor"], index=0)
        objection_severity = st.select_slider("Severity", options=[1,2,3,4,5], value=3)
        competitor_name = st.text_input("Competitor (optional)")
        supporting_data = st.multiselect("Supporting data available", ["Usage metrics", "ROI", "NPS quotes", "Case studies", "Benchmarks"])
        guided.update({
            "objection_type": objection_type,
            "objection_severity": objection_severity,
            "competitor_name": competitor_name,
            "supporting_data": supporting_data,
        })

elif recipe == "NPS Engagement":
    with st.expander("NPS options", expanded=True):
        nps_previous_rating = st.selectbox("Previous NPS", ["Promoter (9–10)", "Passive (7–8)", "Detractor (0–6)"], index=1)
        nps_feedback_theme = st.text_input("Feedback theme (summary)")
        nps_survey_link = st.text_input("Survey link / CTA")
        guided.update({
            "nps_previous_rating": nps_previous_rating,
            "nps_feedback_theme": nps_feedback_theme,
            "nps_survey_link": nps_survey_link,
        })

# -------------------- Quality checklist --------------------
st.markdown("---")
st.markdown("### ✅ Quality Checklist")
for item in [
    "No confidential client data present",
    "Claims are accurate/verifiable (no legal advice)",
    "Outcome/ROI linked to metrics",
    "Clear CTA / next steps included",
]:
    st.checkbox(item)

# -------------------- Generate --------------------
if st.button("✨ Generate Prompt"):
    ctx = dict(
        # Global schema
        client_name=client_name,
        client_type=client_type,
        region=region,
        practice_areas=practice_areas,
        account_owner=account_owner,
        relationship_stage=relationship_stage,
        products_used=products_used,
        usage_metrics=usage_metrics,
        time_saved=time_saved,
        nps_info=nps_info,
        tone=tone,
        length=length,
        include_highlights=include_highlights,
        output_target=output_format,

        # Few-shot
        ex_input=ex_input or "",
        ex_output=ex_output or "",
    )

    # Guided, function-specific
    ctx.update(guided)

    final_prompt = fill_recipe(recipe, lang_code, ctx)
    shaped = shape_output(final_prompt, output_format, client_name, recipe)

    st.subheader("📝 Copy-ready Prompt for AI tool")
    st.code(shaped, language="markdown")

    fname = f"ln_prompt_{recipe.replace('/','_')}_{lang_code}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.txt"
    st.download_button(
        "📥 Download (.txt)",
        shaped.replace("{today}", str(date.today())),
        file_name=fname,
        mime="text/plain"
    )

st.caption("Tip: set Tone to ‘auto’ to localize by Region + Stage (e.g., Japan=polite; Complaint=apologetic).")
