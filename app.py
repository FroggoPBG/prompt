import json
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
st.set_page_config(page_title="LexisNexis Prompt Composer (no APIs)", page_icon="🧠", layout="wide")
st.title("🧠 LexisNexis Prompt Composer (no APIs)")
st.caption("Generate high-quality, localized email prompts you can paste into any AI (ChatGPT, Copilot, Gemini). No external APIs.")

# -------------------- Language & output --------------------
col_lang, col_out = st.columns([1, 1])
with col_lang:
    lang_code = st.selectbox(
        "Target language",
        options=list(SCAFFOLDS.keys()),
        format_func=lambda k: SCAFFOLDS[k]["name"],
        index=0,
    )
with col_out:
    output_format = st.selectbox("Output target", LN_CONTEXT["outputs"], index=0)

# -------------------- Sidebar: global schema --------------------
with st.sidebar:
    st.header("Client identity")
    client_name = st.text_input("Client name", key="client_name")
    client_type = st.selectbox("Client type", LN_CONTEXT["client_types"], index=0, key="client_type")
    region = st.selectbox("Region / Country", LN_CONTEXT["regions"], index=0, key="region")
    practice_areas = st.multiselect("Industry / practice area(s)", LN_CONTEXT["practice_areas"], key="practice_areas")

    st.header("CS / Sales context")
    account_owner = st.text_input("Account owner / RM name", key="account_owner")
    relationship_stage = st.selectbox("Relationship stage", LN_CONTEXT["stages"], index=3, key="relationship_stage")
    products_used = st.multiselect("Primary LexisNexis products used", LN_CONTEXT["products"], key="products_used")

    st.header("Metrics (optional)")
    usage_metrics = st.text_area("Usage metrics (logins, searches, features, report)", key="usage_metrics")
    time_saved = st.text_input("Time saved / efficiency data (e.g., 'avg. 4 hours/week')", key="time_saved")
    nps_info = st.text_area("NPS score / feedback theme (paste)", key="nps_info")

    st.header("Communication settings")
    tone = st.selectbox("Tone", LN_CONTEXT["tones"], index=1, key="tone")
    length = st.selectbox("Length preference", LN_CONTEXT["lengths"], index=1, key="length")

    st.markdown("---")
    st.subheader("Presets")

    # Pack extra defaults (renewal + NPS) into key_metrics dict so we don't need to change presets.py
    extra_defaults = {
        "renewal_defaults": {
            "renewal_date": st.session_state.get("renewal_date"),
            "usage_low_freq": st.session_state.get("usage_low_freq"),
            "usage_limited_modules": st.session_state.get("usage_limited_modules"),
            "usage_low_engagement": st.session_state.get("usage_low_engagement"),
            "usage_freq": st.session_state.get("usage_freq"),
            "usage_modules": st.session_state.get("usage_modules"),
            "usage_other": st.session_state.get("usage_other"),
        },
        "nps_defaults": {
            "nps_previous_rating": st.session_state.get("nps_previous_rating"),
            "nps_survey_link": st.session_state.get("nps_survey_link"),
            "nps_comment_type": st.session_state.get("nps_comment_type"),
            "nps_verbatim": st.session_state.get("nps_verbatim"),
            "nps_helpful_pointer": st.session_state.get("nps_helpful_pointer"),
            "nps_internal_note": st.session_state.get("nps_internal_note"),
        },

"preset_bytes" = export_preset_bytes(
    client_name=client_name,
    client_type=client_type,
    products_used=products_used,
    account_owner=account_owner,
    practice_areas=practice_areas,
    region=region,
    primary_role=primary_role,
    primary_use_case=primary_use_case,
    key_metrics=extra_defaults,
)


    st.download_button("💾 Export client preset (.json)", preset_bytes, file_name="client_preset.json", mime="application/json")

    uploaded = st.file_uploader("📂 Import client preset (.json)", type="json")
    if uploaded:
        try:
            data = json.load(uploaded)
            load_preset_into_state(data)
            # Unpack our extra defaults back into session state
            km = data.get("key_metrics") or {}
            for group in ("renewal_defaults", "nps_defaults"):
                for k, v in (km.get(group) or {}).items():
                    if v is not None:
                        st.session_state[k] = v
            st.success("✅ Preset loaded. Update fields as needed.")
        except Exception as e:
            st.error(f"Failed to read preset: {e}")

# -------------------- Main: function selection --------------------
left, right = st.columns([2, 3])

with left:
    recipe = st.selectbox(
        "Function / Use-case",
        list(PROMPT_RECIPES.keys()),
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

if recipe == "Renewal: Low Usage / Right-size":
    with st.expander("Renewal options — Low usage", expanded=True):
        st.session_state["renewal_date"] = st.text_input("Renewal date or timeframe", value=st.session_state.get("renewal_date", ""))
        st.session_state["usage_low_freq"] = st.text_input("Low frequency note", value=st.session_state.get("usage_low_freq", "e.g., only 2–3 logins in the past 3 months; sporadic usage; declining activity"))
        st.session_state["usage_limited_modules"] = st.text_input("Limited modules note", value=st.session_state.get("usage_limited_modules", "e.g., using basic features; not using premium modules"))
        st.session_state["usage_low_engagement"] = st.text_input("Low engagement note", value=st.session_state.get("usage_low_engagement", "e.g., minimal downloads; no saved searches or alerts"))
        guided.update({
            "renewal_date": st.session_state["renewal_date"],
            "usage_low_freq": st.session_state["usage_low_freq"],
            "usage_limited_modules": st.session_state["usage_limited_modules"],
            "usage_low_engagement": st.session_state["usage_low_engagement"],
        })

elif recipe == "Renewal: Value Evidence":
    with st.expander("Renewal options — Value evidence", expanded=True):
        st.session_state["renewal_date"] = st.text_input("Renewal date or timeframe", value=st.session_state.get("renewal_date", ""))
        st.session_state["usage_freq"] = st.text_input("Access frequency", value=st.session_state.get("usage_freq", "e.g., daily; 3x/week; sporadic"))
        st.session_state["usage_modules"] = st.text_input("Most-used modules/databases", value=st.session_state.get("usage_modules", "e.g., Financial Services PG, Case Law, Legislation"))
        st.session_state["usage_other"] = st.text_input("Other engagement indicators", value=st.session_state.get("usage_other", "e.g., downloads; saved searches; alerts"))
        guided.update({
            "renewal_date": st.session_state["renewal_date"],
            "usage_freq": st.session_state["usage_freq"],
            "usage_modules": st.session_state["usage_modules"],
            "usage_other": st.session_state["usage_other"],
        })

elif recipe == "NPS Engagement":
    with st.expander("NPS options (auto-variants)", expanded=True):
        st.session_state["nps_previous_rating"] = st.selectbox(
            "Previous NPS",
            ["Promoter (9–10)", "Passive (7–8)", "Detractor (0–6)"],
            index={"Promoter (9–10)":0, "Passive (7–8)":1, "Detractor (0–6)":2}.get(st.session_state.get("nps_previous_rating") or "Passive (7–8)", 1)
        )
        st.session_state["nps_survey_link"] = st.text_input("Survey link / CTA", value=st.session_state.get("nps_survey_link", ""))
        guided.update({
            "nps_previous_rating": st.session_state["nps_previous_rating"],
            "nps_survey_link": st.session_state["nps_survey_link"],
        })

elif recipe == "NPS Follow-up":
    with st.expander("NPS follow-up options", expanded=True):
        st.session_state["nps_previous_rating"] = st.selectbox(
            "Previous NPS",
            ["Promoter (9–10)", "Passive (7–8)", "Detractor (0–6)"],
            index={"Promoter (9–10)":0, "Passive (7–8)":1, "Detractor (0–6)":2}.get(st.session_state.get("nps_previous_rating") or "Passive (7–8)", 1)
        )
        st.session_state["nps_comment_type"] = st.selectbox(
            "Comment type",
            ["Feature request", "Usability", "Bug/issue", "General praise/concern"],
            index=0
        )
        st.session_state["nps_verbatim"] = st.text_area("Paste the client's verbatim comment from the survey", value=st.session_state.get("nps_verbatim", ""))
        st.session_state["nps_helpful_pointer"] = st.text_input("Add a helpful pointer (optional)", value=st.session_state.get("nps_helpful_pointer", ""))
        st.session_state["nps_internal_note"] = st.text_area("Internal note (for our records; summarized to the client as appropriate)", value=st.session_state.get("nps_internal_note", ""))
        guided.update({
            "nps_previous_rating": st.session_state["nps_previous_rating"],
            "nps_comment_type": st.session_state["nps_comment_type"],
            "nps_verbatim": st.session_state["nps_verbatim"],
            "nps_helpful_pointer": st.session_state["nps_helpful_pointer"],
            "nps_internal_note": st.session_state["nps_internal_note"],
        })

# -------------------- Quality checklist --------------------
st.markdown("---")
st.markdown("### ✅ Quality Checklist")
for item in [
    "No confidential client data present",
    "Claims are accurate/verifiable (no legal advice)",
    "Outcome/ROI linked to metrics where possible",
    "Clear CTA / next steps included",
]:
    st.checkbox(item, value=True)

# -------------------- Generate --------------------
if st.button("✨ Generate"):
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
        output_target=output_format,

        # Few-shot
        ex_input=ex_input or "",
        ex_output=ex_output or "",
    )

    # Guided, function-specific
    ctx.update(guided)

    final_prompt = fill_recipe(recipe, lang_code, ctx)
    shaped = shape_output(final_prompt, output_format, client_name, recipe)

    st.subheader("📝 Copy-ready output")
    st.code(shaped, language="markdown")

    # Filename: avoid datetime.utcnow deprecation warnings
    fname = f"ln_prompt_{recipe.replace('/','_')}_{lang_code}_{datetime.now().strftime('%Y%m%dT%H%M%S')}.txt"
    st.download_button(
        "📥 Download (.txt)",
        shaped.replace("{today}", str(date.today())),
        file_name=fname,
        mime="text/plain"
    )

st.caption("Tip: choose a recipe, fill the guided options, and paste the result into your AI tool to generate a polished client email.")
