from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int
    #in python ... means required field
    name: str = Field(..., min_length=1, max_length=50,description="Employee name", examples="John Doe")
    department: Optional[str] = 'General'
    salary: float = Field(..., ge=10000, le=200000, description="Employee salary")