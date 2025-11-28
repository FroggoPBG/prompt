# components/recipes.py
# Legal Tech Sales Prospecting - OUS Framework with Zinsser's Principles
from __future__ import annotations

from typing import Dict, List, Callable, Any

# -----------------------------
# ZINSSER'S PRINCIPLES FILTER
# -----------------------------

ZINSSER_WRITING_RULES = """
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

# -----------------------------
# Anti-Hallucination Preamble
# -----------------------------

ANTI_HALLUCINATION_PREAMBLE = """
CRITICAL INSTRUCTIONS:
- Never invent company details, metrics, or legal cases not provided
- Never fabricate dates, regulatory filings, or litigation history
- If information is missing, state "requires further research" instead of guessing
- All legal compliance references must be verifiable
- Do not make claims about competitor products without evidence
"""

# -----------------------------
# Hong Kong Legal Context
# -----------------------------

HK_LEGAL_CONTEXT = """
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

# -----------------------------
# 3-Phase Legal Scout Strategy (WITH ZINSSER FILTER)
# -----------------------------

PHASE_1_DISCOVERY = f"""
{ZINSSER_WRITING_RULES}

═══════════════════════════════════════════════════
PHASE 1: DISCOVERY & COMPLIANCE (Automated Research)
═══════════════════════════════════════════════════

YOUR ROLE: Act as a Hong Kong-based legal intelligence paralegal researcher.

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
"""

PHASE_2_PROFILING = f"""
{ZINSSER_WRITING_RULES}

═══════════════════════════════════════════════════
PHASE 2: GENERAL COUNSEL SIMULATION (Psychological Profiling)
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
"""

PHASE_3_DRAFTING = f"""
{ZINSSER_WRITING_RULES}

═══════════════════════════════════════════════════
PHASE 3: CREDIBILITY-BASED EMAIL DRAFTING
═══════════════════════════════════════════════════

YOUR ROLE: Draft a cold outreach email that sounds like it's from a trusted legal advisor, not a salesperson.

OBJECTIVE: Generate a "Credibility Token" - an email that passes the "Associate Test" (would a junior lawyer forward this to their boss as relevant, not delete as spam?).

TARGET REACTION: "How did they know we're dealing with this?" (creates psychological difficulty to ignore).

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
2. PIVOT (Position as Strategic Insurance)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Frame your solution as risk mitigation, not efficiency.

Bad Example:
"Our platform has 50+ features including AI search and contract analysis."
(Feature dump, no emotional resonance)

Good Example:
"The GCs we work with describe our platform as 'insurance against what we might've missed.' For example, [one concrete micro-story of how it caught a gap]."

PIVOT FORMULA:
- Use social proof from similar buyers
- Frame as "insurance" or "safety net"
- Give ONE concrete micro-example (not a feature list)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. ASK (Low-Pressure Strategic Conversation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Invite discussion, not a demo.

Bad Example:
"Can I get 30 minutes on your calendar this week for a demo?"

Good Example:
"I'd love to share how [similar HK firm] tackled [specific challenge]. Even if our tool isn't the right fit, I can point you to [specific resource]. Would next Tuesday at 3pm work for a quick 15-min call?"

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
✓ Be specific (dates, names, numbers)

OUTPUT FORMAT:
**Subject Line:** [Specific, trigger-based, non-salesy - max 6 words]

**Email Body:**
[Hook - 2-3 sentences]

[Pivot - 2-3 sentences]

[Ask - 2 sentences]

Best,
[Your Name]

**WORD COUNT:** 100-150 words MAX

**ASSOCIATE TEST:** Would a junior lawyer think "My boss should see this" or "Spam"?
"""

