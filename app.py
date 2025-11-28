# app.py
# Legal Tech Sales Prospecting Tool - OUS Framework
from __future__ import annotations

from datetime import datetime
import streamlit as st

from components.recipes import (
    PROMPT_RECIPES,
    fill_recipe,
    generate_full_workflow,
)
from components.presets import export_preset_bytes, load_preset_into_state

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Legal Tech Sales Prospecting - OUS Framework",
    page_icon="⚖️",
    layout="wide",
)

# -------------------- Header --------------------
st.title("⚖️ Legal Tech Sales Prospecting Tool")
st.caption(
    "3-Phase 'Legal Scout & Empathizer' Strategy for Hong Kong Legal Market | "
    "Generate research prompts using the OUS Framework (Outcome → Understanding → Standard)"
)

# -------------------- Sidebar: Prospect Input --------------------
with st.sidebar:
    st.header("🎯 Prospect Information")
    
    company_name = st.text_input(
        "Company/Law Firm Name*",
        key="company_name",
        placeholder="e.g., Liu Chong Hing Investment, Mayer Brown JSM",
        help="Enter the full legal name of the prospect"
    )
    
    company_url = st.text_input(
        "Company Website or Source Link",
        key="company_url",
        placeholder="https://www.example.com or LinkedIn URL",
        help="Paste company website, LinkedIn, or any relevant URL for research"
    )
    
    st.markdown("---")
    st.subheader("🔍 Target Context")
    
    practice_area = st.selectbox(
        "Primary Practice Area / Legal Focus",
        [
            "General/Multiple",
            "M&A and Corporate Finance",
            "Banking & Finance",
            "Litigation & Dispute Resolution",
            "Intellectual Property",
            "Employment Law",
            "Regulatory & Compliance",
            "Real Estate & Property",
            "Tax & Revenue",
        ],
        key="practice_area",
        help="What legal practice area is under most pressure for this prospect?"
    )
    
    buyer_persona = st.selectbox(
        "Buyer Persona",
        [
            "General Counsel (In-House)",
            "Managing Partner (Law Firm)",
            "Senior Partner (Law Firm)",
            "Legal Operations Director",
            "Compliance Head",
            "Barrister (Chambers)",
            "Corporate Secretary",
        ],
        key="buyer_persona",
        help="Who is the primary decision-maker you're targeting?"
    )
    
    industry = st.text_input(
        "Industry Vertical (Optional)",
        key="industry",
        placeholder="e.g., Financial Services, Real Estate, Technology",
        help="If in-house counsel, what industry is the company in?"
    )
    
    notes = st.text_area(
        "Additional Context/Notes (Optional)",
        key="notes",
        placeholder="Any specific triggers, recent news, or context...",
        height=100,
    )
    
    st.markdown("---")
    st.subheader("💾 Presets")
    
    # Export preset
    preset_bytes = export_preset_bytes(
        company_name=company_name,
        company_url=company_url,
        practice_area=practice_area,
        buyer_persona=buyer_persona,
        industry=industry,
        notes=notes,
    )
    
    st.download_button(
        "💾 Save Prospect as Preset",
        preset_bytes,
        file_name=f"prospect_{company_name.replace(' ', '_')}.json",
        mime="application/json",
        help="Save this prospect's info for future use"
    )
    
    # Import preset
    uploaded = st.file_uploader(
        "📂 Load Saved Prospect Preset",
        type="json",
        help="Upload a previously saved prospect preset"
    )
    if uploaded:
        load_preset_into_state(uploaded)
        st.rerun()

# -------------------- Main Content --------------------
st.markdown("---")

# Workflow Selection
workflow_mode = st.radio(
    "Choose Workflow",
    [
        "🚀 Full 4-Prompt Workflow (Recommended)",
        "🔧 Individual Prompt Builder",
    ],
    horizontal=True,
)

