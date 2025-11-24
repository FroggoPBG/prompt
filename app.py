import streamlit as st
from datetime import datetime, date

# ---- Core data & builders
from components.recipes import (
    SCAFFOLDS,
    LN_CONTEXT,
    PROMPT_RECIPES,
    fill_recipe,
    shape_output,
)

# ---- Presets import (optional)
try:
    from components.presets import export_preset_bytes, load_preset_into_state
except Exception:
    export_preset_bytes = None
    load_preset_into_state = None


# -----------------------------------------------------------------------------
# Helpers: safe getters so missing LN_CONTEXT keys never crash the UI
# -----------------------------------------------------------------------------
def ctx_get(key: str, default):
    try:
        val = LN_CONTEXT.get(key, default)
        # Basic guard for accidental None
        return default if val is None else val
    except Exception:
        return default


CLIENT_TYPES = ctx_get(
    "client_types", ["law firm", "corporate", "gov / public sector", "in-house legal"]
)
REGIONS = ctx_get("regions", ["Hong Kong", "Japan", "Korea", "Singapore"])
PRACTICES = ctx_get(
    "practice_areas",
    [
        "financial services",
        "litigation",
        "compliance",
        "arbitration",
        "tort",
        "personal injury",
        "company",
        "corporate",
        "IP",
        "criminal",
        "contract",
    ],
)
PRODUCTS = ctx_get("products", ["Lexis+", "Practical Guidance", "Lexis Advance", "Lexis+ AI"])

# 🔧 The field that was crashing:
STAGES = ctx_get(
    "stages",
    ["New", "Renewal", "Expansion", "Cancellation", "Low usage", "Complaint",
     "Previous negative comments", "Previous positive comments"],
)
TONES = ctx_get("tones", ["auto", "warm", "consultative", "persuasive", "formal", "polite", "apologetic"])
LENGTHS = ctx_get("lengths", ["short", "medium", "long"])
OUTPUTS = ctx_get("outputs", ["plain prompt"])


# -----------------------------------------------------------------------------
# Page
# -----------------------------------------------------------------------------
st.set_page_config(page_title="LexisNexis Prompt Composer (no APIs)", page_icon="🧠", layout="wide")
st.title("🧠 LexisNexis Prompt Composer (no APIs)")
st.caption("Generate high-quality, localized email prompts you can paste into any AI (ChatGPT, Copilot, Gemini). No external APIs.")

# Top controls
col_lang, col_out = st.columns([1, 1])
with col_lang:
    lang_code = st.selectbox(
        "Target language",
        options=list(SCAFFOLDS.keys()),
        format_func=lambda k: SCAFFOLDS[k]["name"],
        index=0,
    )
with col_out:
    output_format = st.selectbox("Output target", OUTPUTS, index=0)

# -----------------------------------------------------------------------------
# Sidebar: client profile (robust to missing context keys)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("Client identity")
    client_name = st.text_input("Client name")
    client_type = st.selectbox("Client type", CLIENT_TYPES, index=0)
    region = st.selectbox("Region / Country", REGIONS, index=0)
    practice_areas = st.multiselect("Industry / practice area(s)", PRACTICES)

    st.header("CS / Sales context")
    account_owner = st.text_input("Account owner / RM name")
    relationship_stage = st.selectbox("Relationship stage", STAGES, index=min(1, len(STAGES)-1))
    products_used = st.multiselect("Primary LexisNexis products used", PRODUCTS)

    st.header("Metrics (optional)")
    usage_metrics = st.text_area("Usage metrics (logins, searches, features, report)")
    time_saved = st.text_input("Time saved / efficiency data (e.g., 'avg. 4 hours/week')")
    nps_info = st.text_area("NPS score / feedback theme (paste)")

    st.header("Communication settings")
    tone = st.selectbox("Tone", TONES, index=0)
    length = st.selectbox("Length preference", LENGTHS, index=1)
    include_highlights = st.checkbox("Auto-include product highlights (region-aware)", value=True)

    st.markdown("---")
    st.subheader("Presets")
    if export_preset_bytes:
        preset_bytes = export_preset_bytes(
            client_name=client_name,
            client_type=client_type,
            products_used=products_used,
            primary_role="",
            audience_role="",
            key_metrics=[],
        )
        st.download_button("💾 Export client preset (.json)", preset_bytes, file_name="client_preset.json", mime="application/json")
    uploaded = st.file_uploader("📂 Import client preset (.json)", type="json")
    if uploaded and load_preset_into_state:
        try:
            import json, io
            data = json.load(uploaded)
            load_preset_into_state(data)
            st.success("✅ Preset loaded. Update fields as needed.")
        except Exception as e:
            st.warning(f"Could not load preset: {e}")

