"""Legal Tech Sales Prospecting Tool - Main Streamlit App."""
from __future__ import annotations

from datetime import datetime

import streamlit as st

from components.presets import export_preset_bytes, load_preset_into_state
from components.recipes import PromptRecipeManager, PromptRecipe, ProspectContext
from components.writing_checker import check_plain_english, get_writing_tips

# ==================== PAGE CONFIG ====================

st.set_page_config(
    page_title="Legal Tech Sales Prospecting - OUS Framework",
    page_icon="⚖️",
    layout="wide",
)

# ==================== CUSTOM CSS ====================

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #6b7280;
        margin-bottom: 2rem;
    }
    .stAlert {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .insight-box {
        background-color: #f0f9ff;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.375rem;
    }
    .warning-box {
        background-color: #fef3c7;
        border-left: 4px solid #f59e0b;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.375rem;
    }
    .success-box {
        background-color: #d1fae5;
        border-left: 4px solid #10b981;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.375rem;
    }
</style>
""", unsafe_allow_html=True)

# ==================== HELPER FUNCTIONS ====================

def generate_insight_driven_emails(context: ProspectContext) -> dict[str, str]:
    """
    Generate three styles of insight-driven emails.
    
    Args:
        context: The prospect research context
        
    Returns:
        Dictionary with three email templates
    """
    trigger = context.trigger_event
    outcome = context.outcome
    unspoken = context.unspoken_concern
    
    # Extract company hint if available
    company_hint = ""
    if "IPO" in trigger or "filing" in trigger.lower():
        company_hint = "firm going public"
    elif "expansion" in trigger.lower():
        company_hint = "firm expanding regionally"
    elif "hire" in trigger.lower() or "hired" in trigger.lower():
        company_hint = "growing firm"
    else:
        company_hint = "firm in your situation"
    
    # TEMPLATE 1: Contrarian Insight Opener
    email_contrarian = f"""Subject: The hidden risk in {trigger[:50]}...

Hi [Name],

I saw {trigger}. Congrats - most firms underestimate how complex that actually is.

Here's what we've learned from helping similar firms through this: {unspoken} is the part that surprises everyone. Most people focus on {outcome}, but the real bottleneck is usually something else entirely.

Quick example: One HK firm we worked with thought they needed better contract review. Turns out they needed better handoff protocols between associates and partners - which cut their M&A close time by 30%.

Worth a 15-minute call to see if you're facing something similar?

I'm free Tues/Wed this week at 10am HKT or 3pm HKT.

Best,
[Your name]

P.S. - If timing's off, I wrote a quick guide on "{unspoken[:40]}..." that might be useful. Happy to send it your way.
"""

    # TEMPLATE 2: Peer Advisor Approach
    email_peer = f"""Subject: Question about {trigger[:50]}...

Hi [Name],

Quick question (not a pitch, promise):

When you're dealing with {trigger}, how are you currently handling {unspoken}?

The reason I ask: We work with {company_hint} going through similar situations, and that's the part that tends to create the most headaches. Most firms think {outcome} is the priority, but in practice, {unspoken} is what actually slows things down.

Does that resonate with your situation?

If it's useful, I can share what we've seen work (and what doesn't). 15 minutes, your call.

Free this week: Tues 10am or Wed 3pm HKT.

Best,
[Your name]
"""

    # TEMPLATE 3: Specific Timeline Hook
    email_timeline = f"""Subject: Quick thought on your timeline

Hi [Name],

I saw {trigger} - based on the typical timeline for this, that means {outcome} needs to happen relatively soon.

Here's the part that usually gets overlooked: {unspoken}.

We've worked with {company_hint}, and this is where things tend to go sideways. Not because teams aren't capable, but because this specific issue often isn't on the radar until it's already creating delays.

One example: A similar firm thought they had plenty of time for their regulatory process, but the back-and-forth on compliance controls ate up 3 weeks they didn't plan for.

Worth a quick conversation to see if you're set up differently?

I have 15 minutes open this week: Tuesday at 10am HKT or Wednesday at 3pm HKT.

Best,
[Your name]

P.S. - Even if this isn't the right time, I'd be happy to intro you to a peer contact who just went through this exact process.
"""

    return {
        "contrarian": email_contrarian,
        "peer_advisor": email_peer,
        "timeline_hook": email_timeline
    }


# ==================== MAIN APP ====================

def main():
    """Main application logic."""
    
    # Header
    st.markdown('<div class="main-header">⚖️ Legal Tech Sales Prospecting Tool</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">OUS Framework: Turn Research into Insight-Driven Outreach</div>', unsafe_allow_html=True)
    
    # ==================== SIDEBAR ====================
    
    with st.sidebar:
        st.header("🎯 Quick Actions")
        
        # Initialize recipe manager
        recipe_manager = PromptRecipeManager()
        
        # Recipe selection
        st.subheader("Select Prospect Type")
        
        # Get recipe options safely
        try:
            recipe_ids = list(recipe_manager.recipes.keys())
            recipe_names = [recipe_manager.recipes[rid].display_name for rid in recipe_ids]
            
            selected_index = st.selectbox(
                "Choose a recipe:",
                options=range(len(recipe_ids)),
                format_func=lambda i: recipe_names[i],
                help="Select the type of prospect you're researching"
            )
            
            selected_recipe = recipe_ids[selected_index]
            recipe = recipe_manager.recipes[selected_recipe]
            
        except Exception as e:
            st.error(f"Error loading recipes: {e}")
            st.stop()
        
        st.markdown("---")
        
        # Preset management
        st.subheader("💾 Presets")
        
        # Save preset
        preset_name = st.text_input(
            "Save current analysis as:",
            placeholder="e.g., Acme Corp - IPO Research"
        )
        
        if st.button("💾 Save Preset", use_container_width=True):
            if preset_name and st.session_state.get('trigger_event'):
                preset_data = {
                    'recipe_id': selected_recipe,
                    'trigger_event': st.session_state.trigger_event,
                    'outcome': st.session_state.outcome,
                    'unspoken_concern': st.session_state.unspoken_concern,
                    'solution_angle': st.session_state.solution_angle,
                    'saved_at': datetime.now().isoformat()
                }
                
                # Initialize presets in session state if needed
                if 'saved_presets' not in st.session_state:
                    st.session_state.saved_presets = {}
                
                st.session_state.saved_presets[preset_name] = preset_data
                st.success(f"✅ Saved: {preset_name}")
            else:
                st.warning("⚠️ Please complete the OUS Framework first")
        
        # Load preset
        if st.session_state.get('saved_presets'):
            st.markdown("**Load a preset:**")
            preset_to_load = st.selectbox(
                "Saved presets:",
                options=list(st.session_state.saved_presets.keys()),
                key="preset_selector"
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("📂 Load", use_container_width=True):
                    load_preset_into_state(st.session_state.saved_presets[preset_to_load])
                    st.success("✅ Preset loaded!")
                    st.rerun()
            
            with col2:
                if st.button("📥 Export", use_container_width=True):
                    preset_bytes = export_preset_bytes(st.session_state.saved_presets[preset_to_load])
                    st.download_button(
                        label="Download",
                        data=preset_bytes,
                        file_name=f"{preset_to_load.replace(' ', '_')}.json",
                        mime="application/json",
                        use_container_width=True
                    )
        
        st.markdown("---")
        
        # Help section
        with st.expander("ℹ️ How This Works"):
            st.markdown("""
            **The OUS Framework:**
            
            1. **Outcome**: What they want to achieve
            2. **Unspoken**: The real concern they won't say
            3. **Solution**: How you address the unspoken need
            
            **Why it works:**
            - Focuses on insight, not features
            - Addresses real concerns, not surface goals
            - Positions you as advisor, not vendor
            """)
    
    # ==================== MAIN CONTENT AREA ====================
    
    # Display selected recipe info
    st.info(f"**{recipe.display_name}** - {recipe.description}")
    
    with st.expander("📋 See the Prompt Recipe"):
        st.code(recipe.get_full_prompt(), language="markdown")
    
    st.markdown("---")
    
    # ==================== OUS FRAMEWORK INPUTS ====================
    
    st.header("🎯 OUS Framework Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔍 Research Inputs")
        
        trigger_event = st.text_area(
            "**Trigger Event** (What happened?)",
            value=st.session_state.get('trigger_event', ''),
            placeholder=recipe.example_inputs['trigger_event'],
            help="What recent event or change made this prospect worth reaching out to now?",
            height=100,
            key='trigger_event'
        )
        
        outcome = st.text_area(
            "**Outcome** (What do they want?)",
            value=st.session_state.get('outcome', ''),
            placeholder=recipe.example_inputs['outcome'],
            help="What is their stated goal or desired outcome?",
            height=100,
            key='outcome'
        )
    
    with col2:
        st.subheader("💡 Insight Development")
        
        unspoken_concern = st.text_area(
            "**Unspoken Concern** (What are they worried about?)",
            value=st.session_state.get('unspoken_concern', ''),
            placeholder=recipe.example_inputs['unspoken_concern'],
            help="What's the real concern they won't say out loud?",
            height=100,
            key='unspoken_concern'
        )
        
        solution_angle = st.text_area(
            "**Solution Angle** (How do you help?)",
            value=st.session_state.get('solution_angle', ''),
            placeholder=recipe.example_inputs['solution_angle'],
            help="How does your solution address their unspoken concern?",
            height=100,
            key='solution_angle'
        )
    
    # Validate all fields are filled
    all_filled = all([trigger_event, outcome, unspoken_concern, solution_angle])
    
    if not all_filled:
        st.warning("⚠️ Fill in all four fields above to generate email templates")
        st.stop()
    
    # Create ProspectContext
    context = ProspectContext(
        trigger_event=trigger_event,
        outcome=outcome,
        unspoken_concern=unspoken_concern,
        solution_angle=solution_angle
    )
    
    # ==================== OUS SUMMARY ====================
    
    st.markdown("---")
    st.header("📊 OUS Framework Summary")
    
    summary_col1, summary_col2, summary_col3 = st.columns(3)
    
    with summary_col1:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown("**🎯 OUTCOME**")
        st.markdown(f"*What they want:*")
        st.markdown(f"{outcome}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with summary_col2:
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("**🤔 UNSPOKEN**")
        st.markdown(f"*What they're worried about:*")
        st.markdown(f"{unspoken_concern}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with summary_col3:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("**✅ SOLUTION**")
        st.markdown(f"*How you help:*")
        st.markdown(f"{solution_angle}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # ==================== EMAIL TEMPLATES (NEW INSIGHT-DRIVEN) ====================
    
    st.markdown("---")
    st.header("📧 Insight-Driven Email Templates")
    
    st.info("""
    **Why these work better:**
    - ✅ Lead with insight, not features
    - ✅ Use specific details from your research
    - ✅ Frame you as a peer advisor, not a vendor
    - ✅ Clear, low-friction call to action
    """)
    
    # Generate three different email styles
    emails = generate_insight_driven_emails(context)
    
    # Tab interface for different email styles
    tab1, tab2, tab3 = st.tabs([
        "🔥 Contrarian Insight", 
        "🤝 Peer Advisor",
        "⏰ Timeline Hook"
    ])
    
    with tab1:
        st.markdown("**Best for:** Sophisticated prospects who are skeptical of typical sales pitches")
        st.text_area(
            "Email Template - Contrarian Insight:",
            value=emails["contrarian"],
            height=400,
            key="email_contrarian_display"
        )
        
        # Writing check
        analysis = check_plain_english(emails["contrarian"])
        grade_label, grade_emoji = analysis.grade_info
        
        st.metric(
            label="Plain English Score",
            value=f"{analysis.score}/100",
            delta=grade_label
        )
        
        if analysis.has_issues:
            with st.expander("⚠️ See Writing Suggestions"):
                if analysis.zombie_words:
                    st.markdown("**Zombie Words Found:**")
                    for issue in analysis.zombie_words:
                        st.markdown(f"- Replace '{issue.text}' → '{issue.suggestion}'")
                
                if analysis.passive_voice:
                    st.markdown("**Passive Voice Found:**")
                    for issue in analysis.passive_voice[:3]:  # Show first 3
                        st.markdown(f"- {issue.suggestion}")
    
    with tab2:
        st.markdown("**Best for:** Building trust with new contacts or warm introductions")
        st.text_area(
            "Email Template - Peer Advisor:",
            value=emails["peer_advisor"],
            height=400,
            key="email_peer_display"
        )
        
        # Writing check
        analysis = check_plain_english(emails["peer_advisor"])
        grade_label, grade_emoji = analysis.grade_info
        
        st.metric(
            label="Plain English Score",
            value=f"{analysis.score}/100",
            delta=grade_label
        )
        
        if analysis.has_issues:
            with st.expander("⚠️ See Writing Suggestions"):
                if analysis.zombie_words:
                    st.markdown("**Zombie Words Found:**")
                    for issue in analysis.zombie_words:
                        st.markdown(f"- Replace '{issue.text}' → '{issue.suggestion}'")
                
                if analysis.passive_voice:
                    st.markdown("**Passive Voice Found:**")
                    for issue in analysis.passive_voice[:3]:
                        st.markdown(f"- {issue.suggestion}")
    
    with tab3:
        st.markdown("**Best for:** Prospects with clear deadlines or time-sensitive trigger events")
        st.text_area(
            "Email Template - Timeline Hook:",
            value=emails["timeline_hook"],
            height=400,
            key="email_timeline_display"
        )
        
        # Writing check
        analysis = check_plain_english(emails["timeline_hook"])
        grade_label, grade_emoji = analysis.grade_info
        
        st.metric(
            label="Plain English Score",
            value=f"{analysis.score}/100",
            delta=grade_label
        )
        
        if analysis.has_issues:
            with st.expander("⚠️ See Writing Suggestions"):
                if analysis.zombie_words:
                    st.markdown("**Zombie Words Found:**")
                    for issue in analysis.zombie_words:
                        st.markdown(f"- Replace '{issue.text}' → '{issue.suggestion}'")
                
                if analysis.passive_voice:
                    st.markdown("**Passive Voice Found:**")
                    for issue in analysis.passive_voice[:3]:
                        st.markdown(f"- {issue.suggestion}")
    
    # ==================== CUSTOMIZATION GUIDE ====================
    
    with st.expander("✍️ How to Customize These Templates"):
        st.markdown("""
        ### Make It Your Own:

        **1. Replace [bracketed placeholders]:**
        - `[Name]` = Their actual first name (use LinkedIn)
        - `[Your name]` = Your actual name and title
        - Dates/times = Actual calendar slots you have open

        **2. Add specific numbers:**
        - Instead of: "This usually creates issues"
        - Use: "We've seen this add 3-4 weeks to timelines in 60% of cases"

        **3. Include a micro-case study:**
        - "One firm in Singapore faced X, solved it with Y, got Z result"
        - Be specific but protect client confidentiality

        **4. Personalize the P.S.:**
        - Offer a specific resource (guide, intro, data point)
        - Makes the email valuable even if they say no
        - Example: "P.S. - I wrote a guide on [unspoken concern] for HK firms. Want me to send it?"

        **5. The subject line test:**
        - Would YOU click on this subject line?
        - If not, make it more specific or controversial
        - Good: "The hidden risk in HKEX filings"
        - Bad: "Following up" or "Quick question"

        ### The Fill-In-The-Blank Checklist:

        Before sending, make sure you've:
        - [ ] Replaced ALL [bracketed text] with real details
        - [ ] Added at least one specific number or statistic
        - [ ] Referenced their actual trigger event (not generic)
        - [ ] Included exact meeting times (not "sometime this week")
        - [ ] Made the P.S. valuable on its own
        - [ ] Checked that you sound like a peer, not a vendor
        """)
    
    # ==================== WRITING TIPS ====================
    
    st.markdown("---")
    
    with st.expander("📚 Plain English Writing Guide"):
        st.markdown(get_writing_tips())
    
    # ==================== FOOTER ====================
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6b7280; padding: 2rem 0;'>
        <p><strong>OUS Framework</strong> - Outcome, Unspoken Concern, Solution</p>
        <p style='font-size: 0.875rem;'>Stop selling features. Start teaching insights.</p>
    </div>
    """, unsafe_allow_html=True)


# ==================== RUN APP ====================

if __name__ == "__main__":
    main()
