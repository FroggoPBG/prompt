import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Multilingual Prompt Builder", page_icon="🧠", layout="wide")

# Simple, hard-coded scaffolds so we don't need any APIs or model downloads
SCAFFOLDS = {
    "en": {
        "name": "English",
        "system": "You are an expert assistant. Follow the user's instructions carefully. Ask for clarifications only when necessary.",
        "prompt_header": "Construct a response with the following requirements:",
        "few_shot_header": "Follow these examples as style/quality guides:",
        "notes_header": "Additional notes & constraints:",
        "output_header": "Final prompt"
    },
    "es": {
        "name": "Español",
        "system": "Eres un asistente experto. Sigue cuidadosamente las instrucciones del usuario. Pide aclaraciones solo cuando sea necesario.",
        "prompt_header": "Elabora una respuesta con los siguientes requisitos:",
        "few_shot_header": "Sigue estos ejemplos como guía de estilo/calidad:",
        "notes_header": "Notas y restricciones adicionales:",
        "output_header": "Prompt final"
    },
    "fr": {
        "name": "Français",
        "system": "Vous êtes un assistant expert. Suivez attentivement les instructions de l’utilisateur. Ne demandez des précisions que si nécessaire.",
        "prompt_header": "Construisez une réponse avec les exigences suivantes :",
        "few_shot_header": "Suivez ces exemples comme guide de style/qualité :",
        "notes_header": "Notes et contraintes supplémentaires :",
        "output_header": "Invite finale"
    },
    "de": {
        "name": "Deutsch",
        "system": "Du bist ein fachkundiger Assistent. Befolge die Anweisungen sorgfältig. Bitte nur bei Bedarf um Klarstellungen.",
        "prompt_header": "Erstelle eine Antwort mit folgenden Anforderungen:",
        "few_shot_header": "Nutze diese Beispiele als Stil-/Qualitätsleitfaden:",
        "notes_header": "Zusätzliche Hinweise & Einschränkungen:",
        "output_header": "Finaler Prompt"
    },
    "zh": {
        "name": "中文",
        "system": "你是一名专家级助手。请严格遵循用户指令，仅在必要时提问澄清。",
        "prompt_header": "请根据以下要求生成回答：",
        "few_shot_header": "请参考以下示例的风格与质量：",
        "notes_header": "其他说明与约束：",
        "output_header": "最终提示词"
    }
}

st.title("🧠 Multilingual Prompt Builder (no APIs)")

colA, colB = st.columns([2, 3])

with colA:
    lang_code = st.selectbox(
        "Target language",
        options=list(SCAFFOLDS.keys()),
        format_func=lambda k: SCAFFOLDS[k]["name"],
        index=0
    )
    s = SCAFFOLDS[lang_code]

    task = st.selectbox(
        "Task type",
        ["Write", "Summarize", "Translate", "Brainstorm", "Classify", "Extract", "Code Review"]
    )

    role = st.text_input("Role/persona (optional)", placeholder="e.g., senior data scientist, legal researcher, copy chief")

    audience = st.text_input("Audience (optional)", placeholder="e.g., non-technical executives, law students, developers")

    tone = st.select_slider("Tone", options=["neutral", "formal", "concise", "persuasive", "friendly", "technical"], value="neutral")

    depth = st.select_slider("Depth/rigor", options=["brief", "standard", "in-depth"], value="standard")

    length = st.select_slider("Target length", options=["very short", "short", "medium", "long"], value="medium")

    constraints = st.text_area("Constraints / must-haves", placeholder="e.g., cite 3 sources; include bullet points; avoid jargon")

    acceptance = st.checkbox("Add self-critique + revision step", value=True)

with colB:
    user_goal = st.text_area("Your goal / problem statement", height=120, placeholder="Describe what you want the model to do.")
    inputs = st.text_area("Key inputs (paste any text/data/instructions)", height=120, placeholder="Optional: source text, facts, requirements…")
    st.caption("Few-shot examples (optional)")
    ex_col1, ex_col2 = st.columns(2)
    with ex_col1:
        ex_input = st.text_area("Example input", height=100, placeholder="Short example input")
    with ex_col2:
        ex_output = st.text_area("Example output", height=100, placeholder="Desired example output")

