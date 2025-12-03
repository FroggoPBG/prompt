"""Components package for Legal Tech Sales Prospecting Tool."""

from components.email_templates import EmailTemplate, EmailTemplateGenerator
from components.presets import ProspectPreset, export_preset_bytes, load_preset_into_state
from components.recipes import ProspectContext, PromptRecipeManager
from components.writing_checker import WritingAnalysis, WritingIssue, check_plain_english, get_writing_tips

__all__ = [
    # Email templates
    "EmailTemplate",
    "EmailTemplateGenerator",
    
    # Presets
    "ProspectPreset",
    "export_preset_bytes",
    "load_preset_into_state",
    
    # Recipes
    "ProspectContext",
    "PromptRecipeManager",
    
    # Writing checker
    "WritingAnalysis",
    "WritingIssue",
    "check_plain_english",
    "get_writing_tips",
]
