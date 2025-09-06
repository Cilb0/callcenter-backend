from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import customer_routes, fault_routes, chat_routes
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routerları ekle
app.include_router(customer_routes.router)
app.include_router(fault_routes.router)
app.include_router(chat_routes.router)

@app.get("/")
async def root():
    return {"message": "Call Center API çalışıyor 🚀", "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")}
