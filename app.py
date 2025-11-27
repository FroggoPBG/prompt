import streamlit as st
import anthropic
import os

# Page config
st.set_page_config(
    page_title="OUS Discovery Tool",
    page_icon="🔍",
    layout="wide"
)

# Initialize Anthropic client
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Title and introduction
st.title("🔍 OUS Discovery Tool")
st.markdown("### Uncover client Outcomes, Understand their pains, and identify their Standards")

# Explanation section with expander
with st.expander("ℹ️ What is the OUS Framework?", expanded=False):
    st.markdown("""
    The **OUS Framework** helps you systematically research and understand potential clients:
    
    **O - Outcome**: The strategic business objectives and long-term goals the customer seeks to achieve
    - What does the customer want to accomplish?
    - What's their vision of success?
    - What are their growth targets and transformation goals?
    
    **U - Understanding Pain**: The identification and in-depth understanding of the customer's primary challenges
    - What problems keep them up at night?
    - What operational, financial, or regulatory challenges do they face?
    - What gaps exist in their current capabilities?
    
    **S - Standard**: The standards and requirements the customer uses to evaluate and compare potential solutions
    - What criteria drive their buying decisions?
    - What technical, compliance, or budget requirements must be met?
    - How do they measure success?
    
    ---
    
    **How to use this tool:**
    1. Enter the company website URL (required)
    2. Optionally paste any additional information you have
    3. Select our product that you're positioning
    4. Choose which OUS element to analyze (or run all three)
    5. Click "Analyze" to get structured insights
    """)

st.divider()

# Main input section
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Client Information")
    
    # Company website input
    company_url = st.text_input(
        "Company Website URL *",
        placeholder="https://www.example.com",
        help="The primary source for OUS analysis"
    )
    
    # Additional information textarea
    additional_info = st.text_area(
        "Additional Information (Optional)",
        placeholder="Paste any additional context: news articles, financial reports, LinkedIn insights, industry analysis, etc.",
        height=200,
        help="Any extra information you have about the client that's not on their website"
    )

with col2:
    st.subheader("🎯 Our Solution")
    
    # Product selection
    products = {
        "Lexis+": "https://www.lexisnexis.com/en-us/products/lexis-plus.page",
        "Practical Guidance": "https://www.lexisnexis.com/en-us/products/practical-guidance.page",
        "Lexis+ AI": "https://www.lexisnexis.com/en-us/products/lexisplus-ai.page",
        "CounselLink": "https://www.lexisnexis.com/en-us/products/enterprise-legal-management.page",
        "Lexis Smart Forms": "https://www.lexisnexis.com/en-us/products/lexis-smart-forms.page",
    }
    
    selected_product = st.selectbox(
        "Select Product *",
        options=list(products.keys()),
        help="Which LexisNexis product are you positioning?"
    )
    
    # Show product link
    if selected_product:
        st.markdown(f"[📎 {selected_product} Details]({products[selected_product]})")
    
    st.divider()
    
    # Analysis type selection
    st.subheader("🔬 Analysis Type")
    analysis_type = st.radio(
        "What to analyze:",
        options=[
            "Complete OUS Analysis",
            "Outcomes Only",
            "Understanding (Pains) Only",
            "Standards Only"
        ],
        help="Choose comprehensive analysis or focus on one element"
    )

st.divider()

