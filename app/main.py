from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import customer_routes, fault_routes, chat_routes

app = FastAPI(title="Müşteri Hizmetleri Botu")

# CORS ayarları - frontend (Netlify) Render API'ye bağlanabilsin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Gerekirse buraya sadece Netlify domainini yazabilirsin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route kayıtları
app.include_router(customer_routes.router, prefix="/customers", tags=["customers"])
app.include_router(fault_routes.router, prefix="/faults", tags=["faults"])
app.include_router(chat_routes.router, prefix="/chat", tags=["chat"])


@app.get("/")
def root():
    return {"message": "Müşteri Hizmetleri Botu API çalışıyor!"}
