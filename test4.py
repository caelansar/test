import time
from multiprocessing import Process, JoinableQueue, Queue
from random import random



def double(n):
    return n * 2


# def producer(in_queue):
#     while 1:
#         wt = random()
#         time.sleep(wt)
#         in_queue.put((double, wt))
#         print('put {}'.format(wt))
#         if wt > 0.9:
#             in_queue.put(None)
#             print('stop producer')
#             break

class Producer(Process):
    def __init__(self,in_queue):
        super().__init__()
        self.in_queue = in_queue

    def run(self):
        while 1:
            wt = random()
            time.sleep(wt)
            self.in_queue.put((double, wt))
            print('put {}'.format(wt))
            if wt > 0.9:
                self.in_queue.put(None)
                print('stop producer')
                break

# def consumer(in_queue, out_queue):
#     while True:
#         task = in_queue.get()
#         if task is None:
#             break
#         print('get {}'.format(task[1]))
#         func, arg = task
#         result = func(arg)
#         out_queue.put(result)

class Consumer(Process):
    def __init__(self,in_queue,out_queue):
        super().__init__()
        self.in_queue = in_queue
        self.out_queue = out_queue
        
    def run(self):
        while True:
            task = self.in_queue.get()
            if task is None:
                break
            print('get {}'.format(task[1]))
            func, arg = task
            result = func(arg)
            self.out_queue.put(result)

tasks_queue = JoinableQueue()
results_queue = Queue()
processes = []
p = Producer(tasks_queue)
p.start()
processes.append(p)
c = Consumer(tasks_queue, results_queue)
c.start()
processes.append(c)


for p in processes:
    p.join()
while True:
    if results_queue.empty():
        break
    r = results_queue.get()
    print('Result:', r)
