"""Prompt Recipe System for Legal Tech Sales Prospecting."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class ProspectContext:
    """Context information about a prospect for email generation."""
    trigger_event: str
    outcome: str
    unspoken_concern: str
    solution_angle: str


@dataclass
class PromptRecipe:
    """A reusable prompt template for different prospect types."""
    
    id: str
    display_name: str
    description: str
    trigger_prompt: str
    outcome_prompt: str
    unspoken_prompt: str
    solution_prompt: str
    example_inputs: Dict[str, str]
    
    def get_full_prompt(self) -> str:
        """Get the complete prompt as a formatted string."""
        return f"""# {self.display_name}

## Trigger Event
{self.trigger_prompt}

## Outcome
{self.outcome_prompt}

## Unspoken Concern
{self.unspoken_prompt}

## Solution Angle
{self.solution_prompt}

---

### Example Inputs:
**Trigger:** {self.example_inputs['trigger_event']}
**Outcome:** {self.example_inputs['outcome']}
**Unspoken:** {self.example_inputs['unspoken_concern']}
**Solution:** {self.example_inputs['solution_angle']}
"""


class PromptRecipeManager:
    """Manages all available prompt recipes."""
    
    def __init__(self):
        """Initialize the recipe manager with predefined recipes."""
        self.recipes: Dict[str, PromptRecipe] = {
            "ipo_hong_kong": PromptRecipe(
                id="ipo_hong_kong",
                display_name="🏢 IPO / Public Listing (Hong Kong)",
                description="For companies preparing for HKEX listing or recent IPO",
                trigger_prompt="What event signals they're going public? (e.g., filing S-1, hiring CFO, announcing listing plans)",
                outcome_prompt="What do they publicly say they want? (e.g., 'complete listing by Q2', 'raise $X million', 'expand shareholder base')",
                unspoken_prompt="What are they NOT saying but worrying about? (e.g., disclosure mistakes, regulatory delays, reputational risk)",
                solution_prompt="How does your solution address the unspoken concern? (Be specific about the outcome, not features)",
                example_inputs={
                    'trigger_event': 'Company filed draft prospectus with HKEX for Main Board listing',
                    'outcome': 'Successfully complete IPO by Q2 2026 and raise HK$500M',
                    'unspoken_concern': 'Worried about disclosure gaps that could delay approval or damage credibility with institutional investors',
                    'solution_angle': 'AI-powered disclosure review catches 94% of common HKEX comment triggers before filing, reducing average approval time from 6 months to 3.5 months'
                }
            ),
            
            "cross_border_ma": PromptRecipe(
                id="cross_border_ma",
                display_name="🌏 Cross-Border M&A",
                description="For firms handling international mergers & acquisitions",
                trigger_prompt="What M&A activity triggered this? (e.g., announced acquisition, hired M&A partner, press release)",
                outcome_prompt="What's their stated deal objective? (e.g., 'close by end of year', 'integrate operations', 'enter new market')",
                unspoken_prompt="What's the hidden risk they're managing? (e.g., regulatory approval delays, cultural integration, hidden liabilities)",
                solution_prompt="How do you de-risk their unspoken concern? (Focus on speed, accuracy, or risk mitigation)",
                example_inputs={
                    'trigger_event': 'Announced $200M acquisition of Singapore tech company',
                    'outcome': 'Close deal within 6 months and integrate tech team seamlessly',
                    'unspoken_concern': 'Worried about missing regulatory filings across 3 jurisdictions and IP ownership issues that could blow up post-close',
                    'solution_angle': 'Multi-jurisdiction compliance tracker ensures no regulatory deadlines are missed, and AI contract review flags IP ownership gaps in target company agreements'
                }
            ),
            
            "regulatory_expansion": PromptRecipe(
                id="regulatory_expansion",
                display_name="📜 Regulatory Compliance / Expansion",
                description="For companies entering new regulated markets",
                trigger_prompt="What expansion or regulatory change happened? (e.g., entering new country, new regulation announced, license application)",
                outcome_prompt="What's their expansion goal? (e.g., 'launch in HK by Q3', 'get license approval', 'achieve compliance')",
                unspoken_prompt="What's their compliance nightmare scenario? (e.g., fines, license rejection, reputational damage)",
                solution_prompt="How do you prevent their nightmare scenario? (Be specific about risk mitigation)",
                example_inputs={
                    'trigger_event': 'Announced expansion into Hong Kong fintech market, applied for SFC license',
                    'outcome': 'Obtain SFC license and launch product within 9 months',
                    'unspoken_concern': 'Terrified of license rejection due to incomplete compliance documentation or missing anti-money laundering controls',
                    'solution_angle': 'Automated compliance documentation system ensures all SFC requirements are met before submission, reducing rejection rate from 40% to 5%'
                }
            ),
            
            "litigation_defense": PromptRecipe(
                id="litigation_defense",
                display_name="⚖️ Litigation / Legal Defense",
                description="For companies facing lawsuits or legal disputes",
                trigger_prompt="What litigation event occurred? (e.g., lawsuit filed, regulatory investigation, class action announced)",
                outcome_prompt="What's their defense objective? (e.g., 'dismiss case', 'minimize damages', 'settle quickly')",
                unspoken_prompt="What's their real fear beyond the case itself? (e.g., discovery exposing other issues, media attention, shareholder lawsuits)",
                solution_prompt="How do you contain the broader risk? (Focus on secondary consequences, not just the case)",
                example_inputs={
                    'trigger_event': 'Class action lawsuit filed alleging securities fraud related to IPO disclosures',
                    'outcome': 'Defend against claims and minimize potential damages',
                    'unspoken_concern': 'Worried that discovery will expose internal communications showing executives knew about undisclosed risks',
                    'solution_angle': 'AI-powered document review identifies potentially problematic communications before discovery, allowing legal team to prepare defense strategy proactively'
                }
            ),
            
            "general_corporate": PromptRecipe(
                id="general_corporate",
                display_name="🏛️ General Corporate / GC Office",
                description="For general counsel managing overall legal operations",
                trigger_prompt="What operational change happened? (e.g., new GC hired, budget cut, team expansion, new initiative)",
                outcome_prompt="What's their operational goal? (e.g., 'reduce outside counsel spend', 'improve contract turnaround', 'scale legal team')",
                unspoken_prompt="What's the political/career risk they're managing? (e.g., board scrutiny, justifying headcount, proving ROI)",
                solution_prompt="How do you make them look good to the board/CEO? (Focus on metrics that matter to executives)",
                example_inputs={
                    'trigger_event': 'New General Counsel hired from Big Law, tasked with modernizing legal operations',
                    'outcome': 'Reduce outside counsel spend by 30% while maintaining quality',
                    'unspoken_concern': 'Worried about justifying legal tech spend to CFO while proving they can handle complexity internally',
                    'solution_angle': 'Dashboard shows real-time savings vs. outside counsel rates, with case studies proving 40% faster contract turnaround for board reporting'
                }
            ),
            
            "private_equity": PromptRecipe(
                id="private_equity",
                display_name="💼 Private Equity / Portfolio Company",
                description="For PE-backed companies or portfolio operations",
                trigger_prompt="What PE event happened? (e.g., new investment, portfolio company acquisition, exit prep, operational improvement mandate)",
                outcome_prompt="What's the PE firm's stated objective? (e.g., 'prepare for exit in 18 months', 'improve EBITDA', 'professionalize operations')",
                unspoken_prompt="What's the real pressure from the PE firm? (e.g., hit IRR targets, justify management fees, avoid write-downs)",
                solution_prompt="How do you help them hit PE metrics? (Focus on speed, cost reduction, or valuation improvement)",
                example_inputs={
                    'trigger_event': 'PE firm acquired majority stake, mandated operational improvements across legal and compliance',
                    'outcome': 'Reduce legal spend by 25% and prepare company for exit in 24 months',
                    'unspoken_concern': 'PE firm will replace management if they don't show measurable improvements in next 2 quarters',
                    'solution_angle': 'Automated contract management cuts legal costs 30% in 90 days, with metrics dashboard that PE firm can show LPs in quarterly reports'
                }
            ),
        }
    
    def get_recipe(self, recipe_id: str) -> PromptRecipe | None:
        """Get a recipe by ID."""
        return self.recipes.get(recipe_id)
    
    def get_all_recipe_ids(self) -> list[str]:
        """Get all available recipe IDs."""
        return list(self.recipes.keys())
    
    def get_all_recipes(self) -> Dict[str, PromptRecipe]:
        """Get all recipes."""
        return self.recipes
