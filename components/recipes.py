from datetime import datetime

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
        "output_header": "Final prompt"
    },
    "es": {
        "name": "Español",
        "system": (
            "Eres un asistente para Customer Success en el sector legal‑tech de LexisNexis. "
            "Responde con un tono profesional, claro y útil. Prioriza la precisión, la concisión y la comprensión del cliente."
        ),
        "prompt_header": "Elabora una respuesta según estos requisitos:",
        "few_shot_header": "Usa estos ejemplos como referencia de tono y estructura:",
        "notes_header": "Notas y restricciones adicionales:",
        "output_header": "Prompt final"
    },
    "fr": {
        "name": "Français",
        "system": (
            "Vous êtes un assistant pour le Customer Success dans le domaine legal‑tech chez LexisNexis. "
            "Adoptez un ton professionnel, clair et utile. Donnez la priorité à l’exactitude, à la concision et à la compréhension du client."
        ),
        "prompt_header": "Rédigez une réponse selon les exigences suivantes :",
        "few_shot_header": "Utilisez ces exemples pour le ton et la structure :",
        "notes_header": "Notes et contraintes supplémentaires :",
        "output_header": "Invite finale"
    },
    "de": {
        "name": "Deutsch",
        "system": (
            "Du unterstützt Customer Success im Legal‑Tech‑Bereich von LexisNexis. "
            "Antworte professionell, klar und hilfsorientiert. Priorisiere Genauigkeit, Kürze und gutes Verständnis für den Kunden."
        ),
        "prompt_header": "Erstelle eine Antwort gemäß folgenden Anforderungen:",
        "few_shot_header": "Nutze diese Beispiele für Tonalität und Struktur:",
        "notes_header": "Zusätzliche Hinweise und Rahmenbedingungen:",
        "output_header": "Finaler Prompt"
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
        "output_header": "最终提示词"
    }
}

LN_CONTEXT = {
    "products": [
        "Lexis+","Lexis+ AI","Practical Guidance","Lexis PSL",
        "Risk Solutions","Regulatory Compliance","Nexis Data+"
    ],
    "roles": [
        "Customer Success Consultant","Relationship Manager",
        "Sales Consultant","Solutions Engineer"
    ],
    "audiences": [
        "GC / CLO","Head of Compliance","Litigation Partner",
        "KM / Innovation Lead","In-house Legal Ops"
    ],
    "goals": [
        "renewal","retention","expansion","adoption","training","QBR prep"
    ],
    "metrics": [
        "license utilisation","time-to-answer","matter intake speed",
        "search success rate","practice adoption","risk flag reduction"
    ]
}

