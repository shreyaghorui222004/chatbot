import streamlit as st
from main import get_response

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("AI Chatbot")


# def is_medical_query(text):
#     text = text.lower()
#
#     medical_keywords = [
#         "fever", "headache", "pain", "dizzy",
#         "cold", "cough", "weak", "weakness",
#         "nausea", "vomit", "vomiting",
#         "sore", "throat", "fatigue",
#         "temperature", "chills"
#     ]
#
#     for keyword in medical_keywords:
#         if keyword in text:
#             return True
#
#     return False
#
#
# def get_fixed_response(text):
#     text = text.lower()
#
#     if "cold" in text or "cough" in text:
#         return "Paracetamol or a cough syrup can help relieve symptoms."
#
#     if "fever" in text:
#         return "Paracetamol or ibuprofen can help reduce fever."
#
#     if "headache" in text:
#         return "Paracetamol can help relieve headache."
#
#     if "weak" in text or "weakness" in text:
#         return "Rest and stay hydrated; eat light nutritious food."
#
#     return None



if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, I am a medical assistant. How can I help you?"}
    ]


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


# Input
user_input = st.chat_input("Type your message...")


if user_input:
    
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    

    # if not is_medical_query(user_text):
    #     reply = "Please ask medical questions only."
    #
    # else:
    #
    #     fixed = get_fixed_response(user_text)
    #
    #     if fixed:
    #         reply = fixed
    #     else:
    #         #
    #         response = get_response(st.session_state.messages)
    #         reply = response.strip().split(".")[0] + "."

   
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })


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


st.sidebar.title(" Settings")

if st.sidebar.button(" Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, I am a medical assistant. How can I help you?"}
    ]
    st.rerun()


