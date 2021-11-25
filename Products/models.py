from .database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean

#ORM(Object Relational Mapping)
#This maps the Products class fields with Products Table

class Products(Base):
    __tablename__ = 'Products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    recommended = Column(Boolean)

class Customers(Base):
    __tablename__ = 'Customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    country = Column(String)
    frequent = Column(Boolean)