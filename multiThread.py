from multiprocessing import Pool
from multiprocessing.dummy import Pool

"""
有时候单核单线程要比多核多线程要快
http://cenalulu.github.io/python/gil-in-python/
http://www.jianshu.com/p/02b7a279c588
"""
import time
from threading import Thread


def my_counter():
    i = 0
    for _ in range(1000000):
        i = i + 1
    return True


def main_sequ():
    start_time = time.time()
    for tid in range(100):
        t = Thread(target=my_counter)
        t.start()
        t.join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))


def mian_multiThread():
    start_time = time.time()
    thread_array = {}
    for tid in range(100):
        t = Thread(target=my_counter)
        t.start()
        thread_array[tid] = t
    for i in range(100):
        thread_array[i].join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))

if __name__ == '__main__':
    main_sequ()
    mian_multiThread()
