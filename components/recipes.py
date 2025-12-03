"""
Prompt Recipe Manager
Handles all prompt generation logic for M&A prospecting workflows.
"""

from typing import Dict
from datetime import datetime

class PromptRecipeManager:
    """Manages prompt templates and generation for all phases."""
    
    @staticmethod
    def _format_context(context: Dict[str, str]) -> str:
        """Format prospect context for inclusion in prompts."""
        parts = []
        
        if context.get("company_name"):
            parts.append(f"**Company:** {context['company_name']}")
        if context.get("industry"):
            parts.append(f"**Industry:** {context['industry']}")
        if context.get("deal_type"):
            parts.append(f"**Transaction Type:** {context['deal_type']}")
        if context.get("legal_entity_type"):
            parts.append(f"**Entity Type:** {context['legal_entity_type']}")
        if context.get("revenue_size"):
            parts.append(f"**Revenue Size:** {context['revenue_size']}")
        if context.get("geographic_scope"):
            scope = ", ".join(context["geographic_scope"]) if isinstance(context["geographic_scope"], list) else context["geographic_scope"]
            parts.append(f"**Geographic Scope:** {scope}")
        if context.get("product_interest"):
            products = ", ".join(context["product_interest"]) if isinstance(context["product_interest"], list) else context["product_interest"]
            parts.append(f"**Product Interest:** {products}")
        if context.get("additional_context"):
            parts.append(f"**Additional Context:** {context['additional_context']}")
        
        return "\n".join(parts)
    
    @staticmethod
    def generate_phase1(context: Dict[str, str]) -> str:
        """Generate Phase 1: Discovery & Risk Research prompt."""
        company = context.get("company_name", "[Company Name]")
        formatted_context = PromptRecipeManager._format_context(context)
        
        return f"""# PHASE 1: DISCOVERY & RISK RESEARCH

## PROSPECT INFORMATION:
{formatted_context}

---

## YOUR TASK:
You are a legal research analyst conducting discovery for a B2B sales team targeting corporate legal/compliance teams. Research **{company}** and identify potential trigger events that create urgency for legal technology solutions.

## RESEARCH AREAS:

### 1. M&A & Corporate Activity
- Recent acquisitions, mergers, or divestitures (last 18 months)
- Leadership changes (new GC, CLO, or compliance executives)
- Corporate restructuring or reorganization announcements
- New market expansions or geographic footprint changes

### 2. Legal & Regulatory Triggers
- Recent litigation, regulatory investigations, or enforcement actions
- Data breaches, privacy incidents, or cybersecurity issues
- Regulatory compliance deadlines (GDPR, SEC filings, industry-specific)
- Government audits or compliance reviews

### 3. Industry & Competitive Pressures
- Industry-wide regulatory changes affecting their sector
- Competitive moves (how peers are responding to similar challenges)
- Market consolidation trends
- Emerging compliance requirements in their industry

### 4. Financial & Operational Signals
- Quarterly earnings reports mentioning legal/compliance costs
- Press releases about compliance programs or risk management
- Job postings for legal/compliance roles (suggesting team expansion)
- Technology modernization initiatives mentioned publicly

---

## OUTPUT FORMAT:

### **TRIGGER EVENTS FOUND:**
- [List specific events with dates/sources - be concrete, not vague]
- [Include links or citations where possible]

### **PRESSURE AREAS:**
- **Primary:** [Main area under pressure - e.g., M&A team stressed, compliance risk high]
- **Secondary:** [Supporting pressure points]

### **WHY THIS MATTERS:**
[1-sentence explanation of why each trigger creates urgency for legal tech solutions]

---

## CONFIDENCE LEVEL:
[ ] High (multiple triggers found across sources)
[ ] Medium (1-2 clear triggers)
[ ] Low (limited public information - suggest exploratory outreach)

---

**Start your research now. Focus on recent (last 12-18 months) publicly available information.**
"""

    @staticmethod
    def generate_phase2(context: Dict[str, str]) -> str:
        """Generate Phase 2: Buyer Psychological Profiling prompt."""
        company = context.get("company_name", "[Company Name]")
        formatted_context = PromptRecipeManager._format_context(context)
        
        return f"""# PHASE 2: BUYER PSYCHOLOGICAL PROFILING

## PROSPECT INFORMATION:
{formatted_context}

---

## YOUR TASK:
Based on the discovery research from Phase 1, analyze the **emotional and psychological state** of the buyer (General Counsel, Legal Ops, or Compliance lead at **{company}**).

## PASTE YOUR PHASE 1 OUTPUT BELOW:
[Paste the trigger events and pressure areas you identified in Phase 1 here]

---

## ANALYSIS FRAMEWORK:

### 1. EMOTIONAL TRIGGERS
Identify the buyer's likely emotional state:
- **Anxiety/Fear:** What are they worried about? (e.g., regulatory penalties, deal delays, reputational damage)
- **Urgency:** What deadlines or time pressures are they facing?
- **Frustration:** What current systems/processes are failing them?
- **Aspiration:** What do they want to achieve? (efficiency, risk reduction, competitive edge)

### 2. PAIN POINTS (Functional)
What specific problems are they dealing with?
- Manual processes eating up time
- Lack of visibility into legal/compliance risks
- Inability to scale operations with current tools
- Difficulty meeting regulatory deadlines
- Inefficient contract management or due diligence workflows

### 3. BUYING MOTIVATIONS
What will make them say "yes" to a meeting?
- **Risk Mitigation:** Avoiding penalties, breaches, or legal exposure
- **Efficiency Gains:** Saving time, reducing manual work
- **Competitive Pressure:** Not falling behind peers
- **Executive Mandate:** Pressure from CEO/Board to modernize
- **Cost Savings:** Reducing external counsel spend or compliance costs

### 4. OBJECTIONS & BARRIERS
What might stop them from engaging?
- "Too busy right now"
- "Already have tools in place"
- "Budget constraints"
- "Not a priority"

---

## OUTPUT FORMAT:

### **BUYER PERSONA PROFILE:**

**Primary Emotion:** [Fear/Urgency/Frustration - pick the dominant one based on triggers]

**Top 3 Pain Points:**
1. [Specific pain point tied to trigger event]
2. [Second pain point]
3. [Third pain point]

**Key Buying Motivation:** [What will make them take a meeting - be specific]

**Likely Objection:** [What barrier they'll throw up + how to counter it]

---

## MESSAGING GUIDANCE:

**Opening Hook (for cold email):**
[Write a 1-sentence trigger-based hook that references their specific situation]

**Value Proposition:**
[1-2 sentences explaining how LexisNexis solves their specific pain - avoid generic language]

---

**Begin your analysis now using the Phase 1 research.**
"""

    @staticmethod
    def generate_phase25(context: Dict[str, str]) -> str:
        """Generate Phase 2.5: Solution Mapping prompt."""
        company = context.get("company_name", "[Company Name]")
        formatted_context = PromptRecipeManager._format_context(context)
        products = context.get("product_interest", [])
        product_context = ", ".join(products) if products else "any relevant LexisNexis products"
        
        return f"""# PHASE 2.5: SOLUTION MAPPING (Product-to-Pain Fit)

## PROSPECT INFORMATION:
{formatted_context}

---

## YOUR TASK:
Map the pain points identified in Phases 1 & 2 to **specific LexisNexis products and features**. This ensures your Phase 3 email mentions concrete solutions instead of vague "we can help" language.

## PASTE YOUR PHASE 1 & 2 OUTPUTS BELOW:
[Paste the trigger events from Phase 1 and pain points from Phase 2 here]

---

## LEXISNEXIS PRODUCT CATALOG:

### **1. Lexis+ AI**
- AI-powered legal research
- Natural language search across case law, statutes, regulations
- Hallucination-free answers with source citations
- **Use cases:** Fast legal research, contract review, regulatory compliance checks

### **2. Practical Guidance**
- Step-by-step how-to guides for legal tasks
- Practice notes, checklists, precedents
- **Use cases:** M&A transaction support, compliance program setup, contract drafting

### **3. Halsbury's Laws of England**
- Authoritative legal encyclopedia
- Cross-referenced legal principles
- **Use cases:** UK legal research, statutory interpretation, precedent analysis

### **4. Corporate Law Suite**
- Company formation and governance tools
- Board resolutions, shareholder agreements
- **Use cases:** Corporate restructuring, governance compliance, M&A documentation

### **5. Lexis Diligence**
- Virtual data room for M&A due diligence
- Secure document sharing and review
- **Use cases:** Buy-side/sell-side due diligence, deal management

### **6. Compliance & Risk Solutions**
- Regulatory change tracking
- Policy management tools
- **Use cases:** Regulatory compliance monitoring, risk assessment, audit preparation

### **7. PSL (Practice Area Specific Products)**
- Employment law, real estate, IP, etc.
- Tailored content and tools for specialists
- **Use cases:** Industry-specific compliance, niche legal research

---

## MAPPING EXERCISE:

For each pain point identified in Phase 2, map to a specific product:

### **Pain Point 1:** [Copy from Phase 2]
- **Recommended Product:** [Choose from above]
- **Specific Feature:** [e.g., "Lexis+ AI's contract analyzer"]
- **How It Helps:** [1 sentence on how this solves their problem]

### **Pain Point 2:** [Copy from Phase 2]
- **Recommended Product:**
- **Specific Feature:**
- **How It Helps:**

### **Pain Point 3:** [Copy from Phase 2]
- **Recommended Product:**
- **Specific Feature:**
- **How It Helps:**

---

## OPTIONAL: If product interest was specified ({product_context}), prioritize those solutions in your mapping.

---

## OUTPUT FORMAT:

### **SOLUTION SUMMARY:**

**Primary Recommendation:** [Top product match]
**Secondary Products:** [2-3 additional products that fit]

**One-Liner for Email:**
[Write a single sentence that ties their trigger event to a specific product feature]

Example: "Given your recent acquisition of XYZ Corp, Lexis Diligence's AI-powered due diligence platform could help your team review contracts 10x faster while flagging hidden risks."

---

**Complete your product-to-pain mapping now.**
"""

    @staticmethod
    def generate_phase3(context: Dict[str, str]) -> str:
        """Generate Phase 3: Credibility-Based Email Drafting prompt."""
        company = context.get("company_name", "[Company Name]")
        formatted_context = PromptRecipeManager._format_context(context)
        
        return f"""# PHASE 3: CREDIBILITY-BASED EMAIL DRAFTING

## PROSPECT INFORMATION:
{formatted_context}

---

## YOUR TASK:
Draft a cold outreach email to the General Counsel or legal/compliance decision-maker at **{company}**. Use insights from Phases 1, 2, and 2.5 to create a highly personalized, trigger-based message.

## PASTE YOUR PHASE 1, 2, & 2.5 OUTPUTS BELOW:
[Paste all previous research here: trigger events, pain points, and product mapping]

---

## EMAIL STRUCTURE:

### **SUBJECT LINE:**
[Write 2-3 subject line options - use trigger events, avoid generic "quick question" language]

**Examples:**
- "Re: [Specific trigger event at Company]"
- "[Company]'s recent [M&A deal/compliance challenge] - quick insight"
- "Following your [announcement/news] - potential efficiency gain"

---

### **EMAIL BODY:**

**OPENING (Trigger Hook):**
[1-2 sentences referencing the specific trigger event from Phase 1. Show you did your homework.]

Example: "I noticed ABC Corp recently acquired XYZ Ltd (announced Oct 2024). Managing due diligence and post-merger integration for cross-border deals like this typically creates significant pressure on legal teams..."

---

**PAIN ACKNOWLEDGMENT:**
[1 sentence showing empathy for their specific challenge - tie to Phase 2 pain points]

Example: "I imagine your team is juggling contract reviews, regulatory filings, and compliance harmonization—all with the same headcount."

---

**VALUE PROPOSITION (Specific Product Mention):**
[2-3 sentences introducing the LexisNexis solution mapped in Phase 2.5. Mention a specific product/feature.]

Example: "We work with legal teams at [similar companies] to accelerate M&A workflows using Lexis Diligence—our AI-powered due diligence platform. It flags risks in contracts automatically, cutting review time by 60-70%."

---

**CREDIBILITY PROOF:**
[1 sentence with social proof - either a similar client, industry stat, or relevant case study]

Example: "We helped [Peer Company in same industry] close their last 3 acquisitions 40% faster while reducing external counsel spend."

---

**CALL TO ACTION:**
[Specific, low-friction ask - suggest a 15-min call or sending a one-pager]

Example: "Would a 15-minute call next week make sense? I can show you a quick demo of how [Product] handles [specific pain point]."

---

**SIGNATURE:**
[Your name]
[Title] | LexisNexis
[Contact info]

---

## TONE GUIDELINES:
- **Conversational, not corporate:** Write like you're talking to a peer, not sending a press release
- **Specific, not generic:** Mention actual products, dates, and numbers
- **Helpful, not salesy:** Position yourself as solving a problem, not pushing a product
- **Concise:** Keep total email under 150 words

---

## OUTPUT:

### **EMAIL DRAFT:**

**Subject:** [Your subject line]

**Body:**
[Your full email text]

---

### **ALTERNATIVE VERSIONS:**
[Provide 1-2 shorter or longer variations for A/B testing]

---

**Draft your email now using all Phase 1-2.5 insights.**
"""

    @staticmethod
    def generate_phase4(context: Dict[str, str]) -> str:
        """Generate Phase 4: Sales Executive Summary prompt."""
        company = context.get("company_name", "[Company Name]")
        formatted_context = PromptRecipeManager._format_context(context)
        
        return f"""# PHASE 4: SALES EXECUTIVE SUMMARY (90-Second Brief)

## PROSPECT INFORMATION:
{formatted_context}

---

## YOUR TASK:
Distill all research from Phases 1-3 into a **one-page cheat sheet** that a sales rep can read in 90 seconds before a call. Focus on what matters: triggers, pain, products, and talk track.

## PASTE YOUR PHASE 1-3 OUTPUTS BELOW:
[Paste trigger events, pain points, product mapping, and email draft here]

---

## EXECUTIVE SUMMARY STRUCTURE:

### **🎯 QUICK SNAPSHOT**
- **Company:** {company}
- **Industry:** [From context]
- **Decision Maker:** [GC/CLO/VP Legal - specify if known]
- **Deal Size Potential:** [Small/Mid/Large - based on company size and pain severity]

---

### **🔥 KEY TRIGGER (Why Now?)**
[1-2 sentences explaining THE primary trigger event that creates urgency]

Example: "Acquired XYZ Corp in Oct 2024 - now dealing with cross-border compliance harmonization and 10,000+ contracts to review."

---

### **💡 TOP 3 PAIN POINTS**
1. **[Pain Point 1]** - [1 sentence impact]
2. **[Pain Point 2]** - [1 sentence impact]
3. **[Pain Point 3]** - [1 sentence impact]

---

### **🛠️ RECOMMENDED PRODUCTS**
- **Primary:** [Product name] - [Why it fits in 1 sentence]
- **Secondary:** [Product name] - [Why it fits in 1 sentence]

---

### **🎤 CALL SCRIPT (Opening Lines)**

**If they answer:**
"Hi [Name], [Your Name] from LexisNexis. I saw you recently [trigger event]. We help legal teams like yours [specific outcome] using [product]. Do you have 2 minutes?"

**If voicemail:**
"Hi [Name], [Your Name] from LexisNexis. Saw your team is dealing with [trigger]. We helped [similar company] solve [similar problem] using [product]. Worth a quick chat? Call me at [number]."

---

### **❓ LIKELY OBJECTIONS & RESPONSES**

**Objection 1:** "We already have tools in place."
**Response:** "Totally understand. Most of our clients had [legacy tool] too—but they were still spending [X hours] on [manual task]. Can I show you a 5-minute demo of how [product] automates that?"

**Objection 2:** "Not a priority right now."
**Response:** "Makes sense. Just for context—[similar company] was in the same spot 6 months ago, then [trigger event] hit and it became urgent fast. Would a 15-min exploratory call be worth it just to have the info?"

---

### **📊 SUCCESS METRICS TO MENTION**
[Pull from product knowledge - e.g., "Clients typically see 60% faster contract review" or "Reduce external counsel spend by 30%"]

---

## OUTPUT FORMAT:

### **ONE-PAGE SALES BRIEF**

[Generate the complete summary using the structure above - keep it to ~300 words max]

---

**Create your 90-second executive summary now.**
"""

    @staticmethod
    def generate_phase5(context: Dict[str, str]) -> str:
        """Generate Phase 5: OUS Framework Analysis prompt."""
        company = context.get("company_name", "[Company Name]")
        formatted_context = PromptRecipeManager._format_context(context)
        
        return f"""# PHASE 5: OUS FRAMEWORK ANALYSIS

## PROSPECT INFORMATION:
{formatted_context}

---

## YOUR TASK:
Apply the **OUS Framework** (Outcome → Understanding → Standard) to refine your positioning for **{company}**. This ensures your messaging aligns with how senior legal buyers think strategically.

## PASTE ALL PREVIOUS PHASE OUTPUTS BELOW:
[Paste research from Phases 1-4 here]

---

## OUS FRAMEWORK BREAKDOWN:

### **O = OUTCOME (What They Want to Achieve)**
What is the end goal the buyer is trying to reach?

**Questions to answer:**
- What business outcome does the GC/CLO need to deliver? (e.g., "close the acquisition on time," "pass the regulatory audit," "reduce legal spend by 20%")
- What does success look like for them in the next 6-12 months?
- How will they measure success? (KPIs, board reporting, etc.)

**Your Analysis:**
[Write 2-3 sentences describing their desired outcome based on triggers and pain points]

---

### **U = UNDERSTANDING (What Stands in Their Way)**
What are the obstacles preventing them from achieving the outcome?

**Questions to answer:**
- What gaps exist in their current capabilities? (lack of tools, insufficient headcount, manual processes)
- What risks could derail their outcome? (regulatory penalties, deal delays, data breaches)
- What don't they know yet that they need to understand? (new regulations, industry best practices)

**Your Analysis:**
[Write 2-3 sentences describing their knowledge/capability gaps]

---

### **S = STANDARD (What Best-in-Class Looks Like)**
What does the industry standard or "best practice" solution look like?

**Questions to answer:**
- How are their peers solving this problem?
- What technology/processes are considered "table stakes" in their industry now?
- What would a modern, efficient legal/compliance operation look like for them?

**Your Analysis:**
[Write 2-3 sentences describing the standard they should aspire to - position LexisNexis as part of that standard]

---

## OUTPUT FORMAT:

### **OUS POSITIONING SUMMARY**

**OUTCOME:** [Their goal in 1 sentence]

**UNDERSTANDING:** [What's blocking them in 1 sentence]

**STANDARD:** [What best practice looks like in 1 sentence]

---

### **MESSAGING REFINEMENT**

Based on this OUS analysis, rewrite your email opening or value prop:

**Before (from Phase 3):**
[Copy your original Phase 3 email hook]

**After (OUS-informed version):**
[Rewrite it to emphasize Outcome, acknowledge Understanding gaps, and position against the Standard]

---

**Example:**

**Before:** "We help legal teams review contracts faster."

**After:** "Most GCs we work with need to close M&A deals 30% faster (OUTCOME) but are stuck with manual contract review processes (UNDERSTANDING). Leading firms now use AI-powered due diligence platforms as the standard (STANDARD)—want to see how [Company] compares?"

---

**Complete your OUS analysis now and refine your messaging.**
"""

    @staticmethod
    def generate_full_workflow(context: Dict[str, str]) -> Dict[str, str]:
        """Generate all phases as a complete workflow."""
        return {
            "phase1": PromptRecipeManager.generate_phase1(context),
            "phase2": PromptRecipeManager.generate_phase2(context),
            "phase25": PromptRecipeManager.generate_phase25(context),  # ✅ FIXED KEY
            "phase3": PromptRecipeManager.generate_phase3(context),
            "phase4": PromptRecipeManager.generate_phase4(context),
            "phase5": PromptRecipeManager.generate_phase5(context)
        }
