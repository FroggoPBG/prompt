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
            "당신은 LexisN
