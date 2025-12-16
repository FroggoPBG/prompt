"""
M&A Prospecting Tool - Streamlit App
Generates AI prompts for legal/compliance discovery research.
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, Optional

import streamlit as st

from components.email_templates import EmailTemplateGenerator
from components.presets import ProspectPreset, export_preset_bytes, load_preset_into_state
from components.recipes import PromptRecipeManager, ProspectContext
from components.writing_checker import check_plain_english, get_writing_tips

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="M&A Prospecting Tool",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

def init_session_state():
    """Initialize all session state variables."""
    defaults = {
        "company_name": "",
        "industry": "",
        "deal_type": "",
        "legal_entity_type": "",
        "revenue_size": "",
        "geographic_scope": [],
        "additional_context": "",
        "product_interest": [],
        "current_phase": "phase1"
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_prospect_context() -> ProspectContext:
    """Extract all prospect context from session state."""
    return ProspectContext(
        company_name=st.session_state.get('company_name', ''),
        industry_sector=st.session_state.get('industry', ''),
        transaction_type=st.session_state.get('deal_type', ''),
        legal_entity_type=st.session_state.get('legal_entity_type', ''),
        transaction_size=st.session_state.get('revenue_size', ''),
        geographic_scope=", ".join(st.session_state.get('geographic_scope', [])),
        deal_context=st.session_state.get('deal_type', ''),
        additional_notes=st.session_state.get('additional_context', ''),
        company_products=", ".join(st.session_state.get('product_interest', []))
    )

def render_copy_button(text: str, key: str, button_label: str = "📋 Copy to Clipboard"):
    """Render a copy-to-clipboard button."""
    st.code(text, language="markdown", line_numbers=False)
    if st.button(button_label, key=key, use_container_width=True):
        st.write("✅ Copied! (Use Ctrl+C or Cmd+C to copy the text above)")

def render_download_button(text: str, filename: str, key: str):
    """Render a download button for prompt text."""
    st.download_button(
        label="⬇️ Download Prompt",
        data=text,
        file_name=filename,
        mime="text/plain",
        key=key,
        use_container_width=True
    )

def render_prompt_expander(
    title: str,
    prompt: str,
    filename: str,
    key_suffix: str,
    expanded: bool = False,
    usage_note: Optional[str] = None
):
    """Render an expandable section with a prompt."""
    with st.expander(title, expanded=expanded):
        if usage_note:
            st.info(f"**How to use:** {usage_note}")
        st.code(prompt, language="markdown", line_numbers=False)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📋 Copy", key=f"copy_{key_suffix}", use_container_width=True):
                st.success("✅ Text ready to copy (use Ctrl+C / Cmd+C on the code block above)")
        with col2:
            render_download_button(prompt, filename, f"download_{key_suffix}")

# ============================================================================
# SIDEBAR - PROSPECT INPUT FORM
# ============================================================================

def render_sidebar():
    """Render the sidebar with prospect input fields."""
    with st.sidebar:
        st.title("🎯 Prospect Details")
        st.markdown("Fill in the information below to generate customized research prompts.")
        
        st.markdown("---")
        
        # Company Information
        st.subheader("📊 Company Information")
        
        st.session_state.company_name = st.text_input(
            "Company Name*",
            value=st.session_state.company_name,
            placeholder="e.g., OLN Law",
            help="The legal name of the target company"
        )
        
        st.session_state.industry = st.selectbox(
            "Practice Area / Industry*",
            options=[
                "",
                "M&A / Corporate Finance",
                "Banking & Finance",
                "Litigation & Dispute Resolution",
                "Intellectual Property",
                "Employment Law",
                "Regulatory & Compliance",
                "Real Estate & Property",
                "Tax & Revenue",
                "Private Client / Wealth",
                "General Practice",
                "Other"
            ],
            index=0 if not st.session_state.industry else None,
            help="Primary practice area or industry sector"
        )
        
        st.session_state.legal_entity_type = st.selectbox(
            "Buyer Persona",
            options=[
                "",
                "Law Firm Partner",
                "General Counsel (In-House)",
                "Legal Operations Director",
                "Barrister",
                "Corporate Secretary",
                "Compliance Officer",
                "Managing Partner",
                "Unknown"
            ],
            help="Primary decision-maker type"
        )
        
        st.markdown("---")
        
        # Deal Context
        st.subheader("🤝 Deal Context")
        
        st.session_state.deal_type = st.selectbox(
            "Engagement Type",
            options=[
                "",
                "New Business (Cold Outreach)",
                "Existing Client (Upsell)",
                "Competitive Displacement",
                "Renewal Risk",
                "Expansion (New Practice Area)",
                "Other/Exploratory"
            ],
            help="Type of engagement"
        )
        
        st.session_state.revenue_size = st.selectbox(
            "Firm Size",
            options=[
                "",
                "Solo / Small (1-10 lawyers)",
                "Mid-size (11-50 lawyers)",
                "Large (51-200 lawyers)",
                "Major (200+ lawyers)",
                "Magic Circle / Global",
                "Unknown"
            ],
            help="Approximate firm size"
        )
        
        st.session_state.geographic_scope = st.multiselect(
            "Geographic Focus",
            options=[
                "Hong Kong",
                "Mainland China",
                "Greater Bay Area",
                "Asia-Pacific",
                "United Kingdom",
                "United States",
                "Global/Multi-Regional"
            ],
            default=st.session_state.geographic_scope if st.session_state.geographic_scope else [],
            help="Primary operating regions"
        )
        
        st.markdown("---")
        
        # Product Interest
        st.subheader("🎯 Product Interest")
        
        st.session_state.product_interest = st.multiselect(
            "LexisNexis Solutions of Interest",
            options=[
                "Lexis+ AI",
                "Practical Guidance",
                "Lexis+ HK",
                "Halsbury's Laws of Hong Kong",
                "Company & Commercial",
                "Litigation & Dispute Resolution",
                "Due Diligence Tools",
                "Regulatory & Compliance",
                "Not Sure/Exploratory"
            ],
            default=st.session_state.product_interest if st.session_state.product_interest else [],
            help="Products or solutions relevant to this prospect"
        )
        
        st.markdown("---")
        
        # Additional Context
        st.subheader("📝 Trigger Events & Notes")
        
        st.session_state.additional_context = st.text_area(
            "Known Triggers & Context",
            value=st.session_state.additional_context,
            placeholder="e.g., Won Asialaw award, hosting Arbitration Week sessions, recent lateral hire from Baker McKenzie, expanding China practice...",
            help="Specific trigger events, news, or intelligence about this prospect",
            height=120
        )
        
        st.markdown("---")
        
        # Reset Button
        if st.button("🔄 Reset All Fields", type="secondary", use_container_width=True):
            for key in st.session_state.keys():
                if key != "current_phase":
                    if isinstance(st.session_state[key], str):
                        st.session_state[key] = ""
                    elif isinstance(st.session_state[key], list):
                        st.session_state[key] = []
            st.rerun()

# ============================================================================
# MAIN CONTENT - PROMPT GENERATORS
# ============================================================================

def render_individual_prompts():
    """Render individual phase prompt generators."""
    st.markdown("### 🎯 Individual Prompt Generators")
    st.info(
        "Generate prompts one phase at a time. Use these if you want to customize "
        "your workflow or only need specific research stages."
    )
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "Phase 1: Discovery",
        "Phase 2: Profiling",
        "Phase 2.5: Solution Map",
        "Phase 2.7: Competitive",
        "Phase 3: Email",
        "Phase 4: Summary",
        "Phase 5: OUS",
        "Phase 6: BANT+"
    ])
    
    company_name = st.session_state.get("company_name", "")
    context = get_prospect_context()
    
    # Phase 1
    with tab1:
        st.markdown("#### 📋 Phase 1: Discovery & Risk Research")
        st.markdown(
            "**Purpose:** Identify legal triggers and compliance pressure points.\n\n"
            "**What you'll get:** A comprehensive research prompt that helps you find:\n"
            "- Recent M&A activity or corporate changes\n"
            "- Regulatory challenges or legal disputes\n"
            "- Privacy/cybersecurity incidents\n"
            "- Industry-specific compliance pressures"
        )
        
        if st.button("Generate Phase 1 Prompt", key="gen_p1", type="primary"):
            if not company_name:
                st.error("❌ Please enter a company name in the sidebar first.")
            else:
                with st.spinner("Generating prompt..."):
                    prompt = PromptRecipeManager.generate_phase1(context)
                st.success("✅ Prompt generated!")
                render_prompt_expander(
                    title="Your Phase 1 Prompt",
                    prompt=prompt,
                    filename=f"phase1_{company_name.replace(' ', '_')}.txt",
                    key_suffix="p1_main",
                    expanded=True
                )
    
    # Phase 2
    with tab2:
        st.markdown("#### 👤 Phase 2: Decision-Making Dynamics")
        st.markdown(
            "**Purpose:** Understand the buyer's decision-making process.\n\n"
            "**What you'll get:** A prompt that analyzes:\n"
            "- Stakeholder mapping\n"
            "- Decision-making style\n"
            "- Communication expectations\n"
            "- Likely objections"
        )
        
        if st.button("Generate Phase 2 Prompt", key="gen_p2", type="primary"):
            if not company_name:
                st.error("❌ Please enter a company name in the sidebar first.")
            else:
                with st.spinner("Generating prompt..."):
                    prompt = PromptRecipeManager.generate_phase2(context)
                st.success("✅ Prompt generated!")
                render_prompt_expander(
                    title="Your Phase 2 Prompt",
                    prompt=prompt,
                    filename=f"phase2_{company_name.replace(' ', '_')}.txt",
                    key_suffix="p2_main",
                    expanded=True,
                    usage_note="Use this AFTER completing Phase 1. Paste the Phase 1 output along with this prompt."
                )
    
    # Phase 2.5
    with tab3:
        st.markdown("#### 🎯 Phase 2.5: Pain Point & Solution Mapping")
        st.markdown(
            "**Purpose:** Map specific pain points to our solutions.\n\n"
            "**What you'll get:** A prompt that creates:\n"
            "- Pain point hypotheses\n"
            "- Product-to-problem alignment\n"
            "- Value proposition mapping\n"
            "- Discovery questions to validate"
        )
        
        if st.button("Generate Phase 2.5 Prompt", key="gen_p25", type="primary"):
            if not company_name:
                st.error("❌ Please enter a company name in the sidebar first.")
            else:
                with st.spinner("Generating prompt..."):
                    prompt = PromptRecipeManager.generate_phase25(context)
                st.success("✅ Prompt generated!")
                render_prompt_expander(
                    title="Your Phase 2.5 Prompt",
                    prompt=prompt,
                    filename=f"phase25_{company_name.replace(' ', '_')}.txt",
                    key_suffix="p25_main",
                    expanded=True,
                    usage_note="Use this AFTER Phases 1 & 2. Paste outputs from both previous phases along with this prompt."
                )
    
    # Phase 2.7 - NEW
    with tab4:
        st.markdown("#### ⚔️ Phase 2.7: Competitive Positioning Analysis")
        st.markdown(
            "**Purpose:** Understand the competitive landscape before outreach.\n\n"
            "**What you'll get:** A prompt that analyzes:\n"
            "- Direct competitors likely targeting this prospect\n"
            "- Indirect competitors (status quo, free resources)\n"
            "- Our differentiation for this specific prospect\n"
            "- Win themes and positioning strategy\n"
            "- Discovery questions to uncover competitive situation"
        )
        
        if st.button("Generate Phase 2.7 Prompt", key="gen_p27", type="primary"):
            if not company_name:
                st.error("❌ Please enter a company name in the sidebar first.")
            else:
                with st.spinner("Generating prompt..."):
                    prompt = PromptRecipeManager.generate_phase27(context)
                st.success("✅ Prompt generated!")
                render_prompt_expander(
                    title="Your Phase 2.7 Prompt",
                    prompt=prompt,
                    filename=f"phase27_{company_name.replace(' ', '_')}.txt",
                    key_suffix="p27_main",
                    expanded=True,
                    usage_note="Use this AFTER Phases 1, 2, & 2.5. This helps you position against competitors before drafting outreach."
                )
    
    # Phase 3
    with tab5:
        st.markdown("#### ✉️ Phase 3: Credibility-Based Email Drafting")
        st.markdown(
            "**Purpose:** Create a personalized cold outreach email.\n\n"
            "**What you'll get:** A prompt that generates:\n"
            "- Quality gate checks (trigger strength, pain point sources)\n"
            "- Hook-Pivot-Ask email structure\n"
            "- Self-assessment against 'Associate Test'\n"
            "- Follow-up email draft\n"
            "- Low-intel fallback if triggers are weak"
        )
        
        st.warning("⚠️ **New:** This phase now includes quality gates to prevent weak emails from being sent.")
        
        if st.button("Generate Phase 3 Prompt", key="gen_p3", type="primary"):
            if not company_name:
                st.error("❌ Please enter a company name in the sidebar first.")
            else:
                with st.spinner("Generating prompt..."):
                    prompt = PromptRecipeManager.generate_phase3(context)
                st.success("✅ Prompt generated!")
                render_prompt_expander(
                    title="Your Phase 3 Prompt",
                    prompt=prompt,
                    filename=f"phase3_{company_name.replace(' ', '_')}.txt",
                    key_suffix="p3_main",
                    expanded=True,
                    usage_note="Use this AFTER Phases 1, 2, 2.5, and 2.7. Paste all previous outputs along with this prompt."
                )
    
    # Phase 4
    with tab6:
        st.markdown("#### 📊 Phase 4: Sales Executive Summary")
        st.markdown(
            "**Purpose:** Create a 90-second brief for time-strapped sales reps.\n\n"
            "**What you'll get:** A one-page summary containing:\n"
            "- Account snapshot\n"
            "- Strategic rationale\n"
            "- Recommended approach\n"
            "- Key unknowns and risks\n"
            "- Next steps"
        )
        
        if st.button("Generate Phase 4 Prompt", key="gen_p4", type="primary"):
            if not company_name:
                st.error("❌ Please enter a company name in the sidebar first.")
            else:
                with st.spinner("Generating prompt..."):
                    prompt = PromptRecipeManager.generate_phase4(context)
                st.success("✅ Prompt generated!")
                render_prompt_expander(
                    title="Your Phase 4 Prompt",
                    prompt=prompt,
                    filename=f"phase4_{company_name.replace(' ', '_')}.txt",
                    key_suffix="p4_main",
                    expanded=True,
                    usage_note="Use this AFTER Phases 1-3. This distills everything into a quick reference guide."
                )
    
    # Phase 5
    with tab7:
        st.markdown("#### 🔍 Phase 5: OUS Framework Analysis")
        st.markdown(
            "**Purpose:** Score the opportunity using Outcome-Understanding-Selection.\n\n"
            "**What you'll get:** Strategic analysis covering:\n"
            "- Outcome alignment (35%)\n"
            "- Understanding of pain (35%)\n"
            "- Selection process favorability (30%)\n"
            "- Overall score and recommendation"
        )
        
        if st.button("Generate Phase 5 Prompt", key="gen_p5", type="primary"):
            if not company_name:
                st.error("❌ Please enter a company name in the sidebar first.")
            else:
                with st.spinner("Generating prompt..."):
                    prompt = PromptRecipeManager.generate_phase5(context)
                st.success("✅ Prompt generated!")
                render_prompt_expander(
                    title="Your Phase 5 Prompt",
                    prompt=prompt,
                    filename=f"phase5_{company_name.replace(' ', '_')}.txt",
                    key_suffix="p5_main",
                    expanded=True,
                    usage_note="Use this to score and prioritize the opportunity based on all previous research."
                )
    
    # Phase 6
    with tab8:
        st.markdown("#### ✅ Phase 6: Deal Qualification (BANT+)")
        st.markdown(
            "**Purpose:** Qualify the opportunity before investing more time.\n\n"
            "**What you'll get:** Assessment covering:\n"
            "- Budget likelihood\n"
            "- Authority mapping\n"
            "- Need severity\n"
            "- Timeline factors\n"
            "- Qualification recommendation"
        )
        
        if st.button("Generate Phase 6 Prompt", key="gen_p6", type="primary"):
            if not company_name:
                st.error("❌ Please enter a company name in the sidebar first.")
            else:
                with st.spinner("Generating prompt..."):
                    prompt = PromptRecipeManager.generate_phase6(context)
                st.success("✅ Prompt generated!")
                render_prompt_expander(
                    title="Your Phase 6 Prompt",
                    prompt=prompt,
                    filename=f"phase6_{company_name.replace(' ', '_')}.txt",
                    key_suffix="p6_main",
                    expanded=True,
                    usage_note="Use this to qualify the opportunity and generate discovery questions for the first call."
                )

def render_full_workflow():
    """Render the full 8-prompt workflow generator."""
    
    st.markdown("### 🎯 Complete Sales Prospecting Sequence")
    
    st.info("""
