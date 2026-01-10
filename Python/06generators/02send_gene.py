def chai_customer():
    print("Welcome! What would you like to order?")
    order  =yield
    while True:
        print(f"Preparing your {order}...")
        order = yield
        
stall = chai_customer()
next(stall)  

stall.send("masala chai")