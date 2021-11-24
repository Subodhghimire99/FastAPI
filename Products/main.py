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


@app.post("/add", status_code = 201)
def add_data(request:Products, db:Session=Depends(get_db)):
    new_product = models.Products(
        name = request.name,
        price = request.price,
        description = request.description,
        recommended = request.recommended,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product) 
    return new_product


@app.get("/products")
def get_data(db:Session = Depends(get_db)):
    products = db.query(models.Products).all()
    return products

@app.get("/products/{id}/")
def get_individual(id, db:Session = Depends(get_db)):
    product = db.query(models.Products).filter(models.Products.id == id).all()
    return product