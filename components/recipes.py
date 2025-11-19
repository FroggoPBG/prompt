# components/recipes.py
# Multilingual prompt-brief builder for CS/RM/Sales (no external APIs)

# ---------- Language scaffolds ----------
SCAFFOLDS = {
    "en": {
        "name": "English",
        "system": (
            "You are an assistant for Customer Success in the legal-tech domain at "
            "LexisNexis. Respond with a professional, clear, and helpful tone. "
            "Prioritize accuracy, brevity, and client understanding."
        ),
        "notes_header": "Additional notes & constraints:",
    },
    "zh": {
        "name": "中文",
        "system": (
            "你是 LexisNexis 法律科技领域的客户成功顾问助理。"
            "请以专业、清晰、亲切的语气回应，确保表达准确、简洁且有助于客户理解。"
        ),
        "notes_header": "补充说明与约束条件：",
    },
    "ko": {
        "name": "한국어",
        "system": (
            "당신은 LexisNexis 법률 테크 분야의 고객 성공 컨설턴트입니다. "
            "전문적이고 명확하며 친절한 어조로 응답하세요. 정확하고 간결하며 "
            "고객의 이해를 돕는 표현을 사용하세요."
        ),
        "notes_header": "추가 설명 및 제약 조건:",
    },
    "ja": {
        "name": "日本語",
        "system": (
            "あなたは LexisNexis のリーガルテック分野におけるカスタマーサクセス・"
            "コンサルタントです。専門的で明確かつ丁寧な口調で回答し、正確さと簡潔さ、"
            "そして相手の理解を重視してください。"
        ),
        "notes_header": "補足説明と制約条件：",
    },
}

# ---------- UI pickers / context ----------
LN_CONTEXT = {
    "regions": ["Global", "Hong Kong", "Japan", "Korea", "Singapore"],
    "client_types": ["law firm", "corporate", "government", "in-house legal"],
    "practice_areas": [
        "financial services", "litigation", "compliance", "arbitration",
        "tort", "personal injury", "company", "corporate", "IP", "criminal",
        "contract",
    ],
    "products": [
        "Lexis+",
        "Lexis+ AI",
        "Practical Guidance",
        "Lexis PSL",
        "Lexis Advance",
        "Lexis Red",
        "Risk Solutions",
        "Regulatory Compliance",
        "Nexis Data+",
    ],
    "roles": [
        "Customer Success Manager",
        "Relationship Manager",
        "Sales / Account Executive",
        "Marketing / Enablement",
    ],
    "audiences": [
        "GC / CLO",
        "Head of Compliance",
        "Litigation Partner",
        "KM / Innovation Lead",
        "In-house Legal Ops",
        "Procurement",
    ],
    "stages": [
        "New", "Renewal", "Expansion", "Cancellation",
        "Low usage", "Complaint", "Previous negative comments",
        "Previous positive comments",
    ],
    "tones": [
        "auto", "neutral", "friendly", "consultative", "persuasive", "formal",
        "polite", "apologetic", "technical", "concise",
    ],
    "lengths": ["very short", "short", "medium", "long"],
    "outputs": ["plain prompt", "email", "CRM note", "slide outline"],
}

# ---------- Region product highlights (safe strings) ----------
PRODUCT_HIGHLIGHTS = {
    "Practical Guidance": {
        "Hong Kong": {
            "Financial Services": {
                "updates": 50,
                "notable": [
                    "Tokenization of real-world assets; HKMA guidance on tokenised products",
                    "SFC framework on security token offerings; insights on tokenised public funds",
                    "Dual licensing regime for virtual-asset trading platforms",
                    "Crypto-assets regulation; Fund Manager Code of Conduct; OFC regime",
                ],
            },
            "Corporate": {
                "updates": 261,
                "notable": [
                    "Custom/Model Articles of Association; majority-minority & deadlock examples",
                    "Board minutes skeletons; virtual general meetings",
                    "Director address non-disclosure; registration of non-HK companies",
                    "First board minutes; resisting winding-up; Companies Registry forms (NAR1/NSC1/NN1)",
                ],
            },
            "Employment": {
                "updates": 341,
                "notable": [
                    "Executive service agreement; employment contract; minimum wage",
                    "Anti-harassment policy; mental-health policy (HK); MPF/ORS overview",
                    "Termination tax; share options/awards; data protection & social media",
                ],
            },
            "Dispute Resolution (HKIAC)": {
                "updates": 242,
                "notable": [
                    "HKIAC 2024: consolidation; awards & orders; third-party funding disclosure",
                    "Emergency relief; pleadings & amendments; time limits",
                ],
            },
        }
    }
}

