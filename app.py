# app.py
# Legal Tech Sales Prospecting Tool - OUS Framework with Zinsser's Principles
from __future__ import annotations

from datetime import datetime
import streamlit as st

from components.recipes import (
    PROMPT_RECIPES,
    fill_recipe,
    generate_full_workflow,
)
from components.presets import export_preset_bytes, load_preset_into_state
from components.writing_checker import (
    check_plain_english,
    get_writing_score_label,
    get_writing_tips,
)
from components.email_templates import generate_templates_from_analysis

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
    "Generate research prompts using the OUS Framework (Outcome → Understanding → Standard) | "
    "**Now with Zinsser's Writing Principles built in**"
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

# Tab Navigation
tab1, tab2, tab3 = st.tabs([
    "🚀 Generate Prompts",
    "✍️ Plain English Checker",
    "📧 Email Templates"
])

# ==================== TAB 1: Generate Prompts ====================
with tab1:
    # Workflow Selection
    workflow_mode = st.radio(
        "Choose Workflow",
        [
            "🚀 Full 5-Prompt Workflow (Recommended)",
            "🔧 Individual Prompt Builder",
        ],
        horizontal=True,
    )

    if workflow_mode == "🚀 Full 5-Prompt Workflow (Recommended)":
        st.markdown("### 🎯 Complete Sales Prospecting Sequence")
        st.info(
            "**This generates all 5 prompts in the correct order:**\n\n"
            "1. **Phase 1**: Discovery & Compliance Research\n"
            "2. **Phase 2**: General Counsel Psychological Profiling\n"
            "3. **Phase 3**: Credibility-Based Email Drafting\n"
            "4. **Sales Executive Summary**: Quick 90-second brief for busy reps\n"
            "5. **OUS Framework**: Outcome → Understanding → Standard Analysis\n\n"
            "Use these prompts sequentially in ChatGPT/Claude to build a complete prospect dossier."
        )
        
        if st.button("✨ Generate Full Workflow", type="primary", use_container_width=True):
            if not company_name:
                st.error("❌ Please enter a company name to generate prompts.")
            else:
                with st.spinner("Generating 5-phase workflow..."):
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
                        key="download_p1",
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
                        key="download_p2",
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
                        key="download_p3",
                    )
                
                # NEW: Sales Executive Summary
                with st.expander("📋 PROMPT 4: Sales Executive Summary (90-Second Brief)", expanded=True):
                    st.markdown(
                        "**🎯 NEW: For Time-Strapped Sales Reps**\n\n"
                        "**Usage:** After completing Prompts 1-3, paste this prompt PLUS all previous outputs. "
                        "The AI will create a one-page cheat sheet that distills everything into a 90-second brief.\n\n"
                        "**Why this matters:** Your sales team won't read 3 pages of research. "
                        "They WILL read a one-page summary that tells them exactly what to say on the call."
                    )
                    st.code(prompts["summary"], language="markdown")
                    st.download_button(
                        "📥 Download Prompt 4 (Sales Summary)",
                        prompts["summary"],
                        file_name=f"4_summary_{company_name.replace(' ', '_')}.txt",
                        mime="text/plain",
                        key="download_p4",
                    )
                
                # OUS Framework
                with st.expander("📋 PROMPT 5: OUS Framework Analysis"):
                    st.markdown(
                        "**Usage:** Use this prompt to apply the Outcome → Understanding → Standard lens "
                        "to all your findings. This helps you refine your positioning."
                    )
                    st.code(prompts["ous"], language="markdown")
                    st.download_button(
                        "📥 Download Prompt 5 (OUS)",
                        prompts["ous"],
                        file_name=f"5_ous_{company_name.replace(' ', '_')}.txt",
                        mime="text/plain",
                        key="download_p5",
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
                    key="download_individual",
                )

