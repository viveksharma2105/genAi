# #walrus operator
# value = 13
# remainder = value % 5
# if remainder:
#     print(f"Remainder is {remainder}")
    
#Using walrus operator
value = 13
if (remainder:= value % 5):
    print(f"Remainder is {remainder}")
    
    
    
#another example
fruits = ["apple", "banana", "cherry", "date"]
if(requested := input("Enter fruit name: ")) in fruits:
    print(f"{requested} is available")
else:
    print(f"{requested} is not available")