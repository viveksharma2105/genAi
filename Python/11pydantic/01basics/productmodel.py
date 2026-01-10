from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name:  str
    price: float
    in_stock: bool = True
    
productOne = Product(id=1, name="CPU", price=99.99, in_stock=True)
productTwo = Product(id=2, name="Mouse", price=9.34)
