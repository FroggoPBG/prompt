# ------------------------------------------------------------
# Core prompt scaffolds, recipes, and builders used by the UI.
# No external APIs. Python 3.9+ compatible.
# ------------------------------------------------------------
from __future__ import annotations
from typing import Dict, List

# -----------------------------
# Language scaffolds (email focus)
# -----------------------------
SCAFFOLDS: Dict[str, Dict[str, str]] = {
    "en": {
        "name": "English",
        "sys": (
            "You are an assistant for client-facing communications (Sales & Customer Success) "
            "in the legal-tech domain at LexisNexis. Respond with a professional, concise email "
            "that is ready to send to a client. Use the headings and structure provided."
        ),
        "role_lbl": "ROLE",
        "goal_lbl": "GOAL",
        "ctx_lbl": "CONTEXT",
        "req_lbl": "DELIVERABLE REQUIREMENTS",
        "info_lbl": "INFORMATION TO GATHER",
        "tone_lbl": "TONE",
        "len_lbl": "LENGTH",
        "extra_lbl": "Additional notes & constraints",
        "nps_pasted_lbl": "NPS Verbatim Insights (pasted)",
        "nps_internal_lbl": "NPS Insights (internal)",
    },
    # You can add more languages later (zh/ko/ja) following the same keys.
}

# -----------------------------
# Shared picklists / context
# -----------------------------
LN_CONTEXT = {
    "outputs": ["plain prompt"],
    "client_types": [
        "in-house legal", "law firm", "corporate", "public sector", "academic"
    ],
    "regions": [
        "Hong Kong", "Singapore", "Japan", "Korea", "Malaysia", "Australia", "Other"
    ],
    "practice_areas": [
        "financial services", "litigation", "corporate", "tax", "IP", "personal injury, tort",
        "regulatory", "criminal", "employment", "real estate"
    ],
    "stages": [
        "New / Onboarding", "Adoption & Growth", "Renewal", "Risk / Churn"
    ],
    "products": [
        "Lexis+", "Practical Guidance", "Lexis Advance", "Lexis Create", "Lexis Red",
        "Nexis"
    ],
    "tones": ["auto", "warm", "consultative", "apologetic", "formal", "friendly"],
    "lengths": ["short", "medium", "long"],
}

# ---------------------------------------
# Optional product blurbs you can append
# ---------------------------------------
PRODUCT_BLURBS = {
    "Lexis+": "Lexis+ combines case law, legislation, practical guidance, and visualization tools in a single search experience designed for faster, more confident answers.",
    "Practical Guidance": "Practical Guidance provides step-by-step how-to content, checklists, precedents, and practice notes written by experts—ideal for faster drafting and onboarding.",
    "Lexis Advance": "Lexis Advance offers comprehensive primary law and journals with powerful filters that help you surface the right authority quickly.",
    "Lexis Create": "Lexis Create embeds drafting tools and clause libraries into Word to help you create consistent, on-brand documents faster.",
    "Nexis": "Nexis aggregates trusted news, companies, and risk data to support due diligence, business development, and regulatory monitoring.",
}

# ------------------------------------------------
# Small helpers
# ------------------------------------------------
def _hdr(label: str, value: str) -> str:
    return f"**{label}**: {value}"

def _list(items: List[str]) -> str:
    return "\n".join([f"- {x}" for x in items])

def _safe(val, default=""):
    return val if val else default

# ------------------------------------------------
# Recipe builders
# ------------------------------------------------

