# app/models.py
from sqlalchemy import Column, Integer, String, DateTime, Text
from .database import Base
import datetime

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    role = Column(String)   # "user" or "assistant"
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
