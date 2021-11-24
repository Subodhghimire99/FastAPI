from fastapi import FastAPI, Depends
from schemas import Products
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

#Creates table based of models
models.Base.metadata.create_all(engine)

@app.get("/")
def index():
    return("Working")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/add")
def add_data(request:Products, db:Session=Depends(get_db)):
    new_product = models.Products(
        id=request.id,
        name = request.name,
        price = request.price,
        description = request.description,
        recommended = request.recommended,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product) 
    return new_product