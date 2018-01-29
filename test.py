from multiprocessing import Process
import requests
def do_something(url):
    r = requests.get(url)
    print(url, r.status_code)


p1 = Process(target=do_something, args=('https://www.baidu.com',))
p2 = Process(target=do_something, args=('https://www.sina.com',))
p3 = Process(target=do_something, args=('https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000',))
p1.start()
p2.start()
p3.start()
p1.join()
p2.join()
p3.join()
print('i am waiting......')