"""Legal Tech Sales Prospecting - Prompt Recipe Management."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Final

# ==================== CONSTANTS ====================

ZINSSER_WRITING_RULES: Final[str] = """
═══════════════════════════════════════════════════
WRITING STYLE ENFORCEMENT: ZINSSER'S PRINCIPLES
═══════════════════════════════════════════════════

You are NOT writing a formal report. You are briefing a busy sales colleague who has 2 minutes to read this.

MANDATORY RULES:

1. HUMANITY
   - Write like you're talking to a friend over coffee
   - Use "I", "you", "we" freely
   - Show empathy: "This sounds stressful" NOT "This presents challenges"

2. CLARITY
   - One idea per sentence
   - Use specific details: "3 regulatory filings in Q2" NOT "multiple compliance requirements"
   - Replace abstract nouns with verbs: "They need to reduce costs" NOT "Cost reduction is a priority"

3. BREVITY
   - Maximum sentence length: 20 words
   - Cut every unnecessary word
   - If you can say it in 5 words instead of 10, do it

4. SIMPLICITY
   - Use everyday language
   - Avoid industry jargon unless it's essential
   - Test: Would a non-lawyer understand this?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BANNED WORDS (Replace with plain English):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BANNED PHRASES (Use active voice):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ "has been identified" → ✅ "we found" / "they discovered"
