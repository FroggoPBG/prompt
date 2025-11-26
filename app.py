# components/recipes.py
# Core language scaffolds, context, and prompt recipes.
from __future__ import annotations

from typing import Dict, List, Callable, Any

# -----------------------------
# Language scaffolds (email focus) - Enhanced with strategic prompt engineering
# -----------------------------

SCAFFOLDS: Dict[str, Dict[str, str]] = {
    "en": {
        "name": "English",
        "sys": (
            "You are a strategic communications assistant for LexisNexis account managers and customer success teams. "
            "Your role is to generate professional, data-driven client emails that demonstrate value, build relationships, "
            "and drive business outcomes. Each email should be:\n"
            "- Personalized using specific client data and usage metrics\n"
            "- Strategically aligned with the client's business stage and needs\n"
            "- Action-oriented with clear next steps\n"
            "- Evidence-based, citing concrete ROI or usage patterns where available\n\n"
            "Avoid: generic templates, legal advice, unsupported claims, or overly salesy language.\n"
            "Default to a consultative, partnership-focused tone unless otherwise specified."
        ),
        "role_lbl": "YOUR ROLE",
        "goal_lbl": "EMAIL OBJECTIVE",
        "ctx_lbl": "CLIENT CONTEXT",
        "usage_lbl": "USAGE DATA & METRICS",  # NEW: Separate section for data
        "req_lbl": "CONTENT REQUIREMENTS",
        "info_lbl": "KEY INFORMATION TO INCORPORATE",
        "tone_lbl": "TONE & VOICE",
        "len_lbl": "TARGET LENGTH",
        "extra_lbl": "CONSTRAINTS & GUIDELINES",
        "nps_pasted_lbl": "NPS VERBATIM FEEDBACK",
        "nps_internal_lbl": "INTERNAL NPS ANALYSIS",
        "success_lbl": "SUCCESS CRITERIA",  # NEW: What makes this email effective
    },
    "ja": {
        "name": "Japanese",
        "sys": (
            "あなたはLexisNexisのアカウントマネージャーとカスタマーサクセスチームのための戦略的コミュニケーションアシスタントです。"
            "あなたの役割は、価値を示し、関係を構築し、ビジネス成果を推進する、プロフェッショナルでデータに基づいたクライアントメールを生成することです。各メールは以下の要件を満たす必要があります：\n"
            "- 具体的なクライアントデータと使用状況指標を使用してパーソナライズする\n"
            "- クライアントのビジネス段階とニーズに戦略的に整合させる\n"
            "- 明確な次のステップを含むアクション志向\n"
            "- 具体的なROIまたは使用パターンを引用したエビデンスベース\n\n"
            "避けるべき事項：一般的なテンプレート、法的アドバイス、裏付けのない主張、過度に営業的な言葉遣い。\n"
            "特に指定がない限り、コンサルティング的でパートナーシップ重視のトーンをデフォルトとします。"
        ),
        "role_lbl": "あなたの役割",
        "goal_lbl": "メールの目的",
        "ctx_lbl": "クライアントコンテキスト",
        "usage_lbl": "使用状況データと指標",
        "req_lbl": "コンテンツ要件",
        "info_lbl": "組み込むべき重要情報",
        "tone_lbl": "トーンと声",
        "len_lbl": "目標の長さ",
        "extra_lbl": "制約とガイドライン",
        "nps_pasted_lbl": "NPS逐語的フィードバック",
        "nps_internal_lbl": "内部NPS分析",
        "success_lbl": "成功基準",
    },
    "zh": {
        "name": "Chinese (Simplified)",
        "sys": (
            "您是LexisNexis客户经理和客户成功团队的战略沟通助手。"
            "您的角色是生成专业的、数据驱动的客户电子邮件，以展示价值、建立关系并推动业务成果。每封电子邮件应该：\n"
            "- 使用具体的客户数据和使用指标进行个性化\n"
            "- 与客户的业务阶段和需求战略性对齐\n"
            "- 以行动为导向，包含明确的后续步骤\n"
            "- 基于证据，在可能的情况下引用具体的ROI或使用模式\n\n"
            "避免：通用模板、法律建议、无根据的声明或过于销售性的语言。\n"
            "除非另有说明，否则默认采用咨询性、注重伙伴关系的语气。"
        ),
        "role_lbl": "您的角色",
        "goal_lbl": "电子邮件目标",
        "ctx_lbl": "客户背景",
        "usage_lbl": "使用数据和指标",
        "req_lbl": "内容要求",
        "info_lbl": "要纳入的关键信息",
        "tone_lbl": "语气和声音",
        "len_lbl": "目标长度",
        "extra_lbl": "约束和指南",
        "nps_pasted_lbl": "NPS逐字反馈",
        "nps_internal_lbl": "内部NPS分析",
        "success_lbl": "成功标准",
    },
}

