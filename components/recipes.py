# ---------------------------------------------------------------
# Core prompt scaffolds, recipes, and builders used by the app UI.
# Safe to use without any external APIs. Python 3.9+ compatible.
# ---------------------------------------------------------------

from __future__ import annotations
from typing import Dict, List
from datetime import date

# ----------------------------
# Language scaffolds (email focus)
# ----------------------------
SCAFFOLDS: Dict[str, Dict[str, str]] = {
    "en": {
        "name": "English",
        "sys": (
            "You are an assistant for Customer Success and Sales in the legal-tech domain at LexisNexis. "
            "Respond with a professional, concise **email** to be sent to a client. "
            "Follow the structure and headings below, keep claims accurate, and avoid legal advice."
        ),
        "role_lbl": "ROLE",
        "goal_lbl": "GOAL",
        "ctx_lbl": "CONTEXT",
        "req_lbl": "DELIVERABLE REQUIREMENTS",
        "info_lbl": "INFORMATION TO GATHER (internal for you, not to display)",
        "tone_lbl": "TONE",
        "len_lbl": "LENGTH",
        "extra_lbl": "Additional notes & constraints",
        "nps_pasted_lbl": "NPS Verbatim Insights (pasted)",
        "nps_internal_lbl": "NPS Insights (internal)",
    },
    # Stubs for localization (add later if needed)
    "zh": {"name": "中文", "sys": "输出一封专业的客户邮件。", "role_lbl": "角色", "goal_lbl": "目标",
           "ctx_lbl": "上下文", "req_lbl": "交付要求", "info_lbl": "需收集信息",
           "tone_lbl": "语气", "len_lbl": "篇幅", "extra_lbl": "补充说明",
           "nps_pasted_lbl": "NPS 文本", "nps_internal_lbl": "NPS 洞察"},
    "ko": {"name": "한국어", "sys": "전문적이고 간결한 고객 이메일을 작성하세요.", "role_lbl": "역할",
           "goal_lbl": "목표", "ctx_lbl": "컨텍스트", "req_lbl": "산출물 요구사항",
           "info_lbl": "수집 정보", "tone_lbl": "톤", "len_lbl": "길이",
           "extra_lbl": "추가 메모", "nps_pasted_lbl": "NPS 원문", "nps_internal_lbl": "NPS 인사이트"},
    "ja": {"name": "日本語", "sys": "プロフェッショナルで簡潔な顧客向けメールを作成してください。", "role_lbl": "役割",
           "goal_lbl": "ゴール", "ctx_lbl": "コンテキスト", "req_lbl": "成果物要件",
           "info_lbl": "収集情報", "tone_lbl": "トーン", "len_lbl": "長さ",
           "extra_lbl": "補足", "nps_pasted_lbl": "NPS 原文", "nps_internal_lbl": "NPS インサイト"},
}

# ----------------------------
# App-wide selectable context
# ----------------------------
LN_CONTEXT: Dict[str, List[str]] = {
    "regions": ["Hong Kong", "Japan", "Korea", "Singapore"],
    "client_types": ["law firm", "in-house legal", "corporate", "government", "public sector"],
    "practice_areas": [
        "financial services", "litigation", "compliance", "arbitration", "personal injury",
        "company", "corporate", "IP", "criminal", "contract", "tax"
    ],
    "tones": ["auto", "warm", "consultative", "neutral", "apologetic", "formal", "polite"],
    "lengths": ["short", "medium", "long"],
    "outputs": ["plain prompt", "email"],
    # These labels map to our PRODUCT_ALIAS below
    "products": [
        "Lexis Analytics (HK)",
        "Lexis+ (HK) — Legal Research",
        "Search Tree",
        "Clause Intelligence",
        "PG — Financial Services (HK)",
        "PG — Commercial (HK)",
        "PG — Corporate (HK)",
        "PG — Data Protection (HK)",
        "PG — Dispute Resolution (HK)",
    ],
}

