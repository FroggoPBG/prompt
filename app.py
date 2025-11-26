# app.py
from __future__ import annotations

from datetime import datetime, date

import streamlit as st

from components.recipes import (
    SCAFFOLDS,
    LN_CONTEXT,
    PROMPT_RECIPES,
    fill_recipe,
    shape_output,
)
from components.presets import export_preset_bytes, load_preset_into_state

# -------------------- Page --------------------
st.set_page_config(
    page_title="LexisNexis Prompt Composer (no APIs)",
    page_icon="🧠",
    layout="wide",
)
st.title("🧠 LexisNexis Prompt Composer (no APIs)")
st.caption(
    "Generate high-quality, localized email prompts you can paste into any AI "
    "(ChatGPT, Copilot, Gemini). No external APIs."
)

# -------------------- Language & output --------------------
col_lang, col_out = st.columns([1, 1])
with col_lang:
    lang_code = st.selectbox(
        "Target language",
        options=list(SCAFFOLDS.keys()),
        format_func=lambda k: SCAFFOLDS[k]["name"],
        index=0,
        key="lang_code",
    )
with col_out:
    output_format = st.selectbox(
        "Output target",
        LN_CONTEXT["outputs"],
        index=0,
        key="output_format",
    )

# -------------------- Sidebar: global schema --------------------
with st.sidebar:
    st.header("Client identity")
    client_name = st.text_input("Client name", key="client_name")
    client_type = st.selectbox(
        "Client type",
        LN_CONTEXT["client_types"],
        index=0,
        key="client_type",
    )
    region = st.selectbox(
        "Region / Country",
        LN_CONTEXT["regions"],
        index=0,
        key="region",
    )
    practice_areas = st.multiselect(
        "Industry / practice area(s)",
        LN_CONTEXT["practice_areas"],
        key="practice_areas",
    )

    st.header("CS / Sales context")
    account_owner = st.text_input("Account owner / RM name", key="account_owner")
    relationship_stage = st.selectbox(
        "Relationship stage",
        LN_CONTEXT["stages"],
        index=1,
        key="relationship_stage",
    )
    products_used = st.multiselect(
        "Primary LexisNexis products used",
        LN_CONTEXT["products"],
        key="products_used",
    )

    primary_role = st.text_input(
        "Primary role / audience (optional)",
        key="primary_role",
        help="e.g., litigation partners, in-house counsel, associates",
    )
    primary_use_case = st.text_input(
        "Primary use case (optional)",
        key="primary_use_case",
        help="e.g., case research, regulatory monitoring, drafting",
    )

    st.header("Metrics (optional)")
    usage_metrics = st.text_area(
        "Usage metrics (logins, searches, features, report)",
        key="usage_metrics",
    )
    time_saved = st.text_input(
        "Time saved / efficiency data (e.g., 'avg. 4 hours/week')",
        key="time_saved",
    )
    nps_info = st.text_area(
        "NPS score / feedback theme (paste)",
        key="nps_info",
    )

    key_metrics = []
    if usage_metrics:
        key_metrics.append("Usage metrics provided")
    if time_saved:
        key_metrics.append("Time-saved evidence provided")
    if nps_info:
        key_metrics.append("NPS feedback pasted")

    st.header("Communication settings")
    tone = st.selectbox("Tone", LN_CONTEXT["tones"], index=0, key="tone")
    length = st.selectbox("Length preference", LN_CONTEXT["lengths"], index=2, key="length")
    include_highlights = st.checkbox(
        "Auto-include product highlights (region-aware)",
        value=True,
        key="include_highlights",
    )

    st.markdown("---")
    st.subheader("Presets")

    preset_bytes = export_preset_bytes(
        client_name=client_name,
        client_type=client_type,
        products_used=products_used,
        account_owner=account_owner,
        practice_areas=practice_areas,
        region=region,
        primary_role=primary_role,
        primary_use_case=primary_use_case,
        key_metrics=key_metrics,
    )

    st.download_button(
        "💾 Export client preset (.json)",
        preset_bytes,
        file_name="client_preset.json",
        mime="application/json",
    )

    uploaded = st.file_uploader("📂 Import client preset (.json)", type="json")
    if uploaded:
        load_preset_into_state(uploaded)

