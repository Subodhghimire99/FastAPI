from fastapi import FastAPI, Depends, status, Response, HTTPException
from .schemas import Products,Customers
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

#Creates table based of models
models.Base.metadata.create_all(engine)


@app.get("/")
def index():
    return(
        {
            'Message':'Welcome to the Products API',
            'EndPoints': {
                '/add':'For adding data (POST Request)',
                '/products': 'For accessing all data (GET Request)',
                '/products/{id}' : 'For accessing data with individual id (GET Request)' 
                }    
        }
    )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/add", status_code = status.HTTP_201_CREATED)
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
def get_individual(id,response:Response, db:Session = Depends(get_db)):
    product = db.query(models.Products).filter(models.Products.id == id).all()
    if not product:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return({"data":f"response with id {id} not found"})
        #Alternatively
        raise HTTPException(status_code=404, detail=f"not found with id {id}")
    return product