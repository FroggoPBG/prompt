# presets.py

"""
STRATEGY DEFINITIONS
Each key represents a specific client situation.
'name': What shows up in the dropdown.
'description': Helps the user pick the right tool.
'fields': The specific data points we need to make the email feel real (Anti-Phishing).
"""

STRATEGIES = {
    "ghosting_breaker": {
        "name": "The 'Ghosting' Breaker",
        "description": "Use this when a client has stopped replying. It uses the 'Negative Reverse' psychology to trigger a correction instinct.",
        "fields": [
            {"key": "client_name", "label": "Client First Name"},
            {"key": "last_topic", "label": "Topic of Last Discussion (e.g., 'the litigation module')"},
            {"key": "days_silent", "label": "Days since last contact (approx)"}
        ]
    },
    "value_first_renewal": {
        "name": "Value-First Renewal Intro",
        "description": "Don't just ask for a contract. Lead with a specific 'Win' or usage stat to trigger the Endowment Effect before mentioning the renewal date.",
        "fields": [
            {"key": "client_name", "label": "Client First Name"},
            {"key": "specific_win", "label": "A specific win/usage stat (e.g., 'your team ran 400 searches last month')"},
            {"key": "renewal_date", "label": "Renewal Date"}
        ]
    },
    "executive_brief": {
        "name": "The Executive Brief (TL;DR)",
        "description": "For high-level decision makers who don't read long emails. summarizing a new feature or risk in 3 bullet points.",
        "fields": [
            {"key": "client_name", "label": "Client First Name"},
            {"key": "feature_name", "label": "New Feature / Update Name"},
            {"key": "benefit_1", "label": "Key Benefit 1 (Save time?)"},
            {"key": "benefit_2", "label": "Key Benefit 2 (Reduce risk?)"}
        ]
    },
    "nps_feedback": {
        "name": "The 'Advice' Request (NPS)",
        "description": "People hate surveys, but they love giving advice. This asks for help improving the service rather than just a score.",
        "fields": [
            {"key": "client_name", "label": "Client First Name"},
            {"key": "recent_interaction", "label": "A recent interaction (e.g., 'our training session on Tuesday')"}
        ]
    }
}
