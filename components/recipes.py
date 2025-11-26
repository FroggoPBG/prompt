# components/recipes.py
# Core language scaffolds, context, and prompt recipes.
from __future__ import annotations

from typing import Dict, List, Callable, Any

# -----------------------------
# Language scaffolds (email focus) - Enhanced with more languages for multi-language support
# -----------------------------

SCAFFOLDS: Dict[str, Dict[str, str]] = {
    "en": {
        "name": "English",
        "sys": (
            "You are an assistant for client-facing teams (Sales and Customer Success) "
            "in the legal-tech domain at LexisNexis. "
            "Respond with a professional, concise email draft to be sent to a client. "
            "Use the structure and headings given. Avoid legal advice."
        ),
        "role_lbl": "ROLE",
        "goal_lbl": "GOAL",
        "ctx_lbl": "CONTEXT",
        "req_lbl": "DELIVERABLE REQUIREMENTS",
        "info_lbl": "INFORMATION TO GATHER",
        "tone_lbl": "TONE",
        "len_lbl": "LENGTH",
        "extra_lbl": "Additional notes & constraints",
        "nps_pasted_lbl": "NPS Verbatim Insights (pasted)",
        "nps_internal_lbl": "NPS Insights (internal)",
    },
    "ja": {
        "name": "Japanese",
        "sys": (
            "あなたはLexisNexisのリーガルテック分野で、クライアント対応チーム（営業およびカスタマーサクセス）のアシスタントです。"
            "クライアントに送信するプロフェッショナルで簡潔なメールドラフトで応答してください。"
            "与えられた構造と見出しを使用してください。法的アドバイスは避けてください。"
        ),
        "role_lbl": "役割",
        "goal_lbl": "目標",
        "ctx_lbl": "コンテキスト",
        "req_lbl": "成果物要件",
        "info_lbl": "収集する情報",
        "tone_lbl": "トーン",
        "len_lbl": "長さ",
        "extra_lbl": "追加の注意事項と制約",
        "nps_pasted_lbl": "NPS 逐語洞察（貼り付け）",
        "nps_internal_lbl": "NPS 洞察（内部）",
    },
    "zh": {
        "name": "Chinese (Simplified)",
        "sys": (
            "您是LexisNexis法律技术领域中面向客户团队（销售和客户成功）的助手。"
            "以专业、简洁的电子邮件草稿回复，该草稿将发送给客户。"
            "使用给定的结构和标题。避免法律建议。"
        ),
        "role_lbl": "角色",
        "goal_lbl": "目标",
        "ctx_lbl": "上下文",
        "req_lbl": "交付要求",
        "info_lbl": "要收集的信息",
        "tone_lbl": "语气",
        "len_lbl": "长度",
        "extra_lbl": "附加说明和约束",
        "nps_pasted_lbl": "NPS 逐字洞察（粘贴）",
        "nps_internal_lbl": "NPS 洞察（内部）",
    },
    # Add more languages as needed, e.g., "ko" for Korean, etc.
}

# -----------------------------
# Shared LexisNexis context - Enhanced with more options for extensibility
# -----------------------------

LN_CONTEXT: Dict[str, Any] = {
    "outputs": ["plain prompt", "email-only output"],
    "client_types": [
        "in-house legal",
        "law firm",
        "government",
        "academic",
        "corporate (non-legal)",
        "other",  # Enhanced: Added for flexibility
    ],
    "regions": [
        "Hong Kong",
        "Singapore",
        "Japan",
        "South Korea",
        "Australia / NZ",
        "Other APAC",
        "Global",
    ],
    "practice_areas": [
        "Financial services",
        "Litigation / disputes",
        "Corporate / commercial",
        "Regulatory / compliance",
        "Intellectual property",
        "Employment",
        "Tax",
        "Other",
    ],
    "products": [
        "Lexis+",
        "Lexis Advance",
        "Practical Guidance",
        "Lexis Draft / drafting tools",
        "News / Company information",
        "NPS / analytics dashboards",
    ],
    "stages": [
        "Prospect / discovery",
        "Onboarding",
        "Adoption",
        "Renewal",
        "Expansion / upsell",
        "At-risk / renewal rescue",
    ],
    "tones": [
        "auto (based on context)",
        "warm",
        "formal",
        "consultative",
        "apologetic",
        "direct",
    ],
    "lengths": ["very short", "short", "medium", "long"],
}

# -----------------------------
# Helper: base email prompt builder - Enhanced with more dynamic elements
# -----------------------------


