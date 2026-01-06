class Tealeaf:
    def __init__(self, age):
        self._age = age  # Private attribute
        
    @property #getter
    def age(self):
        return self._age + 2
        
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age =  age
            
        else:
            raise ValueError("Tealeag age must be btw 1-5")
    
leaf = Tealeaf(2)
print(leaf.age)