from multiprocessing import Process, JoinableQueue, Queue


class Producer(Process):
    def __init__(self, in_q):
        super().__init__()
        self.in_q = in_q

    def run(self):
        for i in range(10):
            self.in_q.put(i)
        print('生产完成')
        self.in_q.put(None)


class Consumer(Process):
    def __init__(self, in_q, out_q):
        super().__init__()
        self.in_q = in_q
        self.out_q = out_q

    def run(self):
        while True:
            item = self.in_q.get()
            if item is not None:
                item = item * 2
                self.in_q.task_done()
                self.out_q.put(item)
            else:
                print('消费完成')
                break


in_q = JoinableQueue()
out_q = Queue()

p = Producer(in_q)
c = Consumer(in_q, out_q)
p.daemon = True
c.daemon = True
p.start()
in_q.join()
c.start()
print('main process end')

while 1:
    if out_q.empty():
        break
    result = out_q.get()
    print('Result:', result)