import threading
import time

def cpu_heavy():
    print("Crunching numbers...")
    count = 0
    for i in range(10**7):
        count += i
    print("Done crunching.")

start = time.time()
threads =  [threading.Thread(target=cpu_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Time taken with threads: {time.time() - start:.2f} seconds")