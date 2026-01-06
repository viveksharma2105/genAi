class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
        
    @classmethod #we use cls (not self)to refer to the class itself
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split('-')
        return cls(tea_type, sweetness, size)
    
    @classmethod
    def from_dict(cls, order_dict):
        return cls(
            order_dict['tea_type'],
            order_dict['sweetness'],
            order_dict['size']
        )
        
order1 = ChaiOrder.from_string("Masala-High-Large")
order2 = ChaiOrder.from_dict({
    "tea_type": "Green",
    "sweetness": "Low",
    "size": "Medium"
})

print(order1.__dict__)  # Output: Masala High Large
print(order2.__dict__)  # Output: Green Low Medium