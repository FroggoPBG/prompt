from dataclasses import dataclass
from typing import Dict

@dataclass
class ProspectContext:
    trigger_event: str
    outcome: str
    unspoken_concern: str
    solution_angle: str

@dataclass
class PromptRecipe:
    id: str
    display_name: str
    description: str
    trigger_prompt: str
    outcome_prompt: str
    unspoken_prompt: str
    solution_prompt: str
    example_inputs: Dict[str, str]
    
    def get_full_prompt(self):
        return f"""# {self.display_name}

## Trigger Event
{self.trigger_prompt}

## Outcome
{self.outcome_prompt}

## Unspoken Concern
{self.unspoken_prompt}

## Solution Angle
{self.solution_prompt}
"""

class PromptRecipeManager:
    def __init__(self):
        self.recipes = {
            "ipo_hong_kong": PromptRecipe(
                id="ipo_hong_kong",
                display_name="IPO / Public Listing (Hong Kong)",
                description="For companies preparing for HKEX listing or recent IPO",
                trigger_prompt="What event signals they are going public?",
                outcome_prompt="What do they publicly say they want?",
                unspoken_prompt="What are they NOT saying but worrying about?",
                solution_prompt="How does your solution address the unspoken concern?",
                example_inputs={
                    'trigger_event': 'Company filed draft prospectus with HKEX for Main Board listing',
                    'outcome': 'Successfully complete IPO by Q2 2026 and raise HK$500M',
                    'unspoken_concern': 'Worried about disclosure gaps that could delay approval',
                    'solution_angle': 'AI-powered disclosure review catches 94% of common HKEX comment triggers'
                }
            ),
            "cross_border_ma": PromptRecipe(
                id="cross_border_ma",
                display_name="Cross-Border M&A",
                description="For firms handling international mergers & acquisitions",
                trigger_prompt="What M&A activity triggered this?",
                outcome_prompt="What is their stated deal objective?",
                unspoken_prompt="What is the hidden risk they are managing?",
                solution_prompt="How do you de-risk their unspoken concern?",
                example_inputs={
                    'trigger_event': 'Announced $200M acquisition of Singapore tech company',
                    'outcome': 'Close deal within 6 months',
                    'unspoken_concern': 'Worried about missing regulatory filings across 3 jurisdictions',
                    'solution_angle': 'Multi-jurisdiction compliance tracker ensures no deadlines are missed'
                }
            ),
            "regulatory_expansion": PromptRecipe(
                id="regulatory_expansion",
                display_name="Regulatory Compliance / Expansion",
                description="For companies entering new regulated markets",
                trigger_prompt="What expansion or regulatory change happened?",
                outcome_prompt="What is their expansion goal?",
                unspoken_prompt="What is their compliance nightmare scenario?",
                solution_prompt="How do you prevent their nightmare scenario?",
                example_inputs={
                    'trigger_event': 'Announced expansion into Hong Kong fintech market',
                    'outcome': 'Obtain SFC license and launch product within 9 months',
                    'unspoken_concern': 'Terrified of license rejection due to incomplete compliance',
                    'solution_angle': 'Automated compliance documentation ensures all SFC requirements are met'
                }
            ),
            "litigation_defense": PromptRecipe(
                id="litigation_defense",
                display_name="Litigation / Legal Defense",
                description="For companies facing lawsuits or legal disputes",
                trigger_prompt="What litigation event occurred?",
                outcome_prompt="What is their defense objective?",
                unspoken_prompt="What is their real fear beyond the case itself?",
                solution_prompt="How do you contain the broader risk?",
                example_inputs={
                    'trigger_event': 'Class action lawsuit filed alleging securities fraud',
                    'outcome': 'Defend against claims and minimize potential damages',
                    'unspoken_concern': 'Worried that discovery will expose internal communications',
                    'solution_angle': 'AI-powered document review identifies problematic communications before discovery'
                }
            ),
            "general_corporate": PromptRecipe(
                id="general_corporate",
                display_name="General Corporate / GC Office",
                description="For general counsel managing overall legal operations",
                trigger_prompt="What operational change happened?",
                outcome_prompt="What is their operational goal?",
                unspoken_prompt="What is the political or career risk they are managing?",
                solution_prompt="How do you make them look good to the board or CEO?",
                example_inputs={
                    'trigger_event': 'New General Counsel hired from Big Law',
                    'outcome': 'Reduce outside counsel spend by 30 percent',
                    'unspoken_concern': 'Worried about justifying legal tech spend to CFO',
                    'solution_angle': 'Dashboard shows real-time savings vs outside counsel rates'
                }
            ),
            "private_equity": PromptRecipe(
                id="private_equity",
                display_name="Private Equity / Portfolio Company",
                description="For PE-backed companies or portfolio operations",
                trigger_prompt="What PE event happened?",
                outcome_prompt="What is the PE firm stated objective?",
                unspoken_prompt="What is the real pressure from the PE firm?",
                solution_prompt="How do you help them hit PE metrics?",
                example_inputs={
                    'trigger_event': 'PE firm acquired majority stake',
                    'outcome': 'Reduce legal spend by 25 percent and prepare for exit in 24 months',
                    'unspoken_concern': 'PE firm will replace management if no improvements in 2 quarters',
                    'solution_angle': 'Automated contract management cuts legal costs 30 percent in 90 days'
                }
            ),
        }
    
    def get_recipe(self, recipe_id):
        return self.recipes.get(recipe_id)
