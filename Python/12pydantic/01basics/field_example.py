from pydantic import BaseModel
from  typing import List, Dict, Optional

class Cart(BaseModel):
    user_id:int
    items: List[str]
    quantities:Dict[str, int]

class Blog(BaseModel):
    title:str
    content:str
    image_url:Optional[str] =None
    
cart_data ={
    'user_id':123,
    'items':["Keyboard", 'Mouse', 'chager'],
    'quantities': {"Keyboard":1, 'Mouse':2, 'chager':1}
}

cart = Cart(**cart_data)