from .database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean


class Products(Base):
    __tablename__ = 'Products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    recommended = Column(Boolean)