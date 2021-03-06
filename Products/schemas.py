#A database schema is the skeleton structure that represents the logical view of the entire database
#In fastAPI documentation they call schema as model

from pydantic import BaseModel
from typing import Optional


class Products(BaseModel):
    name:str
    price:float
    description:str
    recommended:Optional[bool]

class Customers(BaseModel):
    name:str
    age:int
    country:str
    frequent:bool