# ---------- Tone guidance ----------
STYLE_TEMPLATES = {
    "en": {
        "tone_map": {
            "neutral": "Use a neutral, professional tone focused on clarity and actionability.",
            "friendly": "Sound approachable and supportive while remaining professional.",
            "consultative": "Adopt a consultative tone; diagnose needs and guide next steps.",
            "persuasive": "Structure value clearly and emphasize outcomes and ROI.",
            "formal": "Maintain a formal, respectful tone; avoid colloquialisms.",
            "polite": "Be courteous and deferential, prioritizing respectful phrasing.",
            "apologetic": "Acknowledge issues sincerely and state corrective actions.",
            "technical": "Use precise terminology; add brief explanations where needed.",
            "concise": "Be brief and to the point; emphasize essentials.",
        },
        "closing": "Ensure accuracy, easy navigation, and client-centric framing.",
    },
    "zh": {
        "tone_map": {
            "neutral": "保持专业、平和的语气，重点在清晰与可操作性。",
            "friendly": "语气自然亲切，体现合作与支持，同时保持专业度。",
            "consultative": "以咨询式语气识别需求并引导下一步。",
            "persuasive": "结构清晰、数据支撑，强调价值与预期成效。",
            "formal": "保持正式且礼貌的表达，避免口语化与冗长句式。",
            "polite": "用语委婉、礼貌，体现尊重。",
            "apologetic": "真诚致歉并说明改进措施。",
            "technical": "术语准确，必要处简要解释。",
            "concise": "表达精炼，突出要点。",
        },
        "closing": "确保内容准确、易懂，并聚焦客户价值。",
    },
    "ko": {
        "tone_map": {
            "neutral": "전문적이고 중립적인 어조로 명확하고 실행 가능한 표현을 사용하세요.",
            "friendly": "친근하되 전문성을 유지하세요.",
            "consultative": "컨설팅 톤으로 니즈를 파악하고 다음 단계를 제시하세요.",
            "persuasive": "가치를 체계적으로 제시하고 결과/ROI를 강조하세요.",
            "formal": "격식과 예의를 갖춘 표현을 사용하세요.",
            "polite": "정중하고 공손한 표현을 우선하세요.",
            "apologetic": "문제를 진솔하게 인정하고 개선 조치를 명확히 하세요.",
            "technical": "정확한 용어를 사용하고 필요한 경우 간단히 설명하세요.",
            "concise": "간결하고 핵심만 전달하세요.",
        },
        "closing": "정확성, 이해 용이성, 고객 중심 관점을 보장하세요.",
    },
    "ja": {
        "tone_map": {
            "neutral": "専門的で中立的なトーンを維持し、明確で実行可能な表現を用いてください。",
            "friendly": "親しみやすさを保ちつつ、専門性を損なわないでください。",
            "consultative": "コンサルティブな口調でニーズを特定し、次の一手を導いてください。",
            "persuasive": "価値と成果・ROIを分かりやすく強調してください。",
            "formal": "丁寧で礼儀正しい表現を用い、くだけた言い回しは避けてください。",
            "polite": "より丁寧で配慮ある表現を優先してください。",
            "apologetic": "課題を真摯に認め、改善策を明確に述べてください。",
            "technical": "正確な専門用語を使い、必要に応じて簡潔に説明してください。",
            "concise": "簡潔に要点を示してください。",
        },
        "closing": "正確で読みやすく、顧客志向の構成であることを確認してください。",
    },
}

# ---------- Compact recipe bodies ----------
PROMPT_RECIPES = {
    "Renewal Email": (
        "Write a consultative renewal email to {client_name}. Emphasize ROI, "
        "acknowledge pricing feedback, and propose a value review with 2–3 time options."
    ),
    "QBR Brief": (
        "Prepare a consultative QBR summary for {client_name}, highlighting usage trends, "
        "business impact, wins, underused features, and clear recommendations."
    ),
    "Client Follow-up": (
        "Draft a friendly follow-up note to {client_name} after the last meeting, "
        "confirming takeaways and next steps."
    ),
    "Proposal / RFP Response": (
        "Draft proposal language tailored to {client_name}'s sector and scope. Emphasize "
        "differentiators, ROI, timeline, and next steps."
    ),
    "Upsell / Cross-sell Outreach": (
        "Draft outreach that maps current pain points to specific LexisNexis products "
        "with expected outcomes and ROI."
    ),
    "Client Risk Alert": (
        "Draft an empathetic, proactive message addressing risk signals and proposing "
        "mitigation actions."
    ),
    "Client Snapshot & Risk Signals": (
        "Create an internal client snapshot: firm overview, recent developments, "
        "engagement insights, risk & growth signals."
    ),
    "Objection Coach": (
        "Create empathetic, data-backed talking points, plus one reframing question "
        "that shifts from cost to outcomes."
    ),
    # Base key kept for UI; variant text chosen dynamically by nps_previous_rating
    "NPS Engagement": "Draft an NPS engagement email (variant will adapt to prior score).",
}

