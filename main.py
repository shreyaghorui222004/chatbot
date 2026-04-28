from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_response(messages):

    system_prompt = {
        "role": "system",
        "content": (
            "You are a medical assistant chatbot. "
            "Answer ONLY medicine-related questions. "
            "Give SHORT answers (1-2 lines only). "
            "No long explanation. "
            "If not medical, reply: Please ask medical questions only."
        )
    }

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[system_prompt] + messages,
        max_tokens=60
    )

    return response.choices[0].message.content