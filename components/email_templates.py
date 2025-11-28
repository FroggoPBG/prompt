# components/email_templates.py
# Generate fill-in-the-blank email templates from OUS analysis
from __future__ import annotations


def generate_outcome_hook_template(
    company_name: str,
    outcome: str,
    pain_point: str,
    buyer_name: str = "[Name]",
) -> str:
    """
    Template A: The Outcome Hook
    Leads with what they're trying to achieve.
    """
    return f"""Subject: Re: {company_name}'s {outcome[:40]}...

{buyer_name},

I saw {company_name} is working on {outcome}. 

From what we've seen with other HK firms tackling this, the biggest challenge isn't the obvious stuff - it's {pain_point}.

The GCs we work with describe our platform as "insurance against what we might've missed." For example, one HK-listed property firm used it to catch cross-border IP gaps before their audit.

Would it help to share how they approached this? Even if our tool isn't the right fit, I can point you to a useful resource.

Would next Tuesday at 3pm work for a quick 15-min call?

Best,
[Your Name]
"""


def generate_pain_point_entry_template(
    company_name: str,
    specific_challenge: str,
    similar_client: str,
    solution_approach: str,
    buyer_name: str = "[Name]",
) -> str:
    """
    Template B: The Pain Point Entry
    Leads with empathy about their specific struggle.
    """
    return f"""Subject: {specific_challenge} - quick insight

{buyer_name},

I read about {company_name}'s {specific_challenge}.

We recently helped {similar_client} (similar situation) and they found the hidden issue wasn't [obvious problem] - it was [second-order risk].

Here's how they fixed it: {solution_approach}

Not sure if this is relevant to you, but happy to share the full story if useful.

Would a quick 15-min call work? I'm free Tuesday at 11am or Thursday at 2pm.

Best,
[Your Name]

P.S. Even if our solution isn't a fit, I can send you a checklist they used - it's been helpful for other firms dealing with this.
"""


def generate_templates_from_analysis(
    company_name: str,
    outcome: str = "[Outcome - e.g., 'reducing outside counsel spend by 25%']",
    pain_point: str = "[Pain Point - e.g., 'junior associates spending 60% of time on manual cite-checking']",
    specific_challenge: str = "[Specific Challenge - e.g., 'cross-border PDPO compliance after Shenzhen acquisition']",
    similar_client: str = "[Similar Client - e.g., 'a HK-listed fintech company']",
    solution_approach: str = "[Solution Approach - e.g., 'automated compliance gap detection that caught 12 issues before their SFC audit']",
    buyer_name: str = "[Name]",
) -> dict:
    """
    Generate both email templates with placeholders.
    
    Returns dict with keys: 'template_a', 'template_b'
    """
    return {
        "template_a": generate_outcome_hook_template(
            company_name, outcome, pain_point, buyer_name
        ),
        "template_b": generate_pain_point_entry_template(
            company_name, specific_challenge, similar_client, solution_approach, buyer_name
        ),
    }
