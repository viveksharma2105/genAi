#Dictionary
order = dict(type = 'coffee', size = 'medium', quantity = 1)
print(f"Order details: {order}")

#2nd method to create dictionary
recipe = {}
recipe['water'] = '200ml'
recipe['milk'] = '100ml'

print(f"Recipe water: {recipe['water']}")
print(f"Full recipe: {recipe}")
del recipe['milk']
print(f"Recipe after deleting milk: {recipe}")



order2 = {'type': 'coffee', 'size': 'medium', 'quantity': 1}
print(f"is size in order2 ?: {'size' in order2}")
print(f"order2 details (keys): {order2.keys()}")
print(f"order2 details (values): {order2.values()}")
print(f"order2 details (items): {order2.items()}")


size =  order2.get('size', "not specified")  #if size isi not found, return "not specified"
print(f"Order2 size using get(): {size}")