def bulletify(label, content):
    if not content: return ""
    lines = [l.strip() for l in content.split("\n") if l.strip()]
    if not lines: return ""
    return f"- **{label}**\n" + "\n".join([f"  - {l}" for l in lines])

if st.button("Generate prompt"):
    scaffold = SCAFFOLDS[lang_code]

    # Map generic labels into the selected language (kept simple to avoid APIs)
    label_map = {
        "Write": {"en":"Write","es":"Redacta","fr":"Rédige","de":"Schreibe","zh":"撰写"},
        "Summarize": {"en":"Summarize","es":"Resume","fr":"Résume","de":"Fasse zusammen","zh":"总结"},
        "Translate": {"en":"Translate","es":"Traduce","fr":"Traduisez","de":"Übersetze","zh":"翻译"},
        "Brainstorm": {"en":"Brainstorm","es":"Genera ideas","fr":"Brainstorming","de":"Brainstorming","zh":"头脑风暴"},
        "Classify": {"en":"Classify","es":"Clasifica","fr":"Classifiez","de":"Klassifiziere","zh":"分类"},
        "Extract": {"en":"Extract","es":"Extrae","fr":"Extrayez","de":"Extrahiere","zh":"提取"},
        "Code Review": {"en":"Review code","es":"Revisa el código","fr":"Relisez le code","de":"Code prüfen","zh":"代码评审"},
    }

    verb = label_map.get(task, {}).get(lang_code, task)

    # Compose few-shot block if provided
    few_shot_block = ""
    if ex_input.strip() or ex_output.strip():
        few_shot_block = f"\n\n{scaffold['few_shot_header']}\n- **Input**: {ex_input.strip() or '[none]'}\n- **Output**: {ex_output.strip() or '[none]'}"

    # Compose constraints and inputs as bullets
    inputs_block = bulletify("Inputs", inputs)
    constraints_block = bulletify(scaffold["notes_header"], constraints)

    # Build the final prompt text
    lines = []
    lines.append(f"[system]\n{scaffold['system']}")
    lines.append("\n[user]")

    # Header describing the task in target language
    header = f"{verb} a response."
    if lang_code == "es": header = f"{verb} una respuesta."
    if lang_code == "fr": header = f"{verb} une réponse."
    if lang_code == "de": header = f"{verb} eine Antwort."
    if lang_code == "zh": header = f"{verb} 一段回答。"

    lines.append(header)

    # Role, audience, tone, depth, length
    if role: lines.append(f"- Role/persona: {role}")
    if audience: lines.append(f"- Audience: {audience}")
    lines.append(f"- Tone: {tone}")
    lines.append(f"- Depth: {depth}")
    lines.append(f"- Target length: {length}")

    # Goal + requirements
    if user_goal:
        lines.append(f"\n{scaffold['prompt_header']}\n- Goal: {user_goal.strip()}")
    if inputs_block: lines.append(inputs_block)
    if constraints_block: lines.append(constraints_block)

    if acceptance:
        # A language-agnostic critique loop phrased simply
        critique = {
            "en": "Before finalizing, critique your draft for accuracy, clarity, completeness, and bias. Revise once.",
            "es": "Antes de finalizar, critica tu borrador por precisión, claridad, exhaustividad y sesgos. Revisa una vez.",
            "fr": "Avant de finaliser, évaluez l’ébauche pour l’exactitude, la clarté, l’exhaustivité et les biais. Révisez une fois.",
            "de": "Bevor du abschließt, prüfe den Entwurf auf Genauigkeit, Klarheit, Vollständigkeit und Verzerrungen. Überarbeite einmal.",
            "zh": "在定稿前，请从准确性、清晰度、完整性与偏见等角度进行自我评估，并进行一次修订。"
        }[lang_code]
        lines.append(f"- {critique}")

    if few_shot_block: lines.append(few_shot_block)

    final_prompt = "\n".join(lines).strip()

    st.subheader(f"📝 {scaffold['output_header']}")
    st.code(final_prompt, language="markdown")

    # Offer a download with no dependencies
    fname = f"prompt_{lang_code}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.txt"
    st.download_button("Download prompt as .txt", final_prompt, file_name=fname, mime="text/plain")

st.markdown("---")
st.caption("Tip: This app uses only rule-based templates—no external APIs or model calls.")
