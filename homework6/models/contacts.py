from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from models.db import db


class Contact(db.Model):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    mail = Column(String, nullable=False, default="", server_default="")
    subject = Column(String, nullable=False, default="")
    text = Column(String, nullable=False, default="")
    created_at = Column(DateTime, default=datetime.utcnow)