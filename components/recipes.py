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

        # Phase 5: OUS Framework Analysis
        def phase5_prompt():
            return f"""**Phase 5: OUS Framework Analysis**

Analyze this opportunity using the OUS framework. **For each score (1-10), provide specific evidence or reasoning.**

**OPPORTUNITY (weight: 40%)**
- Deal size potential for {context.industry_sector or 'this sector'} (with stated assumptions): **Score:** ___ / **Evidence:**
- Strategic fit with our capabilities: **Score:** ___ / **Evidence:**
- Competitive landscape favorability: **Score:** ___ / **Evidence:**
- Expansion potential beyond initial deal: **Score:** ___ / **Evidence:**

**URGENCY (weight: 30%)**
- External time pressure (regulatory, market, competitive): **Score:** ___ / **Evidence:**
- Internal drivers (budget cycles, initiatives, pain severity): **Score:** ___ / **Evidence:**
- Cost of status quo for them: **Score:** ___ / **Evidence:**
- Risk of losing to competitor: **Score:** ___ / **Evidence:**

**SUCCESS PROBABILITY (weight: 30%)**
- Access to decision-makers: **Score:** ___ / **Evidence:**
- Budget availability signals: **Score:** ___ / **Evidence:**
- Solution-problem fit quality: **Score:** ___ / **Evidence:**
- Implementation feasibility: **Score:** ___ / **Evidence:**
- Cultural/organizational fit: **Score:** ___ / **Evidence:**

**Scoring & Decision Rules:**
- **8+ overall:** Pursue aggressively, prioritize resources, fast-track
- **6-8 overall:** Pursue with standard effort, nurture relationship
- **Below 6:** Deprioritize unless new information emerges

**Calculate weighted overall score and provide clear recommendation with next actions.**"""

        # Phase 6: Qualification
        def phase6_prompt():
            return f"""**Phase 6: Deal Qualification (BANT+ Framework)**

Assess {context.company_name or 'this opportunity'} against qualification criteria.

**IMPORTANT: This is pre-conversation analysis—all assessments are hypotheses to validate in discovery.**

**BUDGET**
- Likely budget range for {context.transaction_type or 'this type of engagement'} (based on firm size/type)
- Probable budget holder and approval process
- Signals of financial health or constraint
- **Confidence level:** High / Medium / Low

**AUTHORITY**
- Probable decision-maker role/title
- Likely influencers and potential blockers
- Expected process complexity
- **Confidence level:** High / Medium / Low

**NEED**
- Estimated pain severity (1-10) with reasoning
- Probable alternatives they're considering
- Fit between our solution and their situation (1-10)
- **Confidence level:** High / Medium / Low

**TIMELINE**
- Likely decision timeline for this purchase type
- Known deadlines or events that might accelerate
- Factors that could cause delays
- **Confidence level:** High / Medium / Low

**ADDITIONAL FACTORS**
- Competitive exposure (who else is probably pursuing them?)
- Political or relationship dynamics we should know about
- Technical or compliance requirements affecting fit
- Cultural considerations

**QUALIFICATION ASSESSMENT:**
- ✅ **Likely Qualified:** Strong signals across BANT—pursue actively
- ⚠️ **Uncertain:** Mixed signals—prioritize validation in early conversations
- ❌ **Likely Unqualified:** Weak signals—deprioritize unless new information emerges

**Priority Level:** A (hot) / B (warm) / C (cold)

**Key Validation Questions for First Conversation:**
1. [Question to validate budget]
2. [Question to validate authority]
3. [Question to validate need]
4. [Question to validate timeline]

**Recommended Next Actions:**"""

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
    
    @classmethod
    def get_phase_names(cls) -> Dict[str, str]:
        """Return phase IDs and display names"""
        return {
            "phase1": "Phase 1: Discovery & Compliance Research",
            "phase2": "Phase 2: Decision-Making Dynamics",
            "phase25": "Phase 2.5: Pain Point Hypothesis & Solution Mapping",
            "phase3": "Phase 3: Credibility-Based Email Outreach",
            "phase4": "Phase 4: Sales Executive Summary",
            "phase5": "Phase 5: OUS Framework Analysis",
            "phase6": "Phase 6: Deal Qualification (BANT+)"
        }
