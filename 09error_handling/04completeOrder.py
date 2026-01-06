class InvalidChaiError(Exception):pass

def bill(flavour, cup):
    menu = {'masala':20, 'ginger':50}
    try:
        if flavour not in menu:
            raise InvalidChaiError("chai  is not available")
        if not isinstance(cup, int):
            raise TypeError('Number  must be an Integer')
        total = menu[flavour] * cup
        print(f"Your bill for {cup} cups of  {flavour} chai : rupees {total}")
    except Exception as e:
        print('Error',e)
    finally:
        print("Thankyou for visiting")
        
bill('mint',2)
bill('masala',3)
bill('lemon',"two")