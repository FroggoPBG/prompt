# components/recipes.py
# Multilingual scaffolds, tone guidance, product highlights, and prompt recipes
# for LexisNexis CS / RM / Sales Consulting
# Languages supported: English (en), Chinese (zh), Korean (ko), Japanese (ja)
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
# Product highlights by region (auto-injected bullets)
# ---------------------------
PRODUCT_HIGHLIGHTS = {
    "Practical Guidance": {
        "Hong Kong": {
            "Financial Services": {
                "updates": 50,
                "notable": [
                    "Tokenization of Real-World Assets and Native Tokenization Techniques",
                    "HKMA regulatory guideline on tokenised product",
                    "HKMA guidance to authorised institutions on tokenised products",
                    "Securities and Futures Commission regulatory framework on security token offerings",
                    "SFC insights on offering tokenised public funds in Hong Kong",
                    "Hong Kong’s Dual Licensing Regime for Virtual Asset Trading Platforms and Service Providers",
                    "Cryptocurrencies or virtual assets in insolvency",
                    "Hong Kong financial regulation of crypto-assets",
                    "Fund Manager Code of Conduct",
                    "Open-Ended Fund Company Regime in Hong Kong",
                ],
            },
            "Corporate": {
                "updates": 261,
                "notable": [
                    "Custom Articles of Association (private company limited by shares)",
                    "Model Articles of Association (private companies limited by shares)",
                    "Deadlock (50/50) and majority–minority AOA examples",
                    "Board minutes – skeleton samples",
                    "Virtual General Meetings – use of technology",
                    "Non-disclosure of residential address of directors",
                    "Registration of non-Hong Kong companies in Hong Kong",
                    "First board minutes (private/public; bespoke/shelf)",
                    "Resisting winding up petitions (Evergrande and beyond)",
                    "Companies Registry forms (NAR1, NSC1, NN1, etc.)",
                ],
            },
            "Employment": {
                "updates": 341,
                "notable": [
                    "Executive service agreement (director or senior employee)",
                    "Employment contract",
                    "Hong Kong minimum wage",
                    "Policy – anti-harassment",
                    "Mental health and well-being policy – Hong Kong",
                    "MPF/ORS overview",
                    "Taxation of termination payments",
                    "Share options / share awards",
                    "Data protection and social media",
                ],
            },
            "Dispute Resolution (HKIAC)": {
                "updates": 242,
                "notable": [
                    "HKIAC (2024) – consolidation of arbitrations",
                    "HKIAC (2024) – awards, decisions and orders of the arbitral tribunal",
                    "HKIAC (2024) – disclosure of third-party funding of arbitration",
                    "HKIAC (2024) – emergency relief",
                    "HKIAC (2024) – statement of claim/defence and amendments",
                    "HKIAC (2024) – time limits",
                ],
            },
        }
    }
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
# Headings for the "prompt-as-a-brief" wrapper (localized)
# ---------------------------
BRIEF_LABELS = {
    "ROLE": {"en": "ROLE", "zh": "角色", "ko": "역할", "ja": "役割"},
    "GOAL": {"en": "GOAL", "zh": "目标", "ko": "목표", "ja": "目的"},
    "REQUIREMENTS": {"en": "DELIVERABLE REQUIREMENTS", "zh": "交付要求", "ko": "전달물 요구사항", "ja": "成果物要件"},
    "TONE": {"en": "TONE", "zh": "语气", "ko": "톤", "ja": "トーン"},
    "LENGTH": {"en": "LENGTH", "zh": "长度", "ko": "분량", "ja": "長さ"},
    "INFO": {"en": "INFORMATION TO GATHER", "zh": "需收集信息", "ko": "수집해야 할 정보", "ja": "収集すべき情報"},
    "CONTEXT": {"en": "CONTEXT", "zh": "上下文", "ko": "컨텍스트", "ja": "コンテキスト"},
    "HIGHLIGHTS": {"en": "Product highlights", "zh": "产品亮点", "ko": "제품 하이라이트", "ja": "製品ハイライト"},
}

# ---------------------------
# Helpers
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

def render_product_highlights(lang_code: str, products_used: list, region: str) -> str:
    if not products_used or not region or region == "Global":
        return ""
    label = BRIEF_LABELS["HIGHLIGHTS"][lang_code]
    lines = []
    for p in products_used:
        reg_table = PRODUCT_HIGHLIGHTS.get(p, {}).get(region)
        if not reg_table:
            continue
        lines.append(f"- **{p} — {region}**")
        for cat, info in reg_table.items():
            updates = info.get("updates")
            notables = info.get("notable", [])
            lines.append(f"  - {cat} — {updates} updates")
            for item in notables:
                lines.append(f"    - {item}")
    if not lines:
        return ""
    return f"- **{label}**\n" + "\n".join(lines)

# ---------------------------
# Structured brief builders per recipe (pulls from dynamic form fields)
# ---------------------------
def _build_brief_sections(recipe: str, lang: str, ctx: dict) -> dict:
    """Return dict with role, goal, requirements(list), tone, length, info_to_gather(list), context(str)"""

    # Translated option labels for objection types
    OBJECTION_MAP = {
        "Price": {"en":"Price","zh":"价格","ko":"가격","ja":"価格"},
        "Usability": {"en":"Usability","zh":"可用性","ko":"사용성","ja":"使いやすさ"},
        "Prefer Competitor": {"en":"Prefer Competitor","zh":"偏好竞品","ko":"경쟁사 선호","ja":"競合の方を好む"},
    }

    # Defaults
    role = ctx.get("role") or "Customer Success Manager"
    tone = ctx.get("tone") or "neutral"
    length = ctx.get("length") or "medium"
    goal = ""
    req = []
    info = []
    context = ""

    if recipe == "Renewal Email":
        level = ctx.get("pricing_concern_level") or "Moderate"
        meeting_opts = (ctx.get("meeting_options") or "").strip()
        products_to_mention = ", ".join(ctx.get("products_used") or [])
        goal = {
            "en": "Demonstrate tangible ROI and reframe the conversation from cost to value.",
            "zh": "展示可量化的投资回报，将讨论从“成本”转向“价值”。",
            "ko": "가시적 ROI를 제시하여 대화를 비용에서 가치 중심으로 전환합니다.",
            "ja": "具体的なROIを示し、議論をコストから価値へ転換します。",
        }[lang]
        req = {
            "en": [
                "Open with appreciation and acknowledge pricing feedback.",
                "Demonstrate delivered value: usage metrics, positive feedback (e.g., NPS), and business outcomes.",
                f"Highlight forward-looking value: introduce {products_to_mention or 'relevant LexisNexis tools'} and upcoming enhancements.",
                "Propose next steps: offer an ROI/value review and include 2–3 date/time options.",
            ],
            "zh": [
                "以感谢合作开篇，并正面回应对价格的反馈。",
                "展示已实现的价值：使用数据、正向反馈（如 NPS）、与业务结果的关联。",
                f"强调前瞻价值：介绍 {products_to_mention or '相关 LexisNexis 工具'} 及即将推出的功能。",
                "提出下一步：邀请进行 ROI/价值复盘，并给出 2–3 个时间选项。",
            ],
            "ko": [
                "감사의 인사로 시작하고 가격 관련 피드백을 공감합니다.",
                "제공한 가치 제시: 사용 지표, 긍정적 피드백(NPS 등), 비즈니스 성과 연결.",
                f"미래 가치 강조: {products_to_mention or '관련 LexisNexis 도구'} 및 예정 기능 소개.",
                "다음 단계 제안: ROI/가치 리뷰 제안 및 2–3개 일정 옵션 포함.",
            ],
            "ja": [
                "感謝の言葉で始め、価格に関するフィードバックに丁寧に言及します。",
                "提供価値の提示：利用指標、ポジティブな評価（NPS等）、業務成果との結び付け。",
                f"将来価値の強調：{products_to_mention or '関連する LexisNexis ツール'} や今後の機能強化を紹介。",
                "次のステップ：ROI/価値レビューの提案と 2～3 の候補日時を記載。",
            ],
        }[lang]
        info = {
            "en": ["Usage metrics", "ROI/time saved", "Practice areas", "Contract details", "NPS quotes"],
            "zh": ["使用数据", "ROI/节省时间", "业务领域", "合同细节", "NPS 评价"],
            "ko": ["사용 지표", "ROI/절감 시간", "업무 영역", "계약 세부사항", "NPS 코멘트"],
            "ja": ["利用指標", "ROI/時間削減", "プラクティス領域", "契約詳細", "NPS コメント"],
        }[lang]
        context = {
            "en": f"Pricing concern level: {level}. Meeting options: {meeting_opts or '[add 2–3 options]'}",
            "zh": f"价格关注程度：{level}。可选会面时间：{meeting_opts or '[添加 2–3 个选项]'}",
            "ko": f"가격 우려 수준: {level}. 미팅 옵션: {meeting_opts or '[2–3개 옵션 추가]'}",
            "ja": f"価格に関する懸念度：{level}。ミーティング候補：{meeting_opts or '[候補を2～3件入力]'}",
        }[lang]

    elif recipe == "QBR Brief":
        window = ctx.get("qbr_window") or "Last Quarter"
        compare = ctx.get("qbr_compare_benchmarks")
        sections = ctx.get("qbr_sections") or []
        goal = {
            "en": "Create a consultative, data-driven QBR that demonstrates outcomes and identifies opportunities.",
            "zh": "生成以数据与咨询为导向的 QBR，展示成果并识别机会。",
            "ko": "성과를 보여주고 기회를 식별하는 데이터 기반 컨설팅형 QBR을 작성합니다.",
            "ja": "成果を示し、機会を特定するデータドリブンなコンサル型QBRを作成します。",
        }[lang]
        chosen = ", ".join(sections) if sections else "All standard sections"
        req = {
            "en": [
                f"Usage & engagement trends for {window}.",
                "Business impact: time saved, risk mitigated, efficiency gains.",
                "Wins since last review, underused features, and clear recommendations.",
            ],
            "zh": [
                f"{window} 的使用与参与度趋势。",
                "业务影响：节省时间、降低风险、提升效率。",
                "自上次评审以来的亮点、未充分使用功能与明确建议。",
            ],
            "ko": [
                f"{window} 기간의 사용/참여 트렌드.",
                "비즈니스 임팩트: 시간 절감, 리스크 완화, 효율 향상.",
                "지난 리뷰 이후의 성과, 미활용 기능, 명확한 제안.",
            ],
            "ja": [
                f"{window} の利用・エンゲージメント傾向。",
                "ビジネス効果：時間短縮、リスク低減、効率化。",
                "前回以降の成果、未活用機能、明確な提言。",
            ],
        }[lang]
        if compare:
            req.append({
                "en": "Include relevant benchmarks for comparison.",
                "zh": "加入相关基准对比。",
                "ko": "관련 벤치마크 비교 포함.",
                "ja": "関連ベンチマークとの比較を含める。",
            }[lang])
        context = {
            "en": f"Selected sections: {chosen}",
            "zh": f"所选章节：{chosen}",
            "ko": f"선택 섹션: {chosen}",
            "ja": f"選択セクション：{chosen}",
        }[lang]

    elif recipe == "Client Snapshot & Risk Signals":
        prepared_by = ctx.get("prepared_by") or "Sales"
        last_eng = ctx.get("last_engagement_date") or ""
        risk = ctx.get("risk_level") or "Medium"
        goal = {
            "en": "Provide a concise briefing for Customer Success before renewal or review.",
            "zh": "在续约或评审前，为客户成功团队提供简明简报。",
            "ko": "갱신/리뷰 전 고객 성공팀을 위한 간결한 브리핑을 제공합니다.",
            "ja": "更新/レビュー前にカスタマーサクセス向けの簡潔なブリーフィングを提供します。",
        }[lang]
        req = {
            "en": [
                "Firm overview and recent developments.",
                "Engagement insights and sentiment.",
                "Risk indicators and growth signals.",
            ],
            "zh": ["客户概况与近期动态。", "互动洞察与情绪。", "风险信号与扩展信号。"],
            "ko": ["고객 개요와 최근 동향.", "참여 인사이트와 분위기.", "리스크 신호와 성장 신호."],
            "ja": ["概要と直近の動向。", "エンゲージメント洞察と感触。", "リスク指標と成長シグナル。"],
        }[lang]
        context = {
            "en": f"Prepared by: {prepared_by}. Last engagement: {last_eng or '—'}. Risk level: {risk}.",
            "zh": f"准备人：{prepared_by}。最近互动：{last_eng or '—'}。风险等级：{risk}。",
            "ko": f"작성자: {prepared_by}. 최근 접점: {last_eng or '—'}. 리스크 수준: {risk}.",
            "ja": f"作成者：{prepared_by}。直近の接点：{last_eng or '—'}。リスクレベル：{risk}。",
        }[lang]

    elif recipe == "Objection Coach":
        typ = ctx.get("objection_type") or "Price"
        severity = ctx.get("objection_severity") or 3
        comp = ctx.get("competitor_name") or ""
        data_pts = ctx.get("supporting_data") or []
        typ_local = OBJECTION_MAP.get(typ, OBJECTION_MAP["Price"])[lang]
        goal = {
            "en": "Craft empathetic, data-backed responses that shift focus from cost to outcomes.",
            "zh": "以同理心与数据支撑回应，将焦点从“成本”转向“结果/价值”。",
            "ko": "공감과 데이터로 뒷받침된 응답을 통해 비용에서 결과 중심으로 초점을 전환합니다.",
            "ja": "共感とデータに基づく回答で、焦点をコストから成果へ転換します。",
        }[lang]
        req = {
            "en": [
                f"Acknowledge the concern ({typ_local}); keep tone collaborative.",
                "Provide 2–3 value points with data where possible.",
                "Ask one reframing question that leads to ROI discussion.",
            ],
            "zh": [
                f"认可并回应其顾虑（{typ_local}），保持合作姿态。",
                "给出 2–3 个以数据支撑的价值点。",
                "提出 1 个引导至 ROI 讨论的重构问题。",
            ],
            "ko": [
                f"우려를 인정하고 공감 표명 ({typ_local}); 협업적 톤 유지.",
                "데이터 기반 가치 포인트 2–3개 제시.",
                "ROI 논의로 연결하는 재프레이밍 질문 1개.",
            ],
            "ja": [
                f"懸念（{typ_local}）を認め、共感を示す（協調的トーン）。",
                "可能であればデータを添えた価値ポイントを2～3提示。",
                "ROI 議論に導くリフレーミングの質問を1つ。",
            ],
        }[lang]
        info = {
            "en": ["Usage metrics", "ROI/time saved", "NPS quotes", "Case studies", "Benchmarks"],
            "zh": ["使用数据", "ROI/节省时间", "NPS 评价", "案例研究", "行业基准"],
            "ko": ["사용 지표", "ROI/절감 시간", "NPS 코멘트", "사례 연구", "벤치마크"],
            "ja": ["利用指標", "ROI/時間削減", "NPS コメント", "事例", "ベンチマーク"],
        }[lang]
        context = {
            "en": f"Type: {typ_local}; Severity: {severity}/5; Competitor: {comp or '—'}; Data available: {', '.join(data_pts) or '—'}",
            "zh": f"类型：{typ_local}；严重程度：{severity}/5；竞品：{comp or '—'}；可用数据：{', '.join(data_pts) or '—'}",
            "ko": f"유형: {typ_local}; 심각도: {severity}/5; 경쟁사: {comp or '—'}; 보유 데이터: {', '.join(data_pts) or '—'}",
            "ja": f"タイプ：{typ_local}／深刻度：{severity}/5／競合：{comp or '—'}／保有データ：{', '.join(data_pts) or '—'}",
        }[lang]

    else:
        goal = {
            "en": "Deliver a professional, complete response.",
            "zh": "生成专业且完整的回应。",
            "ko": "전문적이고 완결성 있는 결과물을 제공합니다.",
            "ja": "専門的で抜け漏れのない成果物を作成します。",
        }[lang]
        req = {
            "en": ["Follow the user’s instructions exactly.", "Be concise and precise."],
            "zh": ["严格遵循指令。", "表述简洁且准确。"],
            "ko": ["지시를 정확히 따르세요.", "간결하고 정확하게 작성하세요."],
            "ja": ["指示に正確に従ってください。", "簡潔かつ正確に記述してください。"],
        }[lang]

    # Length guidance per recipe
    length_map = {
        "Renewal Email": {"en":"250–350 words","zh":"250–350 字","ko":"250–350 단어","ja":"250～350語"},
        "QBR Brief": {"en":"400–500 words","zh":"400–500 字","ko":"400–500 단어","ja":"400～500語"},
        "Client Snapshot & Risk Signals": {"en":"300–400 words","zh":"300–400 字","ko":"300–400 단어","ja":"300～400語"},
        "Objection Coach": {"en":"150–200 words","zh":"150–200 字","ko":"150–200 단어","ja":"150～200語"},
    }
    length_local = length_map.get(recipe, {}).get(lang, "")

    return {
        "role": role,
        "goal": goal,
        "requirements": req,
        "tone": tone,
        "length": length_local or length,
        "info": info,
        "context": context,
    }

def _render_brief(lang: str, sections: dict) -> str:
    # Assemble a localized "prompt-as-a-brief"
    def bullets(items):
        if not items: return ""
        return "\n" + "\n".join([f"- {i}" for i in items])

    L = BRIEF_LABELS
    out = []
    out.append(f"**{L['ROLE'][lang]}**: {sections['role']}")
    out.append(f"**{L['GOAL'][lang]}**: {sections['goal']}")
    if sections.get("context"):
        out.append(f"**{L['CONTEXT'][lang]}**: {sections['context']}")
    if sections.get("requirements"):
        out.append(f"**{L['REQUIREMENTS'][lang]}**:{bullets(sections['requirements'])}")
    if sections.get("info"):
        out.append(f"**{L['INFO'][lang]}**:{bullets(sections['info'])}")
    if sections.get("tone"):
        out.append(f"**{L['TONE'][lang]}**: {sections['tone']}")
    if sections.get("length"):
        out.append(f"**{L['LENGTH'][lang]}**: {sections['length']}")
    return "\n".join(out)

# ---------------------------
# Main fill function
# ---------------------------
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

    # Localized core body (stays as a compact instruction set for the LLM)
    core_body = _get_recipe_text(recipe, lang_code, vals)

    # Structured brief wrapper (driven by dynamic UI fields)
    brief_sections = _build_brief_sections(recipe, lang_code, ctx)
    brief_text = _render_brief(lang_code, brief_sections)

    # Optional user goal / inputs from the right panel
    user_goal = ctx.get("user_goal") or ""
    inputs = ctx.get("inputs") or ""

    # Language tone guidance
    style_tail = ""
    if lang_code in STYLE_TEMPLATES:
        tone_line = STYLE_TEMPLATES[lang_code]["tone_map"].get(ctx.get("tone") or "neutral", "")
        closing = STYLE_TEMPLATES[lang_code]["closing"]
        style_tail = f"\n- {tone_line}\n- {closing}" if tone_line else f"\n- {closing}"

    # Optional HK highlights
    highlights_block = ""
    if ctx.get("include_highlights"):
        highlights_block = render_product_highlights(
            lang_code, ctx.get("products_used") or [], ctx.get("region") or ""
        )

    # Few-shot examples if provided
    few_shot = _few_shot_block(lang_code, ctx.get("ex_input", ""), ctx.get("ex_output", ""))

    # Assemble final prompt
    def bulletify(label, content):
        if not content: return ""
        lines = [l.strip() for l in content.split("\n") if l.strip()]
        if not lines: return ""
        return f"- **{label}**\n" + "\n".join([f"  - {l}" for l in lines])

    label_goal = {"en": "Goal", "zh": "目标", "ko": "목표", "ja": "目的"}[lang_code]
    label_inputs = {"en": "Inputs", "zh": "输入", "ko": "입력", "ja": "入力"}[lang_code]
    goal_block = bulletify(label_goal, user_goal)
    inputs_block = bulletify(label_inputs, inputs)

    final = (
        f"[system]\n{s['system']}\n\n"
        f"[user]\n{brief_text}\n\n"
        f"{core_body}\n"
        f"{goal_block}\n{inputs_block}\n"
        f"{highlights_block}\n\n"
        f"{s['notes_header']}\n"
        f"- Respect confidentiality; avoid legal advice.\n"
        f"- Be precise; prefer verifiable statements.\n"
        f"- Highlight ROI using {vals['metrics']}.\n"
        f"- Suggest next steps with owners & dates."
        f"{style_tail}\n"
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
