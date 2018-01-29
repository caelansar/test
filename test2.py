# # -*- coding: utf-8 -*-
# from multiprocessing import Process, Queue, JoinableQueue
# import time
# import random
#
#
# def double(n):
#     return n * 2
#
#
# def producer(name, task_q):
#     while 1:
#         n = random.random()
#         if n > 0.8:  # 大于0.8时跳出
#             task_q.put(None)
#             print('%s break.' % name)
#             break
#         print('%s produce %s.' % (name, n))
#         task_q.put((double, n))
#
#
# def consumer(name, task_q, result_q):
#     while 1:
#         task = task_q.get()
#         if task is None:
#             print('%s break.' % name)
#             break
#         func, arg = task
#         res = func(arg)
#         time.sleep(0.5)  # 阻塞
#         task_q.task_done()
#         result_q.put(res)
#         print('%s consume %s, result %s' % (name, arg, res))
#
#
# def run():
#     task_q = JoinableQueue()
#     result_q = Queue()
#     processes = []
#     p1 = Process(name='p1', target=producer, args=('p1', task_q))
#     c1 = Process(name='c1', target=consumer, args=('c1', task_q, result_q))
#     p1.start()
#     c1.start()
#     processes.append(p1)
#     processes.append(c1)
#
#     # task_q.join()
#
#     # join()阻塞主进程
#     for p in processes:
#         p.join()
#
#     # 子进程结束后，输出result中的值
#     while 1:
#         if result_q.empty():
#             break
#         result = result_q.get()
#         print('result is: %s' % result)
#
#
# if __name__ == '__main__':
#     run()


import time

from multiprocessing import Process, JoinableQueue, Queue

from random import random



tasks_queue = JoinableQueue()

results_queue = Queue()


def double(n):

    return n * 2


def producer(in_queue):
    while 1:
        wt = random()
        time.sleep(wt)
        in_queue.put((double, wt))
        if wt > 0.9:
            in_queue.put(None)
            print('stop producer')
            break


def consumer(in_queue, out_queue):
    while 1:
        task = in_queue.get()
        if task is None:
            break
        func, arg = task
        result = func(arg)
        # in_queue.task_done()
        out_queue.put(result)


processes = []
p = Process(target=producer, args=(tasks_queue,))
p.start()
processes.append(p)
p = Process(target=consumer, args=(tasks_queue, results_queue))
p.start()
processes.append(p)
# tasks_queue.join()
for p in processes:
    p.join()

while 1:
    if results_queue.empty():
        break
    result = results_queue.get()
    print('Result:', result)
