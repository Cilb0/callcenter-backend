from fastapi import APIRouter, WebSocket
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()

@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Sen müşteri hizmetleri botusun. Kullanıcıya internet, telefon ve TV sorunlarında yardımcı ol."},
                    {"role": "user", "content": data},
                ],
            )
            await websocket.send_text(response.choices[0].message.content)
        except Exception as e:
            await websocket.send_text(f"Hata: {str(e)}")
            break