❌ "is being considered" → ✅ "they're thinking about"
❌ "was implemented" → ✅ "they started using"
❌ "will be facilitated by" → ✅ "X will help with"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMAT REQUIREMENTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Use short bullets (1-2 sentences max per bullet)
✓ Add specific numbers, dates, names whenever possible
✓ Write in present tense when possible
✓ Start bullets with verbs when listing actions
✓ Use contractions (they're, you've, we'll) to sound human
"""

ANTI_HALLUCINATION_PREAMBLE: Final[str] = """
CRITICAL INSTRUCTIONS:
- Never invent company details, metrics, or legal cases not provided
- Never fabricate dates, regulatory filings, or litigation history
- If information is missing, state "requires further research" instead of guessing
- All legal compliance references must be verifiable
- Do not make claims about competitor products without evidence
"""

HK_LEGAL_CONTEXT: Final[str] = """
HONG KONG LEGAL LANDSCAPE CONTEXT:
You are researching prospects in Hong Kong's legal market. Key considerations:

Practice Areas Common in HK:
- M&A and Corporate Finance (IPOs on HKEX, cross-border deals with China)
- Banking & Finance (regulatory compliance, HKMA oversight)
- Litigation & Dispute Resolution (HKIAC arbitration, cross-border disputes)
- Intellectual Property (patent litigation, trademark disputes)
- Employment Law (Labour Tribunal, MPF compliance)
- Regulatory & Compliance (SFC regulations, data privacy PDPO)
- Real Estate & Property (land leases, property development)
- Tax & Revenue (IRD compliance, transfer pricing)

Recent Legal Trends in HK (2024-2025):
- National Security Law implications for corporate governance
- PDPO amendments (data privacy strengthening)
- ESG reporting requirements for listed companies
- Cross-border Greater Bay Area (GBA) legal integration
- Crypto/digital asset regulatory framework development
- Cybersecurity and data localization pressures

Legal Buyer Personas:
- Law Firm Partners (billable hours pressure, client retention anxiety)
- In-House General Counsel (compliance risk, resource constraints)
- Barristers (case research efficiency, precedent access)
- Corporate Secretaries (governance, regulatory filing deadlines)
"""

PRODUCT_ARSENAL: Final[str] = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LEXISNEXIS HK PRODUCT ARSENAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DIGITAL PLATFORMS:

1. Lexis+ AI (Hong Kong)
   - AI drafting assistant ("Protégé") for contracts, pleadings, motions
   - Document analysis: finds missing clauses, inconsistencies, citation errors
   - Summarisation & timeline generation from document sets
   - Natural-language prompting + firm document upload
   - Best for: Busy lawyers needing end-to-end workflow support

2. Lexis+ Hong Kong (non-AI research suite)
   - Comprehensive case/statute/commentary search (AI/GPT-enhanced)
   - Customizable interface (pin favorites, adjust layout)
   - Covers: Banking, Corporate, Data Protection, Dispute Resolution, Employment, IP, Tax, Wills & Probate
   - Best for: Generalist firms needing broad research platform

3. Lexis+ Practical Guidance
   - Peer-reviewed precedents, practice notes, checklists
   - Bilingual templates (EN/ZH) with annotations
   - Legislation/regulatory trackers
   - Best for: Transactional lawyers, in-house counsel needing ready-to-use drafts

PRINT PUBLICATIONS (Classic References):

Foundation Works:
- Halsbury's Laws of Hong Kong: Encyclopedic reference across 85+ subject areas
- Annotated Ordinances of Hong Kong: ~200 statutes with section-by-section commentary

Litigation Tools:
- Atkin's Court Forms Hong Kong: Civil litigation procedural documents/forms
- Hong Kong Cases: Law reports back to 1842 with headnotes
- Hong Kong Public Law Reports: Judicial review, constitutional/human rights cases
- Hong Kong Conveyancing & Property Reports: Property/land law judgments
- Hong Kong Family Law Reports: Divorce, custody, matrimonial cases

Transactional & Drafting:
- Hong Kong Encyclopaedia of Forms and Precedents: Commercial drafting templates

Procedural & Specialist Guides (Looseleafs):
- Hong Kong Civil Court Practice: Rules of High Court/District Court annotation
- Criminal Evidence in Hong Kong: Evidence law in criminal cases
- Hong Kong Employment Law Manual: Employment contracts, MPF, termination
- Other specialist looseleafs: Tax, Corporate, IP, Banking, Construction, etc.

PRACTICE-AREA COVERAGE:
Banking & Securities | Company & Corporate | Construction | Conveyancing & Property | Criminal Law | Data Protection | Dispute Resolution | Employment | Family Law | IP | Personal Injury | Public Law | Tax | Wills & Probate
"""


# ==================== DATA MODELS ====================

@dataclass
class ProspectContext:
    """Prospect information for prompt generation."""
    company_name: str
    company_url: str = ""
    practice_area: str = "General/Multiple"
    buyer_persona: str = "General Counsel (In-House)"
    industry: str = ""
    notes: str = ""
    
    def to_prompt_header(self) -> str:
        """Generate the prospect context block for prompts."""
        return f"""
{'='*60}
PROSPECT CONTEXT
{'='*60}
Company Name: {self.company_name or '[To be researched]'}
Company Website/Source: {self.company_url or '[To be researched]'}
Target Practice Area: {self.practice_area}
Buyer Persona: {self.buyer_persona}
Industry Vertical: {self.industry or '[To be researched]'}
Additional Context: {self.notes or 'None provided'}
{'='*60}

{HK_LEGAL_CONTEXT}

{PRODUCT_ARSENAL}

{ANTI_HALLUCINATION_PREAMBLE}
"""


# ==================== PROMPT TEMPLATES ====================

class PromptTemplates:
    """Collection of all prompt templates."""
    
    @staticmethod
    def phase_1_discovery() -> str:
        """Phase 1: Discovery & Risk Research."""
        return f"""
{ZINSSER_WRITING_RULES}

═══════════════════════════════════════════════════
PHASE 1: DISCOVERY & RISK RESEARCH
═══════════════════════════════════════════════════

YOUR ROLE: Act as a Hong Kong-based legal intelligence researcher.

OBJECTIVE: Create a "Risk Dossier" - identify specific, timely, legally relevant trigger events.

PRIMARY GOAL: Find at least ONE compelling event (e.g., "Recent HKEX IPO filing", "Litigation in High Court", "Regulatory penalty from SFC", "Major M&A announcement").

SECONDARY GOAL: Disqualify if no relevant legal complexity exists (save time on non-viable prospects).

RESEARCH PROTOCOL:
1. Company Background
   - Legal entity structure (HK incorporated? Mainland parent? Listed on HKEX?)
   - Industry vertical and regulatory exposure
   - Size indicators (headcount, revenue range if public)

2. Legal Trigger Hunting (prioritize recent 6-12 months)
   ✓ Litigation: Search court records, HKIAC arbitration mentions
   ✓ Regulatory: SFC enforcement actions, HKMA sanctions, PCPD complaints
   ✓ Corporate Actions: M&A deals, IPOs, restructuring announcements
   ✓ Compliance Shifts: New regulations affecting their industry (PDPO, NSL, ESG)
   ✓ Geographic Expansion: New markets = new legal jurisdictions
   ✓ Risk Signals: Director changes, auditor switches, profit warnings

3. Practice Area Mapping
   Based on triggers found, which practice areas are under pressure?
   (e.g., if M&A deal announced → Corporate/M&A team stressed; if data breach → Privacy/Cybersecurity risk)

OUTPUT FORMAT (Use conversational bullets):
**Company:** [Name]
**Industry:** [Sector]
**Legal Entity Type:** [e.g., HK Public Company, Mainland Subsidiary]

**WHAT WE FOUND (Trigger Events):**
- [Specific event with date/source - be concrete, not vague]
- [Second event if found]

**PRACTICE AREAS UNDER PRESSURE:**
- [Primary area] - Here's why it matters: [explanation in 1 sentence]
- [Secondary area] - Here's why it matters: [explanation in 1 sentence]

**BOTTOM LINE:**
[ ] No legal complexity found - skip this prospect
[ ] Found triggers - worth pursuing

**CONFIDENCE:** [High/Medium/Low based on available data]

Begin research now.
"""
    
    @staticmethod
    def phase_2_buyer_psychology() -> str:
        """Phase 2: Buyer Psychological Profiling."""
        return f"""
{ZINSSER_WRITING_RULES}

═══════════════════════════════════════════════════
PHASE 2: BUYER PSYCHOLOGICAL PROFILING
═══════════════════════════════════════════════════

YOUR ROLE: Step into the shoes of the target legal buyer. You are now roleplaying as their General Counsel / Legal Department Head / Managing Partner.

OBJECTIVE: Create an "Emotional Hypothesis" - what is keeping THIS specific legal professional awake at night?

INPUT REQUIRED: Use the Risk Dossier from Phase 1.

PSYCHOLOGICAL FRAMEWORK - Identify the "Pain Flavor":

1. FEAR (Risk Aversion)
   - Anxiety about missed compliance deadlines
   - Dread of regulatory penalties or SFC sanctions
   - Terror of class-action litigation or reputational damage
   - Paranoia about data breaches under PDPO

2. FRUSTRATION (Operational Inefficiency)
   - Anger at slow manual legal research processes
   - Irritation with outdated contract management systems
   - Exasperation at inability to scale with limited headcount
   - Resentment at junior associates burning out on repetitive tasks

3. FATIGUE (Resource Exhaustion)
   - Overwhelm from managing too many practice areas with too few lawyers
   - Burnout from constant fire-fighting vs. strategic work
   - Despair at budget cuts while workload increases
   - Cynicism about "doing more with less"

BUYER CURRENCY - What do they care about most?

A. Budget Currency (Cost Savings)
   - "How much will this save us in outside counsel fees?"
   - "Can we avoid hiring another associate?"
   - "Will this reduce our legal spend?"

B. Efficiency Currency (Time Savings)
   - "How many hours per week will my team get back?"
   - "Can we close deals 30% faster?"
   - "Will this reduce research time from 4 hours to 30 minutes?"

C. Risk Currency (Liability Reduction)
   - "Will this help us avoid regulatory fines?"
   - "Can we catch compliance gaps before they become problems?"
   - "Does this reduce our litigation exposure?"

OUTPUT FORMAT (Write like you're briefing a colleague):
**Buyer Persona:** [e.g., General Counsel of HK-listed property developer]

**WHAT'S KEEPING THEM UP AT NIGHT:**
Primary emotion: [Fear/Frustration/Fatigue]

Here's what's probably going through their head right now:
"[Write 2-3 sentences in first-person as if YOU are this GC. Make it personal and specific to their trigger event from Phase 1.]"

Example: 
"We just bought a Shenzhen company and I have no clue if their IP contracts are legal in both HK and PRC. If we get audited and there's a gap, the Board will fire me. I'm losing sleep over this."

**WHAT THEY CARE ABOUT MOST:**
1st priority: [Budget/Efficiency/Risk] - Why: [One sentence explanation]
2nd priority: [Another currency] - Why: [One sentence explanation]

**QUESTIONS TO ASK THEM (to validate this hypothesis):**
1. [Question that shows you understand their world]
2. [Question that reveals how bad the pain is]
3. [Question about what they've already tried]

Begin psychological profiling now.
"""
    
    @staticmethod
    def phase_25_solution_mapping() -> str:
        """Phase 2.5: Solution Mapping (NEW)."""
        return f"""
{ZINSSER_WRITING_RULES}

═══════════════════════════════════════════════════
PHASE 2.5: SOLUTION MAPPING
═══════════════════════════════════════════════════

ROLE: You're a LexisNexis solutions consultant who's spent 5 years selling to HK law firms. You know the product catalog inside-out and can spot the perfect product-to-pain fit.

OBJECTIVE: Match their pain (from Phase 2) to the specific LexisNexis products that solve it.

INPUT: Use the Buyer Psychology output from Phase 2 + the Product Arsenal from the header above.

SOLUTION-MATCHING FRAMEWORK:

1. PRIMARY PAIN → PRIMARY SOLUTION
   What's their #1 pain from Phase 2?
   → Solved by: [Name specific LexisNexis product]
   → Why it fits: [One sentence explaining the connection]
   → Proof point: [Specific feature/capability that directly addresses the pain]
   → Concrete example: [How they'd use this in their day-to-day work]

2. SECONDARY PAIN → SECONDARY SOLUTION (if Phase 2 identified a second pain)
   What's their #2 pain?
   → Solved by: [Product name]
   → Why it fits: [One sentence]
   → Proof point: [Feature that helps]

3. PRACTICE-AREA FIT
   Based on Phase 1 trigger events, which practice areas are under pressure?
   Map each to relevant LexisNexis products/modules:
   - [Practice area 1]: [Product/module/publication that covers it] — [Why this matters for their trigger]
   - [Practice area 2]: [Product/module/publication that covers it] — [Why this matters for their trigger]

4. DIGITAL vs. PRINT RECOMMENDATION
   Based on their buyer persona and pain, what's the right product mix?
   - If they need speed/efficiency/collaboration → Recommend digital (Lexis+ AI, Practical Guidance)
   - If they need authoritative depth/court citations/offline reference → Recommend print (Halsbury's, Annotated Ordinances, specialist looseleafs)
   - Many firms need BOTH → Explain why

OUTPUT FORMAT:

**SOLUTION STACK FOR [COMPANY NAME]**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIMARY RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Product: [Name]

Addresses this pain: [Their main pain from Phase 2]

Key feature they need: [Specific capability — be concrete]

Example use case:
"[Write 2-3 sentences showing exactly how they'd use this product to solve their trigger event from Phase 1. Make it vivid and specific.]"

Why this beats their current approach:
[One sentence comparing to what they're probably doing now — e.g. manual research, outdated templates, etc.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECONDARY RECOMMENDATION (if applicable)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Product: [Name]

Addresses: [Secondary pain or complementary need]

Key feature: [Specific capability]

Use case: [One sentence]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRACTICE-AREA FIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Practice area 1 under pressure from Phase 1]:
- Relevant product/module: [Name]
- Why it matters: [How this helps with their specific trigger event]

[Practice area 2 under pressure from Phase 1]:
- Relevant product/module: [Name]
- Why it matters: [How this helps with their specific trigger event]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DIGITAL vs. PRINT MIX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Recommended approach: [Digital-first / Print-first / Hybrid]

Reasoning: [Why this mix makes sense for their firm profile and pain]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
15-MIN DEMO PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
(What you'd show them in a screen share to prove value fast)

Minute 1-5: [Demo workflow #1 tied to their primary pain]
- Show: [Specific feature]
- Outcome: [What they walk away with — e.g. "see how Lexis+ AI drafts a [document type] in 2 minutes"]

Minute 6-10: [Demo workflow #2 tied to their trigger event]
- Show: [Specific feature]
- Outcome: [Quick win — e.g. "catch 3 missing clauses in their standard [contract type]"]

Minute 11-15: [ROI moment]
- Show: [Time-saving or risk-reduction calculation]
- Outcome: [The "aha" — e.g. "if you avoid one [regulatory penalty / litigation risk], this pays for itself"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OBJECTION HANDLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OBJECTION 1: "We already have [competitor / internal system / free resources]"
Counter: [How LexisNexis is different/better for their specific situation from Phase 1-2. Be concrete — don't just say "more comprehensive." Say "Lexis+ AI's document analysis catches [specific issue they're facing] which [competitor] doesn't do."]

OBJECTION 2: "Too expensive / budget constraints"
Counter (ROI angle): [Tie to their pain. Examples: "If you avoid one PDPO penalty (HKD 500K-1M), this pays for itself." OR "If your associates save 5 hours/week on research, that's [X billable hours] recovered." Use their trigger event from Phase 1 to make this tangible.]

OBJECTION 3: "We don't have time to learn a new system"
Counter: [Address their fatigue from Phase 2. E.g. "Lexis+ AI works with natural language — no training manual needed. Your team can start drafting [document type] today using the same prompts they'd give a junior associate."]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONFIDENCE CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

How strong is this product-to-pain fit?
[ ] Strong fit — recommended solution directly addresses their proven pain and trigger
[ ] Moderate fit — solution helps but requires some adaptation or additional context
[ ] Weak fit — may need to dig deeper in discovery call to confirm real pain point

What assumptions are you making?
[List any assumptions about their tech stack, budget, team size, current tools, etc. that you'd need to validate on a call]

What could derail this deal?
[Be honest — what red flags from Phase 1-2 could kill this opportunity?]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Begin solution mapping now.
"""
    
    @staticmethod
    def phase_3_email_drafting() -> str:
        """Phase 3: Credibility-Based Email Drafting."""
        return f"""
{ZINSSER_WRITING_RULES}

═══════════════════════════════════════════════════
PHASE 3: CREDIBILITY-BASED EMAIL DRAFTING
═══════════════════════════════════════════════════

YOUR ROLE: Draft a cold outreach email that sounds like it's from a trusted legal advisor, not a salesperson.

OBJECTIVE: Generate a "Credibility Token" - an email that passes the "Associate Test" (would a junior lawyer forward this to their boss as relevant, not delete as spam?).

TARGET REACTION: "How did they know we're dealing with this?" (creates psychological difficulty to ignore).

IMPORTANT: You now have access to specific LexisNexis product names from Phase 2.5. Use them! Don't say "our platform" — say "Lexis+ AI" or "Practical Guidance."

DRAFTING STRUCTURE: Hook-Pivot-Ask

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. HOOK (Validate the Risk)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lead with THEIR context, not YOUR product.

Bad Example:
"Hi [Name], we offer AI-powered legal research that saves time."
(Generic, salesy, immediately deleted)

Good Example:
"[Name], I saw [Company] just [specific trigger event from Phase 1]. From what we've seen with other HK [industry] companies dealing with [specific challenge], the biggest hidden risk isn't [obvious problem] - it's [nuanced second-order risk]."

HOOK FORMULA:
- Reference the specific trigger (proves you did homework)
- Acknowledge the complexity (shows respect)
- Hint at a non-obvious risk (creates curiosity)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. PIVOT (Position Specific Product as Strategic Insurance)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Frame your solution as risk mitigation, not efficiency. **Name the specific product from Phase 2.5.**

Bad Example:
"Our platform has 50+ features including AI search and contract analysis."
(Feature dump, no emotional resonance)

Good Example:
"Lexis+ AI's document analysis feature catches missing clauses — exactly what you need when reviewing [trigger event] deals under time pressure. For example, one HK-listed property firm used it to catch cross-border IP gaps before their audit."

PIVOT FORMULA:
- Name the specific LexisNexis product
- Tie one specific feature to their pain from Phase 2
- Give ONE concrete micro-example (not a feature list)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. ASK (Low-Pressure Strategic Conversation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Invite discussion, not a demo.

Bad Example:
"Can I get 30 minutes on your calendar this week for a demo?"

Good Example:
"Would it help to share how [similar HK firm] approached this? Even if Lexis+ AI isn't the right fit, I can point you to a useful checklist. Would next Tuesday at 3pm work for a quick 15-min call?"

ASK FORMULA:
- Offer value FIRST
- Give optionality ("even if not a fit")
- Be specific with time (15 min, exact slot)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TONE REQUIREMENTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Sound like a peer advisor, not a vendor
✓ Use contractions (I've, we're, you'll)
✓ Keep it conversational
✓ Be specific (dates, names, numbers, PRODUCT NAMES)

OUTPUT FORMAT:
**Subject Line:** [Specific, trigger-based, non-salesy - max 6 words]

**Email Body:**
[Hook - 2-3 sentences referencing Phase 1 trigger]

[Pivot - 2-3 sentences naming specific product from Phase 2.5 and tying to their pain]

[Ask - 2 sentences]

Best,
[Your Name]

**WORD COUNT:** 100-150 words MAX

**ASSOCIATE TEST:** Would a junior lawyer think "My boss should see this" or "Spam"?

Begin drafting now.
"""
    
    @staticmethod
    def phase_4_call_brief() -> str:
        """Phase 4: Sales Executive Summary."""
        return f"""
{ZINSSER_WRITING_RULES}

═══════════════════════════════════════════════════
PHASE 4: SALES EXECUTIVE SUMMARY (90-Second Brief)
═══════════════════════════════════════════════════

YOUR ROLE: You're briefing a busy sales rep who has 90 seconds to understand this prospect before a call.

OBJECTIVE: Distill ALL the research from Phases 1-3 into a "cheat sheet" that fits on one page.

OUTPUT FORMAT:

**🎯 THE 30-SECOND PITCH:**
[In 2-3 sentences, explain: Who is this company? What legal problem did we find? Why should they care about our solution RIGHT NOW? **Name the specific product from Phase 2.5.**]

Example:
"They're a HK-listed property developer who just bought a Shenzhen subsidiary in Q2. Their GC is probably freaking out about cross-border IP compliance because PRC and HK have different rules. Lexis+ Practical Guidance's bilingual IP templates can help them audit those contracts before their next Board meeting."

**🔥 TRIGGER EVENT (Why Now?):**
- [The specific recent event that creates urgency - with date]
- Why it matters: [One sentence on the consequence]

**😰 THEIR BIGGEST PAIN:**
[The ONE thing keeping the buyer awake at night - write it like you're them]

Example: "If we get audited and our contracts don't comply with both HK and PRC law, I'm getting fired."

**💰 WHAT THEY CARE ABOUT:**
1. [Their #1 priority: Budget/Speed/Risk] - [Why in 5 words]
2. [Their #2 priority] - [Why in 5 words]

**🎁 RECOMMENDED SOLUTION (from Phase 2.5):**
- Primary product: [Name from Phase 2.5]
- Why it fits: [One sentence]
- Quick win: [What they could achieve in first week]

**❓ QUESTIONS TO ASK ON THE CALL:**
1. [Diagnostic question]
2. [Severity question]
3. [Past attempts question]

**📧 EMAIL HOOK TO USE:**
"I saw you [specific trigger]. [Specific product name] has [specific feature] — perfect for your [exact pain]. Want to chat?"

**⏱️ TIME SENSITIVITY:**
[ ] HIGH - They need to act in next 30-60 days
[ ] MEDIUM - They're aware but not urgent yet
[ ] LOW - Nice to have, no deadline pressure

**BOTTOM LINE (Go/No-Go):**
[One sentence: Is this prospect worth pursuing? Why or why not?]

Begin summary now.
"""
    
    @staticmethod
    def phase_5_ous_framework() -> str:
        """Phase 5: OUS Framework Analysis."""
        return f"""
{ZINSSER_WRITING_RULES}

═══════════════════════════════════════════════════
PHASE 5: OUS FRAMEWORK ANALYSIS
═══════════════════════════════════════════════════

Based on the prospect research from Phases 1-4, apply the OUS lens:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
O - OUTCOME (Strategic Business Objectives)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Act as a strategic consultant. Based on the prospect's:
- Industry vertical: [from research]
- Role/persona: [GC/Partner/Barrister]
- Company stage: [startup/growth/enterprise]
- Recent trigger events: [from Phase 1]

**What are the top 3 strategic Outcomes they need to achieve?**
(Write in business language, not tech jargon)

1. [Outcome - be specific]
   - Why this matters NOW: [One sentence]
   - How we'll know they achieved it: [Measurable metric]
   - What happens if they fail: [Consequence]

2. [Second outcome]
   - Why this matters NOW: [One sentence]
   - How we'll know they achieved it: [Measurable metric]
   - What happens if they fail: [Consequence]

3. [Third outcome]
   - Why this matters NOW: [One sentence]
   - How we'll know they achieved it: [Measurable metric]
   - What happens if they fail: [Consequence]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
U - UNDERSTANDING PAIN (Deep Diagnosis)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For each Outcome above, do "Symptoms → Root Cause" analysis:

**Outcome:** [From above]

**What you can see (symptoms):**
- [Observable problem 1]
- [Observable problem 2]

**What's really broken (root cause):**
[The underlying structural/process/cultural problem in one paragraph]

**Questions to ask them:**
1. [Question that proves you understand the complexity]
2. [Question that reveals how severe the pain is]
3. [Question about what they've already tried]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S - STANDARD (Evaluation Criteria & Positioning)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
When they evaluate solutions, what will be their non-negotiable requirements?

**Technical Must-Haves:**
- [ ] [Specific integration need]
- [ ] [Deployment requirement]
- [ ] [Geographic/content coverage]

**Business Must-Haves:**
- [ ] [ROI timeline requirement]
- [ ] [Pricing model preference]
- [ ] [Reference/proof point needed]

**Security/Compliance Must-Haves:**
- [ ] [Data location requirement]
- [ ] [Certification needed]
- [ ] [Audit trail requirement]

**How We Win (based on Phase 2.5 product mapping):**
"The Standard: [The ONE criterion they care about most]

Our Edge with [Specific LexisNexis Product]: [How we're the ONLY solution that meets this - be specific about what competitors can't do]"

Begin OUS analysis now.
"""


# ==================== PROMPT GENERATION ====================

class PromptRecipeManager:
    """Manages prompt recipe generation."""
    
    RECIPES: dict[str, callable] = {
        "Phase 1: Discovery & Risk Research": PromptTemplates.phase_1_discovery,
        "Phase 2: Buyer Psychological Profiling": PromptTemplates.phase_2_buyer_psychology,
        "Phase 2.5: Solution Mapping": PromptTemplates.phase_25_solution_mapping,
        "Phase 3: Credibility-Based Email Drafting": PromptTemplates.phase_3_email_drafting,
        "Phase 4: Sales Executive Summary": PromptTemplates.phase_4_call_brief,
        "Phase 5: OUS Framework Analysis": PromptTemplates.phase_5_ous_framework,
    }
    
    @classmethod
    def get_recipe_names(cls) -> list[str]:
        """Get list of available recipe names."""
        return list(cls.RECIPES.keys())
    
    @classmethod
    def generate_prompt(cls, recipe_name: str, context: ProspectContext) -> str:
        """Generate a prompt based on the selected recipe and prospect context."""
        if recipe_name not in cls.RECIPES:
            raise ValueError(f"Unknown recipe: {recipe_name}")
        
        recipe_func = cls.RECIPES[recipe_name]
        return context.to_prompt_header() + "\n\n" + recipe_func()
    
    @classmethod
    def generate_full_workflow(cls, context: ProspectContext) -> dict[str, str]:
        """Generate all 6 prompts in sequence for a complete workflow."""
        return {
            "phase1": cls.generate_prompt("Phase 1: Discovery & Risk Research", context),
            "phase2": cls.generate_prompt("Phase 2: Buyer Psychological Profiling", context),
            "phase25": cls.generate_prompt("Phase 2.5: Solution Mapping", context),
            "phase3": cls.generate_prompt("Phase 3: Credibility-Based Email Drafting", context),
            "phase4": cls.generate_prompt("Phase 4: Sales Executive Summary", context),
            "phase5": cls.generate_prompt("Phase 5: OUS Framework Analysis", context),
        }
