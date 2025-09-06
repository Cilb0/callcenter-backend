from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# Arıza kaydı modeli
class FaultRequest(BaseModel):
    customer_id: str
    fault_type: str
    description: str

# Geçici bellek içi "veritabanı"
fake_fault_db = []


@router.post("/create")
def create_fault(request: FaultRequest):
    fault_entry = {
        "id": len(fake_fault_db) + 1,
        "customer_id": request.customer_id,
        "fault_type": request.fault_type,
        "description": request.description,
        "created_at": datetime.now().isoformat()
    }
    fake_fault_db.append(fault_entry)
    return {"status": "created", "fault": fault_entry}
