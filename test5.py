import multiprocessing

import time


def consumer(input_q):
    while True:
        item=input_q.get()
        time.sleep(2)
        #处理项目
        print(item)
        #发出信号通知任务完成
        input_q.task_done()
        
def producer(sequence,output_q):
    for item in sequence:
        #将项目放入队列
        output_q.put(item)
    #等待所有项目被处理
    q.join()


#建立进程
if __name__=='__main__':
    q = multiprocessing.JoinableQueue()
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.daemon = True
    cons_p.start()
    cons_p1 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p1.daemon = True
    cons_p1.start()
    sequence = [1, 2, 3, 4]
    t1 = time.time()
    producer(sequence, q)
    t2 = time.time()
    print('main process end ',t2-t1)