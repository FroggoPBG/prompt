# ------------------------------------------------------------
# Core prompt scaffolds, recipes, and builders used by the UI.
# Safe to use without any external APIs. Python 3.9+ compatible.
# ------------------------------------------------------------

from __future__ import annotations
from typing import Dict, List

# ------------------------------
# Language scaffolds (email focus)
# ------------------------------
SCAFFOLDS: Dict[str, Dict[str, str]] = {
    "en": {
        "name": "English",
        "sys": (
            "You are an assistant for client-facing communications at LexisNexis. "
            "Respond with a professional, concise email to be sent to a client. "
            "Use the structure and headings (if any) the user asks for, but keep it short, clear, and actionable."
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
    }
}

# ------------------------------
# Global, reusable context values
# ------------------------------
LN_CONTEXT = {
    "outputs": ["plain prompt", "email draft", "bulleted outline"],
    "client_types": ["in-house legal", "law firm", "gov/academic", "corporate"],
    "regions": [
        "Hong Kong", "Singapore", "Japan", "Korea",
        "Australia", "New Zealand", "India", "Other"
    ],
    "practice_areas": [
        "financial services", "commercial", "employment", "IP",
        "dispute resolution", "personal injury / tort", "regulatory", "tax", "other"
    ],
    "products": ["Lexis+", "Practical Guidance", "Lexis Advance", "News / Dossiers"],
    "stages": ["Prospect", "Onboarding", "Adoption", "Renewal", "At-risk"],
    "tones": ["warm", "neutral", "consultative", "apologetic", "formal"],
    "lengths": ["short", "medium", "long"],
}

# ------------------------------
# Helper: render a short header line (kept minimal)
# ------------------------------
def _header_line(title: str) -> str:
    return f"{title}\n" + "-" * len(title)

# ------------------------------
# Email body builders per recipe
# ------------------------------
def _build_renewal_low_usage(ctx: dict) -> str:
    """Renewal email acknowledging low usage; offers right-sizing/help."""
    client = ctx.get("client_name") or "your team"
    renewal = ctx.get("renewal_date") or "the upcoming term"
    usage_bullets = []
    if ctx.get("usage_low_freq"):
        usage_bullets.append(ctx["usage_low_freq"])
    if ctx.get("usage_limited_modules"):
        usage_bullets.append(ctx["usage_limited_modules"])
    if ctx.get("usage_low_engagement"):
        usage_bullets.append(ctx["usage_low_engagement"])

    usage_txt = ""
    if usage_bullets:
        usage_txt = "\n".join([f"• {b}" for b in usage_bullets])

    body = f"""Dear {client},

I’m reaching out ahead of {renewal} to make sure the subscription still fits your day-to-day needs.

Looking at recent activity, I noticed lower usage than expected and want to be sure you’re getting full value. Here’s a quick view of the pattern we’re seeing:
{usage_txt or "• Lower than typical sign-ins and limited feature use."}

Rather than push a like-for-like renewal, I’d love to:
• Understand whether this is a training issue, a content fit issue, or simply changing team needs
• Walk through how different users are working today, and
• If it’s the right call, right-size the subscription so you’re only paying for what’s useful

Would you be open to a short call to review options? If it makes sense to reduce scope and save costs, I’ll recommend that path. My goal is to keep the setup aligned to your actual work and budget.

Best regards,
{ctx.get("account_owner") or "Account Manager"}
LexisNexis
"""
    return body


def _build_renewal_value_evidence(ctx: dict) -> str:
    """Renewal email highlighting concrete usage value; collaborative tone."""
    client = ctx.get("client_name") or "your team"
    renewal = ctx.get("renewal_date") or "the upcoming term"

    usage_points = []
    if ctx.get("usage_freq"):
        usage_points.append(f"• Access frequency: {ctx['usage_freq']}")
    if ctx.get("usage_modules"):
        usage_points.append(f"• Most-used modules: {ctx['usage_modules']}")
    if ctx.get("usage_other"):
        usage_points.append(f"• Engagement: {ctx['usage_other']}")

    usage_txt = "\n".join(usage_points) if usage_points else "• Regular use across key modules."

    body = f"""Dear {client},

Ahead of {renewal}, I wanted to check in on how the team is using LexisNexis and ensure we align the renewal to your current matters.

Here are a few highlights from your recent activity:
{usage_txt}

I’d value a brief conversation to confirm what’s working well and where we can tune things for the next term—whether that’s optimizing seats, surfacing the right content, or enabling features your team would benefit from.

Would you have 15 minutes this week or next to walk through priorities? I’ll come prepared with options so we keep this collaborative and outcome-focused.

Warm regards,
{ctx.get("account_owner") or "Account Manager"}
LexisNexis
"""
    return body


def _build_nps_engagement(ctx: dict) -> str:
    """General NPS engagement (pre-survey) — tone varies by prior score."""
    prior = (ctx.get("nps_previous_rating") or "").lower()
    client = ctx.get("client_name") or "there"

    if "promoter" in prior:
        opening = ("Thank you again for your previous high rating—your support helps us keep the bar high. "
                   "We’d value your perspective once more.")
        subject = "Appreciate your insights — quick 2-min survey"
        tone_hint = "warm, appreciative, collaborative"
    elif "passive" in prior:
        opening = ("We’re glad things are going well, and we’re committed to moving from “good” to “great.” "
                   "Your candid input helps us focus on what matters.")
        subject = "Help us go from good to great — 2-min check-in"
        tone_hint = "humble, improvement-oriented"
    else:
        opening = ("We’ve been working to improve and would genuinely value your honest perspective. "
                   "If things haven’t changed, we want to know; if they have, we’d love to learn where.")
        subject = "We’re listening — quick 2-min check-in"
        tone_hint = "sincere, non-defensive, respectful"

    link = ctx.get("nps_survey_link") or "[insert survey link]"

    body = f"""Subject: {subject}

Hi {client},

{opening}
The survey takes under 2 minutes, and we read every response personally:

{link}

Thanks in advance for helping us serve you better.
({tone_hint} tone)

Best,
{ctx.get("account_owner") or "Customer Success"}
LexisNexis
"""
    return body


def _build_nps_follow_up(ctx: dict) -> str:
    """Follow-up email tailored to the client’s NPS rating and verbatim comment."""
    client = ctx.get("client_name") or "there"
    rating = ctx.get("nps_previous_rating") or "recent feedback"
    comment_type = ctx.get("nps_comment_type") or "comment"
    verbatim = ctx.get("nps_verbatim") or ""
    pointer = ctx.get("nps_helpful_pointer") or ""
    internal = ctx.get("nps_internal_note") or ""
    closing_cta = ctx.get("cta") or "Would you be open to a brief 10–15 minute call to discuss?"

    pre = ""
    if "promoter" in rating.lower():
        pre = "Thank you for the positive rating—your feedback is incredibly helpful."
    elif "passive" in rating.lower():
        pre = "Thanks for sharing your perspective. We’re focused on moving from good to great."
    else:
        pre = "Thanks for your candid feedback—we take it seriously and want to address it."

    pointer_line = f"\nHelpful note: {pointer}\n" if pointer else ""
    internal_line = f"\n(Internal status: {internal})\n" if internal else ""

    body = f"""Hi {client},

{pre}
I noted your {comment_type.lower()}:
“{verbatim}”

{pointer_line}We’d love to make sure you’re fully covered and supported. {closing_cta}

Please share a couple of times that work, or reply here with details—we’ll take it from there.{internal_line}

Best regards,
{ctx.get("account_owner") or "Customer Success"}
LexisNexis
"""
    return body


# ------------------------------
# Registry of recipes
# ------------------------------
PROMPT_RECIPES: Dict[str, Dict[str, str]] = {
    "Renewal: Low Usage / Right-size": {
        "desc": "Acknowledges low usage; offers training/right-sizing with cost sensitivity.",
        "builder": "renewal_low_usage",
    },
    "Renewal: Value Evidence": {
        "desc": "Uses concrete usage patterns as value proof; collaborative tone.",
        "builder": "renewal_value_evidence",
    },
    "NPS Engagement": {
        "desc": "Survey engagement note; tone adapts to prior score.",
        "builder": "nps_engagement",
    },
    "NPS Follow-up": {
        "desc": "Follow-up on specific NPS verbatim (promoter, passive, detractor).",
        "builder": "nps_follow_up",
    },
}


# ------------------------------
# Public API: fill recipe & shape output
# ------------------------------
def fill_recipe(recipe_name: str, lang_code: str, ctx: dict) -> str:
    builder_key = PROMPT_RECIPES.get(recipe_name, {}).get("builder", "")
    if builder_key == "renewal_low_usage":
        return _build_renewal_low_usage(ctx)
    if builder_key == "renewal_value_evidence":
        return _build_renewal_value_evidence(ctx)
    if builder_key == "nps_engagement":
        return _build_nps_engagement(ctx)
    if builder_key == "nps_follow_up":
        return _build_nps_follow_up(ctx)
    # Fallback
    return "No builder found for the selected function."


def shape_output(text: str, output_target: str, client_name: str, recipe_name: str) -> str:
    if output_target == "bulleted outline":
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        bullets = "\n".join([f"- {l}" for l in lines])
        return bullets
    # For "email draft" or "plain prompt" we just return the text
    return text
