#Loops(while)
temperature = 40

while temperature < 100:
    print(temperature)
    temperature = temperature  + 15    # temperature +=  15
    


#Break, 
flavours = ["ginger",'Out of stock', 'masala', 'discontinued', 'lemon']

for i in flavours:
    if i == 'Out of stock':
        continue
    if i == 'discontinued':
        break
    print(i)
    
print('Outside of loop')


#for-else LOOP
staff = [('A', 13),('B', 15),('C', 17),('D', 12)]

for name, age in staff:
    if age >= 18:
        print(f"{name}")
        break
else:
    print("No staff member is above 18")
    
    
