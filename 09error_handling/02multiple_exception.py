def process_chai(item, quntity):
    try:
        price = {'masala': 20}[item]
        cost = price * quntity
        print(f"total cost {cost}")
    except KeyError:
        print("item not available")
    except TypeError:
        print("quntity must be a number")
        
process_chai('masala', 2)
process_chai('ginger', 'two')