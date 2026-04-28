import streamlit as st
from main import get_response

st.set_page_config(page_title="Groq Chatbot", layout="centered")

st.title("Groq AI Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a medical assistant chatbot."},
        {"role": "assistant", "content": "Hello, I am a medical assistant. How can I help you?"}
    ]

# CSS for left-right chat
st.markdown("""
<style>
.chat-row {
    display: flex;
    width: 100%;
}

.user-row {
    justify-content: flex-end;
}

.bot-row {
    justify-content: flex-start;
}

.user-msg {
    background-color: #2563eb;
    color: white;
    padding: 10px 15px;
    border-radius: 15px;
    margin: 5px;
    max-width: 60%;
}

.bot-msg {
    background-color: #374151;
    color: white;
    padding: 10px 15px;
    border-radius: 15px;
    margin: 5px;
    max-width: 60%;
}
</style>
""", unsafe_allow_html=True)


user_input = st.chat_input("Type your message...")

if user_input:
    
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    
    reply = get_response(st.session_state.messages)

    
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })


for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div class="chat-row user-row">
                <div class="user-msg">{msg["content"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif msg["role"] == "assistant":
        st.markdown(
            f"""
            <div class="chat-row bot-row">
                <div class="bot-msg">{msg["content"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.sidebar.title(" Settings")

if st.sidebar.button(" Clear Chat"):
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]
    st.rerun()