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
            additional_notes=data.get('additional_notes', '')
        )


class PromptRecipeManager:
    """Manages all prompt recipes for sales prospecting workflow"""
    
    @classmethod
    def generate_full_workflow(cls, context: ProspectContext) -> Dict[str, str]:
        """Generate all prompts for the complete workflow"""
        
        # Phase 1: Discovery
        def phase1_prompt():
            return f"""**Phase 1: Discovery & Compliance Research**

Research {context.company_name or 'the target company'} to understand:

1. **Business Model & Operations**
   - Core products/services
   - Revenue streams
   - Key business segments
   - Recent financial performance

2. **Regulatory Environment**
   - Industry-specific regulations
   - Compliance requirements
   - Recent regulatory changes
   - Outstanding compliance issues

3. **Market Position**
   - Competitive landscape
   - Market share
   - Growth trends
   - Strategic initiatives

Provide a comprehensive overview that will inform our engagement strategy."""

        # Phase 2: Buyer Psychological Profiling
        def phase2_prompt():
            return f"""**Phase 2: Buyer Psychological Profiling**

Analyze the decision-making psychology for this {context.transaction_type or 'transaction'}:

1. **Stakeholder Analysis**
   - Identify key decision-makers
   - Map influence and authority
   - Understand reporting structures

2. **Psychological Drivers**
   - Risk tolerance profile
   - Decision-making style (data-driven vs intuitive)
   - Priority concerns (cost, compliance, efficiency)
   - Personal motivations and career incentives

3. **Communication Preferences**
   - Preferred communication channels
   - Level of detail expected
   - Decision timeline and urgency

4. **Objection Anticipation**
   - Likely concerns or hesitations
   - Historical patterns in similar deals
   - Competitive alternatives they might consider"""

        # Phase 2.5: Solution Mapping
        def phase25_prompt():
            return f"""**Phase 2.5: Solution Mapping (Product-to-Pain Fit)**

Map our solutions to identified pain points:

1. **Pain Point Identification**
   - Current challenges in {context.industry_sector or 'their industry'}
   - Specific problems related to {context.transaction_type or 'this transaction type'}
   - Regulatory or compliance gaps

2. **Solution Mapping**
   - Which products/services address each pain point
   - Unique value propositions
   - Competitive advantages
   - ROI potential

3. **Prioritization**
   - Most critical pain points
   - Quick wins vs long-term value
   - Resource requirements

4. **Custom Approach**
   - Tailored solutions for their specific situation
   - Implementation considerations
   - Success metrics"""

        # Phase 3: Credibility-Based Email Drafting
        def phase3_prompt():
            return f"""**Phase 3: Credibility-Based Email Outreach**

Draft a compelling initial outreach email:

**Requirements:**
- Professional yet personable tone
- Reference specific insights about their company
- Clearly articulate value proposition
- Include relevant credentials/social proof
- Strong call-to-action

**Email Structure:**
1. Personalized opening (reference recent news/achievement)
2. Brief value proposition (2-3 sentences)
3. Specific benefit relevant to their situation
4. Soft CTA (meeting request or exploratory call)
5. Professional signature

Keep it concise (under 150 words) and focused on their needs."""

        # Phase 4: Sales Executive Summary
        def phase4_prompt():
            return f"""**Phase 4: Sales Executive Summary**

Create a brief (90-second read) executive summary:

**Include:**
1. **Opportunity Overview**
   - Company profile
   - Transaction details
   - Potential deal size

2. **Key Insights**
   - Critical pain points
   - Decision-maker profile
   - Timing and urgency

3. **Recommended Approach**
   - Primary value propositions
   - Suggested solutions
   - Differentiation strategy

4. **Next Steps**
   - Immediate actions
   - Resource requirements
   - Timeline

Format for quick executive review."""

        # Phase 5: OUS Framework Analysis
        def phase5_prompt():
            return f"""**Phase 5: OUS Framework Analysis**

Analyze this opportunity using the **Opportunity, Urgency, Success** framework:

**OPPORTUNITY**
- Market size and growth potential
- Strategic fit with our capabilities
- Competitive landscape
- Deal structure and pricing potential

**URGENCY**
- Time-sensitive factors (regulatory deadlines, market changes)
- Competitive pressure
- Internal drivers (fiscal year, leadership changes)
- Risk of status quo

**SUCCESS Probability**
- Strength of relationships
- Budget availability
- Decision-making authority clarity
- Solution fit
- Competitive position
- Implementation feasibility

**Scoring:** Rate each dimension (1-10) and provide overall assessment.
**Recommendation:** Pursue aggressively, nurture, or deprioritize?"""

        # Phase 6: Qualification
        def phase6_prompt():
            return f"""**Phase 6: Deal Qualification (BANT+ Framework)**

Assess this opportunity against qualification criteria:

**BUDGET**
- Estimated budget range
- Budget approval process
- Funding source
- Financial constraints

**AUTHORITY**
- Economic buyer identified?
- Technical buyer and influencers
- Procurement involvement
- Decision-making process

**NEED**
- Business pain severity (1-10)
- Impact of not solving
- Alternative solutions considered
- Our solution fit

**TIMELINE**
- Decision timeline
- Implementation window
- Critical deadlines
- Potential delays

**ADDITIONAL FACTORS**
- Competition level
- Political landscape
- Technical requirements
- Legal/compliance considerations

**Recommendation:** Qualified/Not Qualified and priority level (A/B/C)."""

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
