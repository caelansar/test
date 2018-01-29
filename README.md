`apply`方法是**阻塞**的。
意思就是等待当前子进程执行完毕后，在执行下一个进程。进入子进程执行后，等待当前子进程执行完毕，在继续执行下一个进程。例如：有三个进程0，1，2。等待子进程0执行完毕后，在执行子进程1，然后子进程2，最后回到主进程执行主进程剩余部分，

`apply_async `是**异步非阻塞**的。
意思就是：不用等待当前进程执行完毕，随时根据系统调度来进行进程切换。
例如：

```python
import time
from multiprocessing import Process, Pool, current_process
def run():
    print(current_process().name)
    time.sleep(1)
    print('end')

if __name__ == '__main__':
    mylist = [1, 2, 3, 4, 5, 6]
    pool = Pool(4)
    for i in range(4):
        pool.apply_async(run)
    print('main process end')
'''
out put:
main process end
'''
```

因为进程的切换是操作系统来控制的，抢占式的切换模式。首先运行的是主进程，CPU运行很快，这短短的几行代码，完全没有给操作系统进程切换的机会，主进程就运行完毕了，整个程序结束。子进程完全没有机会切换到程序就已经结束了。

`pool.close()`和`pool.join()`告诉主进程，等待所有子进程运行完毕后在运行剩余部分

```python
import time
from multiprocessing import Process, Pool, current_process
def run():
    print(current_process().name)
    time.sleep(1)
    print('end')

if __name__ == '__main__':
    pool = Pool(4)
    for i in range(4):
        pool.apply_async(run)
    pool.close()
    pool.join()
    print('main process end')
'''
out put:
SpawnPoolWorker-1
SpawnPoolWorker-4
SpawnPoolWorker-3
SpawnPoolWorker-2
end
end
end
end
main process end
'''
```