def build_nps_engagement(ctx: dict, lang_code: str) -> str:
    """Promoter / Passive / Detractor variants for initial NPS engagement."""
    scaffold = SCAFFOLDS[lang_code]
    prev = ctx.get("nps_previous_rating", "Passive (7–8)")
    survey = _safe(ctx.get("nps_survey_link", ""))
    theme = _safe(ctx.get("nps_feedback_theme", ""))
    variant = "promoter" if prev.startswith("Promoter") else "passive" if prev.startswith("Passive") else "detractor"

    if variant == "promoter":
        tone_line = "grateful, collaborative"
        para = (
            "Open by appreciating their past high rating and support. "
            "Position them as partners whose input helps us maintain a high standard. "
            "Mention the survey takes under 2 minutes. Keep the tone warm but not overly effusive."
        )
        subject_hint = "Appreciation for your insights"
    elif variant == "passive":
        tone_line = "humble, improvement-oriented"
        para = (
            "Acknowledge we're doing 'good' but aim to be 'great'. "
            "Invite candid input on what to keep / stop / start. "
            "Mention we read every response personally and the survey takes under 2 minutes."
        )
        subject_hint = "Helping us go from good to great"
    else:
        tone_line = "sincere, respectful, non-defensive"
        para = (
            "Acknowledge prior low rating and that we’ve been working on improvements. "
            "Ask whether things have improved, stayed the same, or need more work. "
            "Keep it brief and respectful of their time; mention under 2 minutes."
        )
        subject_hint = "A quick check-in on your experience"

    body = f"""
[system]
{scaffold["sys"]}

[user]
{_hdr(scaffold["role_lbl"], "Customer Success Manager")}
{_hdr(scaffold["goal_lbl"], "NPS Engagement — create content ready to send or adapt.")}
{_hdr(scaffold["ctx_lbl"], f"Client: {_safe(ctx.get('client_name','client'))}; Type: {_safe(ctx.get('client_type','law firm'))}; Region: {_safe(ctx.get('region','Hong Kong'))}; Practice: {_safe(', '.join(ctx.get('practice_areas', [])) or 'n/a')}; Products: {_safe(', '.join(ctx.get('products_used', [])) or 'n/a')}; Stage: {_safe(ctx.get('relationship_stage','Adoption & Growth'))}.")}
{_hdr(scaffold["req_lbl"], "")}
- Adapt tone to prior NPS ({variant}).
- Briefly explain why feedback matters now.
- Provide survey link and a concise CTA.
{_hdr(scaffold["info_lbl"], "")}
- Client name, type, region, practice area(s)
- Products in use; relationship stage
- Usage metrics / adoption; time saved / ROI evidence
- NPS score / theme (if relevant)
- Contract timing (if renewal) and any pricing notes
- Preferred language and tone
{_hdr(scaffold["tone_lbl"], tone_line)}
{_hdr(scaffold["len_lbl"], _safe(ctx.get('length','medium')))}

Draft a short NPS engagement email. Guidance for this case:
- {para}
- Subject should hint: {subject_hint}.
- Feedback theme (if any): {theme or '—'}
- Survey link: {survey or '—'}
"""
    return body.strip()


def build_nps_followup(ctx: dict, lang_code: str) -> str:
    """Follow-up email after NPS response with comment."""
    scaffold = SCAFFOLDS[lang_code]
    prev = ctx.get("nps_previous_rating", "Promoter (9–10)")
    comment_type = _safe(ctx.get("npsf_comment_type", "General feedback"))
    verbatim = _safe(ctx.get("npsf_verbatim", ""))
    pointer = _safe(ctx.get("npsf_pointer", ""))
    escalated = ctx.get("npsf_escalated_note", "")

    variant = "promoter" if prev.startswith("Promoter") else "passive" if prev.startswith("Passive") else "detractor"

    default_tone = "appreciative" if variant == "promoter" else "improvement-oriented" if variant == "passive" else "sincere"
    goal = "NPS Follow-up"

    body = f"""
[system]
{scaffold["sys"]}

[user]
{_hdr(scaffold["role_lbl"], "Customer Success Manager")}
{_hdr(scaffold["goal_lbl"], goal)}
{_hdr(scaffold["ctx_lbl"], f"Client: {_safe(ctx.get('client_name','client'))}; Type: {_safe(ctx.get('client_type','law firm'))}; Region: {_safe(ctx.get('region','Hong Kong'))}; Practice: {_safe(', '.join(ctx.get('practice_areas', [])) or 'n/a')}; Products: {_safe(', '.join(ctx.get('products_used', [])) or 'n/a')}; Stage: {_safe(ctx.get('relationship_stage','Adoption & Growth'))}.")}
{_hdr(scaffold["req_lbl"], "")}
- Adapt tone to prior NPS ({variant}).
- Start by thanking them and referencing their exact comment (quote briefly).
- Address based on type: how-to, feature request, bug/issue, or general praise/concern.
- Offer a helpful next step: quick tip, link/where to click, or request clarifying needs.
- Close with a clear CTA (reply or brief call) and appreciation.
- If relevant, include a product pointer or escalation note.
- Comment type noted: {comment_type}
{_hdr(scaffold["info_lbl"], "")}
- Client info, products, stage, language/tone preferences
- Any helpful product pointers or links
{_hdr(scaffold["tone_lbl"], _safe(ctx.get('tone', default_tone)))}
{_hdr(scaffold["len_lbl"], _safe(ctx.get('length','medium')))}

Draft a concise follow-up email tailored to their rating and comment. Use the proper tone.

Quoted client comment (short excerpt):
\"\"\"{verbatim}\"\"\"

Helpful pointer (optional):
{pointer or '—'}

Internal note / escalation (if provided; summarize for client appropriately):
{escalated or '—'}
"""
    return body.strip()


