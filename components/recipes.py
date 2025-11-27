# recipes.py

def assemble_prompt(strategy_key, inputs):
    """
    Constructs the system and user prompts based on the selected strategy.
    """
    
    # 1. GLOBAL RULES (The "Anti-Phishing" Layer)
    # These rules apply to ALL emails to ensure they look human.
    global_constraints = """
    CRITICAL INSTRUCTIONS:
    1. Do NOT use generic openers like "I hope this email finds you well."
    2. Do NOT use marketing fluff words like "game-changer" or "unlock the power."
    3. Keep the tone: Professional, Direct, and Low-Pressure.
    4. The email must be under 120 words.
    5. Format for readability (short paragraphs).
    """

    # 2. STRATEGY SPECIFIC PROMPTS
    prompts = {
        "ghosting_breaker": f"""
        CONTEXT: The user is an Account Manager. The client ({inputs.get('client_name')}) has been silent for {inputs.get('days_silent')} days regarding '{inputs.get('last_topic')}'.
        
        GOAL: Elicit a "No" response using Chris Voss's "Negative Reverse" technique.
        
        DRAFTING RULES:
        - Subject Line: Should be vague but relevant, e.g., "{inputs.get('last_topic')}?"
        - Opening: Reference the last topic immediately.
        - The Ask: Ask if they have "given up" on this project or if it is no longer a priority.
        - Sign-off: Simple.
        """,

        "value_first_renewal": f"""
        CONTEXT: Renewal is coming up on {inputs.get('renewal_date')}. We need to remind {inputs.get('client_name')} of the value they are getting.
        
        GOAL: Anchor the conversation in value before asking for the meeting.
        
        DRAFTING RULES:
        - Subject Line: "Reviewing your results / {inputs.get('renewal_date')}"
        - Opening: State the specific win: "{inputs.get('specific_win')}".
        - The Bridge: Connect that win to the upcoming renewal.
        - The Ask: A low-friction call to discuss the next year.
        """,

        "executive_brief": f"""
        CONTEXT: Writing to a busy executive named {inputs.get('client_name')} about {inputs.get('feature_name')}.
        
        GOAL: Inform them without wasting time.
        
        DRAFTING RULES:
        - Subject Line: "Update: {inputs.get('feature_name')}"
        - Structure: One sentence intro, three bullet points, one sentence closing.
        - Bullet 1: Focus on {inputs.get('benefit_1')}.
        - Bullet 2: Focus on {inputs.get('benefit_2')}.
        - The Ask: "Do you want me to enable this for your team?" (Yes/No question).
        """,
        
        "nps_feedback": f"""
        CONTEXT: We need feedback from {inputs.get('client_name')} following {inputs.get('recent_interaction')}.
        
        GOAL: Frame this as asking for "Advice" rather than completing a "Survey".
        
        DRAFTING RULES:
        - Subject Line: "Quick question re: {inputs.get('recent_interaction')}"
        - Opening: Mention the recent interaction to prove this isn't an automated bot.
        - The Hook: "I'm trying to improve how we handle X, and I'd value your advice."
        - The Ask: Link to the survey, but frame it as "sharing your thoughts."
        """
    }

    # Return the combined prompt
    specific_instructions = prompts.get(strategy_key, "Draft a professional email.")
    
    full_system_prompt = f"You are an expert Customer Success Manager. \n{global_constraints}"
    full_user_prompt = specific_instructions
    
    return full_system_prompt, full_user_prompt
