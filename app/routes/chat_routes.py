import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# API key al
api_key = os.getenv("OPENAI_API_KEY")
print("DEBUG OPENAI_API_KEY:", api_key)  # Debug için

# OpenAI client
client = OpenAI(api_key=api_key)

# FastAPI router
router = APIRouter(prefix="/chat", tags=["Chatbot"])

# İstek modeli
class ChatRequest(BaseModel):
    message: str

# Yanıt modeli
class ChatResponse(BaseModel):
    response: str

# Sağlık kontrolü endpointi
@router.get("/ping")
async def ping():
    return {"status": "ok"}

# Chat endpointi
@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Sen müşteri hizmetleri destek botusun."},
                {"role": "user", "content": request.message}
            ],
            max_tokens=200
        )

        reply = completion.choices[0].message.content
        return ChatResponse(response=reply)

    except Exception as e:
        print("Chat API hatası:", e)
        raise HTTPException(status_code=500, detail=f"Bot cevap veremedi: {str(e)}")
