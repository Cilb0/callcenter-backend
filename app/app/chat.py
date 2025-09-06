# app/chat.py
import re
from app.routes.customer_routes import fake_customers
from app.routes.fault_routes import fake_fault_db

def rule_based_response(message, session_id=None):
    """
    Çok basit kural tabanlı cevap örneği:
    - Eğer mesaj içinde 4-10 haneli sayı varsa müşteri no kabul et ve doğrula.
    - Eğer "internet/modem" geçiyorsa arıza kaydı açmayı teklif et.
    - Eğer kullanıcı "evet" diyorsa arıza kaydı oluştur (basit).
    """
    text = message.lower()

    # müşteri numarası varsa
    numbers = re.findall(r"\b\d{4,10}\b", message)
    if numbers:
        cid = numbers[0]
        cust = fake_customers.get(cid)
        if cust:
            return f"Müşteri {cid} doğrulandı. İsim: {cust['name']}. Hangi hizmette sorun var? (internet/telefon/televizyon)"
        else:
            return "Müşteri numarası bulunamadı. Lütfen numarayı kontrol edin."

    if any(k in text for k in ["internet", "modem"]):
        return "Anladım, internet arızasıymış. Arıza kaydı oluşturmak ister misiniz? (evet/hayır)"

    if "evet" in text and any(k in text for k in ["internet", "modem", "internet arıza", "arıza"]):
        new_id = len(fake_fault_db) + 1
        entry = {
            "id": new_id,
            "customer_id": session_id or "unknown",
            "fault_type": "internet",
            "description": "Kullanıcı tarafından bildirildi"
        }
        fake_fault_db.append(entry)
        return f"Arıza kaydınız oluşturuldu. Kayit numarası: {new_id}"

    return "Size yardımcı olabilmem için müşteri numaranızı ya da arıza türünü (internet/telefon/televizyon) yazabilir misiniz?"
