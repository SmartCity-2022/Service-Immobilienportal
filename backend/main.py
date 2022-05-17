from fastapi import Depends, FastAPI, status
from config.db import engine, session_local
from config import models
from config.schemas import ImmobilienSchema
from sqlalchemy.orm import Session

models.base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.get("/api")
async def root():
    return {"message": "Hello World"}

@app.get("/api/immobilien")
def get_immobilien(db: Session = Depends(get_db)):
    all_immobilien = db.query(models.Immobilien).all()
    return all_immobilien

@app.post("/api/immobilien", status_code=status.HTTP_201_CREATED)
def add_immobilie(immobilie: ImmobilienSchema, db: Session = Depends(get_db)):
    new_immobilie = models.Immobilien(address=immobilie.address, zipcode=immobilie.zipcode, city=immobilie.city, price=immobilie.price, created_at=immobilie.created_at, updated_at=immobilie.updated_at)
    db.add(new_immobilie)
    db.commit()
    db.refresh(new_immobilie)
    return new_immobilie