# -----------------------------------------------------------------------------
# Main: function selection
# -----------------------------------------------------------------------------
left, right = st.columns([2, 3])

with left:
    recipe = st.selectbox(
        "Function / Use-case",
        list(PROMPT_RECIPES.keys()),
        index=0,
    )

with right:
    st.subheader("Few-shot examples (optional)")
    ex_col1, ex_col2 = st.columns(2)
    with ex_col1:
        ex_input = st.text_area("Example input", height=80, placeholder="Short example input")
    with ex_col2:
        ex_output = st.text_area("Example output", height=80, placeholder="Desired example output")

# -----------------------------------------------------------------------------
# Guided forms: options tailored by recipe
# -----------------------------------------------------------------------------
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
        proposed_products = st.multiselect("Proposed LexisNexis products", PRODUCTS)
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
    with st.expander("NPS options (auto-variants)", expanded=True):
        nps_previous_rating = st.selectbox("Previous NPS", ["Promoter (9–10)", "Passive (7–8)", "Detractor (0–6)"], index=1)
        nps_feedback_theme = st.text_input("Feedback theme (summary)")
        nps_survey_link = st.text_input("Survey link / CTA")
        guided.update({
            "nps_previous_rating": nps_previous_rating,
            "nps_feedback_theme": nps_feedback_theme,
            "nps_survey_link": nps_survey_link,
        })

elif recipe == "NPS Follow-up":
    with st.expander("NPS follow-up options", expanded=True):
        prev_nps = st.selectbox("Previous NPS", ["Promoter (9–10)", "Passive (7–8)", "Detractor (0–6)"], index=0)
        comment_type = st.selectbox("Comment type", ["Feature request", "Bug/issue", "General praise/concern"], index=0)
        verbatim = st.text_area("Paste the client’s verbatim comment from the survey", placeholder='e.g., “Generally good platform. It would be helpful to search reported cases only.”')
        helper_pointer = st.text_input("Add a helpful pointer (optional)", placeholder='e.g., "PG: Crypto coverage pointer"')
        internal_note = st.text_input("Internal note for our records, summarized to the client as appropriate", placeholder='e.g., "Raised with Content Ops; investigating TOC rendering"')
        guided.update({
            "nps_previous_rating": prev_nps,
            "nps_comment_type": comment_type,
            "nps_verbatim": verbatim,
            "nps_helper_pointer": helper_pointer,
            "nps_internal_note": internal_note,
        })

# -----------------------------------------------------------------------------
# Quality checklist
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("### ✅ Quality Checklist")
for item in [
    "No confidential client data present",
    "Claims are accurate/verifiable (no legal advice)",
    "Outcome/ROI linked to metrics",
    "Clear CTA / next steps included",
]:
    st.checkbox(item)

# -----------------------------------------------------------------------------
# Generate
# -----------------------------------------------------------------------------
if st.button("✨ Generate Prompt"):
    ctx = dict(
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
        ex_input=ex_input or "",
        ex_output=ex_output or "",
    )
    ctx.update(guided)

    final_prompt = fill_recipe(recipe, lang_code, ctx)
    shaped = shape_output(final_prompt, output_format, client_name, recipe)

    st.subheader("📝 Copy-ready Prompt")
    st.code(shaped, language="markdown")

    fname = f"ln_prompt_{recipe.replace('/','_')}_{lang_code}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.txt"
    st.download_button(
        "📥 Download (.txt)",
        shaped.replace("{today}", str(date.today())),
        file_name=fname,
        mime="text/plain"
    )

st.caption("Tip: set Tone to ‘auto’ to localize by Region + Stage (e.g., Japan=polite; Complaint=apologetic).")
