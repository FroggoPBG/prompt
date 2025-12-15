
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
        
        header = context.to_prompt_header()
        
        phase1 = header + """**Phase 1: Discovery & Compliance Research**

Research the target company to inform our engagement strategy:

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

        phase2 = header + """**Phase 2: Decision-Making Dynamics Analysis**

Analyze typical decision-making dynamics for this firm when evaluating solutions:

1. **Stakeholder Mapping**
   - Likely decision-making roles (who typically holds authority for this purchase type)
   - Probable influencers and gatekeepers
   - How decisions typically flow in firms of this size and structure

2. **Decision-Making Characteristics**
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

        phase25 = header + """**Phase 2.5: Pain Point Hypothesis & Solution Mapping**

**Part A: Pain Point Hypothesis**

Based on the firm's profile, practice areas, and market position, identify likely operational challenges:

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
   - What limitations come from their size?
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

        # NEW PHASE 3 - Hong Kong Legal Market Version
        phase3 = """============================================================
PROSPECT CONTEXT
============================================================
Company Name: """ + context.company_name + """
Company Website/Source: [To be filled in]
Target Practice Area: """ + (context.industry_sector or "General/Multiple") + """
Buyer Persona: """ + (context.legal_entity_type or "General Counsel (In-House)") + """

============================================================
HONG KONG LEGAL LANDSCAPE CONTEXT
============================================================

You are researching prospects in Hong Kong's legal market. Key considerations:

**Practice Areas Common in HK:**
- M&A and Corporate Finance (IPOs on HKEX, cross-border deals with China)
- Banking & Finance (regulatory compliance, HKMA oversight)
- Litigation & Dispute Resolution (HKIAC arbitration, cross-border disputes)
- Intellectual Property (patent litigation, trademark disputes)
- Employment Law (Labour Tribunal, MPF compliance)
- Regulatory & Compliance (SFC regulations, data privacy PDPO)
- Real Estate & Property (land leases, property development)
- Tax & Revenue (IRD compliance, transfer pricing)

**Recent Legal Trends in HK (2024-2025):**
- National Security Law implications for corporate governance
- PDPO amendments (data privacy strengthening)
- ESG reporting requirements for listed companies
- Cross-border Greater Bay Area (GBA) legal integration
- Crypto/digital asset regulatory framework development
- Cybersecurity and data localization pressures

**Legal Buyer Personas:**
- Law Firm Partners (billable hours pressure, client retention anxiety)
- In-House General Counsel (compliance risk, resource constraints)
- Barristers (case research efficiency, precedent access)
- Corporate Secretaries (governance, regulatory filing deadlines)

============================================================
CRITICAL SAFETY INSTRUCTIONS
============================================================

**CRITICAL INSTRUCTIONS:**
- Never invent company details, metrics, or legal cases not provided
- Never fabricate dates, regulatory filings, or litigation history
- If information is missing, state "requires further research" instead of guessing
- All legal compliance references must be verifiable
- Do not make claims about competitor products without evidence

============================================================
WRITING STYLE ENFORCEMENT: ZINSSER'S PRINCIPLES
============================================================

You are NOT writing a formal report. You are briefing a busy sales colleague who has 2 minutes to read this.

**MANDATORY RULES:**

1. **HUMANITY**
   - Write like you're talking to a friend over coffee
   - Use "I", "you", "we" freely
   - Show empathy: "This sounds stressful" NOT "This presents challenges"

2. **CLARITY**
   - One idea per sentence
   - Use specific details: "3 regulatory filings in Q2" NOT "multiple compliance requirements"
   - Replace abstract nouns with verbs: "They need to reduce costs" NOT "Cost reduction is a priority"

3. **BREVITY**
   - Maximum sentence length: 20 words
   - Cut every unnecessary word
   - If you can say it in 5 words instead of 10, do it

4. **SIMPLICITY**
   - Use everyday language
   - Avoid industry jargon unless it's essential
   - Test: Would a non-lawyer understand this?

---

**BANNED WORDS (Replace with plain English):**

❌ utilization → ✅ use
❌ implementation → ✅ start using / set up
❌ facilitate → ✅ help / make easier
❌ optimization → ✅ improve / make better
❌ leverage → ✅ use
❌ synergy → ✅ teamwork / working together
❌ functionality → ✅ features / what it does
❌ operationalize → ✅ do / make happen
❌ utilize → ✅ use
❌ commence → ✅ start
❌ endeavor → ✅ try
❌ ascertain → ✅ find out

