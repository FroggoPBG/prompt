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

        # Phase 2: Decision-Making Dynamics
        def phase2_prompt():
            return f"""**Phase 2: Decision-Making Dynamics Analysis**

Analyze typical decision-making dynamics for a firm like {context.company_name or 'this firm'} when evaluating {context.company_products or 'solutions in this category'}:

1. **Stakeholder Mapping**
   - Likely decision-making roles (who typically holds authority for this purchase type)
   - Probable influencers and gatekeepers
   - How decisions typically flow in firms of this size and structure

2. **Decision-Making Characteristics (Hypotheses to Validate)**
   - Typical risk tolerance for this firm profile
   - Expected decision-making style (consensus vs. top-down, data-driven vs. relationship-driven)
   - Priority concerns likely given their practice mix and market position
   - Cultural and regional factors affecting how they evaluate vendors (e.g., Hong Kong: partner hierarchy, face considerations, relationship-driven BD)

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
            return f"""**Phase 2.5: Pain Point Hypothesis & Solution Mapping**

**Part A: Pain Point Hypothesis**

Based on {context.company_name or 'the firm'}'s profile, practice areas, and market position, identify likely operational challenges:

1. **Workflow Pain Points**
   - Where does this type of firm typically experience inefficiency?
   - What manual processes consume disproportionate time?
   - Where do quality or speed issues affect client delivery?

2. **Competitive Pressures**
   - How are firms like this being squeezed by larger or more tech-enabled competitors?
   - What client expectations are hardest for them to meet?

3. **Regulatory & Compliance Burden**
   - Which compliance requirements create ongoing operational friction?
   - Where is regulatory change creating new demands?

4. **Resource Constraints**
   - What limitations come from their mid-tier size?
   - Where are they likely stretched thin?

**Rank pain points by probable severity and urgency.**

---

**Part B: Solution Mapping**

For each identified pain point above, map to our capabilities:

- Which of our specific products/services addresses this pain point?
- What's our differentiation versus alternatives they might consider?
- What evidence (case studies, metrics, references) supports our claim?
- What would measurable success look like for them?
- What's the implementation complexity?

**Note: These are hypothesized pain points. Create discovery questions to validate in first conversation.**"""

        # Phase 3: Credibility-Based Email Drafting
        def phase3_prompt():
            return f"""**Phase 3: Credibility-Based Email Outreach**

Draft initial outreach emails for {context.company_name or 'the target firm'}, customized for different stakeholder types.

**Context:**
- We sell: {context.company_products or '[brief product description]'}
- Primary value: [one sentence on core benefit]

**Version A: Senior Partner / Managing Partner**
- **Tone:** Peer-to-peer, respectful of their expertise and time
- **Hook:** Reference their practice strength, directory ranking, or a market trend affecting their work (if no recent news, use these fallbacks)
- **Value prop:** Focus on client delivery and competitive positioning
- **CTA:** Suggest a brief conversation, not a demo
- **Avoid:** Jargon, making it about us, asking for too much too soon

**Version B: Senior Associate / Team Lead**
- **Tone:** Collegial, empathetic to workload pressures
- **Hook:** Reference a practical challenge in their practice area
- **Value prop:** Focus on time savings and reduced friction
- **CTA:** Offer to show how it works in their context
- **Avoid:** Over-promising, feature dumping, generic pain points

**Requirements for All Versions:**
- Under 150 words each
- No buzzwords or vendor-speak
- Specific to their situation (not a template that could go to any law firm)
- One clear ask, not multiple options
- Make it easy to say yes"""

        # Phase 4: Sales Executive Summary
        def phase4_prompt():
            return f"""**Phase 4: Sales Executive Summary**

Create a 90-second executive summary for the {context.company_name or 'this'} opportunity:

1. **Account Snapshot**
   - Firm profile (size, practice focus, positioning)
   - Why they're a fit for us
   - **Estimated** deal size (state assumptions clearly)

2. **Strategic Rationale**
   - Top 2-3 pain points we can likely address
   - Why now (urgency factors, if any)
   - Decision-maker profile (**Known:** [facts] / **Assumed:** [inferences])

3. **Recommended Approach**
   - Lead practice area or use case to emphasize
   - Primary value message for this firm
   - How we differentiate versus likely alternatives

4. **Key Unknowns & Risks**
   - What don't we know yet that could change the picture?
   - What could derail this opportunity?
   - What needs validation in first conversation?

5. **Next Steps**
   - Immediate actions with owners
   - Target timeline to first meeting
   - Required resources

**Format for quick scanning—use bullets, keep sections tight. No fluff.**"""

       # Phase 5: OUS Framework Analysis (CORRECTED)
def phase5_prompt():
    return f"""**Phase 5: OUS Framework Analysis**

Analyze this opportunity using the OUS framework. **For each score (1-10), provide specific evidence or reasoning.**

**OUTCOME (weight: 35%)**
*Strategic objectives and long-term goals the customer seeks to achieve*

- Strategic goals this solution would support (efficiency, growth, compliance, etc.): **Score:** ___ / **Evidence:**
- Alignment with firm's stated priorities or strategic initiatives: **Score:** ___ / **Evidence:**
- Long-term value potential beyond immediate problem-solving: **Score:** ___ / **Evidence:**
- Executive visibility and sponsorship potential: **Score:** ___ / **Evidence:**

**Outcome Subscore:** ___ / 10

---

**UNDERSTANDING PAIN (weight: 35%)**
*Identification and in-depth understanding of the customer's primary challenges*

- Severity of pain points we can address (1=minor annoyance, 10=critical): **Score:** ___ / **Evidence:**
- Cost of status quo (wasted time, lost revenue, compliance risk): **Score:** ___ / **Evidence:**
- Urgency/time pressure to solve this pain: **Score:** ___ / **Evidence:**
- Our ability to articulate their pain better than they can: **Score:** ___ / **Evidence:**

**Understanding Pain Subscore:** ___ / 10

---

**SELECTION PROCESS (weight: 30%)**
*Standards and requirements the customer uses to evaluate solutions*

- Clarity on their evaluation criteria and process: **Score:** ___ / **Evidence:**
- Our competitive positioning against their requirements: **Score:** ___ / **Evidence:**
- Decision-maker access and influence: **Score:** ___ / **Evidence:**
- Budget availability and approval process: **Score:** ___ / **Evidence:**
- Technical/compliance requirements we can meet: **Score:** ___ / **Evidence:**

**Selection Process Subscore:** ___ / 10

---

**OVERALL OUS SCORE CALCULATION:**