# -------------------- Main: function selection --------------------
left, right = st.columns([2, 3])

with left:
    recipe = st.selectbox(
        "Function / Use-case",
        list(PROMPT_RECIPES.keys()),
        index=0,
        key="recipe",
    )

with right:
    st.subheader("Few-shot examples (optional)")
    ex_col1, ex_col2 = st.columns(2)
    with ex_col1:
        ex_input = st.text_area(
            "Example input",
            height=80,
            placeholder="Short example input",
            key="ex_input",
        )
    with ex_col2:
        ex_output = st.text_area(
            "Example output",
            height=80,
            placeholder="Desired example output",
            key="ex_output",
        )

# -------------------- Guided forms by function --------------------
st.markdown("---")
st.markdown("### 🧩 Guided options")

guided: dict = {}

if recipe == "Renewal Email":
    with st.expander("Renewal options", expanded=True):
        renewal_scenario = st.selectbox(
            "Scenario focus",
            [
                "Healthy usage, value reinforcement",
                "Low usage & pricing concerns",
            ],
            index=0,
        )
        contract_details = st.text_input(
            "Contract details (renewal date / price change)",
            key="renewal_contract_details",
        )
        meeting_options = st.text_input(
            "2–3 date/time options (comma-separated)",
            placeholder="e.g., Tue 10am, Wed 2pm, Thu 4pm",
            key="renewal_meeting_options",
        )
        guided.update(
            {
                "renewal_scenario": "low_usage_pricing"
                if "Low usage" in renewal_scenario
                else "value",
                "contract_details": contract_details,
                "meeting_options": meeting_options,
            }
        )

elif recipe == "QBR Brief":
    with st.expander("QBR options", expanded=True):
        qbr_window = st.selectbox(
            "Review period",
            ["Last Month", "Last Quarter", "H1", "FY"],
            index=1,
        )
        qbr_include_benchmarks = st.checkbox(
            "Include industry benchmarks", value=False
        )
        qbr_sections = st.multiselect(
            "Sections to emphasize",
            [
                "Usage & Engagement",
                "Business Impact",
                "Wins",
                "Underused Features",
                "Recommendations",
            ],
            default=["Usage & Engagement", "Business Impact", "Recommendations"],
        )
        guided.update(
            {
                "qbr_window": qbr_window,
                "qbr_include_benchmarks": qbr_include_benchmarks,
                "qbr_sections": qbr_sections,
            }
        )

elif recipe == "Client Follow-up":
    with st.expander("Follow-up options", expanded=True):
        last_meeting_date = st.text_input(
            "Date of last meeting", key="fu_last_meeting_date"
        )
        meeting_topics = st.text_input(
            "Topics covered", key="fu_meeting_topics"
        )
        guided.update(
            {
                "last_meeting_date": last_meeting_date,
                "meeting_topics": meeting_topics,
            }
        )

elif recipe == "Proposal / RFP Response":
    with st.expander("RFP options", expanded=True):
        rfp_sector = st.text_input("Client sector", key="rfp_sector")
        rfp_scope = st.text_area(
            "RFP scope / key requirements", key="rfp_scope"
        )
        rfp_differentiators = st.text_area(
            "Differentiators to emphasize", key="rfp_diff"
        )
        rfp_deadline = st.text_input("Key deadline", key="rfp_deadline")
        guided.update(
            {
                "rfp_sector": rfp_sector,
                "rfp_scope": rfp_scope,
                "rfp_differentiators": rfp_differentiators,
                "rfp_deadline": rfp_deadline,
            }
        )

