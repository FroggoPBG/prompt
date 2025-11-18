# components/recipes.py
# Multilingual scaffolds, tone guidance, and prompt recipes for
# LexisNexis Customer Success / RM / Sales Consulting
# Languages: English (en), Chinese (zh), Korean (ko), Japanese (ja)
from datetime import datetime

# ---------------------------
# Language scaffolds (system + headings)
# ---------------------------
SCAFFOLDS = {
    "en": {
        "name": "English",
        "system": (
            "You are an assistant for Customer Success in the legal-tech domain at LexisNexis. "
            "Respond with a professional, clear, and helpful tone. Prioritize accuracy, brevity, and client understanding."
        ),
        "prompt_header": "Construct a response with the following requirements:",
        "few_shot_header": "Use these examples for tone and structure:",
        "notes_header": "Additional notes & constraints:",
        "output_header": "Final prompt",
    },
    "zh": {
        "name": "中文",
        "system": (
            "你是 LexisNexis 法律科技领域的客户成功顾问助理。"
            "请以专业、清晰、亲切的语气回应，确保表达准确、简洁且有助于客户理解。"
        ),
        "prompt_header": "请根据以下目标与要求撰写回应：",
        "few_shot_header": "可参考以下示例的语气与结构：",
        "notes_header": "补充说明与约束条件：",
        "output_header": "最终提示词",
    },
    "ko": {
        "name": "한국어",
        "system": (
            "당신은 LexisNexis 법률 테크 분야의 고객 성공 컨설턴트입니다. "
            "전문적이고 명확하며 친절한 어조로 응답하세요. 정확하고 간결하며 고객의 이해를 돕는 표현을 사용하세요."
        ),
        "prompt_header": "다음 목표와 요구사항에 따라 답변을 작성하세요:",
        "few_shot_header": "다음 예시를 참고하여 톤과 구조를 맞추세요:",
        "notes_header": "추가 설명 및 제약 조건:",
        "output_header": "최종 프롬프트",
    },
    "ja": {
        "name": "日本語",
        "system": (
            "あなたは LexisNexis のリーガルテック分野におけるカスタマーサクセス・コンサルタントです。"
            "専門的で明確かつ丁寧な口調で回答し、正確さと簡潔さ、そして相手の理解を重視してください。"
        ),
        "prompt_header": "以下の目的と要件に基づいて回答を作成してください：",
        "few_shot_header": "次の例を参考に、トーンと構成を整えてください：",
        "notes_header": "補足説明と制約条件：",
        "output_header": "最終プロンプト",
    },
}

# ---------------------------
# LexisNexis domain context (values for pickers)
# ---------------------------
LN_CONTEXT = {
    "products": [
        "Lexis+",
        "Lexis+ AI",
        "Practical Guidance",
        "Lexis PSL",
        "Risk Solutions",
        "Regulatory Compliance",
        "Nexis Data+",
    ],
    "roles": [
        "Customer Success Consultant",
        "Relationship Manager",
        "Sales Consultant",
        "Solutions Engineer",
    ],
    "audiences": [
        "GC / CLO",
        "Head of Compliance",
        "Litigation Partner",
        "KM / Innovation Lead",
        "In-house Legal Ops",
    ],
    "goals": ["renewal", "retention", "expansion", "adoption", "training", "QBR prep"],
    "metrics": [
        "license utilisation",
        "time-to-answer",
        "matter intake speed",
        "search success rate",
        "practice adoption",
        "risk flag reduction",
    ],
}

