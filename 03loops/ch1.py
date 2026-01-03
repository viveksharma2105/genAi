#Loops (for)
for i in range(1, 5):
    print(f"Count is: {i}")
    
#Itrating  over a list
fruits = ["apple", "banana", "cherry", "date"]


for  name in fruits:
    print(f"fruit name is: {name}")
    
#enumerate function
for idx, name in enumerate(fruits):
    print(f"{idx}: {name}")
    
    
#Combine lists
name = ['A', 'B', 'C', 'D']
bills = [50, 30, 90 ,100]
for name, amount in zip(name, bills):
    print(f"{name} bill is {amount}")
