import threading
import time

def prep_chai(type_, wait_time):
    print(f"Starting  preparing {type_} chai...")
    time.sleep(wait_time)
    print(f"{type_} chai is ready!")

t1 = threading.Thread(target=prep_chai, args=("Masala", 3))
t2 = threading.Thread(target=prep_chai, args=("ginger", 3))

t2.start()
t1.start()
t1.join()
t2.join()
print("Both types of chai are ready now!")