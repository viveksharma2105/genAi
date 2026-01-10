from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    created_at: datetime
    address: Address
    tags: List[str] =[]
    
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )
    
user = User(
    id=1,
    name="Alice Johnson",
    email="example@gmil.com",
    is_active=False,
    created_at=datetime.now(),
    address=Address(
        street="789 Elm St",
        city="Jaipur",
        postal_code="54321"
    ),
    tags=["Premium", "Subscriber"]
)

pyDict = user.model_dump()
print(pyDict)

pyDict_json = user.model_dump_json()
print(pyDict_json)