# ---------- Brief headings ----------
BRIEF_LABELS = {
    "ROLE": {"en": "ROLE", "zh": "角色", "ko": "역할", "ja": "役割"},
    "GOAL": {"en": "GOAL", "zh": "目标", "ko": "목표", "ja": "目的"},
    "CONTEXT": {"en": "CONTEXT", "zh": "上下文", "ko": "컨텍스트", "ja": "コンテキスト"},
    "REQ": {"en": "DELIVERABLE REQUIREMENTS", "zh": "交付要求", "ko": "전달물 요구사항", "ja": "成果物要件"},
    "INFO": {"en": "INFORMATION TO GATHER", "zh": "需收集信息", "ko": "수집해야 할 정보", "ja": "収集すべき情報"},
    "TONE": {"en": "TONE", "zh": "语气", "ko": "톤", "ja": "トーン"},
    "LENGTH": {"en": "LENGTH", "zh": "长度", "ko": "분량", "ja": "長さ"},
    "HIGHLIGHTS": {"en": "Product highlights", "zh": "产品亮点", "ko": "제품 하이라이트", "ja": "製品ハイライト"},
}

# ---------- Helpers ----------
def _auto_tone(region: str, stage: str) -> str:
    region_map = {
        "Japan": "polite",
        "Korea": "formal",
        "Hong Kong": "consultative",
        "Singapore": "neutral",
        "Global": "neutral",
    }
    tone = region_map.get(region or "Global", "neutral")
    if stage in ("Complaint", "Previous negative comments"):
        tone = "apologetic"
    return tone

def _bullets(items):
    if not items:
        return ""
    return "\n" + "\n".join([f"- {i}" for i in items])

def render_product_highlights(lang_code: str, products_used: list, region: str) -> str:
    if not products_used or region in ("", "Global"):
        return ""
    label = BRIEF_LABELS["HIGHLIGHTS"][lang_code]
    lines = []
    for p in products_used:
        reg_table = PRODUCT_HIGHLIGHTS.get(p, {}).get(region)
        if not reg_table:
            continue
        lines.append(f"- **{p} — {region}**")
        for cat, info in reg_table.items():
            lines.append(f"  - {cat} — {info.get('updates')} updates")
            for item in info.get("notable", []):
                lines.append(f"    - {item}")
    return f"**{label}:**\n" + "\n".join(lines) if lines else ""

def _nps_variant_body(previous_rating: str) -> str:
    """Return instruction body for NPS by previous rating bucket."""
    if "Promoter" in (previous_rating or ""):
        return (
            "Write a warm, appreciative NPS engagement email for customers who previously rated 9–10. "
            "Tone: grateful and collaborative; position the client as a partner. "
            "Acknowledge their support and our commitment to maintain high standards. "
            "Mention the survey takes under 2 minutes. Keep concise; avoid being overly effusive. "
            "Subject line should reflect appreciation for their insights."
        )
    if "Passive" in (previous_rating or ""):
        return (
            "Write an aspirational NPS engagement email for customers who previously rated 7–8. "
            "Tone: humble yet motivated. Recognize we've been good and are striving to be great. "
            "Frame their feedback as key to making the experience exceptional. "
            "Ask what to keep, stop, or change. Mention the survey takes under 2 minutes and that we personally read every response. "
            "Subject line should focus on improvement and earning their enthusiastic recommendation."
        )
    # Detractors / default
    return (
        "Write a humble, sincere NPS engagement email for customers who previously rated 0–6. "
        "Tone: respectful, non-defensive, genuinely open. "
        "Acknowledge we've been working on improvements and their honest perspective matters. "
        "Do not over-promise; ask whether things have improved, stayed the same, or still need work. "
        "Mention the survey takes under 2 minutes. Keep brief and respectful. "
        "Subject line should be gentle and non-presumptuous."
    )

