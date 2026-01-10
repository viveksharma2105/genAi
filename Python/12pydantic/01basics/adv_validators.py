from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class  Person(BaseModel):
    first_name: str
    last_name: str
    
    @field_validator("first_name, last_name")
    def name_must_be_capital(cls,v):
        if  not v.istitle():
            raise ValueError("Name mus be capital")
        return v
    
    
class Product(BaseModel):
    price: str #$4.45
    
    @field_validator("price", mode='before')
    def parse_price(cls, v):
        if isinstance(v,  str):
            return float(v.replace("$","").replace(',', ""))
        return v
    
class Daterange(BaseModel):
    startDate: datetime
    endDate: datetime
    
    @model_validator(mode='after')
    def vaidate_date_range(cls,values):
        if  values.startDate >= values.endDate:
            raise  ValueError("Enddate mustbe aafter the Startdate ")
        return values