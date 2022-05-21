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
    telnr: int
    hashed_password: str
    surname: str
    created_at: datetime
    updated_at: datetime
    immobilien = list[ImmobilienSchema] = []
    termin = list[TerminSchema] = []

class UserSchema(BaseModel):
    name: str
    surname: str
    hashed_password: str
    telnr: int
    created_at: datetime
    updated_at: datetime
    termin = list[TerminSchema] = []

class TerminCreateSchema(TerminSchema):
    makler_termin = list[TerminSchema] = []
    user_termin = list[TerminSchema] = []