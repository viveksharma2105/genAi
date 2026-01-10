import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order {i}")
        time.sleep(2)  # Simulate time taken to take an order
        
def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai {i}")
        time.sleep(3)  # Simulate time taken to brew chai
        
# Create threads for taking orders and brewing chai
order_thread = threading.Thread(target=take_orders)
brew_chai_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_chai_thread.start()

#wait for both threads to complete
order_thread.join()
brew_chai_thread.join()
print("All orders taken and chai brewed!")