#field_validator iis used for custom fields same for model we use model_validator
from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username:str
    
    @field_validator('username')
    def username_length(cls,v):
        if len(v) < 4:
            raise ValueError("Username must be atleast 4  char...")
        return v
    
class SignupData(BaseModel):
    password: str
    confirm_password:str
    
    @model_validator(mode='after')
    def pwd_match(cls,values):
        if values.password != values.confirm_password:
            raise ValueError('Password do not match')
        return values