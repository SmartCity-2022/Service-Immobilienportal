from datetime import datetime
from pydantic import BaseModel


class ImmobilienSchema(BaseModel):
    address: str
    zipcode: int
    city: str
    price: int
    created_at: datetime
    updated_at: datetime