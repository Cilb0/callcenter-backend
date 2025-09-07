from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

# Router
router = APIRouter()

# İstek modeli
class CustomerCreate(BaseModel):
    name: str
    email: str

# Yeni müşteri oluştur
@router.post("/", response_model=dict)
async def create_customer(customer: CustomerCreate):
    try:
        db: Session = SessionLocal()
        new_customer = models.Customer(
            name=customer.name,
            email=customer.email
        )
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        return {
            "id": new_customer.id,
            "name": new_customer.name,
            "email": new_customer.email
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")
    finally:
        db.close()