# ---------- Build the structured brief ----------
def build_brief(recipe: str, lang: str, ctx: dict) -> str:
    role = ctx.get("role") or "Customer Success Manager"
    region = ctx.get("region") or "Global"
    stage = ctx.get("relationship_stage") or "Renewal"
    tone = ctx.get("tone") or "auto"
    tone = _auto_tone(region, stage) if tone == "auto" else tone
    length_hint = ctx.get("length") or "medium"

    goals = {
        "Renewal Email": {
            "en": "Demonstrate tangible ROI and reframe the conversation from cost to value.",
            "zh": "展示可量化 ROI，将讨论从“成本”转向“价值”。",
            "ko": "명확한 ROI를 제시하여 대화를 비용에서 가치 중심으로 전환합니다.",
            "ja": "具体的なROIを示し、議論をコストから価値へ転換します。",
        },
        "QBR Brief": {
            "en": "Create a consultative, data-driven QBR that demonstrates outcomes and identifies opportunities.",
            "zh": "生成以数据与咨询为导向的 QBR，展示成果并识别机会。",
            "ko": "성과를 보여주고 기회를 식별하는 데이터 기반 컨설팅형 QBR을 작성합니다.",
            "ja": "成果を示し、機会を特定するデータドリブンなコンサル型QBRを作成します。",
        },
        "Client Follow-up": {
            "en": "Confirm shared understanding and move the account forward with clear next steps.",
            "zh": "确认共识并以明确的下一步推动合作进展。",
            "ko": "합의한 내용을 정리하고 명확한 다음 단계로 진행합니다.",
            "ja": "合意事項を整理し、明確な次のアクションへ前進させます。",
        },
        "Proposal / RFP Response": {
            "en": "Tailor proposal language to the client's scope, differentiators, ROI, and timelines.",
            "zh": "围绕客户范围、差异化、ROI 与时间表量身定制提案语言。",
            "ko": "고객 범위/차별화/ROI/일정을 반영한 제안 문안을 맞춤 제작합니다.",
            "ja": "範囲・差別化・ROI・スケジュールを反映した提案文面を作成します。",
        },
        "Upsell / Cross-sell Outreach": {
            "en": "Map pains to LexisNexis solutions with clear outcomes and ROI.",
            "zh": "基于痛点匹配 LexisNexis 解决方案并明确结果与 ROI。",
            "ko": "고객 페인포인트에 맞는 솔루션과 기대 성과/ROI를 제시합니다.",
            "ja": "課題に合致するソリューションと成果・ROIを提示します。",
        },
        "Client Risk Alert": {
            "en": "Address risk signals early with an empathetic, proactive plan.",
            "zh": "以同理心与前瞻性方案尽早应对风险信号。",
            "ko": "공감과 선제적 계획으로 리스크 신호에 조기 대응합니다.",
            "ja": "共感と先手の計画でリスク兆候に早期対応します。",
        },
        "Client Snapshot & Risk Signals": {
            "en": "Provide a concise internal briefing for Customer Success before renewal or review.",
            "zh": "在续约或评审前，为客户成功团队提供简明的内部简报。",
            "ko": "갱신/리뷰 전 고객 성공팀을 위한 간결한 내부 브리핑을 제공합니다.",
            "ja": "更新/レビュー前にCS向けの簡潔な内部ブリーフィングを提供します。",
        },
        "Objection Coach": {
            "en": "Craft empathetic, data-backed responses that shift focus from cost to outcomes.",
            "zh": "以同理心与数据支撑回应，将焦点从“成本”转向“结果/价值”。",
            "ko": "공감과 데이터로 응답하여 초점을 비용에서 결과로 전환합니다.",
            "ja": "共感とデータに基づき、焦点をコストから成果へ転換します。",
        },
        "NPS Engagement": {
            "en": "Encourage feedback with tone adapted to prior NPS; capture insights to improve.",
            "zh": "根据既往 NPS 评分调整语气，鼓励反馈并收集改进洞察。",
            "ko": "이전 NPS에 맞춘 톤으로 피드백을 유도하고 인사이트를 수집합니다.",
            "ja": "過去のNPSに合わせたトーンでフィードバックを促し、改善の示唆を得ます。",
        },
    }
    goal = goals[recipe][lang]

    req_map = {
        "Renewal Email": [
            "Open with appreciation; acknowledge pricing feedback.",
            "Quantify usage/impact; include any NPS quotes.",
            "Connect outcomes to efficiency/risk reduction.",
            "Introduce relevant products & near-term enhancements.",
            "Propose value review; include 2–3 time options.",
        ],
        "QBR Brief": [
            "Usage & engagement trends for the selected period.",
            "Business impact: time saved, risk mitigated, efficiency gains.",
            "Wins since last review; underused features.",
            "Clear recommendations and next steps.",
        ],
        "Client Follow-up": [
            "Restate objective and key decisions.",
            "Confirm owner + due dates for each action.",
            "Suggest the next check-in window.",
        ],
        "Proposal / RFP Response": [
            "Reflect scope, pain points, and success criteria.",
            "Highlight differentiators and compliance strengths.",
            "Outline ROI, timeline, and responsibilities.",
            "End with a clear CTA and schedule options.",
        ],
        "Upsell / Cross-sell Outreach": [
            "Tie pains to specific LexisNexis products.",
            "State expected outcomes/ROI and proof points.",
            "Offer enablement/trial/training next steps.",
        ],
        "Client Risk Alert": [
            "Acknowledge the risk signal and its impact.",
            "Offer 2–3 mitigation actions (enablement, plan, cadence).",
            "Invite a short call to align on next steps.",
        ],
        "Client Snapshot & Risk Signals": [
            "Firm overview and recent developments.",
            "Engagement insights and sentiment.",
            "Risk indicators and growth signals.",
        ],
        "Objection Coach": [
            "Acknowledge the concern respectfully.",
            "Provide 2–3 data-backed value points.",
            "Ask 1 reframing question to lead into ROI.",
        ],
        "NPS Engagement": [
            "Use the appropriate variant based on prior NPS bucket.",
            "Keep concise and respectful of the reader's time.",
            "Include survey link and a clear, low-friction CTA.",
        ],
    }

    info_map = [
        "Client name, type, region, practice area(s)",
        "Products in use; relationship stage",
        "Usage metrics / adoption; time saved / ROI evidence",
        "NPS score / theme (if relevant)",
        "Contract timing (if renewal) and any pricing notes",
        "Preferred language and tone",
    ]

    # Build context line
    bits = []
    def add(label, value):
        if value:
            bits.append(f"{label}: {value}")

    add("Client", ctx.get("client_name"))
    add("Type", ctx.get("client_type"))
    add("Region", region)
    add("Practice", ", ".join(ctx.get("practice_areas") or []))
    add("Products", ", ".join(ctx.get("products_used") or []))
    add("Stage", stage)
    add("Owner", ctx.get("account_owner"))
    add("Usage metrics", ctx.get("usage_metrics"))
    add("Time saved / Efficiency", ctx.get("time_saved"))
    add("NPS", ctx.get("nps_info"))
    add("Contract", ctx.get("contract_details"))
    add("Output target", ctx.get("output_target"))

    if recipe == "Renewal Email":
        add("Pricing concern", ctx.get("pricing_concern_level"))
        add("Meeting options", ctx.get("meeting_options"))
    if recipe == "QBR Brief":
        add("Period", ctx.get("qbr_window"))
        add("Benchmarks", "Yes" if ctx.get("qbr_include_benchmarks") else "")
        add("Sections", ", ".join(ctx.get("qbr_sections") or []))
    if recipe == "Client Follow-up":
        add("Last meeting", ctx.get("last_meeting_date"))
        add("Topics", ctx.get("meeting_topics"))
    if recipe == "Proposal / RFP Response":
        add("Sector", ctx.get("rfp_sector"))
        add("Scope", ctx.get("rfp_scope"))
        add("Differentiators", ctx.get("rfp_differentiators"))
        add("Deadline", ctx.get("rfp_deadline"))
    if recipe == "Upsell / Cross-sell Outreach":
        add("Pain points", ctx.get("pains"))
        add("Proposed products", ", ".join(ctx.get("proposed_products") or []))
        add("Case studies", ctx.get("case_studies"))
    if recipe == "Client Risk Alert":
        add("Risk trigger", ctx.get("risk_trigger"))
        add("Severity", ctx.get("risk_severity"))
        add("Mitigations", ctx.get("risk_mitigations"))
    if recipe == "Objection Coach":
        add("Objection type", ctx.get("objection_type"))
        add("Severity", ctx.get("objection_severity"))
        add("Competitor", ctx.get("competitor_name"))
        add("Data available", ", ".join(ctx.get("supporting_data") or []))
    if recipe == "NPS Engagement":
        add("Previous NPS", ctx.get("nps_previous_rating"))
        add("Feedback theme", ctx.get("nps_feedback_theme"))
        add("Survey link", ctx.get("nps_survey_link"))

    context = "; ".join([b for b in bits if b])

    # Assemble brief body
    brief_lines = [
        f"**{BRIEF_LABELS['ROLE'][lang]}**: {role}",
        f"**{BRIEF_LABELS['GOAL'][lang]}**: {goals[recipe][lang]}",
        f"**{BRIEF_LABELS['CONTEXT'][lang]}**: {context or '—'}",
        f"**{BRIEF_LABELS['REQ'][lang]}**:{_bullets(req_map[recipe])}",
        f"**{BRIEF_LABELS['INFO'][lang]}**:{_bullets(info_map)}",
        f"**{BRIEF_LABELS['TONE'][lang]}**: {tone}",
        f"**{BRIEF_LABELS['LENGTH'][lang]}**: {length_hint}",
    ]

    if ctx.get("include_highlights"):
        hl = render_product_highlights(lang, ctx.get("products_used") or [], region)
        if hl:
            brief_lines.append(hl)

    # Choose body text (standard recipe or NPS bucketed variant)
    if recipe == "NPS Engagement":
        body = _nps_variant_body(ctx.get("nps_previous_rating"))
    else:
        body = PROMPT_RECIPES[recipe].format(client_name=ctx.get("client_name") or "[Client]")

    return "\n".join(brief_lines) + "\n\n" + body

