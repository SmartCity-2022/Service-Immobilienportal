from datetime import datetime
from pydantic import BaseModel


class ImmobilienSchema(BaseModel):
    address: str
    zipcode: int
    city: str
    price: int
    created_at: datetime
    updated_at: datetime
    
class TerminSchema(BaseModel):
    termin_art: str
    termin_date: datetime
    termin_dauer: int
    user_id: int
    immobilienmakler_id: int
    created_at: datetime
    updated_at: datetime

class ImmobilienmaklerSchema(BaseModel):
    name: str
    surname: str
    telnr: str
    hashed_password: str
    created_at: datetime
    updated_at: datetime

class UserSchema(BaseModel):
    name: str
    surname: str
    hashed_password: str
    telnr: str
    created_at: datetime
    updated_at: datetime