def build_renewal_email(ctx: dict, lang_code: str) -> str:
    """Renewal outreach with two scenarios: low-usage vs healthy-usage."""
    scaffold = SCAFFOLDS[lang_code]
    angle = ctx.get("renewal_angle", "Pricing concern + low usage")
    renewal_date = _safe(ctx.get("renewal_date", ""))
    usage_summary = _safe(ctx.get("usage_summary", ""))
    modules_used = _safe(ctx.get("modules_used", ""))
    engagement = _safe(ctx.get("engagement_indicators", ""))
    region = _safe(ctx.get("region", "Hong Kong"))

    if angle == "Pricing concern + low usage":
        goal = "Renewal — Value Rescue"
        tone = "empathetic, consultative"
        bullets = [
            "Open with a polite greeting and mention the upcoming renewal date.",
            "Acknowledge low usage patterns in a non-accusatory, curious way.",
            "Express genuine concern that they may not be getting full value.",
            "Offer to identify if it’s a training issue, content fit, or changing needs.",
            "Propose a call to align the subscription with actual needs (including potential downsize to save cost).",
            "Position yourself as a partner who wants them to only pay for what’s useful."
        ]
    else:
        goal = "Renewal — Demonstrate Value"
        tone = "warm, consultative"
        bullets = [
            "Open with a polite greeting and the renewal date.",
            "Highlight how their usage supports value (frequency, modules, workflows).",
            "Invite a quick discussion to confirm priorities and any changes for the next term.",
            "Keep the focus collaborative rather than transactional.",
            "Be sensitive to cost without explicitly referencing pricing concerns."
        ]

    body = f"""
[system]
{scaffold["sys"]}

[user]
{_hdr(scaffold["role_lbl"], "Account Manager")}
{_hdr(scaffold["goal_lbl"], goal)}
{_hdr(scaffold["ctx_lbl"], f"Client: {_safe(ctx.get('client_name','client'))}; Type: {_safe(ctx.get('client_type','law firm'))}; Region: {region}; Practice: {_safe(', '.join(ctx.get('practice_areas', [])) or 'n/a')}; Products: {_safe(', '.join(ctx.get('products_used', [])) or 'n/a')}; Stage: {_safe(ctx.get('relationship_stage','Renewal'))}.")}
{_hdr(scaffold["req_lbl"], "")}
{_list(bullets)}
{_hdr(scaffold["info_lbl"], "")}
- Renewal date: {renewal_date or '—'}
- Usage summary: {usage_summary or '—'}
- Modules / databases used: {modules_used or '—'}
- Engagement indicators: {engagement or '—'}
- Any product facts to include below (if provided)
{_hdr(scaffold["tone_lbl"], tone)}
{_hdr(scaffold["len_lbl"], _safe(ctx.get('length','medium')))}

Draft a professional renewal email in natural English for a {region} law firm. Keep it helpful, understanding, and solution-focused.

Optional product facts to weave in (if helpful for context):
{_safe(ctx.get('product_facts','—'))}
"""
    return body.strip()


# ------------------------------------------------
# Registry
# ------------------------------------------------
PROMPT_RECIPES = [
    "Renewal Email",
    "NPS Engagement",
    "NPS Follow-up",
]

_BUILDERS = {
    "Renewal Email": build_renewal_email,
    "NPS Engagement": build_nps_engagement,
    "NPS Follow-up": build_nps_followup,
}

def fill_recipe(recipe: str, lang_code: str, ctx: dict) -> str:
    builder = _BUILDERS.get(recipe)
    if not builder:
        return "Unsupported recipe."
    return builder(ctx, lang_code)

def shape_output(text: str, output_format: str, client_name: str, recipe: str) -> str:
    # For now we only expose "plain prompt" in the UI.
    return text