elif recipe == "Upsell / Cross-sell Outreach":
    with st.expander("Upsell options", expanded=True):
        pains = st.text_area("Client pain points", key="upsell_pains")
        proposed_products = st.multiselect(
            "Proposed LexisNexis products",
            LN_CONTEXT["products"],
            key="upsell_products",
        )
        case_studies = st.text_area(
            "Relevant case studies", key="upsell_case_studies"
        )
        guided.update(
            {
                "pains": pains,
                "proposed_products": proposed_products,
                "case_studies": case_studies,
            }
        )

elif recipe == "Client Risk Alert":
    with st.expander("Risk options", expanded=True):
        risk_trigger = st.selectbox(
            "Risk trigger",
            [
                "Declining usage",
                "Delayed renewal",
                "Negative feedback",
                "Champion turnover",
                "Other",
            ],
            index=0,
        )
        risk_severity = st.select_slider(
            "Severity", options=[1, 2, 3, 4, 5], value=3
        )
        risk_mitigations = st.text_area(
            "Mitigation options (enablement plan, cadence, etc.)",
            key="risk_mitigations",
        )
        guided.update(
            {
                "risk_trigger": risk_trigger,
                "risk_severity": risk_severity,
                "risk_mitigations": risk_mitigations,
            }
        )

elif recipe == "Client Snapshot & Risk Signals":
    with st.expander("Snapshot options", expanded=True):
        prepared_by = st.selectbox(
            "Prepared by",
            ["Sales", "Pre-Sales", "Customer Success"],
            index=0,
        )
        last_engagement_date = st.text_input(
            "Last engagement date", key="snap_last_eng"
        )
        risk_level = st.select_slider(
            "Risk level", options=["Low", "Medium", "High"], value="Medium"
        )
        guided.update(
            {
                "prepared_by": prepared_by,
                "last_engagement_date": last_engagement_date,
                "risk_level": risk_level,
            }
        )

elif recipe == "Objection Coach":
    with st.expander("Objection options", expanded=True):
        objection_type = st.selectbox(
            "Objection type",
            ["Price", "Usability", "Prefer Competitor"],
            index=0,
        )
        objection_severity = st.select_slider(
            "Severity", options=[1, 2, 3, 4, 5], value=3
        )
        competitor_name = st.text_input(
            "Competitor (optional)", key="obj_competitor"
        )
        supporting_data = st.multiselect(
            "Supporting data available",
            [
                "Usage metrics",
                "ROI",
                "NPS quotes",
                "Case studies",
                "Benchmarks",
            ],
            key="obj_support",
        )
        guided.update(
            {
                "objection_type": objection_type,
                "objection_severity": objection_severity,
                "competitor_name": competitor_name,
                "supporting_data": supporting_data,
            }
        )

elif recipe == "NPS Engagement":
    with st.expander("NPS options (auto-variants)", expanded=True):
        nps_previous_rating = st.selectbox(
            "Previous NPS",
            [
                "Promoter (9–10)",
                "Passive (7–8)",
                "Detractor (0–6)",
            ],
            index=1,
        )
        nps_feedback_theme = st.text_input(
            "Feedback theme (summary)", key="nps_theme"
        )
        nps_survey_link = st.text_input(
            "Survey link / CTA", key="nps_link"
        )
        guided.update(
            {
                "nps_previous_rating": nps_previous_rating,
                "nps_feedback_theme": nps_feedback_theme,
                "nps_survey_link": nps_survey_link,
            }
        )

elif recipe == "NPS Follow-up":
    with st.expander("NPS follow-up options", expanded=True):
        nps_previous_rating = st.selectbox(
            "Previous NPS",
            [
                "Promoter (9–10)",
                "Passive (7–8)",
                "Detractor (0–6)",
            ],
            index=0,
        )
        comment_type = st.selectbox(
            "Comment type",
            ["Feature request", "Bug / issue", "Pricing concern", "Usability", "Other"],
            index=0,
        )
        verbatim_comment = st.text_area(
            "Paste the client's verbatim comment from the survey",
            key="nps_follow_comment",
        )
        helpful_pointer = st.text_input(
            "Add a helpful pointer (optional)",
            placeholder="e.g., PG: Crypto coverage pointer",
            key="nps_help_pointer",
        )
        escalation_note = st.text_input(
            "Internal note (for our records, summarised to client as appropriate)",
            key="nps_internal_note",
        )
        guided.update(
            {
                "nps_previous_rating": nps_previous_rating,
                "nps_comment_type": comment_type,
                "nps_followup_comment": verbatim_comment,
                "nps_helpful_pointer": helpful_pointer,
                "nps_internal": escalation_note,
            }
        )

