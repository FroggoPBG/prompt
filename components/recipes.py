from typing import Dict, Optional, Callable

class ProspectContext:
    """Context object containing all prospect information for prompt generation"""
    
    def __init__(
        self,
        company_name: str = "",
        industry_sector: str = "",
        transaction_type: str = "",
        legal_entity_type: str = "",
        transaction_size: str = "",
        geographic_scope: str = "",
        deal_context: str = "",
        additional_notes: str = "",
        company_products: str = ""
    ):
        self.company_name = company_name
        self.industry_sector = industry_sector
        self.transaction_type = transaction_type
        self.legal_entity_type = legal_entity_type
        self.transaction_size = transaction_size
        self.geographic_scope = geographic_scope
        self.deal_context = deal_context
        self.additional_notes = additional_notes
        self.company_products = company_products
    
    def to_prompt_header(self) -> str:
        """Convert context to formatted header for prompts"""
        header_parts = []
        
        if self.company_name:
            header_parts.append(f"**Company:** {self.company_name}")
        if self.industry_sector:
            header_parts.append(f"**Industry:** {self.industry_sector}")
        if self.transaction_type:
            header_parts.append(f"**Transaction Type:** {self.transaction_type}")
        if self.legal_entity_type:
            header_parts.append(f"**Legal Entity:** {self.legal_entity_type}")
        if self.transaction_size:
            header_parts.append(f"**Transaction Size:** {self.transaction_size}")
        if self.geographic_scope:
            header_parts.append(f"**Geographic Scope:** {self.geographic_scope}")
        if self.deal_context:
            header_parts.append(f"**Deal Context:** {self.deal_context}")
        if self.company_products:
            header_parts.append(f"\n**Our Products/Services:**\n{self.company_products}")
        if self.additional_notes:
            header_parts.append(f"**Additional Notes:** {self.additional_notes}")
        
        header = "\n".join(header_parts) if header_parts else "**General Sales Prospecting Context**"
        header += "\n\n---\n\n"
        
        return header
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ProspectContext':
        """Create ProspectContext from dictionary"""
        return cls(
            company_name=data.get('company_name', ''),
            industry_sector=data.get('industry_sector', ''),
            transaction_type=data.get('transaction_type', ''),
            legal_entity_type=data.get('legal_entity_type', ''),
            transaction_size=data.get('transaction_size', ''),
            geographic_scope=data.get('geographic_scope', ''),
            deal_context=data.get('deal_context', ''),
            additional_notes=data.get('additional_notes', ''),
            company_products=data.get('company_products', '')
        )