# ---------- Public API ----------
def fill_recipe(recipe: str, lang_code: str, ctx: dict) -> str:
    s = SCAFFOLDS[lang_code]
    auto = _auto_tone(ctx.get("region") or "Global", ctx.get("relationship_stage") or "")
    effective = auto if (ctx.get("tone") or "auto") == "auto" else ctx.get("tone")
    tone_line = STYLE_TEMPLATES[lang_code]["tone_map"].get(effective or "neutral", "")
    closing = STYLE_TEMPLATES[lang_code]["closing"]

    brief_text = build_brief(recipe, lang_code, ctx)
    ex_in = (ctx.get("ex_input") or "").strip()
    ex_out = (ctx.get("ex_output") or "").strip()
    few = (
        f"\n\nExamples for tone/structure:\n- Input: {ex_in or '[none]'}\n"
        f"- Output: {ex_out or '[none]'}"
        if (ex_in or ex_out)
        else ""
    )

    final = (
        f"[system]\n{s['system']}\n\n"
        f"[user]\n{brief_text}{few}\n\n"
        f"{s['notes_header']}\n"
        f"- Respect confidentiality; avoid legal advice.\n"
        f"- Be precise; prefer verifiable statements.\n"
        f"- Suggest next steps with owners & dates.\n"
        f"- {tone_line}\n- {closing}"
    ).strip()
    return final