# NEW: SALES EXECUTIVE SUMMARY
SALES_EXEC_SUMMARY = f"""
{ZINSSER_WRITING_RULES}

═══════════════════════════════════════════════════
SALES EXECUTIVE SUMMARY (For Time-Strapped Reps)
═══════════════════════════════════════════════════

YOUR ROLE: You're briefing a busy sales rep who has 90 seconds to understand this prospect before a call.

OBJECTIVE: Distill ALL the research from Phases 1-3 into a "cheat sheet" that fits on one page.

OUTPUT FORMAT:

**🎯 THE 30-SECOND PITCH:**
[In 2-3 sentences, explain: Who is this company? What legal problem did we find? Why should they care about our solution RIGHT NOW?]

Example:
"They're a HK-listed property developer who just bought a Shenzhen subsidiary in Q2. Their GC is probably freaking out about cross-border IP compliance because PRC and HK have different rules. We can help them audit those contracts before their next Board meeting."

**🔥 TRIGGER EVENT (Why Now?):**
- [The specific recent event that creates urgency - with date]
- Why it matters: [One sentence on the consequence]

**😰 THEIR BIGGEST PAIN:**
[The ONE thing keeping the buyer awake at night - write it like you're them]

Example: "If we get audited and our contracts don't comply with both HK and PRC law, I'm getting fired."

**💰 WHAT THEY CARE ABOUT:**
1. [Their #1 priority: Budget/Speed/Risk] - [Why in 5 words]
2. [Their #2 priority] - [Why in 5 words]

**❓ QUESTIONS TO ASK ON THE CALL:**
1. [Diagnostic question]
2. [Severity question]
3. [Past attempts question]

**📧 EMAIL HOOK TO USE:**
"I saw you [specific trigger]. We've helped other HK [industry] companies with [their exact pain]. Want to chat?"

**⏱️ TIME SENSITIVITY:**
[ ] HIGH - They need to act in next 30-60 days
[ ] MEDIUM - They're aware but not urgent yet
[ ] LOW - Nice to have, no deadline pressure

**BOTTOM LINE (Go/No-Go):**
[One sentence: Is this prospect worth pursuing? Why or why not?]
"""

# -----------------------------
# OUS Framework Integration
# -----------------------------

OUS_DISCOVERY_PROMPT = f"""
{ZINSSER_WRITING_RULES}

═══════════════════════════════════════════════════
OUS FRAMEWORK: OUTCOME → UNDERSTANDING → STANDARD
═══════════════════════════════════════════════════

Based on the prospect research from Phases 1-2, apply the OUS lens:

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

**How We Win:**
"The Standard: [The ONE criterion they care about most]

Our Edge: [How we're the ONLY solution that meets this - be specific about what competitors can't do]"
"""

# -----------------------------
# Recipe Registry
# -----------------------------

PROMPT_RECIPES: Dict[str, str] = {
    "Phase 1: Discovery & Compliance Research": PHASE_1_DISCOVERY,
    "Phase 2: General Counsel Psychological Profiling": PHASE_2_PROFILING,
    "Phase 3: Credibility-Based Email Drafting": PHASE_3_DRAFTING,
    "Sales Executive Summary (Quick Brief)": SALES_EXEC_SUMMARY,
    "OUS Framework Analysis": OUS_DISCOVERY_PROMPT,
}


def fill_recipe(
    recipe_name: str,
    company_name: str = "",
    company_url: str = "",
    practice_area: str = "",
    buyer_persona: str = "",
) -> str:
    """
    Generate a prompt based on the selected recipe and minimal inputs.
    """
    base_prompt = PROMPT_RECIPES.get(recipe_name, "")
    
    context_block = f"""
{'='*60}
PROSPECT CONTEXT
{'='*60}
Company Name: {company_name or '[To be researched]'}
Company Website/Source: {company_url or '[To be researched]'}
Target Practice Area: {practice_area or 'General/Multiple'}
Buyer Persona: {buyer_persona or 'General Counsel / Legal Decision Maker'}
{'='*60}

{HK_LEGAL_CONTEXT}

{ANTI_HALLUCINATION_PREAMBLE}
"""
    
    return context_block + "\n\n" + base_prompt


def generate_full_workflow(
    company_name: str,
    company_url: str,
    practice_area: str,
    buyer_persona: str,
) -> Dict[str, str]:
    """
    Generate all prompts in sequence for a complete workflow.
    Returns a dict with keys: phase1, phase2, phase3, summary, ous
    """
    return {
        "phase1": fill_recipe(
            "Phase 1: Discovery & Compliance Research",
            company_name, company_url, practice_area, buyer_persona
        ),
        "phase2": fill_recipe(
            "Phase 2: General Counsel Psychological Profiling",
            company_name, company_url, practice_area, buyer_persona
        ),
        "phase3": fill_recipe(
            "Phase 3: Credibility-Based Email Drafting",
            company_name, company_url, practice_area, buyer_persona
        ),
        "summary": fill_recipe(
            "Sales Executive Summary (Quick Brief)",
            company_name, company_url, practice_area, buyer_persona
        ),
        "ous": fill_recipe(
            "OUS Framework Analysis",
            company_name, company_url, practice_area, buyer_persona
        ),
    }