# ---------------------------
# Language-specific tone/style guidance
# ---------------------------
STYLE_TEMPLATES = {
    "en": {
        "tone_map": {
            "neutral": "Use a neutral, professional tone focused on clarity and actionability.",
            "friendly": "Sound approachable and supportive while remaining professional.",
            "formal": "Maintain a formal, respectful tone and avoid colloquialisms.",
            "persuasive": "Structure arguments clearly and emphasise value and outcomes.",
            "technical": "Use precise terminology and explain briefly when needed.",
            "concise": "Be brief and to the point; emphasise essentials.",
        },
        "closing": "Ensure the message is accurate, easy to follow, and client-centric.",
    },
    "zh": {
        "tone_map": {
            "neutral": "保持专业、平和的语气，重点在清晰与可操作性。",
            "friendly": "语气自然亲切，体现合作与支持，同时保持专业度。",
            "formal": "保持正式且礼貌的表达，避免口语化与冗长句式。",
            "persuasive": "结构清晰，有理有据，突出价值与预期成效。",
            "technical": "术语准确，必要处作简要解释，避免模糊表述。",
            "concise": "表达精炼、要点优先，避免重复。",
        },
        "closing": "请确保内容准确、易懂，并体现对客户需求的关注。",
    },
    "ko": {
        "tone_map": {
            "neutral": "전문적이고 중립적인 어조를 유지하며 명확하고 실행 가능한 표현을 사용하세요.",
            "friendly": "친근하고 협력적인 어조를 사용하되, 전문성을 유지하세요.",
            "formal": "격식을 갖춘 공손한 표현을 사용하고 구어체를 피하세요.",
            "persuasive": "논리를 명확히 하고 가치와 결과를 강조하세요.",
            "technical": "정확한 용어를 사용하고 필요한 경우 간단히 설명하세요.",
            "concise": "간결하고 핵심 위주로 작성하세요.",
        },
        "closing": "내용이 정확하고 이해하기 쉬우며, 고객 중심적이어야 합니다.",
    },
    "ja": {
        "tone_map": {
            "neutral": "専門的で中立的なトーンを維持し、明確で実行可能な表現を用いてください。",
            "friendly": "親しみやすく協調的なトーンを保ちつつ、専門性を失わないようにしてください。",
            "formal": "丁寧で礼儀正しい言葉遣いを使用し、くだけた表現を避けてください。",
            "persuasive": "論理を明確にし、価値や成果を強調してください。",
            "technical": "正確な専門用語を使い、必要に応じて簡潔に説明してください。",
            "concise": "簡潔に、要点を明確に述べてください。",
        },
        "closing": "内容が正確で理解しやすく、顧客志向であることを確認してください。",
    },
}

# ---------------------------
# English defaults for all recipes (fallbacks)
# ---------------------------
PROMPT_RECIPES = {
    "Client Snapshot & Risk Signals": """You are a LexisNexis {role}. Research {client_name}, a {client_type}.
Summarise:
• size, key practice areas, strategic priorities
• recent news, mergers, litigation, or policy changes
• 3 likely research/compliance challenges
• churn or expansion signals (with rationale)
Tailor to {audience_role} and relate to {products}. Tone: consultative.""",

    "Insight-Led Conversation Builder": """I’m meeting {client_name} (uses {products}). Generate 6 questions that:
• uncover current workflows and usage
• surface friction / underused features
• explore expansion (cross-sell, training)
• show empathy for {audience_role}
Return bullets grouped by theme.""",

    "Renewal Email": """Write a concise renewal email to {client_name}.
Include:
• outcomes achieved ({wins_or_metrics})
• relevant new features ({products})
• appreciation for partnership
• clear CTA for renewal/value review
Tone: warm, confident, consultative.""",

    "Adoption Plan (90 days)": """Create a 3-month adoption plan for {product_primary} for {client_type}.
Include milestones: training, feature activation, usage tracking, QBR. 
Add 2 ways {product_ai} improves efficiency. Return as week-by-week table + bullets.""",

    "QBR Brief": """Prepare a QBR for {client_name}.
Include:
• usage & engagement trends (hypothesize if missing)
• wins/metrics since last review
• 2 challenges or underused areas
• 3 solutions from LexisNexis mapped to needs
• recommended next steps""",

    "Account Growth Scan": """For {client_name}, list 3 cross-sell opportunities (e.g., {products}). 
Explain alignment to pain points and expected ROI/outcomes.""",

    "Meeting Summary": """From these notes: {meeting_notes}
Summarise:
• objectives & concerns
• follow-ups / deliverables
• upsell or risk indicators
• next steps (owner + due date)""",

    "Objection Coach": """Client hesitates to renew because: {objection}.
Provide:
• 3 empathetic acknowledgements
• 2 data-anchored value points (use {metrics} when possible)
• 1 strategic question to refocus on outcomes.""",

    "Product Explainer": """Explain {product_primary} plainly to {audience_role}.
Give 1 use case, 3 practical benefits, 1 measurable outcome for a legal team.""",

    "Sentiment & Retention Predictor": """Based on last 3 months of comms: {signal_snippets}
Assess tone & engagement. Flag satisfaction/risk/opportunity and suggest 2 retention actions.""",
}

