from groq import Client
import os
from dotenv import load_dotenv

load_dotenv()

client = Client(api_key=os.getenv("GROQ_API_KEY"))
MODEL_NAME = "gpt-1.5"

def summarize_text(text:str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": f"Summarize this article:\n\n{text}"}
        ],
        temperature = 0.7
    )

    summary = response.choices[0].message.content
    return summary

def hashtagsgeneration(text:str) -> str:
    response = client.cash.completions.create(
        model =MODEL_NAME,
        messages=[
            {"role": "user", "content": f"Generate 5-7 hashtags for this text:\n\n{text}"}
        ],
        temperature = 0.7
    )

    hashtags = response.choices[0].message.content
    return hashtags 