def shape_output(text: str, mode: str, client_name: str, recipe: str) -> str:
    if mode == "plain prompt":
        return text
    if mode == "email":
        subj = f"{client_name or 'Client'} — {recipe}"
        return f"Subject: {subj}\n\n[Paste the generated email from your AI tool here]"
    if mode == "CRM note":
        return f"# {recipe} — {client_name}\n- Date: {{today}}\n\n{text}\n\n**Next steps**: [owner] — [date]"
    if mode == "slide outline":
        return (
            f"Title: {client_name or 'Client'} — {recipe}\n"
            f"Slide 1: Context\nSlide 2: Insights\nSlide 3: Recommendations\n"
            f"Slide 4: Next Steps\n\nContent:\n{text}"
        )
    return text
app.py (replace fully)
This adds:

NPS variants (driven by nps_previous_rating)

Save this prompt as template

Share with team (download template JSON)

Prompt history with Reuse button

python
Copy code
import streamlit as st
from datetime import datetime, date

from components.recipes import (
    SCAFFOLDS,
    LN_CONTEXT,
    PROMPT_RECIPES,
    fill_recipe,
    shape_output
)
from components.presets import export_preset_bytes, load_preset_into_state

# ---------- session defaults ----------
if "templates" not in st.session_state:
    st.session_state["templates"] = []  # list of dicts: {name, recipe, lang, output, ctx, created}
if "history" not in st.session_state:
    st.session_state["history"] = []    # list of dicts: {ts, recipe, lang, output, ctx, prompt}

# -------------------- Page --------------------
st.set_page_config(page_title="LexisNexis Prompt Composer (no APIs)", page_icon="🧠", layout="wide")
st.title("🧠 LexisNexis Prompt Composer (no APIs)")
st.caption("Generate high-quality, localized prompt briefs for any AI tool (ChatGPT, Copilot, Gemini) — no external APIs.")

# -------------------- Language & output --------------------
col_lang, col_out = st.columns([1, 1])
with col_lang:
    lang_code = st.selectbox(
        "Target language",
        options=list(SCAFFOLDS.keys()),
        format_func=lambda k: SCAFFOLDS[k]["name"],
        index=0,
    )
with col_out:
    output_format = st.selectbox("Output target", LN_CONTEXT["outputs"], index=0)

# -------------------- Sidebar: global schema --------------------
with st.sidebar:
    st.header("Client identity")
    client_name = st.text_input("Client name")
    client_type = st.selectbox("Client type", LN_CONTEXT["client_types"], index=0)
    region = st.selectbox("Region / Country", LN_CONTEXT["regions"], index=0)
    practice_areas = st.multiselect("Industry / practice area(s)", LN_CONTEXT["practice_areas"])

    st.header("CS context")
    account_owner = st.text_input("Account owner / RM name")
    relationship_stage = st.selectbox("Relationship stage", LN_CONTEXT["stages"], index=1)
    products_used = st.multiselect("Primary LexisNexis products used", LN_CONTEXT["products"])

    st.header("Metrics (optional)")
    usage_metrics = st.text_area("Usage metrics (logins, searches, features, report)")
    time_saved = st.text_input("Time saved / efficiency data (e.g., 'avg. 4 hours/week')")
    nps_info = st.text_area("NPS score / feedback theme (paste)")

    st.header("Communication settings")
    tone = st.selectbox("Tone", LN_CONTEXT["tones"], index=0)  # 'auto' is default
    length = st.selectbox("Length preference", LN_CONTEXT["lengths"], index=2)
    include_highlights = st.checkbox("Auto-include product highlights (region-aware)", value=True)

    st.markdown("---")
    st.subheader("Presets")
    preset_bytes = export_preset_bytes(
        client_name=client_name,
        client_type=client_type,
        products_used=products_used,
        account_owner=account_owner,
        practice_areas=practice_areas,
        region=region,
    )
    st.download_button("💾 Export client preset (.json)", preset_bytes, file_name="client_preset.json", mime="application/json")
    uploaded = st.file_uploader("📂 Import client preset (.json)", type="json")
    if uploaded:
        load_preset_into_state(uploaded)
        st.success("✅ Preset loaded. Update fields as needed.")

# -------------------- Main: function selection --------------------
left, right = st.columns([2, 3])

with left:
    recipe = st.selectbox(
        "Function / Use-case",
        [
            "Renewal Email",
            "QBR Brief",
            "Client Follow-up",
            "Proposal / RFP Response",
            "Upsell / Cross-sell Outreach",
            "Client Risk Alert",
            "Client Snapshot & Risk Signals",
            "Objection Coach",
            "NPS Engagement",
        ],
        index=0
    )

with right:
    st.subheader("Few-shot examples (optional)")
    ex_col1, ex_col2 = st.columns(2)
    with ex_col1:
        ex_input = st.text_area("Example input", height=80, placeholder="Short example input")
    with ex_col2:
        ex_output = st.text_area("Example output", height=80, placeholder="Desired example output")

# -------------------- Guided forms by function --------------------
st.markdown("---")
st.markdown("### 🧩 Guided options")

guided = {}

if recipe == "Renewal Email":
    with st.expander("Renewal options", expanded=True):
        pricing_concern_level = st.select_slider("Pricing concern level", options=["Mild", "Moderate", "High"], value="Moderate")
        contract_details = st.text_input("Contract details (renewal date / price change)")
        meeting_options = st.text_input("2–3 date/time options (comma-separated)", placeholder="e.g., Tue 10am, Wed 2pm, Thu 4pm")
        guided.update({
            "pricing_concern_level": pricing_concern_level,
            "contract_details": contract_details,
            "meeting_options": meeting_options,
        })