# ---------------------------
# Localized (i18n) recipe bodies for key use cases
# If a recipe/lang pair is missing, we fall back to English defaults above.
# ---------------------------
RECIPES_I18N = {
    "Renewal Email": {
        "en": PROMPT_RECIPES["Renewal Email"],
        "zh": """请为 {client_name} 撰写一封简明的续约邮件。
请包含：
• 已取得的成果（{wins_or_metrics}）
• 与其场景相关的新功能（{products}）
• 对合作关系的感谢
• 一个明确的下一步（预约价值复盘/续约讨论）
语气：温和、自信、以咨询为导向。""",
        "ko": """{client_name}에게 보낼 간결한 갱신(재계약) 이메일을 작성하세요.
포함할 내용:
• 달성한 성과 ({wins_or_metrics})
• 관련성 높은 신규 기능 ({products})
• 파트너십에 대한 감사
• 가치 리뷰/갱신 논의를 위한 명확한 다음 단계(CTA)
톤: 따뜻하고 자신감 있으며, 컨설팅 중심.""",
        "ja": """{client_name}宛てに、簡潔な更新（契約更新）メールを作成してください。
含める内容：
• 達成した成果（{wins_or_metrics}）
• 関連する新機能（{products}）
• パートナーシップへの感謝
• 価値レビュー／更新打合せへの明確な次の一手（CTA）
トーン：温かく、自信があり、コンサルティブ。""",
    },

    "Client Snapshot & Risk Signals": {
        "en": PROMPT_RECIPES["Client Snapshot & Risk Signals"],
        "zh": """你是 LexisNexis 的 {role}。请研究 {client_name}（{client_type}），并概述：
• 规模、核心业务领域与战略重点
• 近期新闻/并购/诉讼/政策变化
• 3 个可能的法律研究或合规挑战
• 可能的流失或扩展信号（并说明理由）
请面向 {audience_role} 表达，并结合 {products} 提出洞察。语气：咨询式。""",
        "ko": """당신은 LexisNexis의 {role}입니다. {client_type}인 {client_name}을(를) 조사하고 다음을 요약하세요:
• 규모, 핵심 업무 분야, 전략적 우선순위
• 최근 뉴스/인수합병/소송/규제 변화
• 가능한 리서치·컴플라이언스 과제 3가지
• 이탈 위험 또는 확장 신호(근거 포함)
대상: {audience_role}. {products}와 연계한 인사이트를 제시하세요. 톤: 컨설팅형.""",
        "ja": """あなたは LexisNexis の{role}です。{client_type}である {client_name} を調査し、次を要約してください：
• 規模、主要分野、戦略上の優先事項
• 直近のニュース／M&A／訴訟／政策変更
• 想定されるリサーチ／コンプライアンス課題（3点）
• 離反または拡大の兆候（根拠付き）
想定読者：{audience_role}。{products} と関連付けた示唆を提示。トーン：コンサルティブ。""",
    },

    "Meeting Summary": {
        "en": PROMPT_RECIPES["Meeting Summary"],
        "zh": """基于以下会议记录：{meeting_notes}
请总结：
• 客户目标与关注点
• 后续事项/交付物
• 潜在扩容或风险信号
• 下一步（负责人 + 截止日期）""",
        "ko": """다음 회의 메모를 바탕으로 요약하세요: {meeting_notes}
요약 항목:
• 고객의 주요 목표와 우려
• 후속 작업/딜리버러블
• 업셀 또는 리스크 신호
• 다음 단계(담당자 + 마감일)""",
        "ja": """以下のメモに基づき要約してください：{meeting_notes}
要約項目：
• 顧客の目的と懸念
• フォローアップ／成果物
• アップセルまたはリスクの兆候
• 次のアクション（担当者＋期日）""",
    },

    "Objection Coach": {
        "en": PROMPT_RECIPES["Objection Coach"],
        "zh": """客户对续约有所顾虑，原因是：{objection}。
请提供：
• 3 条体现共情的回应方式
• 2 个以数据为依据的价值点（如可，结合 {metrics}）
• 1 个将对话拉回“业务结果/价值”的策略性问题。""",
        "ko": """고객이 다음 이유로 갱신을 망설이고 있습니다: {objection}
다음을 제시하세요:
• 공감을 담은 인정 표현 3가지
• 데이터 기반 가치 포인트 2가지(가능하면 {metrics} 활용)
• 결과 중심으로 다시 초점을 맞추는 전략적 질문 1가지""",
        "ja": """顧客が更新をためらう理由：{objection}
次を提示してください：
• 共感を示す言い回し 3つ
• データに基づく価値ポイント 2つ（可能であれば {metrics} を活用）
• 成果に焦点を戻す戦略的な問い 1つ""",
    },

    "QBR Brief": {
        "en": PROMPT_RECIPES["QBR Brief"],
        "zh": """为 {client_name} 准备一份 QBR 摘要。
请包含：
• 使用与参与度趋势（如数据缺失可作合理假设）
• 自上次评审以来的成果/指标
• 2 个挑战或未充分使用的功能
• 3 个与其需求匹配的 LexisNexis 解决方案
• 建议的下一步""",
        "ko": """{client_name}을(를) 위한 QBR 요약을 준비하세요.
포함할 내용:
• 사용량/참여도 트렌드(데이터 없으면 합리적 가정)
• 지난 리뷰 이후의 성과/지표
• 미활용 또는 도전 과제 2가지
• 니즈와 매칭되는 LexisNexis 솔루션 3가지
• 권장되는 다음 단계""",
        "ja": """{client_name}向けのQBR要約を作成してください。
含める内容：
• 利用状況・エンゲージメントの傾向（不足データは妥当な仮定で補足可）
• 前回レビュー以降の成果／指標
• 未活用または課題の領域 2点
• ニーズに合致する LexisNexis の解決策 3点
• 推奨される次のステップ""",
    },
}

