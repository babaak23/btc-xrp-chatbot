import streamlit as st
import openai

# Set OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set the expert system prompt
SYSTEM_PROMPT = (
    "You are a top-level cryptocurrency expert specializing in Bitcoin and XRP. "
    "You provide in-depth insights into both macroeconomic trends (such as regulations, adoption, market movements, institutional interest) "
    "and micro-level details (like blockchain protocols, consensus mechanisms, use cases, transaction speeds, tokenomics). "
    "You also understand how Bitcoin and XRP compare, contrast, and potentially complement each other in the evolving financial system. "
    "Explain complex topics clearly and thoroughly. Keep your answers factual and grounded in reliable data. Avoid hype."
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# Streamlit app UI
st.set_page_config(page_title="Bitcoin + XRP Chatbot", page_icon="🪙")
st.title("🪙 Bitcoin + XRP AI Expert")
st.caption("Ask anything about Bitcoin, XRP, or how they intertwine — macro to micro.")

# Chat input
user_input = st.chat_input("Type your question here...")

# If there's a user question, add to chat history and get AI response
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=st.session_state.messages
        )

    reply = response.choices[0].message["content"]
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Display chat history
for msg in st.session_state.messages[1:]:  # Skip system prompt
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