**This generates all 8 prompts in the correct order:**

1. **Phase 1**: Discovery & Compliance Research
2. **Phase 2**: Decision-Making Dynamics
3. **Phase 2.5**: Pain Point Hypothesis & Solution Mapping
4. **Phase 2.7**: Competitive Positioning Analysis ⚔️ *NEW*
5. **Phase 3**: Credibility-Based Email Drafting (with quality gates)
6. **Phase 4**: Sales Executive Summary
7. **Phase 5**: OUS Framework Analysis
8. **Phase 6**: Deal Qualification (BANT+)

Use these prompts sequentially in ChatGPT/Claude to build a complete prospect dossier.
    """)
    
    company_name = st.session_state.get("company_name", "")
    
    if st.button("✨ Generate Full Workflow", type="primary", use_container_width=True):
        if not company_name:
            st.error("❌ Please enter a company name to generate prompts.")
            return
        
        with st.spinner("Generating 8-phase workflow..."):
            context = get_prospect_context()
            prompts = PromptRecipeManager.generate_full_workflow(context)
        
        st.success("✅ Workflow generated! Copy each prompt below and paste into your AI tool sequentially.")
        
        # Phase 1
        render_prompt_expander(
            title="📋 PROMPT 1: Discovery & Compliance Research",
            prompt=prompts["phase1"],
            filename=f"1_discovery_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p1",
            expanded=True,
            usage_note="Paste this into ChatGPT/Claude. The AI will research the company and identify legal triggers."
        )
        
        # Phase 2
        render_prompt_expander(
            title="📋 PROMPT 2: Decision-Making Dynamics",
            prompt=prompts["phase2"],
            filename=f"2_profiling_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p2",
            usage_note="After completing Prompt 1, paste this prompt PLUS the output from Prompt 1."
        )
        
        # Phase 2.5
        render_prompt_expander(
            title="📋 PROMPT 2.5: Pain Point & Solution Mapping",
            prompt=prompts["phase25"],
            filename=f"2_5_solution_mapping_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p25",
            usage_note="After completing Prompts 1 & 2, paste this prompt PLUS the outputs from both."
        )
        
        # Phase 2.7 - NEW
        st.markdown("---")
        render_prompt_expander(
            title="📋 PROMPT 2.7: ⚔️ Competitive Positioning Analysis (NEW)",
            prompt=prompts["phase27"],
            filename=f"2_7_competitive_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p27",
            expanded=True,
            usage_note=(
                "**🆕 NEW STEP: Competitive Analysis** - "
                "Before drafting outreach, understand who else is competing for this prospect. "
                "Paste this prompt PLUS outputs from Phases 1, 2, & 2.5."
            )
        )
        
        # Phase 3
        st.markdown("---")
        render_prompt_expander(
            title="📋 PROMPT 3: Credibility-Based Email Drafting (with Quality Gates)",
            prompt=prompts["phase3"],
            filename=f"3_email_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p3",
            expanded=True,
            usage_note=(
                "**⚠️ IMPROVED:** Now includes quality gates to check trigger strength, pain point sources, "
                "and proof point stakes before drafting. Paste all previous outputs along with this prompt."
            )
        )
        
        # Phase 4
        render_prompt_expander(
            title="📋 PROMPT 4: Sales Executive Summary",
            prompt=prompts["phase4"],
            filename=f"4_summary_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p4",
            usage_note="Creates a 90-second cheat sheet for quick reference before calls."
        )
        
        # Phase 5
        render_prompt_expander(
            title="📋 PROMPT 5: OUS Framework Analysis",
            prompt=prompts["phase5"],
            filename=f"5_ous_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p5",
            usage_note="Score the opportunity using Outcome-Understanding-Selection framework."
        )
        
        # Phase 6
        render_prompt_expander(
            title="📋 PROMPT 6: Deal Qualification (BANT+)",
            prompt=prompts["phase6"],
            filename=f"6_bant_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p6",
            usage_note="Qualify the opportunity and generate discovery questions for the first call."
        )

def render_main_content():
    """Render the main content area."""
    st.title("🎯 HK Legal Market Prospecting Tool")
    st.markdown(
        "**Generate AI-powered research prompts for legal/compliance discovery and sales outreach.**"
    )
    
    st.markdown("---")
    
    # Check if basic info is filled
    if not st.session_state.company_name:
        st.warning(
            "⚠️ **Get Started:** Fill in the prospect details in the sidebar to generate prompts."
        )
        st.info(
            "This tool creates customized prompts that you can paste into ChatGPT or Claude "
            "to research prospects, identify triggers, and craft personalized outreach."
        )
        
        # Show workflow overview
        with st.expander("📋 See the 8-Phase Workflow", expanded=False):
            st.markdown("""
