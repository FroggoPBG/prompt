# ------------------------------------------------------------
# Core prompt scaffolds, recipes, and builders (no external APIs)
# Safe to use on Python 3.9+
# ------------------------------------------------------------
from __future__ import annotations
from typing import Dict

# ----------------------------
# Language scaffolds (email drafting focus)
# ----------------------------
SCAFFOLDS: Dict[str, Dict[str, str]] = {
    "en": {
        "name": "English",
        "sys": (
            "You are an assistant for Client-Facing Communications at LexisNexis "
            "(Sales & Customer Success) in the legal-tech domain. "
            "Respond with a professional, concise email to be sent to a client. "
            "Use the structure and headings provided by the user section."
        ),
        "role_lbl": "ROLE",
        "goal_lbl": "GOAL",
        "ctx_lbl": "CONTEXT",
        "req_lbl": "DELIVERABLE REQUIREMENTS",
        "info_lbl": "INFORMATION TO GATHER",
        "tone_lbl": "TONE",
        "len_lbl": "LENGTH",
        "extra_lbl": "Additional notes & constraints",
    }
}

# ------------------------------------------------------------
# Light global context used by UI pickers (keep keys stable)
# ------------------------------------------------------------
LN_CONTEXT = {
    "outputs": ["plain prompt", "email (markdown)"],
    "tones": ["auto", "warm", "consultative", "neutral", "apologetic", "confident"],
    "lengths": ["short", "medium", "long"],
    "products": [
        "Lexis+",
        "Lexis Advance",
        "Practical Guidance",
        "Lexis+ AI",
    ],
    "stages": ["Prospect", "Onboarding", "Adoption", "Renewal", "Expansion", "At Risk"],
    "regions": ["Hong Kong", "Singapore", "Japan", "South Korea", "Other"],
    "practice_areas": [
        "financial services", "corporate", "litigation", "IP", "tax", "employment", "other"
    ],
}

# ----------------------------
# Helpers
# ----------------------------
def _field(label: str, value: str | list | None) -> str:
    if value is None or value == "" or value == []:
        return ""
    if isinstance(value, list):
        val = ", ".join(value)
    else:
        val = str(value)
    return f"{label}: {val}\n"

def _header(txt: str) -> str:
    return f"**{txt}**:"

