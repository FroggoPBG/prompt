# components/recipes.py
# Legal Tech Sales Prospecting - OUS Framework Recipes
from __future__ import annotations

from typing import Dict, List, Callable, Any

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
# 3-Phase Legal Scout Strategy
# -----------------------------

PHASE_1_DISCOVERY = """
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

OUTPUT FORMAT:
**Company:** [Name]
**Industry:** [Sector]
**Legal Entity Type:** [e.g., HK Public Company, Mainland Subsidiary]

**TRIGGER EVENTS IDENTIFIED:**
1. [Specific event with date/source]
2. [Second event if found]

**PRACTICE AREAS UNDER PRESSURE:**
- [Primary area] - [Why it's relevant]
- [Secondary area] - [Why it's relevant]

**DISQUALIFICATION CHECK:**
[ ] No legal complexity detected - prospect not viable
[ ] Legal triggers found - proceed to Phase 2

**CONFIDENCE LEVEL:** [High/Medium/Low based on data availability]
"""

PHASE_2_PROFILING = """
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

OUTPUT FORMAT:
**Buyer Persona:** [e.g., General Counsel of HK-listed property developer]

**PRIMARY PAIN FLAVOR:** [Fear/Frustration/Fatigue] - [Specific manifestation]

**EMOTIONAL HYPOTHESIS:**
"Based on [trigger from Phase 1], this legal buyer is likely experiencing [specific emotion] because [logical reasoning]. 

The internal dialogue in their head sounds like:
'[First-person narrative of their worry/stress/insecurity]'

Example: 'We just acquired a Shenzhen subsidiary, and I have NO idea if their IP licensing agreements are compliant with both PRC and HK law. If we get audited and there's a gap, the Board will have my head.'"

**BUYER CURRENCY PRIORITY:**
Primary: [Budget/Efficiency/Risk] - [Why this matters most to them now]
Secondary: [Second currency] - [Supporting reason]

**VALIDATION QUESTIONS (to confirm hypothesis in conversation):**
1. [Diagnostic question that demonstrates you understand their context]
2. [Question that reveals the severity of the pain]
3. [Question that uncovers whether they've tried to solve this before]
"""

PHASE_3_DRAFTING = """
═══════════════════════════════════════════════════
PHASE 3: PRIVILEGED COMMUNICATION (Credibility-Based Drafting)
═══════════════════════════════════════════════════

YOUR ROLE: Draft a cold outreach email that sounds like it comes from a trusted legal advisor, not a salesperson.

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
"[Name], I noticed [Company] recently [specific trigger event from Phase 1]. In our work with similar HK-based [industry] companies navigating [specific legal challenge], we've seen that the biggest hidden risk isn't [obvious problem], but rather [nuanced second-order risk that demonstrates deep understanding]."

HOOK FORMULA:
- Reference the specific trigger (proves you did homework)
- Acknowledge the complexity (shows respect for their expertise)
- Hint at a non-obvious consequence (creates curiosity)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. PIVOT (Position as Strategic Insurance)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Frame your solution as risk mitigation, not efficiency.

Bad Example:
"Our platform has 50+ features including AI search and contract analysis."
(Feature dump, no emotional resonance)

Good Example:
"The General Counsels we work with in [practice area] describe our legal intelligence platform as 'the insurance policy against what we might have missed.' Specifically, [one concrete example of how it catches gaps that manual research doesn't]."

PIVOT FORMULA:
- Use social proof from similar buyers (peer validation)
- Frame as "insurance" or "assurance" (speaks to risk aversion)
- Give ONE concrete micro-example (not a feature list)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. ASK (Low-Pressure Strategic Conversation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Invite discussion, not a demo.

Bad Example:
"Can I get 30 minutes on your calendar this week for a demo?"
(Asks for their time without giving value first)

Good Example:
"I'd welcome a brief conversation to share how [similar HK law firm/company] approached [specific challenge]. Even if our solution isn't the right fit, I can point you to [specific resource/insight] that might be helpful. Would [specific day/time] work for a 15-minute call?"

ASK FORMULA:
- Offer value FIRST (insight, benchmark, resource)
- Give optionality ("even if not a fit")
- Be specific with time (15 min, not "sometime")
- Propose exact slot (reduces friction)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TONE REQUIREMENTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Authoritative but humble (advisor, not vendor)
✓ Specific but concise (every word earns its place)
✓ Empathetic but professional (acknowledge stress without being patronizing)
✓ Hong Kong appropriate (respect local business culture - direct but courteous)

FORBIDDEN PHRASES:
❌ "I hope this email finds you well" (cliché)
❌ "We're the leading/award-winning" (unverifiable claims)
❌ "Our AI-powered solution" (buzzword soup)
❌ "Just following up" (signals desperation)
❌ "I'd love to show you" (salesy language)

APPROVED LANGUAGE PATTERNS:
✓ "I noticed [specific fact]"
✓ "In our work with [peer group]"
✓ "The biggest hidden risk we see is"
✓ "Would it be helpful to share"
✓ "Even if our solution isn't the right fit"

OUTPUT FORMAT:
**Subject Line:** [Specific, trigger-based, non-salesy]
Example: "Re: [Company]'s [specific trigger event] - compliance gap consideration"

**Email Body:**
[Hook - 2-3 sentences max]

[Pivot - 2-3 sentences max]

[Ask - 2 sentences max]

[Signature]

**EMAIL LENGTH TARGET:** 100-150 words maximum (legal professionals have zero time for long emails)

**ASSOCIATE TEST:** Would a junior lawyer read this and think "My boss should see this" or "Spam"?
"""