# ---------------------------
# Helpers to assemble the final prompt
# ---------------------------
def _few_shot_block(lang_code: str, ex_input: str, ex_output: str) -> str:
    s = SCAFFOLDS[lang_code]
    if (ex_input or "").strip() or (ex_output or "").strip():
        return (
            f"\n\n{s['few_shot_header']}\n"
            f"- **Input**: {(ex_input or '').strip() or '[none]'}\n"
            f"- **Output**: {(ex_output or '').strip() or '[none]'}"
        )
    return ""

def _get_recipe_text(recipe: str, lang_code: str, vals: dict) -> str:
    table = RECIPES_I18N.get(recipe, {})
    template = table.get(lang_code) or table.get("en") or PROMPT_RECIPES[recipe]
    return template.format(**vals)

def fill_recipe(recipe: str, lang_code: str, ctx: dict) -> str:
    s = SCAFFOLDS[lang_code]
    vals = dict(
        role=ctx.get("role") or "Customer Success Consultant",
        client_name=ctx.get("client_name") or "[Client Name]",
        client_type=ctx.get("client_type") or "in-house legal",
        products=", ".join(ctx.get("products_used") or []) or "Lexis+ / Practical Guidance / Risk Solutions",
        product_primary=((ctx.get("products_used") or ["Lexis+"])[0]),
        product_ai="Lexis+ AI",
        audience_role=ctx.get("audience_role") or "GC / CLO",
        wins_or_metrics=ctx.get("wins_or_metrics") or "[insert outcomes/metrics]",
        metrics=", ".join(ctx.get("key_metrics") or []) or "license utilisation, search success rate",
        meeting_notes=ctx.get("meeting_notes") or "[paste notes]",
        objection=ctx.get("objection") or "[state objection]",
        signal_snippets=ctx.get("signal_snippets") or "[paste excerpts]",
    )

    body = _get_recipe_text(recipe, lang_code, vals)

    # Optional user goal / inputs
    goal = ctx.get("user_goal") or ""
    inputs = ctx.get("inputs") or ""

    # Style controls
    tone = ctx.get("tone") or "neutral"
    depth = ctx.get("depth") or "standard"
    length = ctx.get("length") or "medium"

    # Critique step
    add_critique = bool(ctx.get("add_critique"))
    critique_map = {
        "en": "Before finalizing, critique for accuracy, clarity, completeness, and bias. Revise once.",
        "zh": "在定稿前，请从准确性、清晰度、完整性与偏见等角度进行自我评估，并进行一次修订。",
        "ko": "최종 제출 전 정확성, 명확성, 완결성, 편향 여부를 점검하고 한 차례 수정하세요.",
        "ja": "最終化の前に、正確性・明確さ・網羅性・偏りを自己点検し、1回修正してください。",
    }
    critique_line = f"- {critique_map[lang_code]}" if add_critique else ""

    few_shot = _few_shot_block(lang_code, ctx.get("ex_input", ""), ctx.get("ex_output", ""))

    def bulletify(label, content):
        if not content:
            return ""
        lines = [l.strip() for l in content.split("\n") if l.strip()]
        if not lines:
            return ""
        return f"- **{label}**\n" + "\n".join([f"  - {l}" for l in lines])

    goal_block = bulletify("Goal", goal if lang_code == "en" else {
        "zh": "目标", "ko": "목표", "ja": "目的"
    }.get(lang_code, "Goal") and goal)  # label translation handled below

    # Translate bullet labels for non-English
    label_goal = {"en": "Goal", "zh": "目标", "ko": "목표", "ja": "目的"}[lang_code]
    label_inputs = {"en": "Inputs", "zh": "输入", "ko": "입력", "ja": "入力"}[lang_code]

    def bulletify_local(label, content):
        if not content:
            return ""
        lines = [l.strip() for l in content.split("\n") if l.strip()]
        if not lines:
            return ""
        return f"- **{label}**\n" + "\n".join([f"  - {l}" for l in lines])

    goal_block = bulletify_local(label_goal, goal)
    inputs_block = bulletify_local(label_inputs, inputs)

    # Language tone guidance
    style_tail = ""
    if lang_code in STYLE_TEMPLATES:
        tone_line = STYLE_TEMPLATES[lang_code]["tone_map"].get(tone, "")
        closing = STYLE_TEMPLATES[lang_code]["closing"]
        style_tail = f"\n- {tone_line}\n- {closing}" if tone_line else f"\n- {closing}"

    final = (
        f"[system]\n{s['system']}\n\n"
        f"[user]\n{body}\n"
        f"- Tone: {tone}\n- Depth: {depth}\n- Target length: {length}\n"
        f"{goal_block}\n{inputs_block}\n\n"
        f"{s['notes_header']}\n"
        f"- Respect confidentiality; avoid legal advice.\n"
        f"- Be precise; prefer verifiable statements.\n"
        f"- Highlight ROI using {vals['metrics']}.\n"
        f"- Suggest next steps with owners & dates."
        f"{style_tail}\n"
        f"{critique_line}"
        f"{few_shot}"
    ).strip()

    return final

def shape_output(text: str, mode: str, client_name: str, recipe: str) -> str:
    if mode == "email":
        subj = f"{client_name or 'Client'} — {recipe}"
        return (
            f"Subject: {subj}\n\n"
            f"Hi {client_name or 'team'},\n\n"
            f"[Paste generated content below]\n\n"
            f"Best regards,\n[Your Name]\nLexisNexis"
        )
    if mode == "CRM note":
        return f"# {recipe} — {client_name}\n- Date: {{today}}\n- Owner: [you]\n\n{text}\n\n**Next steps**: [owner] — [date]"
    if mode == "slide outline":
        return (
            f"Title: {client_name or 'Client'} — {recipe}\n"
            f"Slide 1: Context\nSlide 2: Insights\nSlide 3: Recommendations\nSlide 4: Next Steps\n\n"
            f"Content:\n{text}"
        )
    return text
