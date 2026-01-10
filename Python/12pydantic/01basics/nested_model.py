from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    
class User(BaseModel):
    id: int
    name: str
    address: Address
    
address = Address(
    street="123 Main St",
    city="Anytown",
    postal_code="12345"
)

user = User(
    id=1,
    name="John Doe",
    address=address
)

user_data = {
    "id": 2,
    "name": "Jane Smith",
    "address": {
        "street": "456 huda",
        "city": "greenville",
        "postal_code": "67890"
    }
}

user =  User(**user_data)
print(user)