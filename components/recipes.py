# components/recipes.py
# Core language scaffolds, context, and prompt recipes.
from __future__ import annotations

from typing import Dict, List, Callable, Any

# -----------------------------
# Minimal Anti-Hallucination Preamble
# -----------------------------

ANTI_HALLUCINATION_PREAMBLE = """
Never invent names, dates, metrics, or contact details. 
When information is missing, say you'll find out.
"""

# -----------------------------
# Language scaffolds (minimal version)
# -----------------------------

SCAFFOLDS: Dict[str, Dict[str, str]] = {
    "en": {
        "name": "English",
        "sys": "You are a LexisNexis account manager writing professional client emails.",
    },
    "ja": {
        "name": "Japanese",
        "sys": "あなたはLexisNexisのアカウントマネージャーで、プロフェッショナルなクライアントメールを書いています。",
    },
    "zh": {
        "name": "Chinese (Simplified)",
        "sys": "您是LexisNexis客户经理，正在撰写专业的客户电子邮件。",
    },
}

# -----------------------------
# Shared LexisNexis context - Trimmed for brevity
# -----------------------------

LN_CONTEXT: Dict[str, Any] = {
    "outputs": ["plain prompt", "email-only output"],
    "client_types": ["in-house legal", "law firm", "government", "academic", "corporate (non-legal)", "other"],
    "regions": ["Hong Kong", "Singapore", "Japan", "South Korea", "Australia / NZ", "Other APAC", "Global"],
    "practice_areas": ["Financial services", "Litigation", "Corporate", "Regulatory", "IP", "Employment", "Tax", "Other"],
    "products": ["Lexis+", "Lexis Advance", "Practical Guidance", "Lexis Draft", "News", "Analytics"],
    "stages": ["Prospect", "Onboarding", "Adoption", "Renewal", "Expansion", "At-risk"],
    "tones": ["auto", "warm", "formal", "consultative", "apologetic", "direct"],
    "lengths": ["very short", "short", "medium", "long"],
}

# -----------------------------
# Helper: minimal prompt builder
# -----------------------------

def _base_email_prompt(scaffold: Dict[str, str], ctx: Dict[str, Any], task: str) -> str:
    lines: List[str] = []

    lines.append(ANTI_HALLUCINATION_PREAMBLE)
    lines.append("")

    lines.append(scaffold["sys"])
    lines.append("")

    lines.append("CLIENT DATA:")
    lines.append(f"- Name: {ctx.get('client_name', '[Client Name]')}")
    lines.append(f"- Type: {ctx.get('client_type', 'n/a')}")
    lines.append(f"- Region: {ctx.get('region', 'n/a')}")
    lines.append(f"- Products: {', '.join(ctx.get('products_used', []) or ['n/a'])}")
    lines.append(f"- Stage: {ctx.get('relationship_stage', 'n/a')}")
    if ctx.get('usage_metrics'):
        lines.append(f"- Metrics: {ctx.get('usage_metrics')}")
    if ctx.get('nps_info'):
        lines.append(f"- NPS: {ctx.get('nps_info')}")
    lines.append("")

    lines.append("TASK:")
    lines.append(task)
    lines.append("")

    lines.append("DO NOT:")
    lines.append("❌ Invent names (use 'our team' not 'Sarah Chen')")
    lines.append("❌ Provide timelines not given (use 'I'll follow up' not 'within 48 hours')")
    lines.append("❌ Mention metrics not provided")
    lines.append("❌ Reference unmentioned details")
    lines.append("")

    lines.append(f"Tone: {ctx.get('tone', 'consultative')}")
    lines.append(f"Length: {ctx.get('length', 'short')}")

    return "\n".join(lines)

# -----------------------------
# Individual recipes - Simplified versions
# -----------------------------