# -----------------------------
# Shared LexisNexis context - Enhanced with usage metrics structure
# -----------------------------

LN_CONTEXT: Dict[str, Any] = {
    "outputs": ["plain prompt", "email-only output"],
    "client_types": [
        "in-house legal",
        "law firm (small, <20 lawyers)",
        "law firm (mid-size, 20-100 lawyers)",
        "law firm (large, 100+ lawyers)",
        "government",
        "academic",
        "corporate (non-legal)",
        "other",
    ],
    "regions": [
        "Hong Kong",
        "Singapore",
        "Japan",
        "South Korea",
        "Australia / NZ",
        "Mainland China",
        "Other APAC",
        "Global",
    ],
    "practice_areas": [
        "Financial services",
        "Litigation / disputes",
        "Corporate / commercial / M&A",
        "Regulatory / compliance",
        "Intellectual property",
        "Employment / labor",
        "Tax",
        "Real estate",
        "Competition / antitrust",
        "Other",
    ],
    "products": [
        "Lexis+",
        "Lexis Advance",
        "Practical Guidance",
        "Lexis Draft / drafting tools",
        "News / Company information",
        "Analytics & research dashboards",
        "Training & certification programs",
    ],
    "stages": [
        "Prospect / discovery",
        "Trial / evaluation",
        "Onboarding (0-3 months)",
        "Early adoption (3-6 months)",
        "Steady state / mature user",
        "Renewal (within 90 days)",
        "Expansion / upsell opportunity",
        "At-risk / churn risk",
        "Renewal rescue (< 30 days to expiry)",
    ],
    "tones": [
        "auto (context-driven)",
        "warm & collaborative",
        "formal & professional",
        "consultative & strategic",
        "apologetic & recovery-focused",
        "direct & action-oriented",
        "celebratory & appreciative",
    ],
    "lengths": [
        "very short (2-3 sentences, <100 words)",
        "short (1 paragraph, 100-150 words)",
        "medium (2-3 paragraphs, 150-250 words)",
        "long (detailed, 250-400 words)",
    ],
    # NEW: Usage metric categories
    "usage_metrics": {
        "frequency": ["daily", "weekly", "sporadic (monthly or less)", "inactive (no logins in 30+ days)"],
        "engagement_level": ["high (multiple features)", "moderate (2-3 features)", "low (single feature)", "minimal"],
        "trend": ["growing", "stable", "declining", "volatile"],
    },
}

# -----------------------------
# Helper: base email prompt builder - Enhanced with structured data sections
# -----------------------------


