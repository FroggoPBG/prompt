# --------------------------------------------------------------
# Core prompt scaffolds, recipes, and builders used by the UI.
# No external APIs; Python 3.9+ compatible.
# --------------------------------------------------------------

from __future__ import annotations
from typing import Dict, List

# --------------------------------------------------------------
# Quick pointers a CSM can insert in NPS follow-ups
# --------------------------------------------------------------
NPS_KB = {
    "hk_reported_cases_filter": (
        "To view reported cases only: scroll to the Publication tab and click “Hong Kong Cases.” "
        "This filters the results to reported cases only."
    ),
    "pg_crypto_pointer": (
        "Cryptocurrency legal resources are available under Practical Guidance → Financial Services → "
        "Fintech & Virtual Assets."
    ),
}

# --------------------------------------------------------------
# Language scaffolds (email drafting focus)
# --------------------------------------------------------------
SCAFFOLDS: Dict[str, Dict[str, str]] = {
    "en": {
        "name": "English",
        "sys": (
            "You are an assistant for Customer Success in the legal-tech domain at LexisNexis. "
            "Respond with a professional, concise email to be sent to a client. "
            "Use the structure and headings provided."
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
            "你是 LexisNexis 法律科技领域的客户成功助理。请产出一封可直接发送给客户的专业电子邮件，"
            "并使用下列结构与标题。"
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
            "당신은 LexisNexis 법률 테크 분야의 고객 성공 담당자입니다. "
            "아래 구조와 제목을 사용하여 고객에게 바로 보낼 수 있는 전문적이고 간결한 이메일을 작성하세요."
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
            "あなたは LexisNexis のリーガルテック領域におけるカスタマーサクセス担当です。"
            "以下の構成・見出しで、顧客にそのまま送付できる簡潔なプロフェッショナルメールを作成してください。"
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

# --------------------------------------------------------------
# Global picklists used across the UI
# --------------------------------------------------------------
LN_CONTEXT: Dict[str, List[str]] = {
    "client_types": ["law firm", "corporate", "government", "in-house legal"],
    "regions": ["Hong Kong", "Japan", "Korea", "Singapore"],
    "practice_areas": [
        "Financial services", "Litigation", "Compliance", "Arbitration",
        "Personal injury", "Company", "Corporate", "IP",
        "Criminal", "Contract", "Tort"
    ],
    "stages": [
        "New", "Renewal", "Expansion", "Cancellation",
        "Low usage", "Complaint", "Previous negative comments",
        "Previous positive comments",
    ],
    "products": ["Lexis+", "Practical Guidance", "Lexis Advance", "Lexis Red", "Lexis+ AI"],
    "tones": ["auto", "warm", "consultative", "confident", "polite", "apologetic", "neutral"],
    "lengths": ["short", "medium", "long"],
    "outputs": ["plain prompt"],
}

# --------------------------------------------------------------
# Supported recipes (use-cases)
# --------------------------------------------------------------
PROMPT_RECIPES: List[str] = [
    "Renewal Email",
    "QBR Brief",
    "Client Follow-up",
    "Proposal / RFP Response",
    "Upsell / Cross-sell Outreach",
    "Client Risk Alert",
    "Client Snapshot & Risk Signals",
    "Objection Coach",
    "NPS Engagement",
    "NPS Follow-up",  # NEW
]

# --------------------------------------------------------------
# Helpers
# --------------------------------------------------------------
def _join_nonempty(items: List[str]) -> str:
    return "\n".join([f"- {x}" for x in items if x and str(x).strip()])

def _variant_from_nps(label: str) -> str:
    if not label:
        return "unknown"
    t = label.lower()
    if "promoter" in t or "9" in t or "10" in t:
        return "promoter"
    if "passive" in t or "7" in t or "8" in t:
        return "passive"
    if "detractor" in t or any(n in t for n in list("0123456")):
        return "detractor"
    return "unknown"

# --------------------------------------------------------------
# Main recipe builder
# --------------------------------------------------------------
def build_brief(recipe: str, lang_code: str, ctx: dict) -> str:
    s = SCAFFOLDS.get(lang_code, SCAFFOLDS["en"])

    # Common fields from context
    role = ctx.get("role", "Customer Success Manager")
    goal = ctx.get("goal", recipe)
    client_name = ctx.get("client_name") or "client"
    client_type = ctx.get("client_type") or "n/a"
    region = ctx.get("region") or "n/a"
    practice_areas = ", ".join(ctx.get("practice_areas") or []) or "n/a"
    products_used = ", ".join(ctx.get("products_used") or []) or "n/a"
    relationship_stage = ctx.get("relationship_stage") or "n/a"
    tone = ctx.get("tone") or "auto"
    length = ctx.get("length") or "medium"

    # Deliverables / Info gather templates
    deliverables: List[str] = []
    info_gather: List[str] = [
        "Client name, type, region, practice area(s)",
        "Products in use; relationship stage",
        "Usage metrics / adoption; time saved / ROI evidence",
        "NPS score / theme (if relevant)",
        "Contract timing (if renewal) and any pricing notes",
        "Preferred language and tone",
    ]
    body_instruction = "Draft a concise, professional email."

    r = recipe

    # ---------- Recipe-specific rules ----------
    if r == "Renewal Email":
        deliverables = [
            "Open with appreciation and acknowledge pricing feedback if present.",
            "Quantify value delivered (usage metrics, outcomes).",
            "Highlight forward-looking value (relevant features, PG topics, upcoming releases).",
            "Propose a value review; include 2–3 date/time options.",
        ]
        body_instruction = (
            "Draft a warm, consultative renewal email that reframes cost to value and closes with a clear CTA."
        )

    elif r == "QBR Brief":
        deliverables = [
            "Summarize usage & engagement trends.",
            "List notable wins and measurable outcomes.",
            "Call out underused areas and recommended actions.",
            "Propose next steps and owners.",
        ]
        body_instruction = "Draft a data-driven but succinct QBR summary email."

    elif r == "Client Follow-up":
        deliverables = [
            "Recap the meeting date and the topics discussed.",
            "List follow-ups and owners with dates.",
            "Invite questions and next step scheduling.",
        ]
        body_instruction = "Draft a crisp follow-up email that confirms actions and timelines."

    elif r == "Proposal / RFP Response":
        deliverables = [
            "Acknowledge the opportunity and restate the scope.",
            "Highlight differentiators aligned to the sector and requirements.",
            "Confirm timeline and request clarifications if any.",
        ]
        body_instruction = "Draft a concise proposal / RFP response cover email."

    elif r == "Upsell / Cross-sell Outreach":
        deliverables = [
            "Connect client pains to specific LexisNexis products.",
            "Reference relevant case studies or ROI points.",
            "Offer a brief discovery/enablement session.",
        ]
        body_instruction = "Draft an outreach email that is helpful, not pushy."

    elif r == "Client Risk Alert":
        deliverables = [
            "State the risk signal and severity neutrally.",
            "Propose mitigation plan (enablement, cadence, owners).",
            "Invite a quick sync to align on next steps.",
        ]
        body_instruction = "Draft a respectful email to address risk and align on a mitigation plan."

    elif r == "Client Snapshot & Risk Signals":
        deliverables = [
            "Provide quick org snapshot and recent engagement.",
            "List likely challenges and opportunity signals.",
            "Suggest tailored next steps.",
        ]
        body_instruction = "Draft a short research-style email giving a client snapshot and signals."

    elif r == "Objection Coach":
        deliverables = [
            "Acknowledge the concern empathetically.",
            "Provide 1–2 data points reinforcing value.",
            "Ask one strategic question that refocuses on outcomes.",
        ]
        body_instruction = "Draft email language to handle the objection constructively."

    elif r == "NPS Engagement":
        nps_variant = _variant_from_nps(ctx.get("nps_previous_rating", ""))
        deliverables = [
            f"Adapt tone to prior NPS ({nps_variant}).",
            "Briefly state why feedback matters now.",
            "Provide survey link and a concise CTA.",
        ]
        body_instruction = (
            "Draft a short NPS engagement email. "
            "Promoters: appreciative & collaborative. "
            "Passives: humble & improvement-oriented. "
            "Detractors: sincere, non-defensive, respectful."
        )

    elif r == "NPS Follow-up":
        prev = ctx.get("nps_follow_rating", "")
        comment = (ctx.get("nps_follow_comment") or "").strip()
        ctype = (ctx.get("nps_follow_type") or "").strip()
        hint_key = ctx.get("nps_follow_hint")
        escalate = bool(ctx.get("nps_follow_escalate"))
        team_note = (ctx.get("nps_follow_note") or "").strip()

        variant = _variant_from_nps(prev)

        deliverables = [
            f"Adapt tone to prior NPS ({variant}).",
            "Open by thanking them and referencing their exact comment (quote briefly).",
            "Address based on type: how-to, feature request, bug/issue, or general praise/concern.",
            "Offer a helpful next step: quick tip, link/where to click, or request clarifying needs.",
            "Close with clear CTA (reply or brief call) and appreciation.",
        ]

        if hint_key and hint_key in NPS_KB:
            deliverables.append(f"Include pointer: {NPS_KB[hint_key]}")

        if escalate:
            deliverables.append("Inform them the feedback has been shared with the relevant internal team.")
            if team_note:
                deliverables.append(f"Internal note (do not send verbatim): {team_note}")

        if ctype:
            deliverables.append(f"Comment type noted: {ctype}")

        if comment:
            deliverables.append(f"Client comment to reference: “{comment}”")

        body_instruction = (
            "Draft a concise follow-up email tailored to their rating and comment; "
            "use appreciative, improvement-oriented, or sincere tone as appropriate."
        )

    # ---------- Compose ----------
    req_block = _join_nonempty(deliverables)
    info_block = _join_nonempty(info_gather)
    extras = _join_nonempty([
        "Respect confidentiality; avoid legal advice.",
        "Be precise; prefer verifiable statements.",
        "Link outcomes/ROI to metrics where possible.",
        "Suggest next steps with owners & dates.",
    ])

    context_line = (
        f"Client: {client_name}; Type: {client_type}; Region: {region}; "
        f"Practice: {practice_areas}; Products: {products_used}; Stage: {relationship_stage}."
    )

    brief = (
        f"[system]\n{s['sys']}\n\n"
        f"[user]\n"
        f"**{s['role_lbl']}**: {role}\n"
        f"**{s['goal_lbl']}**: {goal}\n"
        f"**{s['ctx_lbl']}**: {context_line}\n"
        f"**{s['req_lbl']}**:\n{req_block}\n"
        f"**{s['info_lbl']}**:\n{info_block}\n"
        f"**{s['tone_lbl']}**: {tone}\n"
        f"**{s['len_lbl']}**: {length}\n\n"
        f"{s['extra_lbl']}:\n{extras}\n\n"
        f"{body_instruction}\n"
    )
    return brief


def fill_recipe(recipe: str, lang_code: str, ctx: dict) -> str:
    return build_brief(recipe, lang_code, ctx)


def shape_output(text: str, output_format: str, client_name: str, recipe: str) -> str:
    # Currently we only expose "plain prompt"; passthrough for future extensibility.
    return text
