from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool
    
input_data = {'id':101, 'name':'Vivek', 'is_active':True} #if we use 25 instead of True it will give pydantic  error

user = User(**input_data)
print(user)