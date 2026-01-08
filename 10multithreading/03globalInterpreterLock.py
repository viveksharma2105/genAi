#By multithreading we can run multiple threads (tasks, function calls) at the same time.
#mutexing of threads is managed by Global Interpreter Lock (GIL) in CPython implementation of Python.
import threading
import time  
def brew_chai():
    print(f"{threading.current_thread().name} started brewing chai")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing chai")
        
thred1 = threading.Thread(target=brew_chai, name="Chai-Maker-1")
thread2 = threading.Thread(target=brew_chai, name="Chai-Maker-2")

start  = time.time()
thred1.start()
thread2.start()
thred1.join()
thread2.join()
end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")