# -----------------------------
# OUS Framework Integration
# -----------------------------

OUS_DISCOVERY_PROMPT = """
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

**Hypothesize the top 3 strategic Outcomes they are likely under pressure to achieve:**

1. [Outcome in business language, not feature language]
   Example: "Reduce outside counsel spend by 25% without sacrificing quality" NOT "Implement AI tools"

2. [Second outcome tied to their specific context]
   Example: "Achieve compliance with new PDPO amendments before Q2 audit" NOT "Buy compliance software"

3. [Third outcome - career/reputation level]
   Example: "Position the legal department as a strategic partner, not a cost center" NOT "Increase efficiency"

**For each outcome, answer:**
- Why is this outcome critical NOW (urgency)?
- What is the measurable success criteria (how will they know they achieved it)?
- What happens if they FAIL to achieve this outcome (downside risk)?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
U - UNDERSTANDING PAIN (Deep Diagnosis)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For each Outcome identified above, perform "Symptoms → Root Cause" analysis:

**Outcome:** [From above]

**Visible Symptoms (what you can observe):**
- [e.g., "High turnover in junior associates"]
- [e.g., "Frequent regulatory filing deadline extensions"]
- [e.g., "Increasing reliance on expensive outside counsel"]

**Root Cause Hypothesis (what's really broken):**
[The underlying operational/structural/cultural problem]
Example: "The firm's legal research tools are 10+ years old, forcing associates to spend 60% of their time on manual cite-checking instead of strategic analysis. This creates burnout (symptom 1) and forces partners to outsource work they should handle internally (symptom 3)."

**Discovery Questions (to validate this in conversation):**
Write 3 diagnostic questions that:
1. Prove you understand the complexity (not obvious questions)
2. Reveal severity (quantify the pain)
3. Uncover failed solutions (what have they already tried?)

Example:
❌ Bad: "Do you struggle with legal research?" (too generic)
✓ Good: "When your M&A team needs to verify cross-border regulatory compliance between HK and PRC, how long does that research typically take, and how confident are you in the comprehensiveness?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S - STANDARD (Evaluation Criteria & Positioning)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Simulate the "Buying Committee" for this prospect.

**When evaluating a solution for [the specific pain/outcome], what will be their non-negotiable Standards?**

Technical Standards:
- [ ] Must integrate with existing systems (specify: e.g., iManage, NetDocuments)
- [ ] Requires zero/minimal IT involvement to deploy
- [ ] Must cover Hong Kong AND cross-border (PRC/Singapore) jurisdictions
- [ ] Must include [specific content type]: case law, legislation, practice notes

Business Standards:
- [ ] ROI payback period < [X months]
- [ ] Pricing model: per-user vs. enterprise vs. usage-based
- [ ] Vendor must have legal industry references in Hong Kong

Security/Compliance Standards:
- [ ] Data sovereignty (where is data stored? HK? Offshore?)
- [ ] ISO 27001 / SOC 2 certification
- [ ] Audit trail for regulatory compliance

**Competitive Positioning:**
Based on these Standards, how do we position our solution to be the ONLY one that meets the most critical standard?

Example:
"The Standard: They require a solution that covers both Hong Kong case law AND PRC regulations in a single search (because their M&A deals are always cross-border).

Our Positioning: Unlike competitors who only cover HK or require separate subscriptions for PRC content, we are the only platform with unified HK-PRC legal intelligence, saving them from toggling between 3 different research tools."

**OUTPUT:**
For each Standard identified, state:
1. Why this Standard exists (the fear/need driving it)
2. How our solution meets it (be specific, not generic)
3. What competitors CANNOT do (create contrast)
"""

# -----------------------------
# Recipe Registry
# -----------------------------

PROMPT_RECIPES: Dict[str, str] = {
    "Phase 1: Discovery & Compliance Research": PHASE_1_DISCOVERY,
    "Phase 2: General Counsel Psychological Profiling": PHASE_2_PROFILING,
    "Phase 3: Credibility-Based Email Drafting": PHASE_3_DRAFTING,
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
    Generate all 4 prompts in sequence for a complete workflow.
    Returns a dict with keys: phase1, phase2, phase3, ous
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
        "ous": fill_recipe(
            "OUS Framework Analysis",
            company_name, company_url, practice_area, buyer_persona
        ),
    }
