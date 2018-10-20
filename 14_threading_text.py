import threading
import time


def test1():
    while True:
        time.sleep(0.5)
        print("text1")


def test2():
    while True:
        time.sleep(0.5)
        print("text2")


if __name__ == "__main__":
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.setDaemon(True)  # 把子线程设置为守护线程，该线程不重要。当主线进程结束的时候，子线进程也结束
    t1.start()
    t2.setDaemon(True)
    t2.start()
    time.sleep(4)       # 4秒后停止主线程
    print("主线程结束")