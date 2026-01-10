#use for logging untill main thread is ended etc
import threading
import time

def monitor_temp():
    while True:
        print(f'Monitoring Temperature... ')
        time.sleep(1)
t = threading.Thread(target=monitor_temp, daemon=True)

t.start()

print("Main Program is doing some work...")