STYLE_TEMPLATES = {
    "en": {
        "tone_map": {
            "neutral": "Use a neutral, professional tone focused on clarity and actionability.",
            "friendly": "Sound approachable and supportive while remaining professional.",
            "formal": "Maintain a formal, respectful tone and avoid colloquialisms.",
            "persuasive": "Structure arguments clearly and emphasise value and outcomes.",
            "technical": "Use precise terminology and explain briefly when needed.",
            "concise": "Be brief and to the point; emphasise essentials."
        },
        "closing": "Ensure the message is accurate, easy to follow, and client‑centric."
    },
    "es": {
        "tone_map": {
            "neutral": "Usa un tono neutro y profesional, centrado en la claridad y la utilidad.",
            "friendly": "Sé cercano y colaborativo sin perder la profesionalidad.",
            "formal": "Mantén un tono formal y respetuoso; evita expresiones coloquiales.",
            "persuasive": "Estructura los argumentos y destaca el valor y los resultados.",
            "technical": "Emplea términos precisos y explica brevemente cuando sea necesario.",
            "concise": "Sé breve y directo; céntrate en lo esencial."
        },
        "closing": "Asegúrate de que el contenido sea exacto, fácil de seguir y centrado en el cliente."
    },
    "fr": {
        "tone_map": {
            "neutral": "Adoptez un ton neutre et professionnel, axé sur la clarté et l’utilité.",
            "friendly": "Restez chaleureux et collaboratif tout en demeurant professionnel.",
            "formal": "Conservez un ton formel et respectueux; évitez les tournures familières.",
            "persuasive": "Structurez les arguments et mettez en avant la valeur et les résultats.",
            "technical": "Employez une terminologie précise avec de brèves explications si besoin.",
            "concise": "Soyez bref et allez à l’essentiel."
        },
        "closing": "Veillez à l’exactitude, à la lisibilité et à l’orientation client."
    },
    "de": {
        "tone_map": {
            "neutral": "Nutze einen neutralen, professionellen Ton mit Fokus auf Klarheit und Nutzen.",
            "friendly": "Klingt freundlich und kooperativ, aber weiterhin professionell.",
            "formal": "Bewahre einen formellen, respektvollen Ton; vermeide Umgangssprache.",
            "persuasive": "Strukturiere Argumente klar und hebe Nutzen sowie Ergebnisse hervor.",
            "technical": "Verwende präzise Fachbegriffe und erkläre kurz bei Bedarf.",
            "concise": "Fasse dich kurz und konzentriere dich aufs Wesentliche."
        },
        "closing": "Achte auf Genauigkeit, gute Lesbarkeit und Kundenorientierung."
    },
    "zh": {
        "tone_map": {
            "neutral": "保持专业、平和的语气，重点在清晰与可操作性。",
            "friendly": "语气自然亲切，体现合作与支持，同时保持专业度。",
            "formal": "保持正式且礼貌的表达，避免口语化与冗长句式。",
            "persuasive": "结构清晰，有理有据，突出价值与预期成效。",
            "technical": "术语准确，必要处作简要解释，避免模糊表述。",
            "concise": "表达精炼、要点优先，避免重复。"
        },
        "closing": "请确保内容准确、易懂，并体现对客户需求的关注。"
    }
}

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
Assess tone & engagement. Flag satisfaction/risk/opportunity and suggest 2 retention actions."""
}

def _few_shot_block(lang_code: str, ex_input: str, ex_output: str) -> str:
    s = SCAFFOLDS[lang_code]
    if (ex_input or "").strip() or (ex_output or "").strip():
        return f"\n\n{s['few_shot_header']}\n- **Input**: {(ex_input or '').strip() or '[none]'}\n- **Output**: {(ex_output or '').strip() or '[none]'}"
    return ""

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
        signal_snippets=ctx.get("signal_snippets") or "[paste excerpts]"
    )
    body = PROMPT_RECIPES[recipe].format(**vals)

    goal = ctx.get("user_goal") or ""
    inputs = ctx.get("inputs") or ""

    tone = ctx.get("tone") or "neutral"
    depth = ctx.get("depth") or "standard"
    length = ctx.get("length") or "medium"

    add_critique = bool(ctx.get("add_critique"))
    critique_map = {
        "en": "Before finalizing, critique for accuracy, clarity, completeness, and bias. Revise once.",
        "es": "Antes de finalizar, critica por precisión, claridad, exhaustividad y sesgos. Revisa una vez.",
        "fr": "Avant de finaliser, évaluez l’ébauche pour l’exactitude, la clarté, l’exhaustivité et les biais. Révisez une fois.",
        "de": "Bevor du abschließt, prüfe den Entwurf auf Genauigkeit, Klarheit, Vollständigkeit und Verzerrungen. Überarbeite einmal.",
        "zh": "在定稿前，请从准确性、清晰度、完整性与偏见等角度进行自我评估，并进行一次修订。"
    }
    critique_line = f"- {critique_map[lang_code]}" if add_critique else ""

    few_shot = _few_shot_block(lang_code, ctx.get("ex_input",""), ctx.get("ex_output",""))

    def bulletify(label, content):
        if not content: return ""
        lines = [l.strip() for l in content.split("\n") if l.strip()]
        if not lines: return ""
        return f"- **{label}**\n" + "\n".join([f"  - {l}" for l in lines])

    goal_block = bulletify("Goal", goal)
    inputs_block = bulletify("Inputs", inputs)

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
        return f"Subject: {subj}\n\nHi {client_name or 'team'},\n\n[Paste generated content below]\n\nBest regards,\n[Your Name]\nLexisNexis"
    if mode == "CRM note":
        return f"# {recipe} — {client_name}\n- Date: {{today}}\n- Owner: [you]\n\n{text}\n\n**Next steps**: [owner] — [date]"
    if mode == "slide outline":
        return f"Title: {client_name or 'Client'} — {recipe}\nSlide 1: Context\nSlide 2: Insights\nSlide 3: Recommendations\nSlide 4: Next Steps\n\nContent:\n{text}"
    return text
