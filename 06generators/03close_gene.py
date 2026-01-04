def localCars():
    yield "Mahindra"
    yield "Tata"
    
def importedCars():
    yield "BMW"
    yield "Audi"
    
def allCars():
    yield from localCars()
    yield from importedCars()
    
for  car in allCars():
    print(car)
    
def  car_showroom():
    try:
        while True:
            order = yield "Which car do you want to buy?"
    except:
        print("Showroom is closed now.")
        
showroom = car_showroom()
print(next(showroom))
showroom.close() #clean up code