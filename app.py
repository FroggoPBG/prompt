import streamlit as st

# -----------------------------------------------------------------------------
# 1. THE PROMPT LIBRARY
# This dictionary stores your scenarios. 
# You can easily add more scenarios by following the pattern below.
# -----------------------------------------------------------------------------
PROMPT_LIBRARY = {
    "Professional Email": {
        "description": "Generate a polished email for work contexts.",
        "icon": "📧",
        "inputs": {
            "recipient": "Who is this email for? (e.g., My Boss, Client)",
            "topic": "What is the email about?",
            "tone": "What is the desired tone? (e.g., Formal, Persuasive, Apologetic)",
            "action": "What action do you want them to take?"
        },
        # The {names} inside the curly braces must match the keys in 'inputs' above
        "template": """
Act as a professional communication expert.
Draft an email to {recipient} regarding {topic}.
The tone should be {tone}.
The main goal of this email is to get the recipient to {action}.
Ensure the email is concise and professional.
"""
    },
    
    "Code Generator": {
        "description": "Create a prompt to generate specific code snippets.",
        "icon": "💻",
        "inputs": {
            "language": "Programming Language (e.g., Python, JavaScript)",
            "task": "What should the code do?",
            "constraints": "Any specific libraries or constraints? (e.g., no external APIs, use pandas)"
        },
        "template": """
You are an expert senior software engineer.
Write a script in {language} that performs the following task:
{task}

Please adhere to these constraints:
{constraints}

Include comments explaining the logic and ensure the code is error-free.
"""
    },

    "Blog Post Outline": {
        "description": "Generate a structured outline for a content piece.",
        "icon": "📝",
        "inputs": {
            "topic": "Blog Topic",
            "audience": "Target Audience",
            "keywords": "SEO Keywords (comma separated)"
        },
        "template": """
Act as a content marketing strategist.
Create a detailed blog post outline about "{topic}" targeting {audience}.
Ensure the following keywords are integrated naturally into the section headers: {keywords}.

The outline should include:
1. Catchy Title options
2. Introduction hook
3. Main body headers (H2 and H3)
4. Conclusion
"""
    },
    
    "Summarizer": {
        "description": "Create a prompt to summarize complex text.",
        "icon": "📚",
        "inputs": {
            "context": "What type of text is this? (e.g., Legal Contract, Scientific Paper)",
            "format": "Output format (e.g., Bullet points, 3 sentences, ELI5)"
        },
        "template": """
I am going to provide you with a {context}.
Please summarize the text provided below.
The output format should be: {format}.

[Paste Text Here]
"""
    }
}

# -----------------------------------------------------------------------------
# 2. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Prompt Library", page_icon="📂", layout="wide")

st.title("📂 Local Prompt Library")
st.markdown("Select a scenario, fill in the details, and generate a ready-to-use prompt.")
st.divider()

# -----------------------------------------------------------------------------
# 3. SIDEBAR SELECTION
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("1. Pick a Scenario")
    
    # Get list of scenarios from our dictionary keys
    scenario_names = list(PROMPT_LIBRARY.keys())
    selected_scenario = st.selectbox("Choose a template:", scenario_names)
    
    # Get the data for the selected scenario
    current_data = PROMPT_LIBRARY[selected_scenario]
    
    st.info(f"**Description:** {current_data['description']}")

# -----------------------------------------------------------------------------
# 4. MAIN INPUT FORM
# -----------------------------------------------------------------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader(f"{current_data['icon']} {selected_scenario} Details")
    
    # We use a form so the page doesn't reload on every keystroke
    with st.form("prompt_input_form"):
        user_inputs = {}
        
        # Dynamically generate text boxes based on the 'inputs' dictionary
        for key, label in current_data["inputs"].items():
            user_inputs[key] = st.text_input(label)
            
        submitted = st.form_submit_button("Generate Prompt")

# -----------------------------------------------------------------------------
# 5. OUTPUT GENERATION
# -----------------------------------------------------------------------------
with col2:
    st.subheader("🚀 Generated Prompt")
    
    if submitted:
        # Check if all fields are filled (optional validation)
        if all(user_inputs.values()):
            try:
                # Fill in the template slots with user inputs
                final_prompt = current_data["template"].format(**user_inputs)
                
                st.success("Prompt generated! Copy it below.")
                st.text_area("Copy this:", value=final_prompt, height=400)
                
            except KeyError as e:
                st.error(f"Error in template configuration: Missing key {e}")
        else:
            st.warning("Please fill in all fields to generate the prompt.")
    else:
        st.info("Fill out the form on the left and hit 'Generate' to see the result here.")
