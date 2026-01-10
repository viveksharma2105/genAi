class Car:
    size = "Large"
    
    #by  using self we can access the attributes and methods of the class 
    def describe(self):
        return f"This car is {self.size} in size."
    
my_car =  Car()
print(my_car.describe()) #or
print(Car.describe(my_car))


#another refrence
your_car = Car()
your_car.size = "Small"
print(Car.describe(your_car))