---

**BANNED PHRASES (Use active voice):**

❌ "has been identified" → ✅ "we found" / "they discovered"
❌ "is being considered" → ✅ "they're thinking about"
❌ "was implemented" → ✅ "they started using"
❌ "will be facilitated by" → ✅ "X will help with"

---

**FORMAT REQUIREMENTS:**

✓ Use short bullets (1-2 sentences max per bullet)
✓ Add specific numbers, dates, names whenever possible
✓ Write in present tense when possible
✓ Start bullets with verbs when listing actions
✓ Use contractions (they're, you've, we'll) to sound human

============================================================
PHASE 3: CREDIBILITY-BASED EMAIL DRAFTING
============================================================

**YOUR ROLE:** Draft a cold outreach email that sounds like it's from a trusted legal advisor, not a salesperson.

**OBJECTIVE:** Generate a "Credibility Token" - an email that passes the "Associate Test" (would a junior lawyer forward this to their boss as relevant, not delete as spam?).

**TARGET REACTION:** "How did they know we're dealing with this?" (creates psychological difficulty to ignore).

**DRAFTING STRUCTURE: Hook-Pivot-Ask**

---

### 1. HOOK (Validate the Risk)

Lead with THEIR context, not YOUR product.

**Bad Example:** "Hi [Name], we offer AI-powered legal research that saves time." (Generic, salesy, immediately deleted)

**Good Example:** "[Name], I saw [Company] just [specific trigger event from Phase 1]. From what we've seen with other HK [industry] companies dealing with [specific challenge], the biggest hidden risk isn't [obvious problem] - it's [nuanced second-order risk]."

**HOOK FORMULA:**
- Reference the specific trigger (proves you did homework)
- Acknowledge the complexity (shows respect)
- Hint at a non-obvious risk (creates curiosity)

---

### 2. PIVOT (Position as Strategic Insurance)

Frame your solution as risk mitigation, not efficiency.

**Bad Example:** "Our platform has 50+ features including AI search and contract analysis." (Feature dump, no emotional resonance)

**Good Example:** "The GCs we work with describe our platform as 'insurance against what we might've missed.' For example, [one concrete micro-story of how it caught a gap]."

**PIVOT FORMULA:**
- Use social proof from similar buyers
- Frame as "insurance" or "safety net"
- Give ONE concrete micro-example (not a feature list)

---

### 3. ASK (Low-Pressure Strategic Conversation)

Invite discussion, not a demo.

**Bad Example:** "Can I get 30 minutes on your calendar this week for a demo?"

**Good Example:** "I'd love to share how [similar HK firm] tackled [specific challenge]. Even if our tool isn't the right fit, I can point you to [specific resource]. Would next Tuesday at 3pm work for a quick 15-min call?"

**ASK FORMULA:**
- Offer value FIRST
- Give optionality ("even if not a fit")
- Be specific with time (15 min, exact slot)

---

**TONE REQUIREMENTS:**

✓ Sound like a peer advisor, not a vendor
✓ Use contractions (I've, we're, you'll)
✓ Keep it conversational
✓ Be specific (dates, names, numbers)

---

**OUTPUT FORMAT:**

**Subject Line:** [Specific, trigger-based, non-salesy - max 6 words]

**Email Body:**
[Hook - 2-3 sentences]

[Pivot - 2-3 sentences]

[Ask - 2 sentences]

Best,
[Your Name]

**WORD COUNT:** 100-150 words MAX

**ASSOCIATE TEST:** Would a junior lawyer think "My boss should see this" or "Spam"?"""

        phase4 = header + """**Phase 4: Sales Executive Summary**

Create a 90-second executive summary for this opportunity:

1. **Account Snapshot**
   - Firm profile (size, practice focus, positioning)
   - Why they're a fit for us
   - Estimated deal size (state assumptions clearly)

2. **Strategic Rationale**
   - Top 2-3 pain points we can likely address
   - Why now (urgency factors, if any)
   - Decision-maker profile (Known vs Assumed)

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

        phase5 = header + """**Phase 5: OUS Framework Analysis**

Analyze this opportunity using the OUS framework. For each score (1-10), provide specific evidence or reasoning.

**OUTCOME (weight: 35%)**

- Strategic goals this solution would support: **Score:** ___ / **Evidence:**
- Alignment with stated priorities or strategic initiatives: **Score:** ___ / **Evidence:**
- Long-term value potential beyond immediate problem-solving: **Score:** ___ / **Evidence:**
- Executive visibility and sponsorship potential: **Score:** ___ / **Evidence:**

**Outcome Subscore:** ___ / 10

---

**UNDERSTANDING PAIN (weight: 35%)**

- Severity of pain points we can address (1=minor annoyance, 10=critical business issue): **Score:** ___ / **Evidence:**
- Cost of status quo (wasted time, lost revenue, compliance risk, competitive disadvantage): **Score:** ___ / **Evidence:**
- Urgency/time pressure to solve this pain: **Score:** ___ / **Evidence:**
- Our ability to articulate their pain better than they can (shows deep understanding): **Score:** ___ / **Evidence:**

**Understanding Pain Subscore:** ___ / 10

---

**SELECTION PROCESS (weight: 30%)**

- Clarity on their evaluation criteria and decision process: **Score:** ___ / **Evidence:**
- Our competitive positioning against their stated requirements: **Score:** ___ / **Evidence:**
- Decision-maker access and influence: **Score:** ___ / **Evidence:**
- Budget availability and approval process favorability: **Score:** ___ / **Evidence:**
- Technical/compliance requirements alignment: **Score:** ___ / **Evidence:**

**Selection Process Subscore:** ___ / 10

---

**OVERALL OUS SCORE:**
Overall = (Outcome × 0.35) + (Understanding Pain × 0.35) + (Selection Process × 0.30)

**Overall Score:** ___ / 10

**Decision Rules:**
- 8+ overall: Pursue aggressively
- 6-8 overall: Pursue with standard effort
- Below 6: Deprioritize or qualify out

**RECOMMENDATION:**
[Based on the overall score, provide clear next actions and resource allocation guidance]

**KEY GAPS TO ADDRESS:**
[What critical information is missing? What needs validation in first conversation?]"""

        phase6 = header + """**Phase 6: Deal Qualification (BANT+ Framework)**

Assess this opportunity against qualification criteria.

**IMPORTANT: This is pre-conversation analysis—all assessments are hypotheses to validate in discovery.**

**BUDGET**
- Likely budget range for this type of engagement (based on firm size/type)
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

        return {
            "phase1": phase1,
            "phase2": phase2,
            "phase25": phase25,
            "phase3": phase3,
            "phase4": phase4,
            "phase5": phase5,
            "phase6": phase6
        }
    
    @classmethod
    def generate_phase1(cls, context: ProspectContext) -> str:
        """Generate Phase 1 prompt"""
        return cls.generate_full_workflow(context)["phase1"]
    
    @classmethod
    def generate_phase2(cls, context: ProspectContext) -> str:
        """Generate Phase 2 prompt"""
        return cls.generate_full_workflow(context)["phase2"]
    
    @classmethod
    def generate_phase25(cls, context: ProspectContext) -> str:
        """Generate Phase 2.5 prompt"""
        return cls.generate_full_workflow(context)["phase25"]
    
    @classmethod
    def generate_phase3(cls, context: ProspectContext) -> str:
        """Generate Phase 3 prompt"""
        return cls.generate_full_workflow(context)["phase3"]
    
    @classmethod
    def generate_phase4(cls, context: ProspectContext) -> str:
        """Generate Phase 4 prompt"""
        return cls.generate_full_workflow(context)["phase4"]
    
    @classmethod
    def generate_phase5(cls, context: ProspectContext) -> str:
        """Generate Phase 5 prompt"""
        return cls.generate_full_workflow(context)["phase5"]
    
    @classmethod
    def generate_phase6(cls, context: ProspectContext) -> str:
        """Generate Phase 6 prompt"""
        return cls.generate_full_workflow(context)["phase6"]
    
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
            "phase3": "Phase 3: Credibility-Based Email Outreach (HK Legal Market)",
            "phase4": "Phase 4: Sales Executive Summary",
            "phase5": "Phase 5: OUS Framework Analysis",
            "phase6": "Phase 6: Deal Qualification (BANT+)"
        }
