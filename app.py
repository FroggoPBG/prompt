"""
M&A Prospecting Tool - Streamlit App
Generates AI prompts for legal/compliance discovery research.
"""

from __future__ import annotations

from datetime import datetime

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
        "geographic_scope": "",
        "additional_context": "",
        "product_interest": "",
        "current_phase": "phase1"
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_prospect_context() -> Dict[str, str]:
    """Extract all prospect context from session state."""
    return {
        "company_name": st.session_state.company_name,
        "industry": st.session_state.industry,
        "deal_type": st.session_state.deal_type,
        "legal_entity_type": st.session_state.legal_entity_type,
        "revenue_size": st.session_state.revenue_size,
        "geographic_scope": st.session_state.geographic_scope,
        "additional_context": st.session_state.additional_context,
        "product_interest": st.session_state.product_interest
    }

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
            placeholder="e.g., ABC Corporation",
            help="The legal name of the target company"
        )
        
        st.session_state.industry = st.selectbox(
            "Industry/Sector*",
            options=[
                "",
                "Financial Services",
                "Healthcare/Life Sciences",
                "Technology/Software",
                "Manufacturing",
                "Energy/Utilities",
                "Real Estate",
                "Professional Services",
                "Retail/Consumer Goods",
                "Other"
            ],
            index=0 if not st.session_state.industry else None,
            help="Primary industry sector"
        )
        
        st.session_state.legal_entity_type = st.selectbox(
            "Legal Entity Type",
            options=[
                "",
                "Public Company (Listed)",
                "Private Company",
                "Private Equity Owned",
                "Family Office/HNW Owned",
                "Government Entity",
                "Non-Profit",
                "Partnership/LLP",
                "Unknown"
            ],
            help="Legal structure of the organization"
        )
        
        st.markdown("---")
        
        # Deal Context
        st.subheader("🤝 Deal Context")
        
        st.session_state.deal_type = st.selectbox(
            "Transaction Type",
            options=[
                "",
                "M&A (Buyer)",
                "M&A (Seller)",
                "M&A (Target)",
                "Private Equity Deal",
                "Corporate Restructuring",
                "IPO Preparation",
                "Regulatory Compliance Project",
                "Other/Exploratory"
            ],
            help="Type of transaction or engagement"
        )
        
        st.session_state.revenue_size = st.selectbox(
            "Company Size (Revenue)",
            options=[
                "",
                "< $10M",
                "$10M - $50M",
                "$50M - $250M",
                "$250M - $1B",
                "$1B - $5B",
                "$5B+",
                "Unknown"
            ],
            help="Approximate annual revenue"
        )
        
        st.session_state.geographic_scope = st.multiselect(
            "Geographic Scope",
            options=[
                "United Kingdom",
                "European Union",
                "United States",
                "Asia-Pacific",
                "Middle East",
                "Latin America",
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
                "Halsbury's Laws",
                "Corporate Law Suite",
                "Due Diligence Tools",
                "Compliance & Risk Solutions",
                "PSL (Practice Area Specific)",
                "Not Sure/Exploratory"
            ],
            default=st.session_state.product_interest if st.session_state.product_interest else [],
            help="Products or solutions relevant to this prospect"
        )
        
        st.markdown("---")
        
        # Additional Context
        st.subheader("📝 Additional Notes")
        
        st.session_state.additional_context = st.text_area(
            "Extra Context (Optional)",
            value=st.session_state.additional_context,
            placeholder="Any specific challenges, known triggers, or additional information...",
            help="Free-form notes about this prospect",
            height=100
        )
        
        st.markdown("---")
        
        # Reset Button
        if st.button("🔄 Reset All Fields", type="secondary", use_container_width=True):
            for key in st.session_state.keys():
                if key != "current_phase":
                    st.session_state[key] = "" if isinstance(st.session_state[key], str) else []
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
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Phase 1: Discovery",
        "Phase 2: Profiling",
        "Phase 2.5: Solution Map",
        "Phase 3: Email",
        "Phase 4: Summary",
        "Phase 5: OUS"
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
        st.markdown("#### 👤 Phase 2: Buyer Psychological Profiling")
        st.markdown(
            "**Purpose:** Understand the buyer's emotional state and pain points.\n\n"
            "**What you'll get:** A prompt that analyzes:\n"
            "- Emotional triggers (anxiety, urgency, fear)\n"
            "- Decision-making pressures\n"
            "- Stakeholder concerns\n"
            "- Psychological buying motivations"
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
        st.markdown("#### 🎯 Phase 2.5: Solution Mapping (Product-to-Pain Fit)")
        st.markdown(
            "**Purpose:** Map specific LexisNexis products to identified pain points.\n\n"
            "**What you'll get:** A prompt that creates:\n"
            "- Product-to-problem alignment\n"
            "- Specific feature callouts\n"
            "- Value proposition mapping\n"
            "- Competitive positioning insights"
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
    
    # Phase 3
    with tab4:
        st.markdown("#### ✉️ Phase 3: Credibility-Based Email Drafting")
        st.markdown(
            "**Purpose:** Create a personalized cold outreach email.\n\n"
            "**What you'll get:** A prompt that generates:\n"
            "- Trigger-based opening hook\n"
            "- Specific product mentions\n"
            "- Credibility-building language\n"
            "- Clear call-to-action"
        )
        
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
                    usage_note="Use this AFTER Phases 1, 2, and 2.5. Paste all previous outputs along with this prompt."
                )
    
    # Phase 4
    with tab5:
        st.markdown("#### 📊 Phase 4: Sales Executive Summary")
        st.markdown(
            "**Purpose:** Create a 90-second brief for time-strapped sales reps.\n\n"
            "**What you'll get:** A one-page summary containing:\n"
            "- Key trigger events\n"
            "- Primary pain points\n"
            "- Recommended products\n"
            "- Call script talking points"
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
    with tab6:
        st.markdown("#### 🔍 Phase 5: OUS Framework Analysis")
        st.markdown(
            "**Purpose:** Apply the Outcome → Understanding → Standard lens.\n\n"
            "**What you'll get:** Strategic analysis covering:\n"
            "- Desired business outcomes\n"
            "- Deep understanding of challenges\n"
            "- Industry best practices and standards"
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
                    usage_note="Use this to refine your positioning and messaging based on all previous research."
                )

def render_full_workflow():
    """Render the full 6-prompt workflow generator."""
    st.markdown("### 🎯 Complete Sales Prospecting Sequence")
    st.info(
        "**This generates all 6 prompts in the correct order:**\n\n"
        "1. **Phase 1**: Discovery & Risk Research\n"
        "2. **Phase 2**: Buyer Psychological Profiling\n"
        "3. **Phase 2.5**: 🆕 Solution Mapping (Product-to-Pain Fit)\n"
        "4. **Phase 3**: Credibility-Based Email Drafting\n"
        "5. **Phase 4**: Sales Executive Summary (90-second brief)\n"
        "6. **Phase 5**: OUS Framework Analysis\n\n"
        "Use these prompts sequentially in ChatGPT/Claude to build a complete prospect dossier."
    )
    
    company_name = st.session_state.get("company_name", "")
    
    if st.button("✨ Generate Full Workflow", type="primary", use_container_width=True):
        if not company_name:
            st.error("❌ Please enter a company name to generate prompts.")
            return
        
   with st.spinner("Generating 6-phase workflow..."):
            context = ProspectContext(
                company_name=st.session_state.get('company_name', ''),
                industry_sector=st.session_state.get('industry_sector', ''),
                transaction_type=st.session_state.get('transaction_type', ''),
                legal_entity_type=st.session_state.get('legal_entity_type', ''),
                transaction_size=st.session_state.get('transaction_size', ''),
                geographic_scope=st.session_state.get('geographic_scope', ''),
                deal_context=st.session_state.get('deal_context', ''),
                additional_notes=st.session_state.get('additional_notes', '')
            )
            prompts = PromptRecipeManager.generate_full_workflow(context)
        
        st.success("✅ Workflow generated! Copy each prompt below and paste into your AI tool sequentially.")
        
        # Phase 1
        render_prompt_expander(
            title="📋 PROMPT 1: Discovery & Risk Research",
            prompt=prompts["phase1"],
            filename=f"1_discovery_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p1",
            expanded=True,
            usage_note="Paste this into ChatGPT/Claude. The AI will research the company and identify legal triggers."
        )
        
        # Phase 2
        render_prompt_expander(
            title="📋 PROMPT 2: Buyer Psychological Profiling",
            prompt=prompts["phase2"],
            filename=f"2_profiling_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p2",
            usage_note="After completing Prompt 1, paste this prompt PLUS the output from Prompt 1."
        )
        
        # Phase 2.5 - FIXED
        st.markdown("---")
        render_prompt_expander(
            title="📋 PROMPT 2.5: 🆕 Solution Mapping (Product-to-Pain Fit)",
            prompt=prompts["phase25"],  # ✅ FIXED: Changed from "phase2.5" to "phase25"
            filename=f"2_5_solution_mapping_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p25",
            expanded=True,
            usage_note=(
                "**🎯 NEW STEP: Product-to-Pain Mapping** - "
                "After completing Prompts 1 & 2, paste this prompt PLUS the outputs from both. "
                "The AI will map specific LexisNexis products to their pain points."
            )
        )
        
        # Phase 3
        render_prompt_expander(
            title="📋 PROMPT 3: Credibility-Based Email Drafting",
            prompt=prompts["phase3"],
            filename=f"3_email_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p3",
            usage_note="After completing Prompts 1, 2, & 2.5, paste this prompt PLUS all outputs."
        )
        
        # Phase 4
        st.markdown("---")
        render_prompt_expander(
            title="📋 PROMPT 4: Sales Executive Summary (90-Second Brief)",
            prompt=prompts["phase4"],
            filename=f"4_summary_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p4",
            expanded=False,
            usage_note=(
                "**🎯 For Time-Strapped Sales Reps** - "
                "Creates a one-page cheat sheet for quick reference before calls."
            )
        )
        
        # Phase 5
        render_prompt_expander(
            title="📋 PROMPT 5: OUS Framework Analysis",
            prompt=prompts["phase5"],
            filename=f"5_ous_{company_name.replace(' ', '_')}.txt",
            key_suffix="wf_p5",
            usage_note="Final strategic analysis to refine your positioning."
        )

def render_main_content():
    """Render the main content area."""
    st.title("🎯 M&A Prospecting Tool")
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
        return
    
    # Display current prospect summary
    with st.container():
        st.markdown("#### 📊 Current Prospect")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Company", st.session_state.company_name)
        with col2:
            st.metric("Industry", st.session_state.industry or "Not specified")
        with col3:
            st.metric("Deal Type", st.session_state.deal_type or "Not specified")
    
    st.markdown("---")
    
    # Main workflow options
    workflow_mode = st.radio(
        "Choose your workflow:",
        options=["Full Workflow (All 6 Phases)", "Individual Prompts"],
        horizontal=True,
        help="Full Workflow generates all prompts at once. Individual Prompts lets you generate one phase at a time."
    )
    
    st.markdown("---")
    
    if workflow_mode == "Full Workflow (All 6 Phases)":
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
        "M&A Prospecting Tool | Built for LexisNexis Sales Teams | December 2025"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