class PromptRecipeManager:
    """Manages all prompt recipes for sales prospecting workflow"""
    
    @classmethod
    def generate_full_workflow(cls, context: ProspectContext) -> Dict[str, str]:
        """Generate all prompts for the complete workflow"""
        
        # Phase 1: Discovery
        def phase1_prompt():
            return f"""**Phase 1: Discovery & Compliance Research**

Research {context.company_name or 'the target company'} to inform our engagement strategy:

1. **Business Model & Operations**
   - Core practice areas and service offerings
   - Client profile (industries, company sizes, geographic focus)
   - Firm structure (partnership size, office locations, headcount trends)
   - Indicators of firm health (ranking movements, lateral hires, office changes)

2. **Technology & Operations Posture**
   - Known technology investments or innovation initiatives
   - Legal operations function (if any)
   - Public statements about efficiency, AI, or modernization
   - Any technology partnerships or vendor relationships mentioned publicly

3. **Regulatory Environment**
   - Regulations governing the firm itself (Law Society, AML, data privacy)
   - Regulations they advise clients on (indicates expertise and client needs)
   - Recent regulatory developments affecting their practice areas

4. **Market Position**
   - Competitive positioning versus peer firms
   - Directory rankings and recognition trends
   - Strategic initiatives or stated growth priorities

**For each section, distinguish clearly between verified facts (with sources) and reasonable inferences.**"""

        # Phase 2: Buyer Psychological Profiling
        def phase2_prompt():
            return f"""**Phase 2: Decision-Making Dynamics Analysis**

Analyze typical decision-making dynamics for a firm like {context.company_name or 'this firm'} when evaluating {context.company_products or 'our solutions'}:

1. **Stakeholder Mapping**
   - Likely decision-making roles (who typically holds authority for this purchase type)
   - Probable influencers and gatekeepers
   - How decisions typically flow in firms of this size and structure

2. **Decision-Making Characteristics (Hypotheses to Validate)**
   - Typical risk tolerance for this firm profile
   - Expected decision-making style (consensus vs. top-down, data-driven vs. relationship-driven)
   - Priority concerns likely given their practice mix and market position
   - Cultural and regional factors affecting how they evaluate vendors

3. **Communication Expectations**
   - Appropriate channels for initial outreach
   - Level of formality expected
   - How firms like this typically structure evaluation processes
   - Expected timeline for this type of purchase

4. **Objection Mapping**
   - Likely concerns based on firm profile and product category
   - Common hesitations from similar firms in past deals
   - Competitive alternatives they're probably aware of

**Note: These are working hypotheses based on firm type and market context. Validate and refine through actual conversations.**"""

        # Phase 2.5: Solution Mapping
        def phase25_prompt():
            return f"""**Phase 2.5: Solution Mapping (Product-to-Pain Fit)**

Map our solutions to identified pain points for {context.company_name or 'this firm'}:

1. **Pain Point Identification**
   - Current challenges in {context.industry_sector or 'their industry'}
   - Specific problems related to {context.transaction_type or 'this transaction type'}
   - Regulatory or compliance gaps
   - Operational inefficiencies based on their profile

2. **Solution Mapping**
   - Which of our products/services address each pain point
   - Unique value propositions for their specific situation
   - Competitive advantages over alternatives they might consider
   - Quantifiable ROI potential

3. **Prioritization**
   - Most critical pain points to address
   - Quick wins vs long-term value
   - Resource requirements and implementation complexity

4. **Custom Approach**
   - Tailored solutions for their specific situation
   - Implementation considerations given their structure
   - Success metrics relevant to their priorities"""

        # Phase 3: Credibility-Based Email Drafting
        def phase3_prompt():
            return f"""**Phase 3: Credibility-Based Email Outreach**

Draft a compelling initial outreach email for {context.company_name or 'this prospect'}:

**Requirements:**
- Professional yet personable tone
- Reference specific insights about their firm
- Clearly articulate value proposition
- Include relevant credentials/social proof
- Strong but soft call-to-action

**Email Structure:**
1. Personalized opening (reference recent news/achievement/insight from research)
2. Brief value proposition (2-3 sentences max)
3. Specific benefit relevant to their situation
4. Soft CTA (exploratory call or meeting request)
5. Professional signature

**Constraints:**
- Keep under 150 words
- Focus on their needs, not our features
- Avoid generic sales language
- Make it easy to say yes"""

        # Phase 4: Sales Executive Summary
        def phase4_prompt():
            return f"""**Phase 4: Sales Executive Summary**

Create a brief (90-second read) executive summary for {context.company_name or 'this opportunity'}:

**Include:**
1. **Opportunity Overview**
   - Firm profile and key characteristics
   - Transaction/engagement details
   - Potential deal size and scope

2. **Key Insights**
   - Critical pain points identified
   - Decision-maker profile and dynamics
   - Timing and urgency factors

3. **Recommended Approach**
   - Primary value propositions to emphasize
   - Suggested solutions/products
   - Differentiation strategy vs. competitors

4. **Next Steps**
   - Immediate actions required
   - Resource requirements
   - Proposed timeline

**Format for quick executive review - bullet points, no fluff.**"""

        # Phase 5: OUS Framework Analysis
        def phase5_prompt():
            return f"""**Phase 5: OUS Framework Analysis**

Analyze this opportunity using the **Opportunity, Urgency, Success** framework:

**OPPORTUNITY**
- Market size and growth potential for {context.industry_sector or 'this sector'}
- Strategic fit with our capabilities
- Competitive landscape and positioning
- Deal structure and pricing potential
- Expansion potential (upsell/cross-sell)

**URGENCY**
- Time-sensitive factors (regulatory deadlines, market changes)
- Competitive pressure or threats
- Internal drivers (fiscal year, leadership changes, growth targets)
- Cost of maintaining status quo
- Current pain severity

**SUCCESS Probability**
- Strength of relationships and access
- Budget availability indicators
- Decision-making authority clarity
- Solution-problem fit quality
- Competitive position strength
- Implementation feasibility
- Cultural/organizational fit

**Scoring:** Rate each dimension (1-10) with brief justification.
**Overall Assessment:** Calculate weighted score.
**Recommendation:** Pursue aggressively, nurture and develop, or deprioritize?"""

        # Phase 6: Qualification
        def phase6_prompt():
            return f"""**Phase 6: Deal Qualification (BANT+ Framework)**

Assess this opportunity against qualification criteria:

**BUDGET**
- Estimated budget range for {context.transaction_type or 'this type of engagement'}
- Budget approval process at firms like this
- Likely funding source
- Financial constraints or considerations

**AUTHORITY**
- Economic buyer likely identified? (role/title)
- Technical buyer and key influencers
- Procurement involvement expected?
- Decision-making process (committee vs. individual)

**NEED**
- Business pain severity (1-10 scale)
- Impact of not solving (quantify if possible)
- Alternative solutions they might consider
- Our solution fit quality (1-10)

**TIMELINE**
- Expected decision timeline
- Implementation window
- Critical deadlines driving urgency
- Potential delays or obstacles

**ADDITIONAL FACTORS**
- Known competition for this deal
- Political/relationship landscape
- Technical requirements or constraints
- Legal/compliance considerations
- Cultural fit with our solution

**QUALIFICATION DECISION:**
- Status: Qualified / Conditionally Qualified / Not Qualified
- Priority Level: A (hot) / B (warm) / C (cold)
- Key gaps to address before advancing
- Recommended next actions"""

        # Build the prompts dictionary
        header = context.to_prompt_header()
        
        prompts = {
            "phase1": header + "\n\n" + phase1_prompt(),
            "phase2": header + "\n\n" + phase2_prompt(),
            "phase25": header + "\n\n" + phase25_prompt(),
            "phase3": header + "\n\n" + phase3_prompt(),
            "phase4": header + "\n\n" + phase4_prompt(),
            "phase5": header + "\n\n" + phase5_prompt(),
            "phase6": header + "\n\n" + phase6_prompt()
        }
        
        return prompts
    
    @classmethod
    def get_individual_prompt(cls, phase: str, context: ProspectContext) -> str:
        """Get a single prompt by phase name"""
        all_prompts = cls.generate_full_workflow(context)
        return all_prompts.get(phase, "")
