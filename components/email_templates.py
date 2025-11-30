def generate_insight_driven_email(context: ProspectContext) -> str:
    """
    Generate an email that leads with insight, not features.
    
    This version:
    - Opens with a counterintuitive insight
    - Uses specific numbers and timelines
    - Frames you as a peer advisor, not a vendor
    - Has a clear, low-friction CTA
    """
    
    # Extract key elements
    trigger = context.trigger_event
    outcome = context.outcome
    unspoken = context.unspoken_concern
    solution = context.solution_angle
    
    # TEMPLATE 1: The "Contrarian Insight" Opener
    email_contrarian = f"""Subject: The hidden risk in {trigger}

Hi [Name],

I saw {trigger}. Congrats - most firms underestimate how complex that actually is.

Here's what we've learned from helping [similar company type] through this: {unspoken} is the part that surprises everyone. Most people focus on {outcome}, but the real bottleneck is usually [specific process detail].

Quick example: One HK firm we worked with thought they needed better contract review. Turns out they needed better handoff protocols between associates and partners - which cut their M&A close time by 30%.

Worth a 15-minute call to see if you're facing something similar?

I'm free Tues/Wed this week at 10am HKT or 3pm HKT.

Best,
[Your name]

P.S. - If timing's off, I wrote a quick guide on "{unspoken}" that might be useful. Happy to send it your way.
"""

    # TEMPLATE 2: The "Peer Advisor" Approach
    email_peer = f"""Subject: Question about {trigger}

Hi [Name],

Quick question (not a pitch, promise):

When you're dealing with {trigger}, how are you handling {unspoken}?

The reason I ask: We work with [type of firm] going through similar situations, and that's the part that tends to create the most headaches. Most firms think {outcome} is the priority, but in practice, {unspoken} is what actually slows things down.

For example: [Specific company type] usually runs into issues around [specific pain point]. Does that resonate with your situation?

If it's useful, I can share what we've seen work (and what doesn't). 15 minutes, your call.

Free this week: Tues 10am or Wed 3pm HKT.

Best,
[Your name]
"""

    # TEMPLATE 3: The "Specific Timeline" Hook
    email_timeline = f"""Subject: 8 weeks until [their deadline]

Hi [Name],

I saw {trigger} - if you're following the typical timeline, that means {outcome} needs to happen by [specific date based on trigger event].

Here's the part that usually gets overlooked: {unspoken}.

We've worked with [similar firms], and this is where things tend to go sideways. Not because teams aren't capable, but because {specific bottleneck detail}.

One example: [Similar company] thought they had plenty of time for their HKEX filing, but the back-and-forth on disclosure controls ate up 3 weeks they didn't plan for.

Worth a quick conversation to see if you're set up differently?

I have 15 minutes open this week: Tuesday at 10am HKT or Wednesday at 3pm HKT.

Best,
[Your name]

P.S. - Even if this isn't the right time, I'd be happy to intro you to [relevant peer contact] who just went through this exact process.
"""

    return {
        "contrarian": email_contrarian,
        "peer_advisor": email_peer,
        "timeline_hook": email_timeline
    }
    
