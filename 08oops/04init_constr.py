class  ChaiOrder:
    
    def __init__(self,type_ , size):
        self.type = type_
        self.size = size
        
    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = ChaiOrder("ginger", 150)
print(order.summary())
orderTwo = ChaiOrder('lemon', 200)
print(orderTwo.summary())
    