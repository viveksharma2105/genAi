## if condition
isKettle_boiled = True

if isKettle_boiled:
    print('Time to make coffee')
    
   
#if-else condition   
snack =  input("Entre you snack: ")    

if snack == 'samosa' or snack == 'burger':
    print("your order is confirmed")
    
else:
    print("we don't have this item")

# if-elif-else condition    
cup = input("Enter your cup size (small/medium/large): ").lower()

if cup == 'small':
    print("Price is $2")
elif cup == 'medium':
    print("Price is $3")
elif cup == 'large':
    print("Price is $4")
else:
    print("Invalid cup size")