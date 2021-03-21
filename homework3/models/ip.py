from .base import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)


class IP(Base):
    __tablename__ = "ips"

    id = Column(Integer, primary_key=True)
    country = Column(String(32), unique=False)
    region = Column(String(32), unique=False)
    city = Column(String(32), unique=False)
    zip = Column(String(32), unique=False)
    lat = Column(Float, unique=False)
    lon = Column(Float, unique=False)
    ip = Column(String(32), unique=False)
    source = Column(Integer, unique=False)
