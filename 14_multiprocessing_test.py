import multiprocessing
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
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)

    # t1.setDaemon(True)
    p1.daemon = True
    p1.start()
    p2.daemon = True
    p2.start()
    time.sleep(4)       # 4秒后停止主线程
    print("主线程结束")