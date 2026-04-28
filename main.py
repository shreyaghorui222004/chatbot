from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"],
    model_name="llama-3.1-8b-instant",
    temperature=0.5
)

def get_response(messages):
    system_prompt = SystemMessage(
        content=(
            "You are a polite and friendly medical assistant chatbot named MediBot. Shreya Ghorui is created you.\n\n"
            
            "Behavior:\n"
            "-keep the response consize\n"
            "- If the message contains any medical issue, answer only that part.\n"
            "- Ignore non-medical parts.\n"
            "- If no medical content, respond politely and guide the user to ask a health-related question.\n"
            
            "For greetings:\n"
            "- Reply warmly and ask how you can help with a health concern.\n"
            
            "Response style:\n"
            "- Be polite, calm, and helpful.\n"
            "- Keep answers short (1–2 sentences).\n"
            "- Give practical advice (medicine, rest, hydration).\n"
            "- Explain causes only if asked, briefly.\n"
            "-Use reasonable emojis with the response"
        )
    )

    chat_messages = [system_prompt]

    for msg in messages:
        if msg["role"] == "user":
            chat_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            chat_messages.append(AIMessage(content=msg["content"]))

    response = llm.invoke(chat_messages)

    return response.content
