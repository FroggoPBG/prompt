import streamlit as st
import time

# 1. Set up the page configuration
st.set_page_config(page_title="Local Bot", page_icon="💬")

st.title("💬 Simple Local Chatbot")
st.caption("This bot runs locally without any API keys.")

# 2. Initialize chat history in session state
# This keeps the messages on the screen when the app reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display existing chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle user input
if prompt := st.chat_input("Type something here..."):
    
    # A. Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # B. Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # C. Generate a response
    # Since we are NOT using an API, we define simple logic here.
    # You can change this logic to whatever you want.
    response_text = f"I am a local bot. You just said: '{prompt}'"

    # D. Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulate a "typing" effect
        for char in response_text:
            full_response += char
            time.sleep(0.02) # Adjust speed of typing
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # E. Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