elif recipe == "QBR Brief":
    with st.expander("QBR options", expanded=True):
        qbr_window = st.selectbox("Review period", ["Last Month", "Last Quarter", "H1", "FY"], index=1)
        qbr_include_benchmarks = st.checkbox("Include industry benchmarks", value=False)
        qbr_sections = st.multiselect(
            "Sections to emphasize",
            ["Usage & Engagement", "Business Impact", "Wins", "Underused Features", "Recommendations"],
            default=["Usage & Engagement", "Business Impact", "Recommendations"]
        )
        guided.update({
            "qbr_window": qbr_window,
            "qbr_include_benchmarks": qbr_include_benchmarks,
            "qbr_sections": qbr_sections,
        })

elif recipe == "Client Follow-up":
    with st.expander("Follow-up options", expanded=True):
        last_meeting_date = st.text_input("Date of last meeting")
        meeting_topics = st.text_input("Topics covered")
        guided.update({
            "last_meeting_date": last_meeting_date,
            "meeting_topics": meeting_topics,
        })

elif recipe == "Proposal / RFP Response":
    with st.expander("RFP options", expanded=True):
        rfp_sector = st.text_input("Client sector")
        rfp_scope = st.text_area("RFP scope / key requirements")
        rfp_differentiators = st.text_area("Differentiators to emphasize")
        rfp_deadline = st.text_input("Key deadline")
        guided.update({
            "rfp_sector": rfp_sector,
            "rfp_scope": rfp_scope,
            "rfp_differentiators": rfp_differentiators,
            "rfp_deadline": rfp_deadline,
        })

elif recipe == "Upsell / Cross-sell Outreach":
    with st.expander("Upsell options", expanded=True):
        pains = st.text_area("Client pain points")
        proposed_products = st.multiselect("Proposed LexisNexis products", LN_CONTEXT["products"])
        case_studies = st.text_area("Relevant case studies")
        guided.update({
            "pains": pains,
            "proposed_products": proposed_products,
            "case_studies": case_studies,
        })

elif recipe == "Client Risk Alert":
    with st.expander("Risk options", expanded=True):
        risk_trigger = st.selectbox("Risk trigger", ["Declining usage", "Delayed renewal", "Negative feedback", "Champion turnover", "Other"], index=0)
        risk_severity = st.select_slider("Severity", options=[1,2,3,4,5], value=3)
        risk_mitigations = st.text_area("Mitigation options (enablement plan, cadence, etc.)")
        guided.update({
            "risk_trigger": risk_trigger,
            "risk_severity": risk_severity,
            "risk_mitigations": risk_mitigations,
        })

elif recipe == "Client Snapshot & Risk Signals":
    with st.expander("Snapshot options", expanded=True):
        prepared_by = st.selectbox("Prepared by", ["Sales", "Pre-Sales", "Customer Success"], index=0)
        last_engagement_date = st.text_input("Last engagement date")
        risk_level = st.select_slider("Risk level", options=["Low","Medium","High"], value="Medium")
        guided.update({
            "prepared_by": prepared_by,
            "last_engagement_date": last_engagement_date,
            "risk_level": risk_level,
        })

elif recipe == "Objection Coach":
    with st.expander("Objection options", expanded=True):
        objection_type = st.selectbox("Objection type", ["Price", "Usability", "Prefer Competitor"], index=0)
        objection_severity = st.select_slider("Severity", options=[1,2,3,4,5], value=3)
        competitor_name = st.text_input("Competitor (optional)")
        supporting_data = st.multiselect("Supporting data available", ["Usage metrics", "ROI", "NPS quotes", "Case studies", "Benchmarks"])
        guided.update({
            "objection_type": objection_type,
            "objection_severity": objection_severity,
            "competitor_name": competitor_name,
            "supporting_data": supporting_data,
        })

elif recipe == "NPS Engagement":
    with st.expander("NPS options (auto-variants)", expanded=True):
        nps_previous_rating = st.selectbox("Previous NPS", ["Promoter (9–10)", "Passive (7–8)", "Detractor (0–6)"], index=1)
        nps_feedback_theme = st.text_input("Feedback theme (summary)")
        nps_survey_link = st.text_input("Survey link / CTA")
        guided.update({
            "nps_previous_rating": nps_previous_rating,
            "nps_feedback_theme": nps_feedback_theme,
            "nps_survey_link": nps_survey_link,
        })

# -------------------- Quality checklist --------------------
st.markdown("---")
st.markdown("### ✅ Quality Checklist")
for item in [
    "No confidential client data present",
    "Claims are accurate/verifiable (no legal advice)",
    "Outcome/ROI linked to metrics",
    "Clear CTA / next steps included",
]:
    st.checkbox(item)

