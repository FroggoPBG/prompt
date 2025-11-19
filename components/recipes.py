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
