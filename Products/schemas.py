#A database schema is the skeleton structure that represents the logical view of the entire database
#In fastAPI documentation they call schema as model

from pydantic import BaseModel
from typing import Optional


class Products(BaseModel):
    id:int
    name:str
    price:float
    description:str
    recommended:Optional[bool]