# -------------------- Generate --------------------
if st.button("✨ Generate Prompt"):
    ctx = dict(
        client_name=client_name,
        client_type=client_type,
        region=region,
        practice_areas=practice_areas,
        account_owner=account_owner,
        relationship_stage=relationship_stage,
        products_used=products_used,
        usage_metrics=usage_metrics,
        time_saved=time_saved,
        nps_info=nps_info,
        tone=tone,
        length=length,
        include_highlights=include_highlights,
        output_target=output_format,
        ex_input=ex_input or "",
        ex_output=ex_output or "",
    )
    ctx.update(guided)

    final_prompt = fill_recipe(recipe, lang_code, ctx)
    shaped = shape_output(final_prompt, output_format, client_name, recipe)

    st.subheader("📝 Copy-ready Prompt for AI tool")
    st.code(shaped, language="markdown")

    # download
    fname = f"ln_prompt_{recipe.replace('/','_')}_{lang_code}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.txt"
    st.download_button(
        "📥 Download (.txt)",
        shaped.replace("{today}", str(date.today())),
        file_name=fname,
        mime="text/plain"
    )

    # history push
    st.session_state["history"].append({
        "ts": datetime.utcnow().isoformat() + "Z",
        "recipe": recipe,
        "lang": lang_code,
        "output": output_format,
        "ctx": ctx,
        "prompt": shaped.replace("{today}", str(date.today())),
    })
    # keep last 50
    st.session_state["history"] = st.session_state["history"][-50:]

# -------------------- Templates, Sharing, History --------------------
st.markdown("---")
st.markdown("### 🧰 Templates, Sharing & History")

tcol1, tcol2, tcol3 = st.columns([2, 2, 2])

with tcol1:
    st.markdown("**Save this prompt as template**")
    tpl_name = st.text_input("Template name", placeholder="e.g., NPS Detractor (JP) short")
    if st.button("💾 Save template"):
        if tpl_name.strip():
            st.session_state["templates"].append({
                "name": tpl_name.strip(),
                "recipe": recipe,
                "lang": lang_code,
                "output": output_format,
                "ctx": {
                    "client_name": client_name,
                    "client_type": client_type,
                    "region": region,
                    "practice_areas": practice_areas,
                    "account_owner": account_owner,
                    "relationship_stage": relationship_stage,
                    "products_used": products_used,
                    "usage_metrics": usage_metrics,
                    "time_saved": time_saved,
                    "nps_info": nps_info,
                    "tone": tone,
                    "length": length,
                    "include_highlights": include_highlights,
                    "output_target": output_format,
                    "ex_input": ex_input or "",
                    "ex_output": ex_output or "",
                    **guided,
                },
                "created": datetime.utcnow().isoformat() + "Z",
            })
            st.success("Template saved locally.")
        else:
            st.warning("Please enter a template name.")

with tcol2:
    st.markdown("**Share with team**")
    # Export the newest generated prompt (if any) as a .json context pack
    if st.session_state["history"]:
        latest = st.session_state["history"][-1]
        import json, io
        pack = {
            "type": "ln-prompt-pack",
            "version": 1,
            "recipe": latest["recipe"],
            "lang": latest["lang"],
            "output": latest["output"],
            "ctx": latest["ctx"],
            "prompt": latest["prompt"],
            "created": latest["ts"],
        }
        bio = io.BytesIO(json.dumps(pack, indent=2, ensure_ascii=False).encode())
        bio.seek(0)
        st.download_button("⬇️ Download share pack (.json)", bio, file_name="ln_prompt_share_pack.json", mime="application/json")
    else:
        st.info("Generate a prompt first to export a share pack.")

with tcol3:
    st.markdown("**Templates & History**")
    # templates list
    if st.session_state["templates"]:
        tpl_names = [t["name"] for t in st.session_state["templates"]]
        pick = st.selectbox("Templates", options=["— select —"] + tpl_names, index=0)
        if pick != "— select —":
            idx = tpl_names.index(pick)
            tpl = st.session_state["templates"][idx]
            if st.button("📥 Load template"):
                # hydrate fields into session_state
                for k, v in tpl["ctx"].items():
                    st.session_state[k] = v
                st.success("Template loaded. Adjust fields if needed, then click Generate.")
    else:
        st.caption("No templates yet.")

st.markdown("#### History")
if st.session_state["history"]:
    # simple viewer of last 5
    last5 = st.session_state["history"][-5:][::-1]
    labels = [f"{h['ts']} — {h['recipe']} [{h['lang']}] → {h['output']}" for h in last5]
    picked = st.selectbox("Recent prompts", options=["— select —"] + labels, index=0)
    if picked != "— select —":
        idx = labels.index(picked)
        h = last5[idx]
        st.code(h["prompt"], language="markdown")
        if st.button("🔁 Reuse this prompt’s inputs"):
            # Restore context to current form
            for k, v in h["ctx"].items():
                st.session_state[k] = v
            st.success("Restored inputs from history. Review and click Generate.")
else:
    st.caption("No history yet — generate a prompt to start.")
    
st.caption("Tip: set Tone to ‘auto’ to localize by Region + Stage (e.g., Japan=polite; Complaint=apologetic).")
