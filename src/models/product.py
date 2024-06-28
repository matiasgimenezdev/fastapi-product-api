from pydantic import BaseModel
from typing import Union


class Product(BaseModel):
    product_id: int
    description: str
    price: float
    tax: Union[float, None] = None
    stock: Union[int, None] = 0
