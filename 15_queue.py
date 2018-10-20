from queue import Queue
import time
import threading

q = Queue()
for i in range(1,20):
    q.put("https://www.baidu.com/page/{}/".format(i))

def test1():
    while True:
        time.sleep(0.5)
        url = q.get()
        print("*****test1*****{}*****".format(url))
        # q.task_done()

def test2():
    while True:
        time.sleep(0.5)
        url = q.get()
        print("*****test2*****{}*****".format(url))
        q.task_done()

if __name__ == '__main__':
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()

    q.join()

    print("主线程结束")