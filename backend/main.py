from fastapi import Depends, FastAPI, status
from config.db import engine, session_local
from config import models
from config.schemas import ImmobilienSchema, ImmobilienmaklerSchema, UserSchema, TerminSchema
from sqlalchemy.orm import Session

models.base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/immobilien")
def get_immobilien(db: Session = Depends(get_db)):
    all_immobilien = db.query(models.Immobilien).all()
    return all_immobilien

@app.get("/api/immobilien/{id}")
def get_immobilien_by_id(id: int, db: Session = Depends(get_db)):
    immobilien = db.query(models.Immobilien).filter(models.Immobilien.id == id).first()
    return immobilien

@app.post("/api/immobilien", status_code=status.HTTP_201_CREATED)
def add_immobilie(immobilie: ImmobilienSchema, db: Session = Depends(get_db)):
    new_immobilie = models.Immobilien(address=immobilie.address, zipcode=immobilie.zipcode, city=immobilie.city, price=immobilie.price, created_at=immobilie.created_at, updated_at=immobilie.updated_at)
    db.add(new_immobilie)
    db.commit()
    db.refresh(new_immobilie)
    return new_immobilie

@app.delete("/api/immobilien/{id}")
def delete_immobilie(id: int, db: Session = Depends(get_db)):
    immobilie = db.query(models.Immobilien).get(id)
    db.delete(immobilie)
    db.commit()
    return "Immobilie deleted"

@app.put("/api/immobilien/{id}")
def update_immobilie(id: int, immobilie: ImmobilienSchema, db: Session = Depends(get_db)):
    db_immobilie = db.query(models.Immobilien).get(id)
    db_immobilie.address = immobilie.address
    db_immobilie.zipcode = immobilie.zipcode
    db_immobilie.city = immobilie.city
    db_immobilie.price = immobilie.price
    db_immobilie.updated_at = immobilie.updated_at
    db.commit()
    return db_immobilie

@app.get("/api/immobilienmakler")
def get_immobilienmakler(db: Session = Depends(get_db)):
    all_immobilienmakler = db.query(models.Immobilienmakler).all()
    return all_immobilienmakler

@app.get("/api/immobilienmakler/{id}")
def get_immobilienmakler_by_id(id: int, db: Session = Depends(get_db)):
    immobilienmakler = db.query(models.Immobilienmakler).filter(models.Immobilienmakler.id == id).first()
    return immobilienmakler

@app.post("/api/immobilienmakler", status_code=status.HTTP_201_CREATED)
def add_immobilienmakler(immobilienmakler: ImmobilienmaklerSchema, db: Session = Depends(get_db)):
    new_immobilienmakler = models.Immobilienmakler(name=immobilienmakler.name, surname=immobilienmakler.surname, telnr=immobilienmakler.telnr, hashed_password=immobilienmakler.hashed_password, created_at=immobilienmakler.created_at, updated_at=immobilienmakler.updated_at)
    db.add(new_immobilienmakler)
    db.commit()
    db.refresh(new_immobilienmakler)
    return new_immobilienmakler

@app.put("/api/immobilienmakler/{id}")
def update_immobilienmakler(id: int, immobilienmakler: ImmobilienmaklerSchema, db: Session = Depends(get_db)):
    db_immobilienmakler = db.query(models.Immobilienmakler).get(id)
    db_immobilienmakler.name = immobilienmakler.name
    db_immobilienmakler.telnr = immobilienmakler.telnr
    db_immobilienmakler.hashed_password = immobilienmakler.hashed_password
    db_immobilienmakler.surname = immobilienmakler.surname
    db_immobilienmakler.updated_at = immobilienmakler.updated_at
    db.commit()
    return db_immobilienmakler

@app.delete("/api/immobilienmakler/{id}")
def delete_immobilienmakler(id: int, db: Session = Depends(get_db)):
    immobilienmakler = db.query(models.Immobilienmakler).get(id)
    db.delete(immobilienmakler)
    db.commit()
    return "Immobilienmakler deleted"

@app.get("/api/user")
def get_users(db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()
    return all_users

@app.get("/api/user/{id}")
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    return user

@app.post("/api/user", status_code=status.HTTP_201_CREATED)
def add_user(user: UserSchema, db: Session = Depends(get_db)):
    hashed_password = user.hashed_password
    new_user = models.User(name=user.name, surname=user.surname, telnr=user.telnr, hashed_password=hashed_password, created_at=user.created_at, updated_at=user.updated_at)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.put("/api/user/{id}")
def update_user(id: int, user: UserSchema, db: Session = Depends(get_db)):
    db_user = db.query(models.User).get(id)
    db_user.name = user.name
    db_user.surname = user.surname
    db_user.telnr = user.telnr
    db_user.hashed_password = user.hashed_password
    db_user.updated_at = user.updated_at
    db.commit()
    return db_user

@app.delete("/api/user/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).get(id)
    db.delete(user)
    db.commit()
    return "User deleted"

@app.get("/api/termine")
def get_termine(db: Session = Depends(get_db)):
    all_termine = db.query(models.Termin).all()
    return all_termine

@app.get("/api/termine/{id}")
def get_termin_by_id(id: int, db: Session = Depends(get_db)):
    termin = db.query(models.Termin).filter(models.Termin.id == id).first()
    return termin

@app.post("/api/termine", status_code=status.HTTP_201_CREATED)
def add_termin(termin: TerminSchema, db: Session = Depends(get_db)):
    new_termin = models.Termin(date=termin.date, time=termin.time, created_at=termin.created_at, updated_at=termin.updated_at)
    db.add(new_termin)
    db.commit()
    db.refresh(new_termin)
    return new_termin

@app.put("/api/termine/{id}")
def update_termin(id: int, termin: TerminSchema, db: Session = Depends(get_db)):
    db_termin = db.query(models.Termin).get(id)
    db_termin.date = termin.date
    db_termin.time = termin.time
    db_termin.updated_at = termin.updated_at
    db.commit()
    return db_termin

@app.delete("/api/termine/{id}")
def delete_termin(id: int, db: Session = Depends(get_db)):
    termin = db.query(models.Termin).get(id)
    db.delete(termin)
    db.commit()
    return "Termin deleted"