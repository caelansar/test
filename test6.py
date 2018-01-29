import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

def run(fn):
    #fn: 函数参数是数据列表的一个元素
    time.sleep(1)
    return fn*fn


if __name__ == "__main__":
    testFL = [1, 2, 3, 4, 5, 6]
    rl = []
    rl2 = []
    print('sequence:')  # 顺序执行(即串行执行)
    s = time.time()
    for fn in testFL:
        run(fn)

    e1 = time.time()
    print("顺序执行时间：", e1 - s)

    print('concurrent:')  # 创建多个进程，并行执行
    pool = Pool(5)  #创建拥有5个进程数量的进程池
    #testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    # rl =pool.map(run, testFL)
    for i in testFL:
        r = pool.apply_async(run, (i,))
        rl.append(r)
    pool.close()#关闭进程池，不再接受新的进程
    pool.join()#主进程阻塞等待子进程的退出
    e2 = time.time()
    print("并行执行时间：", e2 - e1)
    print([r.get() for r in rl])

    tpool = ThreadPool(5)
    for i in testFL:
        r = tpool.apply_async(run, (i,))
        rl2.append(r)
    tpool.close()  # 关闭线程池，不再接受新的进程
    tpool.join()  # 主线程阻塞等待子线程的退出
    e3 = time.time()
    print("线程执行时间：", e3 - e2)
    print([r.get() for r in rl2])
