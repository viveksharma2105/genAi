#Integers

a = 2
b =  4

totalsum = a + b
totalsub = b - a
totalmul = a * b
totaldiv = b / a
totalfloordiv = b // a
totalpower = a ** b
print("Total:", totalsum)
print("Total Sub:", totalsub)
print("Total Mul:", totalmul)
print("Total Div:", totaldiv) #float
print("Total Floor Div:", totalfloordiv)
print("Total Power:", totalpower)

#Booleans
is_active = True
count = 10
totalcount = count + is_active  # True is treated as 1 (called Upcasting)
print("Total Count:", totalcount)


milk_price = 2  #if it is 0, none then it is treated as False
print("Milk has Price: ", bool(milk_price))


#logical operations
is_raining = False
has_umbrella = True
can_go_outside = is_raining and has_umbrella  
print("Can go outside:", can_go_outside)



#Real numbers (float)
a = 5.5
b = 2.0
total = a + b
print("Total Float:", total)




#Strings  (are immutable)
first_name = "John"
last_name = "Doe"
print("Full Name:", first_name + " " + last_name)


#indexing
description = "honesty is the best policy"
print(f"First 4 words: {description[:5:2]}") #if its [:5:2] then :2 means one letter gap
print(f"Last word: {description[20:]}")
print(f"Reverse string: {description[::-1]}") #reverse the string

StartWithCapital = description.capitalize()
Capatilized = description.upper()
print(f"StartWithCapital: {StartWithCapital}")
print(f"Capatilized: {Capatilized}")



