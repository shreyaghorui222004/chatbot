from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()


llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

def get_response(messages):
    system_prompt = SystemMessage(
        content=(
            "You are a medical assistant chatbot. "
            "Answer ONLY medicine-related questions. "
            "Give SHORT answers (1-2 lines only). "
            "No long explanation. "
            "If not medical, reply: Please ask medical questions only."
        )
    )

    chat_messages = [system_prompt]

    for msg in messages:
        if msg["role"] == "user":
            chat_messages.append(HumanMessage(content=msg["content"]))

    
    response = llm.invoke(chat_messages)

    return response.content