# -------------------- Quality checklist --------------------
st.markdown("---")
st.markdown("### ✅ Quality Checklist")
for item in [
    "No confidential client data present",
    "Claims are accurate/verifiable (no legal advice)",
    "Outcome/ROI linked to metrics",
    "Clear CTA / next steps included",
]:
    st.checkbox(item, value=True)

# -------------------- Generate --------------------
if st.button("✨ Generate Prompt"):
    # Enhanced: Basic validation before generation
    if not client_name:
        st.warning("Please enter a client name to generate a prompt.")
    elif not recipe:
        st.warning("Please select a function/use-case.")
    else:
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
            primary_role=primary_role,
            primary_use_case=primary_use_case,
            key_metrics=key_metrics,
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

        fname = (
            f"ln_prompt_{recipe.replace('/','_').replace(' ','_')}_"
            f"{lang_code}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.txt"
        )
        st.download_button(
            "📥 Download (.txt)",
            shaped.replace("{today}", str(date.today())),
            file_name=fname,
            mime="text/plain",
        )

        # Enhanced: Quick feedback loop (simple thumbs up/down)
        st.markdown("---")
        st.subheader("Rate this prompt")
        col_thumb1, col_thumb2 = st.columns(2)
        with col_thumb1:
            if st.button("👍 Good"):
                st.success("Thanks for the feedback! Marked as good.")
                # Here you could log to session_state or a file, but keeping no API/no downloads
        with col_thumb2:
            if st.button("👎 Needs improvement"):
                st.warning("Thanks! What could be better? (Note for future iterations)")
                # Optional: Add a text area for comments, but keep simple

st.caption(
    "Tip: You can use different functions (Renewal, QBR, NPS Follow-up, etc.) "
    "and compare AI outputs generated from these prompts vs. generic prompts "
    "to demonstrate quality and ROI."
)

# Enhanced: Simple analytics dashboard (using session_state for persistence, no external storage)
if "usage_stats" not in st.session_state:
    st.session_state.usage_stats = {
        "generations": 0,
        "recipes_used": {},
    }

if st.button("View Usage Stats"):
    st.session_state.usage_stats["generations"] += 1  # Increment on generate, but for demo
    if recipe in st.session_state.usage_stats["recipes_used"]:
        st.session_state.usage_stats["recipes_used"][recipe] += 1
    else:
        st.session_state.usage_stats["recipes_used"][recipe] = 1

    st.markdown("### 📊 Usage Analytics")
    st.write(f"Total prompt generations: {st.session_state.usage_stats['generations']}")
    st.bar_chart(st.session_state.usage_stats["recipes_used"])

# Enhanced: Template library (static dropdown for quick presets)
st.sidebar.markdown("---")
st.sidebar.subheader("Quick Templates")
template = st.sidebar.selectbox(
    "Load a template",
    ["None", "Standard Renewal", "Quick NPS Follow-up"],
)
if template == "Standard Renewal":
    st.session_state.client_name = "Sample Client"
    st.session_state.recipe = "Renewal Email"
    st.success("Template loaded: Standard Renewal")
elif template == "Quick NPS Follow-up":
    st.session_state.recipe = "NPS Follow-up"
    st.success("Template loaded: Quick NPS Follow-up")

# Enhanced: Dark mode toggle (simple CSS injection)
theme = st.sidebar.selectbox("Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                background-color: #1E1E1E;
            }
            .stApp {
                background-color: #121212;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
