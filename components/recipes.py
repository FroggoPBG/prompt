# components/recipes.py
# ---------------------------------------------------------------------
# Core prompt scaffolds, recipes, and builders used by the Streamlit UI.
# Safe to use without any external APIs. Python 3.9+ compatible.
# ---------------------------------------------------------------------

from __future__ import annotations
from typing import Dict, List
# Handy inserts the CSM can include in one click
NPS_KB = {
    "hk_reported_cases_filter": (
        "To view reported cases only: scroll to the Publication tab and click “Hong Kong Cases.” "
        "This filters results to reported cases only."
    ),
    "pg_crypto_pointer": (
        "Cryptocurrency legal resources are available under Practical Guidance → Financial Services → "
        "Fintech & Virtual Assets."
    ),
}

# ----------------------------
# Language scaffolds (email drafting focus)
# ----------------------------
SCAFFOLDS = {
    "en": {
        "name": "English",
        "sys": (
            "You are a consultant for Customer Success in the legal-tech domain at LexisNexis. "
            "Draft a professional, clear, and client-ready email that another AI can generate directly. "
            "Use the fields and headings below to inform tone, context, and purpose. "
            "Do not describe a prompt or summary — focus on writing an effective client email. "
            "Maintain accuracy, confidentiality, and a consultative tone appropriate to the situation."
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
    "zh": {
        "name": "中文 (简体)",
        "sys": (
            "你是 LexisNexis 法律科技领域的客户成功助理。请根据以下结构撰写一封专业、清晰、可直接发送给客户的电子邮件。"
            "不要描述提示或摘要，只写邮件内容。请确保表达准确、语气得体，并符合客户沟通的专业语境。"
        ),
        "role_lbl": "角色",
        "goal_lbl": "目标",
        "ctx_lbl": "上下文",
        "req_lbl": "交付要求",
        "info_lbl": "需收集信息",
        "tone_lbl": "语气",
        "len_lbl": "篇幅",
        "extra_lbl": "补充说明与约束",
        "nps_pasted_lbl": "NPS 文本洞察（粘贴）",
        "nps_internal_lbl": "内部 NPS 洞察",
    },
    "ko": {
        "name": "한국어",
        "sys": (
            "당신은 LexisNexis 법률 테크 분야의 고객 성공 어시스턴트입니다. "
            "아래 구조를 참고하여 고객에게 바로 보낼 수 있는 전문적이고 명확한 이메일을 작성하세요. "
            "프롬프트나 요약을 설명하지 말고, 실제 이메일 내용을 작성하세요. "
            "정확성과 기밀을 지키며, 상황에 맞는 컨설팅형 톤을 유지하세요."
        ),
        "role_lbl": "역할",
        "goal_lbl": "목표",
        "ctx_lbl": "컨텍스트",
        "req_lbl": "산출물 요구사항",
        "info_lbl": "수집할 정보",
        "tone_lbl": "톤",
        "len_lbl": "길이",
        "extra_lbl": "추가 메모 및 제약",
        "nps_pasted_lbl": "NPS 원문 인사이트(붙여넣기)",
        "nps_internal_lbl": "내부 NPS 인사이트",
    },
    "ja": {
        "name": "日本語",
        "sys": (
            "あなたは LexisNexis のリーガルテック分野におけるカスタマーサクセスアシスタントです。"
            "以下の構成に従い、クライアントに直接送信できるプロフェッショナルで明確なメール本文を作成してください。"
            "プロンプトや要約は書かず、メール本文に集中してください。"
            "正確性と機密性を守り、状況にふさわしいコンサルティブなトーンを維持してください。"
        ),
        "role_lbl": "役割",
        "goal_lbl": "ゴール",
        "ctx_lbl": "コンテキスト",
        "req_lbl": "成果物要件",
        "info_lbl": "収集すべき情報",
        "tone_lbl": "トーン",
        "len_lbl": "長さ",
        "extra_lbl": "補足・制約",
        "nps_pasted_lbl": "NPS テキスト・インサイト（貼り付け）",
        "nps_internal_lbl": "社内 NPS インサイト",
    },
}


# ----------------------------
# General picklists for UI
# ----------------------------
LN_CONTEXT = {
    "outputs": ["plain text", "email", "crm note"],
    "client_types": ["law firm", "corporate", "government", "in-house legal"],
    "regions": ["Hong Kong", "Japan", "Korea", "Singapore"],
    "practice_areas": [
        "Financial services", "Litigation", "Compliance", "Arbitration",
        "Tort", "Personal injury", "Company", "Corporate", "IP", "Criminal", "Contract"
    ],
    "stages": ["New", "Renewal", "Expansion", "Cancellation", "Low usage", "Complaint"],
    "products": ["Lexis+", "Practical Guidance", "Lexis Advance", "Lexis Red", "Lexis+ AI"],
    "tones": ["auto", "warm", "consultative", "confident", "formal", "polite", "apologetic", "neutral", "persuasive"],
    "lengths": ["short", "medium", "long"],
}

PROMPT_RECIPES = [
    "Renewal Email",
    "QBR Brief",
    "Client Follow-up",
    "Proposal / RFP Response",
    "Upsell / Cross-sell Outreach",
    "Client Risk Alert",
    "Client Snapshot & Risk Signals",
    "Objection Coach",
    "NPS Engagement",
    "NPS Follow-up", 
]

# ----------------------------
# Helpers
# ----------------------------

def _tone_auto(lang: str, region: str, stage: str) -> str:
    # Simple localization heuristic for "auto"
    jpkr_formal = {"Japan", "Korea"}
    if region in jpkr_formal:
        base = "polite"
    else:
        base = "consultative"
    if stage.lower() in {"complaint", "cancellation"}:
        return "apologetic"
    return base

def _fmt_list(items: List[str]) -> str:
    return "\n".join([f"- {x}" for x in items])

def _normalize_lines(text: str) -> List[str]:
    """Best-effort cleanup to produce readable bullets from raw text."""
    if not text:
        return []
    raw = [ln.strip(" \t-•\u2022") for ln in text.splitlines() if ln.strip()]
    lines: List[str] = []
    for ln in raw:
        # keep headings and short bullets; split very long sentences on '; '
        if "; " in ln and len(ln) > 140:
            parts = [p.strip() for p in ln.split("; ") if p.strip()]
            lines.extend(parts)
        else:
            lines.append(ln)
    return lines[:20]

def _render_nps_text_block(lang: str, text: str) -> str:
    if not text:
        return ""
    lbl = SCAFFOLDS[lang]["nps_pasted_lbl"]
    bullets = _normalize_lines(text)
    return f"**{lbl}:**\n" + _fmt_list(bullets)

# ----------------------------
# Main brief builder
# ----------------------------

def build_brief(
    lang: str,
    recipe_name: str,
    ctx: Dict
) -> str:
    """
    Build the *prompt brief* used by another AI to generate the final comms.
    """
    sc = SCAFFOLDS[lang]
    role = sc["role_lbl"]; goal = sc["goal_lbl"]; context = sc["ctx_lbl"]
    req = sc["req_lbl"]; info = sc["info_lbl"]; tone_lbl = sc["tone_lbl"]
    len_lbl = sc["len_lbl"]; extra = sc["extra_lbl"]

    # Tone resolve
    tone = ctx.get("tone", "auto")
    if tone == "auto":
        tone = _tone_auto(lang, ctx.get("region", "Hong Kong"), ctx.get("relationship_stage", "New"))

    # Shared context tokens
    client_name = ctx.get("client_name", "").strip() or "client"
    ctype = ctx.get("client_type", "law firm")
    region = ctx.get("region", "Hong Kong")
    practice = ", ".join(ctx.get("practice_areas", []) or [])
    products = ", ".join(ctx.get("products_used", []) or [])
    stage = ctx.get("relationship_stage", "New")
    usage = ctx.get("usage_metrics", "")
    time_saved = ctx.get("time_saved", "")
    nps_info = ctx.get("nps_info", "")
    length = ctx.get("length", "medium")

    # Product highlights auto-include (simple example)
    highlights: List[str] = []
    if ctx.get("include_highlights"):
        if "Practical Guidance" in products:
            highlights.append("Practical Guidance: curated precedents, checklists, and how-to guidance.")
        if "Lexis+ AI" in products:
            highlights.append("Lexis+ AI: trusted, grounded responses with citations to primary law.")
        if "Lexis+" in products and "Lexis+ AI" not in products:
            highlights.append("Lexis+: integrated research, analytics and drafting tools.")

    # Guided extras per recipe
    deliverable: List[str] = []
    gather: List[str] = [
        "Client name, type, region, practice area(s)",
        "Products in use; relationship stage",
        "Usage metrics / adoption; time saved / ROI evidence",
        "NPS score / theme (if relevant)",
        "Contract timing (if renewal) and any pricing notes",
        "Preferred language and tone",
    ]

    # Body instruction (what we want the AI to write)
    body = ""

    # ---------- Per recipe ----------
    r = recipe_name

    if r == "Renewal Email":
        deliverable = [
            "Open with appreciation; acknowledge any pricing concerns.",
            "Demonstrate concrete value delivered (usage metrics, outcomes).",
            "Highlight forward-looking value (features, PG topics, roadmap).",
            "Propose a collaborative value review; include 2–3 meeting options.",
        ]
        # guided
        if ctx.get("contract_details"):
            deliverable.append(f"Include contract context: {ctx['contract_details']}.")
        if ctx.get("meeting_options"):
            deliverable.append(f"Offer meeting time(s): {ctx['meeting_options']}.")

        body = (
            "Draft a consultative renewal email (250–350 words) reframing from cost to value. "
            "Be warm and confident, not pushy."
        )

    elif r == "QBR Brief":
        deliverable = [
            "Summarize usage & engagement trends.",
            "Show wins/metrics since last period.",
            "Call out underused features & opportunities.",
            "Close with clear next-step recommendations."
        ]
        if ctx.get("qbr_window"):
            deliverable.insert(0, f"Review period: {ctx['qbr_window']}.")
        if ctx.get("qbr_sections"):
            deliverable.append("Emphasize sections: " + ", ".join(ctx["qbr_sections"]))
        if ctx.get("qbr_include_benchmarks"):
            deliverable.append("Include relevant industry benchmarks where helpful.")
        body = "Create a concise QBR narrative ready for slides or email summary."

    elif r == "Client Follow-up":
        deliverable = [
            "Recap meeting purpose and key takeaways.",
            "List action items with owners and dates.",
            "Confirm next meeting or check-in."
        ]
        if ctx.get("last_meeting_date"):
            deliverable.insert(0, f"Reference last meeting date: {ctx['last_meeting_date']}.")
        if ctx.get("meeting_topics"):
            deliverable.append("Topics covered: " + ctx["meeting_topics"])
        body = "Write a brief, friendly follow-up email."

    elif r == "Proposal / RFP Response":
        deliverable = [
            "Restate client needs in their language.",
            "Map capabilities to requirements; highlight differentiators.",
            "Include timeline and next steps.",
        ]
        if ctx.get("rfp_sector"):
            deliverable.insert(0, f"Client sector: {ctx['rfp_sector']}.")
        if ctx.get("rfp_scope"):
            deliverable.append("Scope/requirements: " + ctx["rfp_scope"])
        if ctx.get("rfp_differentiators"):
            deliverable.append("Differentiators: " + ctx["rfp_differentiators"])
        if ctx.get("rfp_deadline"):
            deliverable.append("Key deadline: " + ctx["rfp_deadline"])
        body = "Draft a crisp response outline suitable for proposal text."

    elif r == "Upsell / Cross-sell Outreach":
        deliverable = [
            "Lead with a relevant insight/pain point.",
            "Position the recommended product(s) to solve it.",
            "Offer enablement/trial/next step with a clear CTA."
        ]
        if ctx.get("pains"):
            deliverable.insert(0, "Pain points: " + ctx["pains"])
        if ctx.get("proposed_products"):
            deliverable.append("Proposed products: " + ", ".join(ctx["proposed_products"]))
        if ctx.get("case_studies"):
            deliverable.append("Reference case studies: " + ctx["case_studies"])
        body = "Write a short outreach email focused on business outcomes."

    elif r == "Client Risk Alert":
        deliverable = [
            "State the risk signal and likely impact.",
            "List 2–3 mitigation actions with owners and dates.",
            "Set cadence for follow-up and measurement."
        ]
        if ctx.get("risk_trigger"):
            deliverable.insert(0, f"Risk trigger: {ctx['risk_trigger']}.")
        if ctx.get("risk_severity"):
            deliverable.append(f"Severity (1-5): {ctx['risk_severity']}")
        if ctx.get("risk_mitigations"):
            deliverable.append("Mitigations to consider: " + ctx["risk_mitigations"])
        body = "Create an internal note or client-safe summary outlining the risk plan."

    elif r == "Client Snapshot & Risk Signals":
        deliverable = [
            "Client overview (size, practice focus, products).",
            "Recent news or events affecting priorities.",
            "3 likely challenges; churn or expansion signals.",
            "Clear suggestions for next actions."
        ]
        if ctx.get("prepared_by"):
            deliverable.insert(0, f"Prepared by: {ctx['prepared_by']}.")
        if ctx.get("last_engagement_date"):
            deliverable.append(f"Last engagement: {ctx['last_engagement_date']}")
        if ctx.get("risk_level"):
            deliverable.append(f"Risk level: {ctx['risk_level']}")
        body = "Generate a one-page snapshot to brief a CS/AE colleague."

    elif r == "Objection Coach":
        # dynamic objection choices
        ot = (ctx.get("objection_type") or "").lower()
        deliverable = [
            "Acknowledge the concern empathetically.",
            "Provide 2 data-backed value points.",
            "Ask 1 strategic question to re-focus on outcomes.",
        ]
        if ot:
            deliverable.insert(0, f"Objection focus: {ot}.")
        if ctx.get("objection_severity"):
            deliverable.append(f"Severity (1-5): {ctx['objection_severity']}")
        if ctx.get("competitor_name"):
            deliverable.append("Competitor named: " + ctx["competitor_name"])
        if ctx.get("supporting_data"):
            deliverable.append("Use supporting data: " + ", ".join(ctx["supporting_data"]))
        body = "Draft 3 short response options the CSM can adapt live."

    elif r == "NPS Engagement":
        # Variant line shows the single selected variant (not the triad)
        prev = ctx.get("nps_previous_rating", "")
        variant_txt = ""
        if "Promoter" in prev:
            variant_txt = "promoter"
        elif "Passive" in prev:
            variant_txt = "passive"
        elif "Detractor" in prev:
            variant_txt = "detractor"
        else:
            variant_txt = "unknown"

        deliverable = [
            f"Adapt tone to prior NPS ({variant_txt}).",
            "Briefly state why feedback matters now.",
            "Provide survey link and a concise CTA."
        ]
        if ctx.get("nps_survey_link"):
            deliverable.append("Use the provided survey link/CTA.")
        body = (
            "Draft a short NPS engagement email. "
            "Promoters: appreciative and collaborative. "
            "Passives: humble and improvement-oriented. "
            "Detractors: sincere, non-defensive, respectful."
        )
            elif r == "NPS Follow-up":
        # Inputs expected from UI
        prev = ctx.get("nps_follow_rating", "")  # Promoter/Passive/Detractor
        comment = (ctx.get("nps_follow_comment") or "").strip()
        ctype = (ctx.get("nps_follow_type") or "").strip()  # How-to / Feature / Bug / Praise
        hint_key = ctx.get("nps_follow_hint")  # kb key or "None"
        escalate = bool(ctx.get("nps_follow_escalate"))
        team_note = (ctx.get("nps_follow_note") or "").strip()

        # Show which variant we’re responding to
        variant = "unknown"
        if "Promoter" in prev:
            variant = "promoter"
        elif "Passive" in prev:
            variant = "passive"
        elif "Detractor" in prev:
            variant = "detractor"

        # Deliverable guidelines
        deliverable = [
            f"Adapt tone to prior NPS ({variant}).",
            "Open by thanking them for the feedback and referencing their exact comment.",
            "Address the comment based on its type (how-to, feature request, bug/issue, general praise/concern).",
            "Offer either a quick tip, a pointer to existing functionality, or an invitation to clarify needs.",
            "Close with a clear next step (reply or brief call) and appreciation."
        ]

        # Optional inserts
        if hint_key and hint_key in NPS_KB:
            deliverable.append(f"Include this helpful pointer: {NPS_KB[hint_key]}")

        if escalate:
            deliverable.append("Inform the client that the feedback has been shared with the relevant internal team.")
            if team_note:
                deliverable.append(f"Internal note (do not send verbatim): {team_note}")

        # Add specific asks by type
        if ctype:
            deliverable.append(f"Comment type noted: {ctype}")

        # Body instruction
        body = (
            "Draft a concise, respectful follow-up email tailored to their NPS rating and comment. "
            "If it’s a how-to question and a solution exists, provide the steps. "
            "If it’s a feature request, acknowledge, relate to roadmap/alternatives if applicable, and invite specifics. "
            "If it’s a bug/issue, acknowledge impact, set expectation that the team is reviewing, and offer an update path. "
            "Keep tone aligned to the rating (promoter: appreciative; passive: improvement-oriented; detractor: sincere, non-defensive)."
        )


    else:
        deliverable = ["Produce a clear, helpful response."]
        body = "Write a concise, professional message."

    # Compose main brief
    brief_lines: List[str] = []

    # System
    brief_lines.append(f"[system]\n{sc['sys']}\n")

    # User block
    brief_lines.append("[user]")
    brief_lines.append(f"**{role}**: Customer Success Manager")
    brief_lines.append(f"**{goal}**: {r} — create content ready to send or adapt.")
    brief_lines.append(
        f"**{context}**: Client: {client_name}; Type: {ctype}; Region: {region}; "
        f"Practice: {practice or 'n/a'}; Products: {products or 'n/a'}; Stage: {stage}."
    )

    if highlights:
        brief_lines.append("**Product highlights to consider**:")
        brief_lines.append(_fmt_list(highlights))

    # Requirements + Info
    brief_lines.append(f"**{req}**:")
    brief_lines.append(_fmt_list(deliverable))

    brief_lines.append(f"**{info}**:")
    brief_lines.append(_fmt_list(gather))

    # Tone/length
    brief_lines.append(f"**{tone_lbl}**: {tone}")
    brief_lines.append(f"**{len_lbl}**: {length}")

    # Optional context notes
    extras: List[str] = [
        "Respect confidentiality; avoid legal advice.",
        "Be precise; prefer verifiable statements.",
        "Link outcomes/ROI to metrics where possible.",
        "Suggest next steps with owners & dates.",
    ]
    if usage:
        extras.append(f"Include usage insight: {usage}")
    if time_saved:
        extras.append(f"Include efficiency/ROI note: {time_saved}")
    if nps_info:
        extras.append(f"NPS theme/quote: {nps_info}")

    brief_lines.append(f"\n{sc['extra_lbl']}:")
    brief_lines.append(_fmt_list(extras))

    # Attach pasted NPS text (no JSON required)
    nps_text = ctx.get("nps_text", "")
    if nps_text:
        brief_lines.append("\n" + _render_nps_text_block(lang, nps_text))

    # Final instruction
    brief_lines.append("\n" + body)

    return "\n".join(brief_lines).strip()


# ----------------------------
# Public API
# ----------------------------

def fill_recipe(recipe_name: str, lang: str, ctx: Dict) -> str:
    """Return the full prompt brief string."""
    if lang not in SCAFFOLDS:
        lang = "en"
    return build_brief(lang, recipe_name, ctx)


def shape_output(prompt_text: str, output_format: str, client_name: str, recipe_name: str) -> str:
    """
    Light post-formatting for different output targets.
    (No external templates to keep this self-contained.)
    """
    of = (output_format or "plain text").lower()
    if of == "email":
        # Wrap the brief as instructions for an email generator AI
        header = f"## Email brief for {client_name or 'client'} — {recipe_name}\n\n"
        return header + prompt_text
    elif of == "crm note":
        header = f"## CRM note for {client_name or 'client'} — {recipe_name}\n\n"
        return header + prompt_text
    # default: plain text
    return prompt_text