| Phase | Name | Purpose |
|-------|------|---------|
| 1 | Discovery & Compliance Research | Find triggers and pressure points |
| 2 | Decision-Making Dynamics | Understand how they buy |
| 2.5 | Pain Point & Solution Mapping | Match our products to their problems |
| 2.7 | **Competitive Positioning** ⚔️ | Know who else is in the deal |
| 3 | Credibility-Based Email | Draft outreach that passes the "Associate Test" |
| 4 | Sales Executive Summary | 90-second brief for before calls |
| 5 | OUS Framework Analysis | Score and prioritize the opportunity |
| 6 | Deal Qualification (BANT+) | Qualify before investing more time |
            """)
        return
    
    # Display current prospect summary
    with st.container():
        st.markdown("#### 📊 Current Prospect")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Company", st.session_state.company_name)
        with col2:
            st.metric("Practice Area", st.session_state.industry or "Not specified")
        with col3:
            st.metric("Buyer Persona", st.session_state.legal_entity_type or "Not specified")
        with col4:
            st.metric("Engagement Type", st.session_state.deal_type or "Not specified")
    
    # Show trigger context if provided
    if st.session_state.additional_context:
        st.markdown("**Known Triggers:**")
        st.info(st.session_state.additional_context)
    
    st.markdown("---")
    
    # Main workflow options
    workflow_mode = st.radio(
        "Choose your workflow:",
        options=["Full Workflow (All 8 Phases)", "Individual Prompts"],
        horizontal=True,
        help="Full Workflow generates all prompts at once. Individual Prompts lets you generate one phase at a time."
    )
    
    st.markdown("---")
    
    if workflow_mode == "Full Workflow (All 8 Phases)":
        render_full_workflow()
    else:
        render_individual_prompts()

# ============================================================================
# MAIN APP
# ============================================================================

def main():
    """Main application entry point."""
    init_session_state()
    render_sidebar()
    render_main_content()
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666; font-size: 0.9em;'>"
        "HK Legal Market Prospecting Tool | Built for LexisNexis Sales Teams | December 2025"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
