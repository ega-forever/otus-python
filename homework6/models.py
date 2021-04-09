from sqlalchemy import Integer, String, Column
from models.db import db

class Contact(db.Model):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    mail = Column(String(32), unique=False)
    from_mail = Column(String(32), unique=False)