# ===============================================================
# Product knowledge base (HK) — auto-inserted pointers
# (Curated from your product doc at /mnt/data/Feature.odt)
# ===============================================================
PRODUCT_KB = {
    "lexis_analytics_hk": {
        "name": "Lexis® Analytics Hong Kong",
        "one_liner": "AI litigation analytics to turn case-law data into strategy.",
        "bullets": [
            "Discern most relevant cases in seconds with robust AI analytics.",
            "‘Bubble mind map’ shows patterns across thousands of precedents.",
            "Legal Issue Relationship Graph recommends related issues you may miss.",
            "Outcome analytics & judicial treatment to judge case authority quickly.",
        ],
        "source": "/mnt/data/Feature.odt",
    },
    "lexis_plus_hk_research": {
        "name": "Lexis+® Hong Kong — Legal Research",
        "one_liner": "All-in-one research ecosystem with AI-assisted answers and summaries.",
        "bullets": [
            "Fast answers and citable authorities via the AI-enhanced search bar.",
            "GPT-style case syntheses and instant case-to-case recommendations.",
            "Fine control: ‘Exclude’ and ‘Must Include’ filters in Search Within Results.",
        ],
        "source": "/mnt/data/Feature.odt",
    },
    "search_tree": {
        "name": "Search Tree (Lexis+ Hong Kong)",
        "one_liner": "Visual interface for Boolean & Natural Language search across content.",
        "bullets": [
            "Explore results visually and pivot quickly to the most relevant documents.",
        ],
        "source": "/mnt/data/Feature.odt",
    },
    "clause_intelligence": {
        "name": "Lexis® Clause Intelligence",
        "one_liner": "AI drafting assistant that compares your draft to trusted clauses.",
        "bullets": [
            "Retrieves up-to-date clauses and proposes ready-to-publish edits.",
            "Cuts review time and reduces drafting errors; reinforces best practice.",
        ],
        "source": "/mnt/data/Feature.odt",
    },
    "pg_financial_services": {
        "name": "Practical Guidance — Financial Services (HK)",
        "one_liner": "End-to-end FS compliance & markets know-how (incl. FinTech / VA).",
        "bullets": [
            "Regulatory architecture, supervision, prudential & conduct rules.",
            "Financial crime, enforcement, markets/trading, funds & asset management.",
            "Insurance, cross-border investment, international taxation & guides.",
        ],
        "source": "/mnt/data/Feature.odt",
    },
    "pg_commercial": {
        "name": "Practical Guidance — Commercial (HK)",
        "one_liner": "Contracting and go-to-market operations for commercial lawyers.",
        "bullets": [
            "Contract, consumer, competition, IP, IT, e-commerce, franchising.",
            "Templates, checklists, playbooks for repeatable tasks.",
        ],
        "source": "/mnt/data/Feature.odt",
    },
    "pg_corporate": {
        "name": "Practical Guidance — Corporate (HK)",
        "one_liner": "Company lifecycle + transactions from governance to ECM/M&A.",
        "bullets": [
            "Incorporation, meetings, governance, share capital, secretarial.",
            "Private M&A, JVs, PE, ECM, takeovers; financing, tax, offshore.",
        ],
        "source": "/mnt/data/Feature.odt",
    },
    "pg_data_protection": {
        "name": "Practical Guidance — Data Protection (HK)",
        "one_liner": "PDPO-aligned compliance with global context (incl. GDPR).",
        "bullets": [
            "Processing lifecycle, usage, breaches, surveillance & cybersecurity.",
            "Employee/supplier data, reputation, international laws.",
        ],
        "source": "/mnt/data/Feature.odt",
    },
    "pg_dispute_resolution": {
        "name": "Practical Guidance — Dispute Resolution (HK)",
        "one_liner": "Civil procedure, ADR & arbitration—from filing to enforcement.",
        "bullets": [
            "Jurisdiction, injunctions, evidence, settlement, costs & appeals.",
            "Enforcement (local/international/PRC); mediation & arbitration.",
        ],
        "source": "/mnt/data/Feature.odt",
    },
}

# Map UI labels to KB keys
PRODUCT_ALIAS = {
    "Lexis Analytics (HK)": "lexis_analytics_hk",
    "Lexis+ (HK) — Legal Research": "lexis_plus_hk_research",
    "Search Tree": "search_tree",
    "Clause Intelligence": "clause_intelligence",
    "PG — Financial Services (HK)": "pg_financial_services",
    "PG — Commercial (HK)": "pg_commercial",
    "PG — Corporate (HK)": "pg_corporate",
    "PG — Data Protection (HK)": "pg_data_protection",
    "PG — Dispute Resolution (HK)": "pg_dispute_resolution",
}


def _format_product_highlights(selected_labels: List[str]) -> str:
    """Returns a formatted block with product pointers for the email."""
    if not selected_labels:
        return ""
    items: List[str] = []
    for label in selected_labels:
        kb_key = PRODUCT_ALIAS.get(label)
        if not kb_key:
            continue
        entry = PRODUCT_KB.get(kb_key)
        if not entry:
            continue
        bullets = "\n".join([f"- {b}" for b in entry["bullets"]])
        items.append(
            f"**{entry['name']}** — {entry['one_liner']}\n{bullets}"
        )
    if not items:
        return ""
    return (
        "### Helpful product pointers (auto-inserted)\n"
        + "\n\n".join(items)
        + "\n"
    )


