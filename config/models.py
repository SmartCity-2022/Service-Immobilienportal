from .db import base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Immobilien(base):
    __tablename__ = 'immobilien'
    id = Column(Integer, primary_key=True, index=True)
    makler_id = Column(Integer, ForeignKey('immobilienmakler.id'))
    address = Column(String(255))
    zipcode = Column(String(255))
    city = Column(String(255))
    price = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    makler = relationship("Immobilienmakler", back_populates="immobilien")

class Immobilienmakler(base):
    __tablename__ = 'immobilienmakler'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    telnr = Column(String(255))
    hashed_password = Column(String(255))
    surname = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    immobilien = relationship('Immobilien', back_populates='makler')
    termin = relationship('Termin', back_populates='immobilienmakler')

class User(base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    surname = Column(String(255))
    hashed_password = Column(String(255))
    telnr = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    termin = relationship('Termin', back_populates='user')

class Termin(base):
    __tablename__ = 'termin'
    id = Column(Integer, primary_key=True, index=True)
    termin_art = Column(String(255))
    termin_date = Column(DateTime)
    termin_dauer = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    immobilienmakler_id = Column(Integer, ForeignKey('immobilienmakler.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
    makler_termin = relationship('Immobilienmakler', back_populates='termin')
    user_termin = relationship('User', back_populates='termin')