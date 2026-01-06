#Error like 
# missing index ,
# missing key, 
# division by zero ,
# Type error,
# name error


# IndexError
order  = ['apple', 'banana']
#print(order[2])


#try and except block
chai_menu = {'masala': 30, 'ginger': 35}
try:
    chai_menu['lemon'] #KeyError
except KeyError:
    print("The key you are trying to access does not exist in the dictionary.")
    
    
    
    print("Hello Code")
    
    
    
    
#complex example
def serveChai(flavour):
    try:
        print(f"Preparing your {flavour} chai.") 
        if flavour == 'unknown':
            raise  ValueError('we dont know the flavour')
    except ValueError as e:
        print('Error: ', e)
    else:
        print(f"{flavour} chai is ready!")
    finally:
        print('next customer...')
        
serveChai('unknown')