# ==================== TAB 2: Plain English Checker ====================
with tab2:
    st.markdown("## ✍️ Plain English Writing Checker")
    st.markdown(
        "**Paste your draft email or message below.** "
        "This tool will flag zombie nouns, jargon, and passive voice based on Zinsser's Principles."
    )
    
    draft_text = st.text_area(
        "Your Draft Text:",
        height=250,
        placeholder="Paste your email draft here...\n\nExample:\n'We are pleased to facilitate the implementation of our robust solution to optimize your legal workflows and leverage synergies...'",
        key="draft_text"
    )
    
    col1, col2 = st.columns([1, 3])
    with col1:
        check_button = st.button("🔍 Check My Writing", type="primary", use_container_width=True)
    
    if check_button and draft_text:
        with st.spinner("Analyzing your writing..."):
            results = check_plain_english(draft_text)
        
        # Display Score
        score = results["score"]
        grade, emoji = get_writing_score_label(score)
        
        st.markdown("---")
        st.markdown(f"### {emoji} Writing Quality Score: {score}/100 ({grade})")
        
        # Display Issues
        if results["zombie_words"] or results["passive_voice"]:
            st.warning("⚠️ **Issues Found - See below for suggestions**")
            
            # Zombie Words
            if results["zombie_words"]:
                st.markdown("#### 🧟 Zombie Nouns / Jargon Detected")
                st.markdown("Replace these corporate buzzwords with plain English:")
                
                for zombie, replacement in results["zombie_words"]:
                    st.markdown(f"- ❌ **'{zombie}'** → ✅ **'{replacement}'**")
            
            # Passive Voice
            if results["passive_voice"]:
                st.markdown("#### 🔄 Passive Voice Detected")
                st.markdown("Switch to active voice to sound more human:")
                
                for sentence, suggestion in results["passive_voice"]:
                    with st.expander(f"📝 {sentence[:60]}..."):
                        st.markdown(f"**Full sentence:** {sentence}")
                        st.markdown(f"**Issue:** {suggestion}")
                        st.markdown("**Fix:** Rewrite using active voice (subject does the action)")
        else:
            st.success("✅ **Great job!** No major issues found. Your writing is clear and direct.")
        
        # Writing Tips Expander
        st.markdown("---")
        with st.expander("💡 How to Improve This Draft"):
            st.markdown(get_writing_tips())
    
    elif check_button and not draft_text:
        st.error("❌ Please paste some text to check.")
    
    # Always show writing tips
    st.markdown("---")
    with st.expander("✍️ How to Use These Insights in Your Outreach"):
        st.markdown(get_writing_tips())

# ==================== TAB 3: Email Templates ====================
with tab3:
    st.markdown("## 📧 Fill-in-the-Blank Email Templates")
    st.markdown(
        "**After completing your OUS analysis**, use these templates as starting points. "
        "They're pre-populated with placeholders - just replace the bracketed text with your findings."
    )
    
    st.info(
        "💡 **Pro Tip:** Copy Template A or B, paste into the Plain English Checker tab, "
        "and make sure it passes the writing test before sending!"
    )
    
    # Input fields for template generation
    st.markdown("### 📝 Template Inputs (Optional)")
    st.caption("Fill these in to generate customized templates, or use the default placeholders")
    
    col1, col2 = st.columns(2)
    
    with col1:
        template_outcome = st.text_input(
            "Outcome (from OUS analysis)",
            placeholder="e.g., reducing outside counsel spend by 25%",
            key="template_outcome"
        )
        
        template_pain = st.text_input(
            "Pain Point",
            placeholder="e.g., junior associates spending 60% time on manual cite-checking",
            key="template_pain"
        )
        
        template_challenge = st.text_input(
            "Specific Challenge",
            placeholder="e.g., cross-border PDPO compliance after Shenzhen acquisition",
            key="template_challenge"
        )
    
    with col2:
        template_similar_client = st.text_input(
            "Similar Client (anonymized)",
            placeholder="e.g., a HK-listed fintech company",
            key="template_similar_client"
        )
        
        template_solution = st.text_input(
            "Solution Approach",
            placeholder="e.g., automated gap detection that caught 12 issues before SFC audit",
            key="template_solution"
        )
        
        template_buyer_name = st.text_input(
            "Buyer's First Name",
            placeholder="[Name]",
            key="template_buyer_name"
        )
    
    if st.button("✨ Generate Templates", type="primary", use_container_width=True):
        if not company_name:
            st.error("❌ Please enter a company name in the sidebar first.")
        else:
            templates = generate_templates_from_analysis(
                company_name=company_name,
                outcome=template_outcome or "[Outcome - e.g., 'reducing outside counsel spend by 25%']",
                pain_point=template_pain or "[Pain Point - e.g., 'junior associates spending 60% of time on manual cite-checking']",
                specific_challenge=template_challenge or "[Specific Challenge - e.g., 'cross-border PDPO compliance after Shenzhen acquisition']",
                similar_client=template_similar_client or "[Similar Client - e.g., 'a HK-listed fintech company']",
                solution_approach=template_solution or "[Solution Approach - e.g., 'automated compliance gap detection']",
                buyer_name=template_buyer_name or "[Name]",
            )
            
            st.success("✅ Templates generated! Edit these to match your voice.")
            
            # Template A
            with st.expander("📧 TEMPLATE A: The Outcome Hook", expanded=True):
                st.markdown("**When to use:** When you know their strategic goal from research")
                st.code(templates["template_a"], language="markdown")
                st.download_button(
                    "📥 Download Template A",
                    templates["template_a"],
                    file_name=f"template_A_outcome_{company_name.replace(' ', '_')}.txt",
                    mime="text/plain",
                    key="download_template_a"
                )
            
            # Template B
            with st.expander("📧 TEMPLATE B: The Pain Point Entry"):
                st.markdown("**When to use:** When you know their specific struggle/challenge")
                st.code(templates["template_b"], language="markdown")
                st.download_button(
                    "📥 Download Template B",
                    templates["template_b"],
                    file_name=f"template_B_pain_{company_name.replace(' ', '_')}.txt",
                    mime="text/plain",
                    key="download_template_b"
                )
            
            st.markdown("---")
            st.info(
                "💡 **Next Steps:**\n\n"
                "1. Copy Template A or B\n"
                "2. Replace all [bracketed placeholders] with your research findings\n"
                "3. Paste into the **Plain English Checker** tab to verify it sounds human\n"
                "4. Send!"
            )

