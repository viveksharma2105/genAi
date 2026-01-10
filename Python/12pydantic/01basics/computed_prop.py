from pydantic import BaseModel, computed_field,Field

class Product(BaseModel):
    price: float
    quantity:  int
    
    @computed_field
    @property
    def totalPrice(self) -> float:
        return self.price * self.quantity
    
    
class Booking(BaseModel):
    user_id: int
    room_id: int 
    nights: int  = Field(...,ge=1)
    rate_perNight: float
    
    @computed_field
    @property
    def total(self) -> float:
        return self.nights * self.rate_perNight
    
booking = Booking(
    user_id=123,
    room_id=456,
    nights=8,
    rate_perNight=100.00
)

print(booking.total)
print(booking.model_dump())