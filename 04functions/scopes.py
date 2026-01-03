# def  chaiCounter():
#     chaiOrder = "lemon"
#     def printOrder():
#         chaiOrder = "masala"
#         print("Inner order is:", chaiOrder)
#     printOrder() #inner fuction scope is over  here
#     print("Outer order is:", chaiOrder)
# chaiCounter()


#example 2
def outerFunction():
    color = "red"
    def innerFunction():
        nonlocal color
        color = "blue"
        print("inner color is:", color)
    innerFunction()
    print("Outer color is:", color)


outerFunction()


#example 3
list = [1,2,3]

def modifyList(idx):
    idx[1]  = 100
    
modifyList(list)
print(list)  #list is modified because lists are mutable


#example 4 args & keywordargs
def car(type, feature):
    print(f"Car type and feature is: {type}, {feature}")
    
car("sedan", "sunroof")    
car(feature="4X4", type="suv")

#example 5 args & keywordargs
def bike(*type, **feature):
    print("Bike args are:", type)
    print("Bike kwargs are:", feature)
bike("sports", "cruiser", brand="Yamaha", cc=150)    