# -------------------- Usage Guide --------------------
st.markdown("---")
with st.expander("📖 How to Use This Tool (Updated Guide)"):
    st.markdown("""
    ### 🎯 Quick Start Guide
    
    **Step 1: Enter Prospect Info (Sidebar)**
    - Enter company/law firm name
    - Paste their website or LinkedIn URL
    - Select practice area and buyer persona
    
    **Step 2: Generate Prompts (Tab 1)**
    - Use **Full Workflow** mode for complete prospect research
    - **NEW:** Prompt 4 now generates a Sales Executive Summary (90-second brief for busy reps)
    - Use prompts sequentially in ChatGPT/Claude
    
    **Step 3: Check Your Writing (Tab 2) 🆕**
    - Draft your email based on AI outputs
    - Paste into Plain English Checker
    - Fix zombie nouns and passive voice
    - Aim for score 80+ before sending
    
    **Step 4: Use Email Templates (Tab 3) 🆕**
    - Two pre-built templates based on your research
    - Template A: Outcome Hook (leads with their goal)
    - Template B: Pain Point Entry (leads with empathy)
    - Fill in bracketed placeholders with your findings
    
    ---
    
    ### 🧠 OUS Framework Explained
    
    **O - Outcome:** What strategic business goal does the buyer need to achieve?
    - Example: "Reduce outside counsel spend by 25%"
    
    **U - Understanding Pain:** What specific operational pain is blocking that outcome?
    - Example: "Junior associates spend 60% of time on manual research"
    
    **S - Standard:** What criteria will they use to evaluate solutions?
    - Example: "Must integrate with iManage, cover HK + PRC law, deploy in <2 weeks"
    
    ---
    
    ### ✍️ Zinsser's Principles (Built into Every Prompt)
    
    **1. Humanity** - Sound like a person, not a corporation
    - Use "I", "you", "we"
    - Show empathy
    
    **2. Clarity** - One idea per sentence
    - Use specific details (dates, numbers, names)
    - Replace abstract nouns with verbs
    
    **3. Brevity** - Cut every unnecessary word
    - Max 150 words per email
    - If you can say it in 5 words instead of 10, do it
    
    **4. Simplicity** - Use everyday language
    - Avoid jargon unless essential
    - Would a non-lawyer understand this?
    
    ---
    
    ### ⚡ Pro Tips
    
    - **For best results:** Run prompts 1 → 2 → 3 → 4 → 5 sequentially
    - **Time saver:** Use Prompt 4 (Sales Summary) to brief your team in 90 seconds
    - **Quality check:** Use Plain English Checker on every draft before sending
    - **Template hack:** Generate both templates, pick the one that fits better, then customize
    - **Red flag:** If your email gets a writing score below 70, rewrite it
    """)

# -------------------- Footer --------------------
st.markdown("---")
st.caption(
    "**Legal Tech Sales Prospecting Tool v2.0** | OUS Framework + Zinsser's Principles | "
    "Designed for Hong Kong legal market prospecting | "
    f"Session: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
)
