#ON LIST
menu = ["masala chai", 'Ice tea', 'coffee', "lemon tea"]

Inced_tea =[i for i in menu if 'tea' in i]
length_tea =[i for i in menu if len(i) >  7]
print(Inced_tea)  # Output: ['Ice tea', 'lemon tea']
print(length_tea)  


#ON SET
numbers = [100, 22, 36, 22, 55, 62, 55, 78, 90, 22]

unique_numbers =  {i for i in numbers }
#length_number =  {i for i in numbers if len(i) > 3 }  ## it the list is string the  we apply this
print(unique_numbers)
#print(length_number)


#example
recipies = {
    "masala chai": ["tea", "milk", "sugar", "spice"],
    'Ice tea': ["tea", "ice", "lemon", "sugar"],                
    "coffee": ["coffee", "milk", "sugar"]
}
#extreme case
unique_spices = {spices for ingridients in recipies.values() for spices in ingridients}
print(unique_spices)


#dictionary
price_inr = {
    'book': 50,
    'fruit': 15,
    'juice':30
}

price_usd = {key:value / 80 for key, value in price_inr.items()}
print(f'price in USD: {price_usd}')