# components/recipes.py
# Multilingual prompt-brief builder for CS/RM/Sales (no external APIs)

# ---------- Language scaffolds ----------
SCAFFOLDS = {
    "en": {
        "name": "English",
        "system": (
            "You are an assistant for Customer Success in the legal-tech domain at LexisNexis. "
            "Respond with a professional, clear, and helpful tone. Prioritize accuracy, brevity, and client understanding."
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
            "전문적이고 명확하며 친절한 어조로 응답하세요. 정확하고 간결하며 고객의 이해를 돕는 표현을 사용하세요."
        ),
        "notes_header": "추가 설명 및 제약 조건:",
    },
    "ja": {
        "name": "日本語",
        "system": (
            "あなたは LexisNexis のリーガルテック分野におけるカスタマーサクセス・コンサルタントです。"
            "専門的で明確かつ丁寧な口調で回答し、正確さと簡潔さ、そして相手の理解を重視してください。"
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
        "tort", "personal injury", "company", "corporate", "IP", "criminal", "contract",
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
        "Low usage", "Complaint", "Previous negative comments", "Previous positive comments",
    ],
    "tones": ["auto", "neutral", "friendly", "consultative", "persuasive", "formal", "polite", "apologetic", "technical", "concise"],
    "lengths": ["very short", "short", "medium", "long"],
    "outputs": ["plain prompt", "email", "CRM note", "slide outline"],
}

# ---------- Region product highlights (short, valid) ----------
PRODUCT_HIGHLIGHTS = {
    "Practical Guidance": {
        "Hong Kong": {
            "Financial Services": {
                "updates": 50,
                "notable": [
                    "Tokenization of Real-World Assets; HKMA guidelines on tokenised products",
                    "SFC framework on security token offerings; insights on tokenised public funds",
                    "Dual licensing regime for virtual asset trading platforms",
                    "Crypto-assets regulation; Fund Manager Code of Con