def _base_email_prompt(scaffold: Dict[str, str], ctx: Dict[str, Any], body_instruction: str) -> str:
    s = scaffold
    
    # Core client information
    client_name = ctx.get("client_name") or "[Client Name]"
    client_type = ctx.get("client_type") or "n/a"
    region = ctx.get("region") or "n/a"
    practice = ", ".join(ctx.get("practice_areas") or []) or "n/a"
    products = ", ".join(ctx.get("products_used") or []) or "n/a"
    stage = ctx.get("relationship_stage") or "n/a"
    tone = ctx.get("tone") or "auto (context-driven)"
    length = ctx.get("length") or "medium (2-3 paragraphs, 150-250 words)"

    # Usage data (NEW: structured)
    usage_data = ctx.get("usage_data", {})
    doc_accesses = usage_data.get("doc_accesses", "n/a")
    searches = usage_data.get("searches", "n/a")
    alerts = usage_data.get("alerts", "n/a")
    login_frequency = usage_data.get("login_frequency", "n/a")
    engagement_trend = usage_data.get("engagement_trend", "n/a")
    time_period = usage_data.get("time_period", "n/a")
    top_modules = usage_data.get("top_modules", [])
    
    # Additional context
    ex_input = ctx.get("ex_input") or ""
    ex_output = ctx.get("ex_output") or ""
    nps_verbatim = ctx.get("nps_info") or ""
    internal_nps = ctx.get("nps_internal") or ""
    contract_date = ctx.get("contract_expiry") or "n/a"
    pricing_notes = ctx.get("pricing_notes") or ""

    lines: List[str] = []

    # System prompt
    lines.append("=== SYSTEM INSTRUCTIONS ===")
    lines.append(s["sys"])
    lines.append("")

    # User prompt structure
    lines.append("=== YOUR TASK ===")
    lines.append(f"**{s['role_lbl']}**: Account Manager / Customer Success professional at LexisNexis")
    lines.append(f"**{s['goal_lbl']}**: {ctx.get('goal_text', 'Client communication')}")
    lines.append("")

    # Client context section
    lines.append(f"**{s['ctx_lbl']}**:")
    lines.append(f"- Client name: {client_name}")
    lines.append(f"- Client type: {client_type}")
    lines.append(f"- Region: {region}")
    lines.append(f"- Practice area(s): {practice}")
    lines.append(f"- Products subscribed: {products}")
    lines.append(f"- Relationship stage: {stage}")
    if contract_date != "n/a":
        lines.append(f"- Contract expiry: {contract_date}")
    if pricing_notes:
        lines.append(f"- Pricing context: {pricing_notes}")
    lines.append("")

    # Usage data section (NEW: prominence for data-driven emails)
    if any(v != "n/a" for v in [doc_accesses, searches, alerts, login_frequency]):
        lines.append(f"**{s['usage_lbl']}**:")
        if time_period != "n/a":
            lines.append(f"- Analysis period: {time_period}")
        if doc_accesses != "n/a":
            lines.append(f"- Document accesses: {doc_accesses}")
        if searches != "n/a":
            lines.append(f"- Searches performed: {searches}")
        if alerts != "n/a":
            lines.append(f"- Active alerts: {alerts}")
        if login_frequency != "n/a":
            lines.append(f"- Login frequency: {login_frequency}")
        if engagement_trend != "n/a":
            lines.append(f"- Engagement trend: {engagement_trend}")
        if top_modules:
            lines.append(f"- Most used modules: {', '.join(top_modules)}")
        lines.append("")

    # Content requirements
    lines.append(f"**{s['req_lbl']}**:")
    lines.extend(body_instruction.strip().splitlines())
    lines.append("")

    # Information to incorporate
    lines.append(f"**{s['info_lbl']}**:")
    lines.append("✓ Use specific client name and context throughout")
    lines.append("✓ Reference usage metrics with concrete numbers where available")
    lines.append("✓ Connect usage patterns to business value (time saved, risk reduced, efficiency gained)")
    lines.append("✓ Acknowledge the relationship stage and adapt messaging accordingly")
    lines.append("✓ Include actionable next steps with clear owners and timelines")
    lines.append("✓ Cite specific features/modules where relevant to their practice area")
    lines.append("")

    # Tone and style
    lines.append(f"**{s['tone_lbl']}**: {tone}")
    lines.append(f"**{s['len_lbl']}**: {length}")
    lines.append("")

    # Constraints
    lines.append(f"**{s['extra_lbl']}**:")
    lines.append("✗ Do NOT provide legal advice or specific legal interpretations")
    lines.append("✗ Do NOT make claims about ROI without supporting data")
    lines.append("✗ Do NOT use generic template language ('I hope this email finds you well')")
    lines.append("✗ Do NOT be overly salesy - focus on partnership and value")
    lines.append("✓ DO respect client confidentiality and data privacy")
    lines.append("✓ DO suggest concrete, low-friction next steps")
    lines.append("✓ DO acknowledge concerns or challenges transparently when relevant")
    lines.append("")

    # NPS feedback (if available)
    if nps_verbatim:
        lines.append(f"**{s['nps_pasted_lbl']}**:")
        lines.append(f'"{nps_verbatim.strip()}"')
        lines.append("")
    
    if internal_nps or ctx.get("nps_internal_summary"):
        lines.append(f"**{s['nps_internal_lbl']}**:")
        lines.append((internal_nps or ctx.get("nps_internal_summary", "")).strip())
        lines.append("")

    # Few-shot examples (if provided)
    if ex_input or ex_output:
        lines.append("=== EXAMPLE REFERENCE ===")
        if ex_input:
            lines.append(f"Example scenario: {ex_input}")
        if ex_output:
            lines.append(f"Example output style: {ex_output}")
        lines.append("")

    # Success criteria (NEW: helps AI understand quality bar)
    if s.get("success_lbl"):
        lines.append(f"**{s['success_lbl']}**:")
        lines.append("This email succeeds if it:")
        lines.append("1. Feels personalized and specific to this client's situation")
        lines.append("2. Uses data to demonstrate value, not just make claims")
        lines.append("3. Has a clear, single call-to-action")
        lines.append("4. Strikes the appropriate tone for the relationship stage")
        lines.append("5. Could NOT be sent to another client without modification")
        lines.append("")

    lines.append("=== OUTPUT ===")
    lines.append("Now generate the email following all requirements above.")
    
    return "\n".join(lines)