# Analyze button
if st.button("🚀 Analyze Client", type="primary", use_container_width=True):
    
    # Validation
    if not company_url:
        st.error("⚠️ Please enter a company website URL")
    elif not selected_product:
        st.error("⚠️ Please select a product")
    else:
        # Build the prompt based on analysis type
        prompts = {
            "Outcomes Only": f"""You are a business analyst helping identify strategic objectives for a potential client.

TASK:
Visit and analyze the following company website, then identify their likely strategic business outcomes and long-term goals.

COMPANY WEBSITE:
{company_url}

ADDITIONAL INFORMATION PROVIDED:
{additional_info if additional_info else "None provided"}

WHAT TO LOOK FOR:
- About Us / Company Overview pages
- Investor Relations / Annual Reports
- Press Releases / News section
- Leadership messages / CEO letters
- Strategic initiatives / Future plans pages
- Product roadmap or service expansion announcements

ANALYSIS FRAMEWORK:
1. **Strategic Objectives**: What are their stated or implied top-level business goals for the next 1-3 years?
2. **Growth Targets**: What markets, products, or capabilities are they trying to expand?
3. **Transformation Goals**: Are they undergoing digital transformation, restructuring, market repositioning, or operational change?
4. **Competitive Positioning**: How are they trying to differentiate or defend their market position?
5. **Financial Outcomes**: What financial metrics or targets are they likely focused on?
6. **Risk Mitigation Goals**: What strategic risks are they trying to reduce or hedge against?

OUTPUT FORMAT:

**PRIMARY OUTCOMES** (top 2-3 strategic goals)
- [Outcome 1 with supporting evidence from website]
- [Outcome 2 with supporting evidence from website]

**SECONDARY OUTCOMES** (supporting goals)
- [List additional objectives]

**EVIDENCE SOURCES**
- List specific pages/sections where you found this information

**IMPLICATIONS FOR {selected_product}**
- How {selected_product} could support these outcomes
- Which outcomes align best with our value proposition

**INFORMATION GAPS**
- What key information wasn't available
- Additional sources we should check

CONSTRAINTS:
- Base analysis on provided website and information
- Quote or cite specific sections when possible
- Flag assumptions clearly
- If insufficient information, state what's missing""",

            "Understanding (Pains) Only": f"""You are a business analyst specializing in identifying organizational pain points and challenges.

TASK:
Visit and analyze the following company website, then identify their primary pain points, challenges, and operational friction.

COMPANY WEBSITE:
{company_url}

ADDITIONAL INFORMATION PROVIDED:
{additional_info if additional_info else "None provided"}

WHAT TO LOOK FOR:
- Challenges mentioned in About Us or Leadership messages
- Problems their products/services solve (implies they face these too)
- Investor Relations / Risk Factors sections
- News about restructuring, layoffs, market challenges
- Job postings (gaps in their team = pain points)
- Customer testimonials

ANALYSIS FRAMEWORK:
1. **Operational Pain Points**: What inefficiencies, bottlenecks, or process issues are they likely facing?
2. **Financial Pressure**: What financial challenges are evident?
3. **Regulatory/Compliance Risks**: What legal, compliance, or regulatory burdens are they managing?
4. **Market/Competitive Threats**: What external pressures threaten their business?
5. **Technology/Capability Gaps**: Where do they lack tools, systems, or expertise?
6. **Organizational/People Challenges**: Are there talent, culture, or structural issues?
7. **Reputational/Stakeholder Risks**: What threatens their reputation?

PRIORITIZATION:
Rank pain points by:
- **Severity**: How much does this impact their business?
- **Urgency**: How immediate is the threat?
- **Solvability**: Could {selected_product} address this pain?

OUTPUT FORMAT:

**CRITICAL PAINS** (most severe/urgent)
- [Pain point 1]: [Evidence + Impact + Urgency]
- [Pain point 2]: [Evidence + Impact + Urgency]

**MODERATE PAINS** (important but less urgent)
- [List with context]

**INFERRED PAINS** (reading between the lines)
- [What they don't say directly but is implied]

**EVIDENCE SOURCES**
- List specific pages/sections

**{selected_product} SOLUTION FIT**
- Which pains we can directly address
- Which pains are outside our scope
- Questions to validate these pains

**INFORMATION GAPS**
- What we couldn't determine
- Recommended additional research

CONSTRAINTS:
- Base analysis on provided information
- Distinguish explicit statements from inferences
- Cite specific sources
- Flag where additional discovery is needed""",

            "Standards Only": f"""You are a procurement and decision-analysis specialist helping understand how a client evaluates solutions.

TASK:
Visit and analyze the following company website, then identify the standards, criteria, and requirements they likely use to evaluate and compare potential solutions.

COMPANY WEBSITE:
{company_url}

ADDITIONAL INFORMATION PROVIDED:
{additional_info if additional_info else "None provided"}

WHAT TO LOOK FOR:
- Procurement/Vendor pages or policies
- Technology/Partner ecosystem pages
- Compliance/Certifications they hold
- Quality standards or industry memberships
- Case studies or vendor announcements
- Job postings (reveals their tech stack, requirements)
- Annual reports

ANALYSIS FRAMEWORK:
1. **Decision-Making Criteria**: What factors drive their buying decisions?
2. **Evaluation Process**: How do they evaluate vendors?
3. **Budget/Financial Standards**: What are their budget constraints, ROI expectations?
4. **Technical Requirements**: What technical standards, integrations must solutions meet?
5. **Compliance/Regulatory Standards**: What certifications are mandatory?
6. **Vendor Standards**: What do they expect from vendors?
7. **Internal Stakeholders**: Who influences or approves decisions?
8. **Success Metrics**: How will they measure if a solution is working?

OUTPUT FORMAT:

**MUST-HAVE STANDARDS** (non-negotiable requirements)
- [Standard 1]: [Evidence/Page where found]
- [Standard 2]: [Evidence/Page where found]

**IMPORTANT CRITERIA** (strong preferences)
- [List with context and source]

**INFERRED STANDARDS** (reading between the lines)
- What their industry, size, or values suggest

**EVALUATION PROCESS CLUES**
- Decision makers mentioned
- Procurement process hints
- Partner/vendor relationship approach

**EVIDENCE SOURCES**
- List specific pages analyzed

**{selected_product} ALIGNMENT**
- How we meet their standards
- Potential gaps or concerns
- Competitive positioning

**VALIDATION QUESTIONS**
- Questions to confirm these standards
- Information gaps to fill

**INFORMATION GAPS**
- What the website doesn't reveal
- Additional research needed

CONSTRAINTS:
- Base analysis on provided information
- Mark assumptions vs. facts
- Reference specific evidence
- Identify unknowns""",

            "Complete OUS Analysis": f"""You are a strategic account researcher conducting comprehensive client discovery.

TASK:
Visit and analyze the following company website, then provide a complete OUS assessment: their Outcomes, Understanding (pains), and Standards.

COMPANY WEBSITE:
{company_url}

ADDITIONAL INFORMATION PROVIDED:
{additional_info if additional_info else "None provided"}

RESEARCH CHECKLIST:
☐ Homepage / About Us
☐ Leadership team / CEO messages
☐ Investor Relations / Annual Reports / Press Releases
☐ Products/Services pages
☐ News / Blog
☐ Careers / Job Postings
☐ Partners / Technology ecosystem
☐ Case Studies / Customer Success
☐ Compliance / Certifications

PROVIDE:

## 1. OUTCOMES (Strategic Objectives)
**Primary Goals** (top 2-3 strategic outcomes based on website)
**Supporting Goals**
**Evidence** (cite specific pages/quotes)

## 2. UNDERSTANDING (Pain Points)
**Critical Pains** (most severe/urgent challenges)
**Moderate Pains**
**Inferred Pains** (reading between the lines)
**Evidence** (cite specific pages/quotes)

## 3. STANDARDS (Evaluation Criteria)
**Must-Have Requirements**
**Key Decision Criteria**
**Evaluation Process Clues**
**Evidence** (cite specific pages/quotes)

## 4. {selected_product} STRATEGIC POSITIONING
**Best Entry Point** (where to start the conversation)
**Value Proposition Alignment** (how we fit their OUS)
**Competitive Advantages** (why we're a good fit)
**Potential Objections** (concerns they might raise)

## 5. DISCOVERY & NEXT STEPS
**Discovery Questions** (what to ask to validate this analysis)
**Information Gaps** (what we don't know yet)
**Additional Research Needed** (LinkedIn, news, industry reports, etc.)

CONSTRAINTS:
- Start with the provided website as primary source
- Distinguish facts from inferences
- Cite specific pages for all claims
- Flag information gaps clearly
- Be specific, not generic"""
        }
        
        # Select the appropriate prompt
        selected_prompt = prompts[analysis_type]
        
        # Show spinner while processing
        with st.spinner(f"🔍 Analyzing {company_url}..."):
            try:
                # Call Claude API
                message = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=4096,
                    messages=[
                        {"role": "user", "content": selected_prompt}
                    ]
                )
                
                # Display results
                st.success("✅ Analysis Complete!")
                
                # Show the analysis in an expandable container
                with st.container():
                    st.markdown("### 📋 Analysis Results")
                    st.markdown(message.content[0].text)
                
                # Download button
                st.download_button(
                    label="💾 Download Analysis",
                    data=message.content[0].text,
                    file_name=f"OUS_Analysis_{company_url.replace('https://', '').replace('http://', '').replace('/', '_')}.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"❌ Error during analysis: {str(e)}")
                st.info("Please check your API key and try again.")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    <p>OUS Discovery Tool | Powered by Claude AI</p>
</div>
""", unsafe_allow_html=True)
