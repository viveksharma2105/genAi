#we use functions to avoid code duplication, improve code  readability, and make maintenance easier.
def print_order(name, price):
    print(f"Order details: {name} - ${price}")
    
print_order("Sam",25)


#example 2
def clc_bill(cups, price_per_cup):
    return cups * price_per_cup

print(clc_bill(2, 5))
print_order("Alice", clc_bill(3, 5))