# ----------------------------
# Renewal Email builder (your two variants)
# ----------------------------
def build_renewal_email(ctx: dict, lang: str) -> str:
    """
    Builds a drafting prompt for a renewal email with two scenarios:
    1) Low usage + pricing concerns (empathetic, value-protecting, okay to downsize)
    2) Healthy usage (highlight value & usage naturally, relationship-focused)
    """
    sys = SCAFFOLDS[lang]["sys"]

    role = "Account Manager"
    goal = "Renewal outreach — draft email tailored to usage pattern."
    client_ctx = (
        f"Client: {ctx.get('client_name') or 'client'}; "
        f"Type: {ctx.get('client_type') or 'n/a'}; "
        f"Region: {ctx.get('region') or 'n/a'}; "
        f"Practice: {', '.join(ctx.get('practice_areas') or []) or 'n/a'}; "
        f"Products: {', '.join(ctx.get('products_used') or []) or 'n/a'}; "
        f"Stage: {ctx.get('relationship_stage') or 'n/a'}."
    )

    tone = ctx.get("tone") or "consultative"
    length = ctx.get("length") or "medium"

    renewal_date = ctx.get("renewal_date") or ctx.get("contract_details") or ""
    usage_freq = ctx.get("usage_frequency") or ""
    usage_modules = ctx.get("module_utilization") or ""
    usage_engagement = ctx.get("engagement_indicators") or ""
    meeting_options = ctx.get("meeting_options") or ""
    has_pricing_concern = (ctx.get("renewal_variant") == "Low usage & pricing concern")

    if has_pricing_concern:
        # Variant 1: Low usage + pricing concerns
        requirements = (
            "- Open with a polite greeting.\n"
            f"- Mention the upcoming renewal date ({renewal_date}).\n"
            "- Acknowledge the low usage pattern in a non-accusatory, curious way.\n"
            "- Express concern they may not be getting full value.\n"
            "- Offer help to identify whether it's training, wrong content fit, or changing needs.\n"
            "- Suggest a call to align the subscription with actual needs (downsize to save cost if appropriate).\n"
            "- Position as a partner who wants them to only pay for what's useful.\n"
            "- Keep the tone helpful, understanding, and focused on the right solution."
        )
        usage_block = (
            "Their recent usage indicators include:\n"
            f"• Frequency: {usage_freq or 'n/a'}\n"
            f"• Modules used: {usage_modules or 'n/a'}\n"
            f"• Engagement signals: {usage_engagement or 'n/a'}\n"
        )
        closing = (
            "Please propose a short call to discuss options. "
            f"If helpful, offer times ({meeting_options}) or invite them to suggest a convenient time."
        )
        final_instruction = (
            "Write a professional, empathetic, consultative **email**. "
            "Acknowledge that low usage might mean the current setup isn't working and you want to fix that "
            "rather than push an unchanged renewal. Be explicit that you're open to adjusting or reducing the "
            "subscription if that’s what makes sense."
        )

    else:
        # Variant 2: Healthy usage — demonstrate value without mentioning pricing concerns
        requirements = (
            "- Open with a polite greeting.\n"
            f"- Mention the upcoming renewal date ({renewal_date}).\n"
            "- Highlight specific usage patterns as evidence of value and workflow integration.\n"
            "- Show genuine interest in how they use the platform for their matters.\n"
            "- Request a call to discuss needs before finalizing renewal (collaborative tone).\n"
            "- Keep tone polite, convincing, and relationship-focused.\n"
            "- Do not explicitly mention pricing concerns."
        )
        usage_block = (
            "Observed usage highlights:\n"
            f"• Frequency: {usage_freq or 'n/a'}\n"
            f"• Most-used modules/databases: {usage_modules or 'n/a'}\n"
            f"• Other engagement indicators: {usage_engagement or 'n/a'}\n"
        )
        closing = (
            "Please suggest a short call to confirm the renewal scope and ensure it fits their upcoming matters. "
            f"Offer suggested times ({meeting_options}) or invite them to propose alternatives."
        )
        final_instruction = (
            "Write a professional, warm, consultative **email** that makes the client feel heard and valued."
        )

    # Prompt skeleton
    prompt = []
    prompt.append("[system]")
    prompt.append(sys)
    prompt.append("\n[user]")
    prompt.append(f"**{SCAFFOLDS[lang]['role_lbl']}**: {role}")
    prompt.append(f"**{SCAFFOLDS[lang]['goal_lbl']}**: {goal}")
    prompt.append(f"**{SCAFFOLDS[lang]['ctx_lbl']}**: {client_ctx}")
    if usage_block:
        prompt.append(usage_block)

    prompt.append(f"**{SCAFFOLDS[lang]['req_lbl']}**:\n{requirements}")
    prompt.append("**" + SCAFFOLDS[lang]['info_lbl'] + "**:")
    prompt.append(
        "- Client name, type, region, practice area(s)\n"
        "- Products in use; relationship stage; renewal timing\n"
        "- Usage frequency / modules used / engagement signals\n"
        "- Preferred tone and length"
    )
    prompt.append(f"**{SCAFFOLDS[lang]['tone_lbl']}**: {tone}")
    prompt.append(f"**{SCAFFOLDS[lang]['len_lbl']}**: {length}")

    prompt.append("\n" + _header(SCAFFOLDS[lang]["extra_lbl"]))
    extra = (
        "- Respect confidentiality; avoid legal advice.\n"
        "- Be precise; prefer verifiable statements.\n"
        "- Suggest clear next steps (owner & time window).\n"
        "- Keep formatting simple (paragraphs + short bullets if needed)."
    )
    prompt.append(extra)

    prompt.append("\nDraft the email now.\n")
    prompt.append(final_instruction)

    return "\n".join(prompt)


# ----------------------------
# Other functions/recipes registry
# ----------------------------
PROMPT_RECIPES: Dict[str, Dict[str, str]] = {
    # key names are used by app.py selectbox
    "Renewal Email": {
        "builder": "build_renewal_email",
    },
    # (You can keep other recipes here if you already had them)
}

# ----------------------------
# Public builders
# ----------------------------
def fill_recipe(recipe: str, lang_code: str, ctx: dict) -> str:
    """Dispatch to the appropriate builder based on recipe key."""
    if recipe == "Renewal Email":
        return build_renewal_email(ctx, lang_code)
    # Fallback
    return "Unknown recipe."

def shape_output(text: str, output_format: str, client_name: str | None, recipe: str) -> str:
    """Optionally wrap/shape the final output."""
    if output_format == "email (markdown)":
        title = f"# {recipe} – {client_name or 'Client'}"
        return f"{title}\n\n{text}"
    return text