# -----------------------------
# Individual recipes - Significantly enhanced with strategic framing
# -----------------------------

def _renewal_email(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    scenario = ctx.get("renewal_scenario", "value")
    
    # Enhanced: Different strategic approaches based on scenario
    if scenario == "low_usage_pricing":
        body = """
**Email Structure:**

1. **Opening (warm, non-judgmental)**
   - Thank them for their partnership
   - State upcoming renewal date clearly
   - Acknowledge you've been reviewing their account health

2. **Honest assessment (empathetic, consultative)**
   - Share the specific usage data you've observed (cite actual numbers)
   - Frame it as concern, not accusation: "I want to make sure you're getting value"
   - Acknowledge this suggests the current setup may not be optimal

3. **Root cause exploration (partnership mindset)**
   - Ask open-ended questions:
     * Is the content not matching your firm's needs?
     * Are there training or onboarding gaps we can address?
     * Have your firm's priorities shifted?
   - Position yourself as wanting to understand, not defend

4. **Solutions-oriented proposal**
   - Offer 2-3 concrete options:
     * Resize the package to better fit actual usage (lower cost)
     * Targeted training to improve adoption
     * Trial of different modules more aligned with their practice
   - Emphasize: "We'd rather you have a smaller subscription you love than a large one you don't use"

5. **Low-pressure next step**
   - Suggest a brief call (15-20 minutes) to discuss
   - Make it clear this is about finding the right fit, not pushing a renewal
   - Provide 2-3 specific time slots

**Tone requirements:**
- Empathetic but direct
- Consultative, not defensive
- Focus on partnership and problem-solving
- Acknowledge the pricing elephant in the room without being apologetic
"""
    
    elif scenario == "healthy_usage_price_sensitive":
        body = """
**Email Structure:**

1. **Value-first opening**
   - Thank them for their partnership
   - State renewal date
   - Lead with a usage insight that shows engagement

2. **Data-driven value demonstration**
   - Cite specific metrics: "{X} document accesses, {Y} searches, {Z} alerts set up over {period}"
   - Connect to their practice: "Your team's heavy use of [specific modules] suggests strong support for [practice area] work"
   - If possible, translate to time saved or efficiency gained

3. **Strategic insights (show you're paying attention)**
   - Highlight 1-2 underutilized features that could add value
   - Reference any NPS feedback or previous conversations about their needs
   - Connect usage patterns to their business goals

4. **Renewal discussion framing (collaborative)**
   - Acknowledge budget planning season and the need to justify spend
   - Position the call as: "Let's review what's working and ensure 2025-26 aligns with your priorities"
   - Offer flexibility: open to discussing package adjustments if needs have changed

5. **Clear, warm CTA**
   - Suggest specific meeting times
   - Frame as partnership check-in, not sales call
   - Reference their ongoing value to you as a client

**Tone requirements:**
- Warm and appreciative
- Confident in value but not pushy
- Acknowledge cost considerations without discounting
- Focus on ROI and partnership longevity
"""
    
    else:  # Standard renewal
        body = """
**Email Structure:**

1. **Appreciative opening**
   - Thank them for another successful year
   - State renewal timeline clearly

2. **Year-in-review highlights**
   - Share 2-3 compelling usage statistics
   - Connect usage to business outcomes where possible
   - Mention any particularly successful collaborations or support moments

3. **Forward-looking alignment**
   - Ask about their priorities for the coming year
   - Probe for any changing needs or new practice areas
   - Show interest in evolving with their firm

4. **Renewal process**
   - Explain next steps clearly
   - Offer options if relevant (package adjustments, add-ons)
   - Suggest a planning call

5. **Partnership tone close**
   - Reinforce relationship, not just transaction
   - Clear next step with specific timing

**Tone requirements:**
- Warm and relationship-focused
- Professional but not formal
- Forward-looking and collaborative
"""

    ctx = dict(ctx)
    ctx["goal_text"] = f"Renewal Email ({scenario.replace('_', ' ').title()})"
    
    main_prompt = _base_email_prompt(scaffold, ctx, body)
    
    # Enhanced: Scenario-specific quality criteria
    additional_guidance = f"""
=== SCENARIO-SPECIFIC QUALITY CRITERIA ===

For scenario type: {scenario}

**What makes THIS scenario different:**
"""
    
    if scenario == "low_usage_pricing":
        additional_guidance += """
- The client has already expressed price concerns, so being defensive about value will backfire
- Low usage data supports their concern - acknowledge this honestly
- Your goal is to salvage the relationship at a rightsized level, not force a full renewal
- Success = client feels heard and sees you as a partner solving their problem, not a vendor protecting revenue
- The email should make them MORE likely to engage, not feel trapped or pressured

**Red flags to avoid:**
✗ Defending the value of features they're not using
✗ Blaming them for low adoption
✗ Rushing to discount without understanding root cause
✗ Generic "let's do more training" without acknowledging pricing concern
"""
    
    elif scenario == "healthy_usage_price_sensitive":
        additional_guidance += """
- They're getting value (data proves it) but cost is still a concern
- Your advantage: strong usage gives you concrete ROI story to tell
- Don't be defensive about price, but don't preemptively discount either
- Frame the call as optimization, not justification
- Success = they see the renewal as an investment with measurable returns, not a grudge purchase

**Red flags to avoid:**
✗ Assuming usage data speaks for itself without interpretation
✗ Being tone-deaf to budget pressures
✗ Overselling features they're already using
✗ Making it feel like a sales pitch instead of a business review
"""
    
    else:
        additional_guidance += """
- Standard renewal with healthy relationship
- Balance appreciation with forward-looking planning
- Keep it professional but warm
- Success = smooth renewal process with opportunity to identify upsell/expansion

**Red flags to avoid:**
✗ Taking the renewal for granted
✗ Being too transactional
✗ Missing opportunity to deepen the relationship
"""
    
    return main_prompt + "\n\n" + additional_guidance


def _qbr_brief(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
**QBR Email Structure:**

1. **Executive summary (2-3 sentences)**
   - Review period covered
   - Overall health assessment (thriving/steady/needs attention)
   - Key achievement or concern

2. **Usage & engagement snapshot**
   - Core metrics with period-over-period comparison if available
   - Most-used products/features
   - User adoption across the organization

3. **Business outcomes & value delivered**
   - Time saved (if measurable)
   - Key matters or projects supported
   - ROI indicators or efficiency gains

4. **Opportunities & recommendations**
   - 2-3 underutilized features with potential impact
   - Training or configuration suggestions
   - Potential expansions aligned with their practice growth

5. **Action items & next steps**
   - Specific recommendations with owners
   - Timeline for follow-up
   - Meeting invitation for deeper discussion

**Format:**
- Use bullet points and clear sections for scannability
- Include specific numbers, not just directional trends
- Highlight wins prominently
- Frame opportunities positively, not as criticism
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "Quarterly Business Review Summary"
    return _base_email_prompt(scaffold, ctx, body)


def _client_followup(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
**Follow-up Email Structure:**

1. **Context reset (brief)**
   - Reference when you last met/spoke
   - Mention 1-2 key topics discussed

2. **Commitments delivered**
   - List actions you committed to
   - Provide status on each with links/attachments
   - Be specific about what you're delivering

3. **Client action items (gentle accountability)**
   - Remind them of anything they agreed to review/decide
   - Make it easy: provide specific questions or options
   - No pressure, but clear on what's needed to move forward

4. **Open loop closure**
   - Ask 1-2 targeted follow-up questions about the discussion
   - Show you were listening and thinking about their situation

5. **Clear next step**
   - Specific CTA (meeting, decision, feedback)
   - Suggest timing
   - Make it easy to respond

**Tone:**
- Professional but personable
- Efficient (respect their time)
- Helpful, not pushy
- Shows you're organized and on top of things
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "Post-Meeting Follow-up"
    return _base_email_prompt(scaffold, ctx, body)


def _proposal_rfp(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
**RFP Response Email Structure:**

1. **Acknowledgment & appreciation**
   - Thank them for the opportunity
   - Confirm receipt and timeline

2. **Understanding demonstration**
   - Restate their 3-4 key requirements in your own words
   - Shows you read and understood the RFP
   - Sets up your response framework

3. **Capability mapping (high-level)**
   - Map LexisNexis strengths to each major requirement
   - Highlight 2-3 key differentiators relevant to their needs
   - Regional/practice-specific fit where applicable

4. **Process & next steps**
   - Clarify any RFP questions or timeline
   - Propose optional value-add (workshop, Q&A session, reference call)
   - Commit to formal response timeline

5. **Relationship emphasis**
   - Express genuine interest in the opportunity
   - Reference any existing relationship or knowledge of their firm
   - Confidence but not arrogance in closing

**Tone:**
- Professional and responsive
- Confident in capabilities
- Detail-oriented (shows you read the RFP carefully)
- Collaborative, not just competitive
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "RFP Response / Proposal Introduction"
    return _base_email_prompt(scaffold, ctx, body)


def _upsell_cross_sell(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
**Upsell/Cross-sell Email Structure:**

1. **Current value anchor**
   - Start with what's working well in current usage
   - Use specific data: "Your team has accessed X documents in [module] over Y months"
   - Build from success, not create new need

2. **Natural extension (the "and" story)**
   - Introduce additional product/module as logical next step
   - Connect to observable patterns: "Given your heavy use of X, teams typically benefit from Y"
   - Link to their practice area or stated goals

3. **Specific use cases (not generic benefits)**
   - Provide 2-3 concrete scenarios where this would help THEIR work
   - If possible, reference similar clients in their practice area/region
   - Make it feel like insider knowledge, not sales pitch

4. **Low-friction exploration**
   - Offer demo, trial, or pilot
   - Suggest short timeframe (30-day trial, 20-min demo)
   - Make it easy to say yes to learning more

5. **No-pressure close**
   - Frame as "wanted to flag this for you"
   - Give them space to think
   - Clear but not pushy next step

**Tone:**
- Consultative and helpful
- Confident but not aggressive
- Focus on expanding value, not just revenue
- Make them feel like you're looking out for them
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "Upsell / Cross-sell Opportunity"
    return _base_email_prompt(scaffold, ctx, body)


def _client_risk_alert(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
**Client Risk Email Structure:**

1. **Direct but caring opening**
   - Acknowledge the concerning signal (declining usage, negative feedback, etc.)
   - No defensiveness or excuse-making
   - "I've noticed X and want to understand what's happening"

2. **Specific observation**
   - Share the exact data/feedback that triggered concern
   - Be factual, not accusatory
   - Show you're paying attention to their account

3. **Genuine inquiry (not assumptions)**
   - Ask open-ended questions about root cause
   - Possibilities: training gap, content fit, team changes, priorities shifted
   - Make it safe for them to be honest

4. **Concrete action plan**
   - Offer 2-3 specific interventions based on likely scenarios
   - Assign ownership (what you'll do, what you need from them)
   - Timeline for check-ins

5. **Partnership reaffirmation**
   - Express commitment to making this work
   - Acknowledge challenges without minimizing
   - Clear, easy next step (usually a call)

**Tone:**
- Calm and professional
- Non-defensive but proactive
- Empathetic but solution-focused
- Shows you care about the relationship, not just the revenue
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "Client Risk Intervention"
    return _base_email_prompt(scaffold, ctx, body)


def _client_snapshot(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    body = """
**Client Snapshot Email Structure:**

(This is primarily internal-facing but client-ready)

1. **Client profile header**
   - Name, type, region, key contacts
   - Products subscribed & contract dates
   - Practice areas served

2. **Health metrics**
   - Usage trends (growing/stable/declining)
   - Engagement indicators
   - NPS score if available

3. **Key opportunities**
   - Upsell/cross-sell potential
   - Underutilized features
   - Expansion possibilities

4. **Risk signals**
   - Declining usage
   - Upcoming renewal concerns
   - Competitive threats
   - Organizational changes

5. **Recommended actions**
   - Priority ranking (high/medium/low)
   - Owner assignments
   - Timeline

**Format:**
- Scannable (bullets, headers, metrics)
- Factual and objective
- Actionable (not just FYI)
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "Client Health Snapshot"
    return _base_email_prompt(scaffold, ctx, body)


def _objection_coach(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    objection_type = ctx.get("objection_type", "pricing")
    
    body = f"""
**Objection Response Email for: {objection_type}**

1. **Acknowledge sincerely**
   - Validate their concern without dismissing
   - "I understand that {objection_type} is an important consideration"
   - Avoid being defensive

2. **Clarify understanding**
   - Ask a clarifying question to ensure you understand the real issue
   - Sometimes the stated objection masks a deeper concern

3. **Tailored response (2-3 points)**
   - Address the specific objection with evidence where possible
   - For pricing: ROI data, comparison to alternatives, flexible options
   - For usability: training resources, success stories, support options
   - For competitors: differentiation without badmouthing
   - Use their context (practice area, firm size, region)

4. **Evidence & social proof**
   - Case study or testimonial from similar client if available
   - Specific features/data that counter the objection
   - Third-party validation where applicable

5. **Low-barrier next step**
   - Offer to demonstrate the solution (not just talk about it)
   - Suggest trial, pilot, or focused demo
   - Make it easy to verify your claims themselves

**Tone:**
- Respectful and non-defensive
- Confident but not dismissive
- Problem-solving focused
- Shows you understand their perspective
"""
    ctx = dict(ctx)
    ctx["goal_text"] = f"Objection Response: {objection_type.title()}"
    return _base_email_prompt(scaffold, ctx, body)


def _nps_engagement(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    prior = ctx.get("nps_previous_rating", "Unknown")
    
    body = f"""
**NPS Survey Invitation Email**

**Tone adaptation based on prior rating: {prior}**

1. **Opening (rating-specific)**
   - **Promoters (9-10)**: Warm, appreciative, partnership-focused
     * "Your feedback has been invaluable in shaping how we support you..."
   - **Passives (7-8)**: Humble, improvement-oriented
     * "We're always looking to improve our service to you..."
   - **Detractors (0-6)**: Sincere, non-defensive, respectful
     * "We know we haven't always met your expectations, and your honest feedback helps us do better..."
   - **Unknown**: Neutral but appreciative

2. **Why this matters NOW**
   - Specific reason for this NPS timing (quarterly review, post-renewal, product launch)
   - How their input will be used concretely
   - Make it feel important, not routine

3. **The ask (clear and simple)**
   - NPS survey link prominently placed
   - Estimated time to complete
   - Emphasis on candid feedback

4. **What happens next**
   - Commit to reading every response
   - Explain follow-up process (especially for concerns)
   - Timeline for acting on feedback

5. **Gratitude**
   - Thank them for their time
   - Acknowledge that feedback is a gift

**Tone guidelines by rating:**
- Promoters: Collaborative, partnership-focused, invite co-creation
- Passives: Improvement-focused, asking what would make it "great"
- Detractors: Respectful, non-defensive, genuinely want to improve
- Unknown: Professional, appreciative, open

**Length: SHORT** - NPS asks should be quick and clear
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "NPS Survey Invitation"
    return _base_email_prompt(scaffold, ctx, body)


def _nps_follow_up(scaffold: Dict[str, str], ctx: Dict[str, Any]) -> str:
    rating = ctx.get("nps_previous_rating", "Promoter (9–10)")
    comment_type = ctx.get("nps_comment_type", "General feedback")
    verbatim = ctx.get("nps_followup_comment", "")

    body = f"""
**NPS Follow-up Email**

**Context:**
- Previous rating: {rating}
- Comment category: {comment_type}
- Verbatim: "{verbatim[:200]}{'...' if len(verbatim) > 200 else ''}"

**Structure (rating-adapted):**

1. **Personalized thank you**
   - Reference their specific comment (quote a distinctive phrase)
   - Shows you actually read it, not automated

2. **Rating-specific response:**
   
   **For Promoters (9-10):**
   - Express genuine appreciation
   - If they mentioned specific feature: share related tip or upcoming enhancement
   - Invite them to be reference, beta tester, or advisor
   - Keep it brief and appreciative
   
   **For Passives (7-8):**
   - Thank them for honest feedback
   - Ask 1-2 focused questions to understand what would make it a 9-10
   - If they mentioned an issue: explain what you're doing about it
   - Invite short call to explore improvement ideas
   
   **For Detractors (0-6):**
   - Apologize sincerely for falling short (be specific to their concern)
   - Explain action taken or escalation to appropriate team
   - If technical: provide timeline for resolution
   - If service-related: explain process changes
   - Invite call to discuss (make it genuinely optional)
   - Do NOT be defensive or make excuses

3. **Specific response to their comment type:**
   - Feature request: roadmap context, workarounds, timeline if available
   - Usability complaint: training resources, support contact, configuration help
   - Pricing concern: ROI discussion, package alternatives (carefully)
   - Positive feedback: amplify, ask permission to share, thank them

4. **Helpful resource or next step**
   - Link to relevant help article, video, or resource
   - Specific action item if applicable
   - Contact for follow-up (make it easy)

5. **Open door close**
   - Invite ongoing dialogue
   - Provide direct contact info
   - Thank them again

**Tone requirements:**
- Personalized (could ONLY be sent to this person based on their comment)
- Responsive and action-oriented
- Appropriate to rating (appreciative/curious/apologetic)
- Human and authentic, not corporate template

**Length: SHORT to MEDIUM** - Respect their time, they already gave feedback
"""
    ctx = dict(ctx)
    ctx["goal_text"] = "NPS Follow-up"
    return _base_email_prompt(scaffold, ctx, body)


# -----------------------------
# Recipe registry + dispatcher
# -----------------------------

PROMPT_RECIPES: Dict[str, Callable[[Dict[str, str], Dict[str, Any]], str]] = {
    "Renewal Email": _renewal_email,
    "QBR Brief": _qbr_brief,
    "Client Follow-up": _client_followup,
    "Proposal / RFP Response": _proposal_rfp,
    "Upsell / Cross-sell Outreach": _upsell_cross_sell,
    "Client Risk Alert": _client_risk_alert,
    "Client Snapshot & Risk Signals": _client_snapshot,
    "Objection Coach": _objection_coach,
    "NPS Engagement": _nps_engagement,
    "NPS Follow-up": _nps_follow_up,
}


def fill_recipe(recipe_name: str, lang_code: str, ctx: Dict[str, Any]) -> str:
    """
    Generate a complete prompt for the specified recipe and language.
    """
    scaffold = SCAFFOLDS.get(lang_code, SCAFFOLDS["en"])
    recipe_fn = PROMPT_RECIPES.get(recipe_name)
    if not recipe_fn:
        raise ValueError(f"Unknown recipe: {recipe_name}. Available: {list(PROMPT_RECIPES.keys())}")
    return recipe_fn(scaffold, ctx)


def shape_output(
    prompt_text: str,
    output_target: str,
    client_name: str,
    recipe_name: str,
) -> str:
    """
    Shape the final output based on target format.
    """
    if output_target == "email-only output":
        return (
            prompt_text
            + "\n\n=== OUTPUT FORMAT ===\n"
            + "Generate ONLY the email body ready to send. Do not include:\n"
            + "- The prompt instructions\n"
            + "- Meta-commentary about the email\n"
            + "- Subject line (unless specifically requested)\n"
            + "- Signature block (unless specifically requested)\n\n"
            + "Start directly with the email greeting and content."
        )
    return prompt_text
