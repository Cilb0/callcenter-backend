from fastapi import APIRouter

router = APIRouter()

# Örnek müşteri verisi (gerçekte veritabanından gelecek)
fake_customers = {
    "12345": {"name": "Ali Veli", "services": ["internet", "telefon"]},
    "67890": {"name": "Ayşe Fatma", "services": ["televizyon"]}
}


@router.get("/verify/{customer_id}")
def verify_customer(customer_id: str):
    """Müşteri numarasını doğrular"""
    customer = fake_customers.get(customer_id)
    if customer:
        return {"status": "valid", "customer": customer}
    return {"status": "invalid", "message": "Müşteri bulunamadı"}
