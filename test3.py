from threading import Thread
from queue import Queue


class Producer(Thread):
    def __init__(self, name, q):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(10):
            q.put(i)
            print('produce a {}'.format(i))


class Consumer(Thread):
    def __init__(self, name, q):
        super().__init__()
        self.name = name

    def run(self):
        while True:
            item = q.get()
            item += 2
            print('cousume a {}'.format(item))
            q.task_done()


q = Queue()
p = Producer('p', q)
c = Consumer('c', q)
p.setDaemon(True)
c.setDaemon(True)
p.start()
c.start()
q.join()
print('main thread end')