def _base_email_prompt(scaffold: Dict[str, str], ctx: Dict[str, Any], body_instruction: str) -> str:
    s = scaffold
    # For convenience
    client_name = ctx.get("client_name") or "client"
    client_type = ctx.get("client_type") or "n/a"
    region = ctx.get("region") or "n/a"
    practice = ", ".join(ctx.get("practice_areas") or []) or "n/a"
    products = ", ".join(ctx.get("products_used") or []) or "n/a"
    stage = ctx.get("relationship_stage") or "n/a"
    tone = ctx.get("tone") or "auto"
    length = ctx.get("length") or "medium"

    ex_input = ctx.get("ex_input") or ""
    ex_output = ctx.get("ex_output") or ""

    nps_verbatim = ctx.get("nps_info") or ""
    internal_nps = ctx.get("nps_internal") or ""

    lines: List[str] = []

    lines.append("[system]")
    lines.append(s["sys"])
    lines.append("")
    lines.append("[user]")
    lines.append(f"**{s['role_lbl']}**: Client-facing professional (Sales / Customer Success)")
    lines.append(f"**{s['goal_lbl']}**: {ctx.get('goal_text','Client communication')}.")
    lines.append(
        f"**{s['ctx_lbl']}**: Client: {client_name}; Type: {client_type}; "
        f"Region: {region}; Practice: {practice}; Products: {products}; Stage: {stage}."
    )
    lines.append(f"**{s['req_lbl']}**:")
    lines.extend(body_instruction.strip().splitlines())
    lines.append(f"**{s['info_lbl']}**:")
    lines.append("- Client name, type, region, practice area(s)")
    lines.append("- Products in use; relationship stage")
    lines.append("- Usage metrics / adoption; time saved / ROI evidence")
    lines.append("- NPS score / theme (if relevant)")
    lines.append("- Contract timing (if renewal) and any pricing notes")
    lines.append("- Preferred language and tone")
    lines.append(f"**{s['tone_lbl']}**: {tone}")
    lines.append(f"**{s['len_lbl']}**: {length}")
    lines.append("")
    lines.append(f"{s['extra_lbl']}:")
    lines.append("- Respect confidentiality; avoid legal advice.")
    lines.append("- Be precise; prefer verifiable statements.")
    lines.append("- Link outcomes/ROI to metrics where possible.")
    lines.append("- Suggest next steps with owners & dates.")
    if nps_verbatim:
        lines.append("")
        lines.append(f"**{s['nps_pasted_lbl']}**:")
        lines.append(nps_verbatim.strip())
    if internal_nps or ctx.get("nps_internal_summary"):
        lines.append("")
        lines.append(f"**{s['nps_internal_lbl']}**:")
        lines.append((internal_nps or ctx.get("nps_internal_summary", "")).strip())

    if ex_input or ex_output:
        lines.append("")
        lines.append("Few-shot examples (optional):")
        if ex_input:
            lines.append(f"- Example input: {ex_input}")
        if ex_output:
            lines.append(f"- Example output: {ex_output}")

    lines.append("")
    lines.append("Draft the email now.")
    return "\n".join(lines)


# -----------------------------
# Individual recipes - Enhanced with minor tweaks for better personalization
# -----------------------------

