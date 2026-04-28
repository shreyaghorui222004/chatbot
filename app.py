import streamlit as st
from main import get_response

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 AI Chatbot")


# ✅ Medical detection
def is_medical_query(text):
    text = text.lower()

    medical_keywords = [
        "fever", "headache", "pain", "dizzy",
        "cold", "cough", "weak", "weakness",
        "nausea", "vomit", "vomiting",
        "sore throat", "body pain", "fatigue",
        "temperature", "chills"
    ]

    return any(word in text for word in medical_keywords)


# ✅ Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, I am a medical assistant. How can I help you?"}
    ]


# ✅ UI Styling
st.markdown("""
<style>
.chat-row { display: flex; width: 100%; }
.user-row { justify-content: flex-end; }
.bot-row { justify-content: flex-start; }

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


# ✅ Input
user_input = st.chat_input("Type your message...")


if user_input:
    # store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # ✅ STRICT FILTER LOGIC
    if not is_medical_query(user_input):
        reply = "Please ask medical questions only."
    else:
        response = get_response(st.session_state.messages)
        reply = response.strip()

    # store bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })


# ✅ Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="chat-row user-row">
            <div class="user-msg">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-row bot-row">
            <div class="bot-msg">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)


# ✅ Sidebar
st.sidebar.title("⚙️ Settings")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, I am a medical assistant. How can I help you?"}
    ]
    st.rerun()