from multiprocessing import Process, Queue
import time

def prep_chai(queue):
    queue.put("Chai is ready")

if __name__ == '__main__':
    queue = Queue()

p = Process(target=prep_chai,args=(queue,))
p.start()
p.join()
print(queue.get())