def _renewal_email(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    scenario = ctx.get("renewal_scenario", "value")
    if scenario == "low_usage_pricing":
        body = """
- Mention upcoming renewal date and contract basics.
- Gently acknowledge low or declining usage patterns in a non-accusatory tone.
- Express concern that the client may not be getting full value from the current subscription.
- Offer to explore whether the issue is training, content fit, or changing firm needs.
- Propose a consultative call to:
  - review usage together,
  - identify gaps, and
  - consider resizing / simplifying the package so they only pay for what they truly use.
- Emphasise partnership: your goal is to fix the setup, not to push an unchanged renewal.
- Keep tone empathetic, calm, and focused on solutions.
"""
    else:
        body = """
- Mention upcoming renewal date and thank them for their partnership.
- Highlight specific usage patterns (frequency, key modules, engagement indicators) that show value.
- Connect usage back to their practice area or matter types where possible.
- Acknowledge they will be reviewing budget and priorities.
- Invite a call to:
  - confirm what is working well,
  - identify new needs, and
  - ensure the package is aligned with their 2025–2026 goals.
- Maintain a warm, relationship-focused tone.
"""

    ctx = dict(ctx)
    ctx["goal_text"] = "Renewal Email"

    main_prompt = _base_email_prompt(scaffold, ctx, body)

    # Separate the additional scenario guidance with a marker
    additional_guidance = """
Additional scenario guidance for the model:
- If usage is low and pricing concerns exist, follow this style:
  "I'm an account manager at LexisNexis in Hong Kong reaching out to a law firm client about their upcoming subscription renewal. The client has previously expressed pricing concerns, and their usage data shows concerning patterns. Their usage data indicates low frequency, limited module utilisation, and low engagement. Write a professional, empathetic, consultative email that acknowledges this, explores root causes, offers to resize the package if needed, and positions LexisNexis as a partner who wants them to only pay for what is useful."
- If usage is healthy but pricing is still sensitive, follow this style:
  "I'm an account manager at LexisNexis in Hong Kong reaching out to a law firm client about their upcoming subscription renewal. The client has previously expressed pricing concerns, so I need to be sensitive to cost while demonstrating value. Their usage shows healthy frequency, strong use of specific modules, and meaningful engagement. Write a professional, warm email that highlights concrete value from usage, invites a collaborative renewal discussion, and makes the client feel heard and valued."
"""

    return main_prompt + "\n\n[ADDITIONAL_GUIDANCE]\n" + additional_guidance


def _qbr_brief(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
- Summarise the review period (e.g., last quarter, FY).
- Provide a brief client snapshot: products in use, main users/teams, key goals.
- Highlight 3–5 usage / outcome headlines (e.g., time saved, matters supported).
- Call out any underused features or modules with potential impact.
- Suggest 2–3 recommendations and next steps with owners and timelines.
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "QBR Brief"
    return _base_email_prompt(scaffold, ctx, body)


def _client_followup(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
- Reference the last meeting date and 1–2 key topics discussed.
- Recap any actions you committed to and their status.
- Provide links or resources promised (e.g., training, content, case studies).
- Ask 1–2 specific follow-up questions.
- Close with a clear, polite CTA (scheduling next call, confirming decisions, etc.).
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "Client Follow-up"
    return _base_email_prompt(scaffold, ctx, body)


def _proposal_rfp(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
- Acknowledge receipt of the RFP / proposal request.
- Briefly restate the client's objectives in your own words.
- Map LexisNexis capabilities to 3–5 key requirements.
- Highlight differentiators and relevant regional / product fit.
- Offer a clear next step (e.g., workshop, Q&A session, timeline confirmation).
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "Proposal / RFP Response"
    return _base_email_prompt(scaffold, ctx, body)


def _upsell_cross_sell(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
- Start from existing value: how current products support their work.
- Introduce 1–2 additional modules or products with clear linkage to their practice.
- Reference any NPS / feedback themes or usage gaps that support the upsell story.
- Suggest specific use cases, not generic benefits.
- Offer a low-friction next step (short demo, pilot, or trial).
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "Upsell / Cross-sell Outreach"
    return _base_email_prompt(scaffold, ctx, body)


def _client_risk_alert(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
- Summarise the risk trigger (declining usage, delayed renewal, negative feedback, etc.).
- Draft an email that calmly acknowledges the situation without sounding defensive.
- Offer a concrete plan: training, check-in cadence, or configuration review.
- Emphasise partnership and willingness to adapt.
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "Client Risk Alert"
    return _base_email_prompt(scaffold, ctx, body)


def _client_snapshot(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
- Draft an internal-facing summary email that could be reused with the client.
- Include client profile, key contacts, segments, products in use, and regions.
- Summarise usage trends, NPS signals, and key risks/opportunities.
- Keep the tone factual and concise.
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "Client Snapshot & Risk Signals"
    return _base_email_prompt(scaffold, ctx, body)


def _objection_coach(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
- Draft an email reply to a specific objection (price, usability, competitor, etc.).
- Acknowledge the concern sincerely.
- Provide 2–3 tailored points addressing the objection with evidence where possible.
- Offer a next step (e.g., targeted demo, training session, or alternative configuration).
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "Objection Coach"
    return _base_email_prompt(scaffold, ctx, body)


def _nps_engagement(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    prior = ctx.get("nps_previous_rating", "Passive (7–8)")
    prior_label = prior.split()[0]

    body = f"""
- Draft a short NPS engagement email that adapts tone based on previous rating: {prior_label}.
- Promoters (9–10): warm, appreciative, collaborative; emphasise partnership and invite ideas.
- Passives (7–8): humble, improvement-oriented; ask what would make the experience 'great'.
- Detractors (0–6): sincere, non-defensive, respectful; acknowledge issues and invite candid feedback.
- Briefly state why feedback matters now and how it will be used.
- Include the survey link / CTA from the context.
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "NPS Engagement"
    return _base_email_prompt(scaffold, ctx, body)


def _nps_follow_up(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    rating = ctx.get("nps_previous_rating", "Promoter (9–10)")
    comment_type = ctx.get("nps_comment_type", "Feature request")
    verbatim = ctx.get("nps_followup_comment", "")

    body = f"""
- Draft a concise NPS follow-up email tailored to:
  - Previous NPS rating: {rating}
  - Comment type: {comment_type}
- Open by thanking them and referencing their exact comment (quote or brief paraphrase).
- For promoters: appreciative, partnership-focused, offer next best step (tip, link, or quick call).
- For passives: curious, improvement-oriented, ask 1–2 focused questions.
- For detractors: apologetic but not defensive, reference actions taken or escalation to the right team.
- If relevant, include a helpful pointer (e.g., where to find a feature or resource).
- Invite them to reply with more detail or to jump on a short call.
- Use the pasted comment verbatim as input: \"{verbatim[:120]}...\"
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "NPS Follow-up"
    return _base_email_prompt(scaffold, ctx, body)


# -----------------------------
# Recipe registry + dispatcher - Enhanced with new recipes for extensibility
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
    # Enhanced: Added new example recipes
    "Event Invite Follow-Up": _client_followup,  # Reuse existing for simplicity
    "Contract Negotiation Starter": _proposal_rfp,  # Reuse and adapt as needed
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
    """
    For now we keep it simple:
    - 'plain prompt' → unchanged
    - 'email-only output' → hint to the model to output only the email body
    """
    if output_target == "email-only output":
        return (
            prompt_text
            + "\n\n[assistant]\nPlease output only the final email body, without repeating the instructions."
        )
    return prompt_text
