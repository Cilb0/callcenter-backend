# app/services/openai_client.py
import os
import openai
from dotenv import load_dotenv

load_dotenv()  # .env içinden OPENAI_API_KEY okur
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

def query_openai(messages, model="gpt-3.5-turbo", max_tokens=400, temperature=0.2):
    """
    messages: list of {"role": "user"/"assistant"/"system", "content": "..."}
    returns: text reply (str)
    """
    if not OPENAI_API_KEY:
        return "AI servisi yapılandırılmamış (OPENAI_API_KEY yok)."

    try:
        resp = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return resp["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"AI çağrısı sırasında hata: {str(e)}"
