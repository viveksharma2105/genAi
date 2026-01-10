from typing import  Optional, Union, List
from pydantic import BaseModel

#Optional Nested Models
class Address(BaseModel):
    street: str
    city: str
    postal_code: str
  
class  Company(BaseModel):
    name:  str
    address: Optional[Address] =None
    
class Employee (BaseModel):
    id: int
    name: str
    company: Optional[Company] =None
    
    
#Mixed Data Types in Nested Models
class TextContent(BaseModel):
    type: str = "text"
    content: str
    
    
class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt_text: str
    
class  Article(BaseModel):
    title: str
    section: List[Union[TextContent, ImageContent]] #Mixed content types in a list



