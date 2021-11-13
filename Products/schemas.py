from pydantic import BaseModel
from typing import Optional


class Products(BaseModel):
    id:int
    name:str
    price:float
    description:str
    recommended:Optional[bool]