def _renewal_email(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    scenario = ctx.get("renewal_scenario", "value")
    task = f"Write a renewal email for upcoming contract. Scenario: {scenario}. " \
           f"Acknowledge usage, propose call to discuss. Include provided contract details if any."
    
    lines: List[str] = []
    lines.append(_base_email_prompt(scaffold, ctx, task))
    lines.append("")
    
    lines.append("USAGE METRICS HANDLING:")
    lines.append("When metrics are provided in CLIENT DATA, use them to inform your tone and approach, but DO NOT include the actual numbers in the email.")
    lines.append("Instead of citing figures, describe usage patterns:")
    lines.append("- High usage → 'strong engagement,' 'actively using the platform,' 'well-integrated into your workflow'")
    lines.append("- Feature-specific usage → 'I notice your team is making good use of [feature],' 'particularly the alerts functionality'")
    lines.append("- Alerts/monitoring → 'your proactive approach to monitoring legal developments'")
    lines.append("")
    lines.append("Examples:")
    lines.append("❌ DON'T write: 'Your team made 2,839 document accesses and 1,331 searches'")
    lines.append("✅ DO write: 'Your team has been actively engaged with the platform'")
    lines.append("❌ DON'T write: 'You've set up 222 alerts'")
    lines.append("✅ DO write: 'I'm pleased to see your firm is making good use of the alerts feature to stay ahead of legal developments'")
    lines.append("")
    lines.append("Remember: Metrics are for your context only. The client knows their own usage. Keep acknowledgments natural and non-intrusive.")
    
    return "\n".join(lines)

def _qbr_brief(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    task = "Write a QBR summary email. Include provided metrics if any. Highlight wins and recommendations."
    return _base_email_prompt(scaffold, ctx, task)

def _client_followup(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    task = "Write a follow-up email after meeting. Reference provided topics if any. Propose next steps."
    return _base_email_prompt(scaffold, ctx, task)

def _proposal_rfp(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    task = "Write an RFP response email. Acknowledge requirements, highlight fit. Propose next steps."
    return _base_email_prompt(scaffold, ctx, task)

def _upsell_cross_sell(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    task = "Write an upsell email. Reference current usage, suggest additions. Offer demo."
    return _base_email_prompt(scaffold, ctx, task)

def _client_risk_alert(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    task = "Write a risk alert email. Acknowledge issue, propose solutions. Suggest call."
    return _base_email_prompt(scaffold, ctx, task)

def _client_snapshot(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    task = "Write a client snapshot email. Summarize profile, metrics, risks if provided."
    return _base_email_prompt(scaffold, ctx, task)

def _objection_coach(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    task = f"Write an objection response email for {ctx.get('objection_type', 'general')}. Acknowledge concern, provide evidence if available."
    return _base_email_prompt(scaffold, ctx, task)

def _nps_engagement(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    nps_previous_rating = ctx.get("nps_previous_rating", "n/a")
    nps_survey_link = ctx.get("nps_survey_link", "n/a")
    task = f"Write an NPS engagement email that will be sent BEFORE an upcoming NPS survey. The purpose is to: " \
           f"Prepare the client that they'll receive a new NPS survey soon (this week if timing specified). " \
           f"Encourage them to complete it. Request detailed/specific feedback to help us improve. " \
           f"Acknowledge their previous NPS rating and show we value their input. " \
           f"Include survey link only if provided. Adapt tone based on previous NPS rating: {nps_previous_rating}."
    return _base_email_prompt(scaffold, ctx, task)

def _nps_follow_up(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    rating = ctx.get("nps_previous_rating", "Unknown")
    verbatim = ctx.get("nps_followup_comment", "")
    task = f"Write NPS follow-up to {rating} rating. Feedback: '{verbatim}'. Acknowledge, commit to action without inventing details."
    return _base_email_prompt(scaffold, ctx, task)

# -----------------------------
# Recipe registry + dispatcher
# -----------------------------

PROMPT_RECIPES: Dict[str, Callable[[Dict[str, str], Dict[str, Any]], str]] = {
    "Renewal Email": _renewal_email,
    "QBR Brief": _qbr_brief,
    "Client Follow-up": _client_followup,
    "Proposal / RFP Response": _proposal_rfp,
    "Upsell / Cross-sell Outreach": _upsell_cross_sell,
    "Client Risk Alert": _client_risk_alert,
    "Client Snapshot & Risk Signals": _client_snapshot,
    "Objection Coach": _objection_coach,
    "NPS Engagement": _nps_engagement,
    "NPS Follow-up": _nps_follow_up,
}


def fill_recipe(recipe_name: str, lang_code: str, ctx: Dict[str, Any]) -> str:
    scaffold = SCAFFOLDS.get(lang_code, SCAFFOLDS["en"])
    recipe_fn = PROMPT_RECIPES.get(recipe_name)
    if not recipe_fn:
        raise ValueError(f"Unknown recipe: {recipe_name}")
    return recipe_fn(scaffold, ctx)


def shape_output(
    prompt_text: str,
    output_target: str,
    client_name: str,
    recipe_name: str,
) -> str:
    if output_target == "email-only output":
        return prompt_text + "\n\nOutput only the email body."
    return prompt_text
