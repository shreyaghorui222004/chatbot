from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

def get_response(messages):
    system_prompt = SystemMessage(
    content=(
        "You are a medical assistant chatbot.\n"
        "If the user's message contains ANY medical symptom, answer ONLY that part.\n"
        "Ignore all non-medical parts completely.\n"
        "If there is NO medical content, reply: 'Please ask medical questions only.'\n"
        "Give ONLY ONE short, direct answer (max 10-12 words).\n"
        "Prefer medicine or actionable advice over explanations.\n"
        "Do NOT explain causes or background.\n"
        "Do NOT give multiple options or long sentences.\n"
    )
)

    chat_messages = [system_prompt]

    for msg in messages:
        if msg["role"] == "user":
            chat_messages.append(HumanMessage(content=msg["content"]))

    response = llm.invoke(chat_messages)

    return response.content