# components/writing_checker.py
# Plain English Writing Checker - Zinsser's Principles Enforcement
from __future__ import annotations

import re
from typing import List, Tuple, Dict

# Zombie Nouns and Jargon Dictionary
ZOMBIE_WORDS: Dict[str, str] = {
    "utilization": "use",
    "utilize": "use",
    "implementation": "start using / set up",
    "facilitate": "help / make easier",
    "optimization": "improve",
    "optimize": "improve",
    "leverage": "use",
    "synergy": "teamwork",
    "functionality": "features",
    "operationalize": "do / make happen",
    "commence": "start",
    "endeavor": "try",
    "ascertain": "find out",
    "paradigm": "model / approach",
    "deliverable": "result / product",
    "ideate": "brainstorm / think",
    "incentivize": "encourage / reward",
    "actionable": "useful / clear",
    "bandwidth": "time / capacity",
    "circle back": "follow up / return to",
    "touch base": "talk / meet",
    "drill down": "examine / look closely",
    "move the needle": "make progress",
    "low-hanging fruit": "easy wins",
    "take offline": "discuss privately",
    "deep dive": "detailed analysis",
    "thought leader": "expert",
    "best practice": "proven method",
    "value-add": "benefit / advantage",
    "game-changer": "major improvement",
    "robust": "strong / reliable",
    "seamless": "smooth / easy",
    "cutting-edge": "new / advanced",
    "state-of-the-art": "newest / best available",
    "holistic": "complete / comprehensive",
    "strategic": "planned / important",
    "integrated": "combined / connected",
    "innovative": "new / creative",
    "scalable": "can grow / expandable",
}

# Passive Voice Patterns
PASSIVE_PATTERNS: List[str] = [
    r"\b(is|are|was|were|be|been|being)\s+\w+ed\b",
    r"\b(has|have|had)\s+been\s+\w+ed\b",
    r"\b(will|shall)\s+be\s+\w+ed\b",
]


def check_plain_english(text: str) -> Dict[str, List[Tuple[str, str]]]:
    """
    Analyze text for zombie nouns, jargon, and passive voice.
    
    Returns:
        Dict with keys:
        - 'zombie_words': List of (found_word, suggested_replacement)
        - 'passive_voice': List of (sentence_fragment, suggestion)
        - 'score': Overall writing quality score (0-100)
    """
    results = {
        "zombie_words": [],
        "passive_voice": [],
        "score": 100,
    }
    
    text_lower = text.lower()
    
    # Check for zombie words
    for zombie, replacement in ZOMBIE_WORDS.items():
        # Use word boundaries to avoid partial matches
        pattern = r'\b' + re.escape(zombie) + r'\b'
        if re.search(pattern, text_lower):
            results["zombie_words"].append((zombie, replacement))
            results["score"] -= 5  # Deduct points for each zombie word
    
    # Check for passive voice
    sentences = re.split(r'[.!?]+', text)
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        
        for pattern in PASSIVE_PATTERNS:
            matches = re.finditer(pattern, sentence, re.IGNORECASE)
            for match in matches:
                passive_phrase = match.group(0)
                results["passive_voice"].append((
                    sentence,
                    f"Passive voice detected: '{passive_phrase}'. Try active voice instead."
                ))
                results["score"] -= 3  # Deduct points for passive voice
    
    # Ensure score doesn't go below 0
    results["score"] = max(0, results["score"])
    
    return results


def get_writing_score_label(score: int) -> Tuple[str, str]:
    """
    Convert numeric score to a letter grade and emoji.
    
    Returns:
        Tuple of (grade, emoji)
    """
    if score >= 90:
        return "A - Excellent", "🟢"
    elif score >= 80:
        return "B - Good", "🟡"
    elif score >= 70:
        return "C - Fair", "🟠"
    else:
        return "D - Needs Work", "🔴"


def get_writing_tips() -> str:
    """
    Return a markdown-formatted guide on writing better outreach emails.
    """
    return """
### ✍️ How to Use These Insights in Your Outreach

**The Goal:** Turn research into human conversation, not corporate brochures.

---

#### 🎯 **Rule 1: Lead with THEIR World, Not Yours**

❌ **Bad:** "We offer AI-powered legal research solutions..."  
✅ **Good:** "I saw you just filed an IPO on HKEX. That usually means..."

**Why it works:** You prove you did homework before asking for their time.

---

#### 🗣️ **Rule 2: Use "I" and "You" Freely**

❌ **Bad:** "The platform facilitates optimization of legal workflows."  
✅ **Good:** "You'll cut research time from 4 hours to 30 minutes."

**Why it works:** Sounds like a conversation, not a press release.

---

#### ✂️ **Rule 3: Cut the Fluff**

Every word must earn its place. Test: If you remove a word, does the sentence still make sense? If yes, delete it.

❌ **Bad:** "We are currently in the process of implementing a comprehensive solution..."  
✅ **Good:** "We're setting up a solution..."  
✅ **Better:** "We're building..."

---

#### 🎯 **Rule 4: Focus on THEIR Specific Outcome**

Generic goals are boring. Specific outcomes create urgency.

❌ **Bad:** "Improve efficiency" (everyone says this)  
✅ **Good:** "Close M&A deals 30% faster by catching compliance gaps earlier"

**How to find this:** Look at the OUS analysis - what's their Outcome tied to their recent trigger event?

---

#### 💬 **Rule 5: Sound Like a Peer, Not a Vendor**

Lawyers are skeptical of sales pitches. Frame your message as advice, not advertising.

❌ **Bad:** "Our award-winning platform is the industry-leading..."  
✅ **Good:** "The GCs we work with describe this as 'insurance against what we might've missed.'"

**Tip:** Use phrases like:
- "In our experience with similar HK firms..."
- "The hidden risk we've seen is..."
- "Here's what worked for [similar company]..."

---

#### 📧 **Rule 6: Keep Emails Under 150 Words**

If your email is longer than 150 words, you've lost them. Get to the point.

**Structure:**
1. **Hook (2 sentences):** Reference their trigger event
2. **Pivot (2 sentences):** How you help with their specific pain
3. **Ask (1 sentence):** Specific call to action with exact time/date

---

#### 🚫 **Banned Phrases (Just Delete These)**

- "I hope this email finds you well"
- "Just following up"
- "I'd love to pick your brain"
- "Circling back"
- "Per my last email"
- "Let me know if you have any questions"

**Why:** They scream "generic sales email."

---

#### ✅ **Approved Openers**

- "I noticed [specific fact about their company]..."
- "I saw you recently [trigger event]..."
- "Quick question about [their specific challenge]..."

**Why:** Specific, relevant, and shows you did research.

---

#### 🧪 **The "Associate Test"**

Before you send, ask: *If a junior lawyer read this, would they forward it to their boss or delete it as spam?*

If it sounds like it could be sent to 100 other companies, rewrite it.

---

### 🔥 **Final Tip: Use the Fill-in-the-Blank Templates**

After you finish the OUS analysis, scroll down to see two pre-populated email templates based on your research. These are starting points - edit them to sound like YOU, not a robot.
"""
