import json
from datetime import datetime, date

import streamlit as st

from components.recipes import (
    SCAFFOLDS,
    LN_CONTEXT,
    PRODUCT_BLURBS,
    PROMPT_RECIPES,
    fill_recipe,
    shape_output,
)
from components.presets import export_preset_bytes, load_preset_into_state


# -------------------- Page --------------------
st.set_page_config(page_title="LexisNexis Prompt Composer (no APIs)", page_icon="🧠", layout="wide")
st.title("🧠 LexisNexis Prompt Composer (no APIs)")
st.caption("Generate high-quality, localized **email prompts** you can paste into any AI (ChatGPT, Copilot, Gemini). No external APIs.")

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
    client_name = st.text_input("Client name")
    client_type = st.selectbox("Client type", LN_CONTEXT["client_types"], index=1)
    region = st.selectbox("Region / Country", LN_CONTEXT["regions"], index=0)
    practice_areas = st.multiselect("Industry / practice area(s)", LN_CONTEXT["practice_areas"])

    st.header("CS context")
    account_owner = st.text_input("Account owner / RM name")
    relationship_stage = st.selectbox("Relationship stage", LN_CONTEXT["stages"], index=2)
    products_used = st.multiselect("Primary LexisNexis products used", LN_CONTEXT["products"])

    st.header("Metrics (optional)")
    usage_metrics = st.text_area("Usage metrics (logins, searches, features, report)")
    time_saved = st.text_input("Time saved / efficiency data (e.g., 'avg. 4 hours/week')")
    nps_info = st.text_area("NPS score / feedback theme (paste)")

    st.header("Communication settings")
    tone = st.selectbox("Tone", LN_CONTEXT["tones"], index=0)
    length = st.selectbox("Length preference", LN_CONTEXT["lengths"], index=1)

    st.markdown("---")
    st.subheader("Product facts (optional)")
    chosen_blurbs = st.multiselect(
        "Add product blurbs",
        options=list(PRODUCT_BLURBS.keys()),
        default=[]
    )
    product_facts_free = st.text_area("Additional product facts or notes (optional)")

    # Combine product facts now so it's available for any recipe
    combined_product_facts = ""
    if chosen_blurbs:
        combined_product_facts += "\n".join([f"- {k}: {PRODUCT_BLURBS[k]}" for k in chosen_blurbs])
    if product_facts_free.strip():
        combined_product_facts += ("\n" if combined_product_facts else "") + product_facts_free.strip()

    st.markdown("---")
    st.subheader("Presets")
    # match your presets.py signature exactly
    preset_bytes = export_preset_bytes(
        client_name=client_name,
        client_type=client_type,
        products_used=products_used,
        primary_role=account_owner,         # mapped to 'primary_role'
        audience_role=relationship_stage,   # mapped to 'audience_role'
        key_metrics=[],                     # optional list; keep empty if not used
    )
    st.download_button(
        "💾 Export client preset (.json)",
        preset_bytes,
        file_name="client_preset.json",
        mime="application/json"
    )
    uploaded = st.file_uploader("📂 Import client preset (.json)", type="json")
    if uploaded:
        try:
            data = json.loads(uploaded.getvalue().decode("utf-8"))
            load_preset_into_state(data)
            st.success("✅ Preset loaded. Update fields as needed.")
        except Exception as e:
            st.error(f"Could not load preset: {e}")

# -------------------- Main: function selection --------------------
left, right = st.columns([2, 3])

with left:
    recipe = st.selectbox("Function / Use-case", PROMPT_RECIPES, index=0)

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
        renewal_angle = st.selectbox(
            "Angle",
            ["Pricing concern + low usage", "Pricing concern but healthy usage"],
            index=0
        )
        renewal_date = st.text_input("Renewal date (e.g., 2026-03-31)")
        usage_summary = st.text_area(
            "Usage summary (free-text)",
            placeholder="e.g., only 2–3 logins in past 3 months; sporadic usage; declining activity"
        )
        modules_used = st.text_input(
            "Most-used modules/databases (if healthy-usage)",
            placeholder="e.g., Financial Services Practical Guidance; Case Law; Legislation"
        )
        engagement_indicators = st.text_input(
            "Engagement indicators",
            placeholder="e.g., downloads, saved searches, alerts"
        )
        guided.update({
            "renewal_angle": renewal_angle,
            "renewal_date": renewal_date,
            "usage_summary": usage_summary,
            "modules_used": modules_used,
            "engagement_indicators": engagement_indicators,
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
        nps_previous_rating = st.selectbox("Previous NPS", ["Promoter (9–10)", "Passive (7–8)", "Detractor (0–6)"], index=0)
        npsf_comment_type = st.selectbox(
            "Comment type",
            ["Feature request", "How-to / navigation", "Bug / issue", "General feedback / praise", "Pricing"],
            index=0
        )
        npsf_verbatim = st.text_area(
            "Paste the client's verbatim comment from the survey",
            placeholder='e.g., “Generally good platform. It would be helpful to search reported cases only.”'
        )
        npsf_pointer = st.text_input(
            "Add a helpful pointer (optional)",
            placeholder='e.g., “PG: Crypto coverage pointer” or “To filter to reported cases… > Publication > Hong Kong Cases”'
        )
        npsf_escalated_note = st.text_area(
            "We escalated this internally / will update them (optional)",
            placeholder="e.g., Logged with Content Ops; investigating TOC rendering for commentaries."
        )
        guided.update({
            "nps_previous_rating": nps_previous_rating,
            "npsf_comment_type": npsf_comment_type,
            "npsf_verbatim": npsf_verbatim,
            "npsf_pointer": npsf_pointer,
            "npsf_escalated_note": npsf_escalated_note,
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
        output_target=output_format,

        # Few-shot (optional)
        ex_input=ex_input or "",
        ex_output=ex_output or "",

        # Product facts for email body (optional)
        product_facts=combined_product_facts.strip(),
    )

    # Guided, function-specific
    ctx.update(guided)

    final_prompt = fill_recipe(recipe, lang_code, ctx)
    shaped = shape_output(final_prompt, output_format, client_name, recipe)

    st.subheader("📝 Copy-ready prompt for your AI tool")
    st.code(shaped, language="markdown")

    # download
    fname = f"ln_prompt_{recipe.replace('/','_')}_{lang_code}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.txt"
    st.download_button(
        "📥 Download (.txt)",
        shaped.replace("{today}", str(date.today())),
        file_name=fname,
        mime="text/plain"
    )

st.caption("Tip: set Tone to ‘auto’ to localize by Region + Stage (e.g., Japan = more formal; Detractor = sincere & apologetic).")