if workflow_mode == "🚀 Full 4-Prompt Workflow (Recommended)":
    st.markdown("### 🎯 Complete Sales Prospecting Sequence")
    st.info(
        "**This generates all 4 prompts in the correct order:**\n\n"
        "1. **Phase 1**: Discovery & Compliance Research\n"
        "2. **Phase 2**: General Counsel Psychological Profiling\n"
        "3. **Phase 3**: Credibility-Based Email Drafting\n"
        "4. **OUS Framework**: Outcome → Understanding → Standard Analysis\n\n"
        "Use these prompts sequentially in ChatGPT/Claude to build a complete prospect dossier."
    )
    
    if st.button("✨ Generate Full Workflow", type="primary", use_container_width=True):
        if not company_name:
            st.error("❌ Please enter a company name to generate prompts.")
        else:
            with st.spinner("Generating 4-phase workflow..."):
                prompts = generate_full_workflow(
                    company_name=company_name,
                    company_url=company_url,
                    practice_area=practice_area,
                    buyer_persona=buyer_persona,
                )
            
            # Display all prompts
            st.success("✅ Workflow generated! Copy each prompt below and paste into your AI tool sequentially.")
            
            # Phase 1
            with st.expander("📋 PROMPT 1: Discovery & Compliance Research", expanded=True):
                st.markdown(
                    "**Usage:** Paste this into ChatGPT/Claude. "
                    "The AI will research the company and identify legal triggers."
                )
                st.code(prompts["phase1"], language="markdown")
                st.download_button(
                    "📥 Download Prompt 1",
                    prompts["phase1"],
                    file_name=f"1_discovery_{company_name.replace(' ', '_')}.txt",
                    mime="text/plain",
                )
            
            # Phase 2
            with st.expander("📋 PROMPT 2: General Counsel Psychological Profiling"):
                st.markdown(
                    "**Usage:** After completing Prompt 1, paste this prompt PLUS the output from Prompt 1. "
                    "The AI will analyze the buyer's emotional state and pain points."
                )
                st.code(prompts["phase2"], language="markdown")
                st.download_button(
                    "📥 Download Prompt 2",
                    prompts["phase2"],
                    file_name=f"2_profiling_{company_name.replace(' ', '_')}.txt",
                    mime="text/plain",
                )
            
            # Phase 3
            with st.expander("📋 PROMPT 3: Credibility-Based Email Drafting"):
                st.markdown(
                    "**Usage:** After completing Prompts 1 & 2, paste this prompt PLUS the outputs. "
                    "The AI will draft your cold outreach email."
                )
                st.code(prompts["phase3"], language="markdown")
                st.download_button(
                    "📥 Download Prompt 3",
                    prompts["phase3"],
                    file_name=f"3_email_{company_name.replace(' ', '_')}.txt",
                    mime="text/plain",
                )
            
            # OUS Framework
            with st.expander("📋 PROMPT 4: OUS Framework Analysis"):
                st.markdown(
                    "**Usage:** Use this prompt to apply the Outcome → Understanding → Standard lens "
                    "to all your findings. This helps you refine your positioning."
                )
                st.code(prompts["ous"], language="markdown")
                st.download_button(
                    "📥 Download Prompt 4 (OUS)",
                    prompts["ous"],
                    file_name=f"4_ous_{company_name.replace(' ', '_')}.txt",
                    mime="text/plain",
                )

else:  # Individual Prompt Builder
    st.markdown("### 🔧 Build Individual Prompts")
    
    recipe_choice = st.selectbox(
        "Select Prompt Type",
        list(PROMPT_RECIPES.keys()),
        help="Choose which specific prompt you want to generate"
    )
    
    if st.button("✨ Generate Prompt", type="primary", use_container_width=True):
        if not company_name:
            st.error("❌ Please enter a company name.")
        else:
            with st.spinner("Generating prompt..."):
                prompt = fill_recipe(
                    recipe_name=recipe_choice,
                    company_name=company_name,
                    company_url=company_url,
                    practice_area=practice_area,
                    buyer_persona=buyer_persona,
                )
            
            st.success("✅ Prompt generated!")
            st.code(prompt, language="markdown")
            
            filename = f"{recipe_choice.replace(' ', '_').replace(':', '')}_{company_name.replace(' ', '_')}.txt"
            st.download_button(
                "📥 Download Prompt",
                prompt,
                file_name=filename,
                mime="text/plain",
            )

# -------------------- Usage Guide --------------------
st.markdown("---")
with st.expander("📖 How to Use This Tool"):
    st.markdown("""
    ### 🎯 Quick Start Guide
    
    **Step 1: Enter Prospect Info (Sidebar)**
    - Enter company/law firm name
    - Paste their website or LinkedIn URL
    - Select practice area and buyer persona
    
    **Step 2: Generate Prompts**
    - Use **Full Workflow** mode for complete prospect research
    - OR use **Individual Prompt Builder** for specific needs
    
    **Step 3: Use Prompts in AI Tool**
    - Copy each prompt in order
    - Paste into ChatGPT, Claude, or your enterprise AI
    - Feed the output of Prompt 1 into Prompt 2, etc.
    
    **Step 4: Craft Your Outreach**
    - Prompt 3 will generate your cold email
    - Use Prompt 4 (OUS) to refine positioning
    
    ---
    
    ### 🧠 OUS Framework Explained
    
    **O - Outcome:** What strategic business goal does the buyer need to achieve?
    - Example: "Reduce outside counsel spend by 25%"
    
    **U - Understanding Pain:** What specific operational pain is blocking that outcome?
    - Example: "Junior associates spend 60% of time on manual research"
    
    **S - Standard:** What criteria will they use to evaluate solutions?
    - Example: "Must integrate with iManage, cover HK + PRC law, deploy in <2 weeks"
    
    ---
    
    ### ⚡ Pro Tips
    
    - **For best results:** Always run prompts sequentially (1 → 2 → 3 → 4)
    - **Time saver:** Save prospects as presets to avoid re-entering info
    - **Quality check:** The email from Prompt 3 should sound like it's from a legal advisor, not a salesperson
    - **Red flag:** If the AI hallucinates facts, regenerate with stricter anti-hallucination reminder
    """)

# -------------------- Footer --------------------
st.markdown("---")
st.caption(
    "**Legal Tech Sales Prospecting Tool** | OUS Framework | "
    "Designed for Hong Kong legal market prospecting | "
    f"Session: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
)