def _inject_products_into_prompt(base_prompt: str, ctx: Dict) -> str:
    """If 'include_highlights' is True, append product blurbs to the output."""
    if not ctx.get("include_highlights"):
        return base_prompt
    selected = ctx.get("products_used") or []
    block = _format_product_highlights(selected)
    if not block:
        return base_prompt
    return base_prompt.rstrip() + "\n\n" + block


# ----------------------------
# Helpers
# ----------------------------
def _auto_tone(region: str, stage: str) -> str:
    """Simple auto tone heuristic by region + stage."""
    if stage.lower() in {"complaint", "detractor", "low usage", "cancellation"}:
        return "apologetic"
    if region in {"Japan", "Korea"}:
        return "polite"
    return "consultative"


def _ctx_line(ctx: Dict) -> str:
    """Compact context line for prompts."""
    parts = [
        f"Client: {ctx.get('client_name','n/a')}",
        f"Type: {ctx.get('client_type','n/a')}",
        f"Region: {ctx.get('region','n/a')}",
        f"Practice: {', '.join(ctx.get('practice_areas', []) or ['n/a'])}",
        f"Products: {', '.join(ctx.get('products_used', []) or ['n/a'])}",
        f"Stage: {ctx.get('relationship_stage','n/a')}",
    ]
    return "; ".join(parts)


def _header(lang: str, goal: str, ctx: Dict, deliverables: List[str]) -> str:
    labels = SCAFFOLDS[lang]
    tone = ctx.get("tone", "auto")
    if tone == "auto":
        tone = _auto_tone(ctx.get("region", ""), ctx.get("relationship_stage", ""))
    length = ctx.get("length", "medium")

    header = [
        "[system]",
        labels["sys"],
        "",
        "[user]",
        f"**{labels['role_lbl']}**: Customer Success / Sales (client-facing)",
        f"**{labels['goal_lbl']}**: {goal}",
        f"**{labels['ctx_lbl']}**: {_ctx_line(ctx)}.",
        f"**{labels['req_lbl']}**:",
    ]
    for d in deliverables:
        header.append(f"- {d}")
    header.extend(
        [
            f"**{labels['info_lbl']}**:",
            "- Client metrics and usage evidence (only if needed).",
            "- No confidential or legal advice.",
            f"**{labels['tone_lbl']}**: {tone}",
            f"**{labels['len_lbl']}**: {length}",
            "",
            "Draft the email in a way that is immediately sendable.",
        ]
    )
    return "\n".join(header)


# ----------------------------
# Recipe builders
# ----------------------------
def build_renewal(ctx: Dict, lang: str) -> str:
    deliverables = [
        "Open with appreciation; acknowledge pricing feedback (if any).",
        "Demonstrate concrete value (usage metrics, outcomes, risk mitigation).",
        "Introduce forward-looking value (Practical Guidance, upcoming features).",
        "Propose a value review with 2–3 time options.",
    ]
    body = _header(lang, "Renewal outreach", ctx, deliverables)
    return body


def build_qbr(ctx: Dict, lang: str) -> str:
    deliverables = [
        "Summarize period usage and business impact.",
        "Highlight wins and under-used features.",
        "Propose recommendations and next steps.",
    ]
    return _header(lang, "QBR follow-up / brief", ctx, deliverables)


def build_follow_up(ctx: Dict, lang: str) -> str:
    deliverables = [
        "Reference last meeting and any open actions.",
        "Confirm next steps, owners, and dates.",
    ]
    return _header(lang, "Client meeting follow-up", ctx, deliverables)


def build_rfp(ctx: Dict, lang: str) -> str:
    deliverables = [
        "Acknowledge scope and timeline.",
        "Position LexisNexis differentiators aligned to requirements.",
        "Request clarifications and propose a next checkpoint.",
    ]
    return _header(lang, "Proposal / RFP response email", ctx, deliverables)


def build_upsell(ctx: Dict, lang: str) -> str:
    deliverables = [
        "Tie pains to specific modules/features that solve them.",
        "Include relevant case studies if available.",
        "Offer a brief discovery / demo with time options.",
    ]
    return _header(lang, "Upsell / Cross-sell outreach", ctx, deliverables)


