#generators function
def chai():
    yield "cup 1: masala chai"
    yield "cup 2: masala chai"
    yield "cup 3: masala chai"
    
print(chai()) #generator object

for cup in chai():
    print(cup)


#example 2
#generators function
def chai1():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"
   
result = chai1()
print(next(result))  #cup 1
print(next(result))  #cup 2



#infinite generator(used for streaming data, live data feeds)
def infinite_chai():
    count = 1
    while True:
        yield f"refill #{count}"
        count += 1
        
refill = infinite_chai()

for _ in range(5):
    print(next(refill))