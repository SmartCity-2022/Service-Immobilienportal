from .db import base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Immobilien(base):
    __tablename__ = 'immobilien'
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(255))
    zipcode = Column(String(255))
    city = Column(String(255))
    price = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
