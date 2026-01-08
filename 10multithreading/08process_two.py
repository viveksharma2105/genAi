from multiprocessing import Process
import time

def cpu_heavy():
    print("Crunching numbers...")
    count = 0
    for i in range(10**9):
        count += i
    print("Done crunching.")

if __name__ == "__main__":
    start = time.time()
processes =  [Process(target=cpu_heavy) for _ in range(2)]
[p.start() for p in processes]
[p.join() for p in processes]

print(f"Time taken with processes: {time.time() - start:.2f} seconds")