def build_risk(ctx: Dict, lang: str) -> str:
    deliverables = [
        "Flag risk driver (usage drop, renewal risk, negative feedback, etc.).",
        "Propose mitigation plan (enablement, cadence, owners, checkpoints).",
        "Invite quick sync to de-risk together.",
    ]
    return _header(lang, "Client risk alert & recovery", ctx, deliverables)


def build_snapshot(ctx: Dict, lang: str) -> str:
    deliverables = [
        "Provide client snapshot and early risk/opportunity signals.",
        "Keep neutral and action-oriented; this is prepared by Sales for CSM.",
    ]
    return _header(lang, "Client snapshot & risk signals", ctx, deliverables)


def build_objection(ctx: Dict, lang: str) -> str:
    deliverables = [
        "Identify objection type (price/usability/competitor) and calibrate tone.",
        "Provide concise, evidence-backed response and options.",
        "Offer next steps tailored to the objection.",
    ]
    return _header(lang, "Objection response email", ctx, deliverables)


def build_nps_engagement(ctx: Dict, lang: str) -> str:
    rating = (ctx.get("nps_previous_rating") or "").lower()
    tone_line = "Promoters: appreciative; Passives: humble, improvement-oriented; Detractors: sincere, non-defensive."
    if "promoter" in rating:
        rating_text = "promoter"
    elif "passive" in rating:
        rating_text = "passive"
    elif "detractor" in rating:
        rating_text = "detractor"
    else:
        rating_text = "unknown"

    deliverables = [
        f"Adapt tone to prior NPS (**{rating_text}**).",
        "Briefly state why feedback matters now.",
        "Provide survey link and a concise CTA.",
        tone_line,
    ]
    return _header(lang, "NPS engagement", ctx, deliverables)


def build_nps_follow_up(ctx: Dict, lang: str) -> str:
    rating = (ctx.get("nps_previous_rating") or "").lower()
    if "promoter" in rating:
        variant = "thank them; acknowledge specific praise; offer a helpful pointer or advanced usage tip; invite quick check-in."
    elif "passive" in rating:
        variant = "appreciate feedback; acknowledge ‘good not great’; ask what to improve; include direct CTA."
    else:
        variant = "acknowledge pain non-defensively; state we escalated where applicable; set expectation to update; invite details."

    deliverables = [
        f"Follow-up to NPS comment (previous rating: **{rating or 'n/a'}**).",
        "Open by referencing their exact comment (quote briefly).",
        "Address by comment type (feature request / bug / usability / general).",
        "Offer next step: quick tip, link, or request clarifying needs.",
        "Close with a clear CTA and appreciation.",
        f"Variant guidance: {variant}",
    ]
    return _header(lang, "NPS follow-up (comment-specific)", ctx, deliverables)


# Register recipes available to the app
PROMPT_RECIPES: Dict[str, callable] = {
    "Renewal Email": build_renewal,
    "QBR Brief": build_qbr,
    "Client Follow-up": build_follow_up,
    "Proposal / RFP Response": build_rfp,
    "Upsell / Cross-sell Outreach": build_upsell,
    "Client Risk Alert": build_risk,
    "Client Snapshot & Risk Signals": build_snapshot,
    "Objection Coach": build_objection,
    "NPS Engagement": build_nps_engagement,
    "NPS Follow-up": build_nps_follow_up,
}


def fill_recipe(recipe_name: str, lang: str, ctx: Dict) -> str:
    """Build the email prompt for the selected recipe."""
    lang = lang or "en"
    if lang not in SCAFFOLDS:
        lang = "en"
    fn = PROMPT_RECIPES.get(recipe_name)
    if not fn:
        fn = build_follow_up
    prompt_str = fn(ctx, lang)
    # Append pasted NPS insights if present (for NPS workflows)
    pasted = (ctx.get("nps_pasted") or "").strip()
    if pasted:
        prompt_str += "\n\n" + f"**{SCAFFOLDS[lang]['nps_pasted_lbl']}**:\n{pasted}\n"
    # Auto product pointers (if toggled on)
    prompt_str = _inject_products_into_prompt(prompt_str, ctx)
    return prompt_str


def shape_output(text: str, target: str, client_name: str, recipe_name: str) -> str:
    """Format for 'plain prompt' or 'email'."""
    if target == "email":
        return text + "\n\n" + f"--\nSent on {date.today().isoformat()} • {client_name or 'Client'}"
    # plain prompt (default)
    return text
