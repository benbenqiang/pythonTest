import socket

import time

from kazoo.client import KazooClient
from pyhdfs import HdfsClient


def scan(port):
    s = socket.socket()
    s.settimeout(0.1)
    print('scanning :', port)
    if s.connect_ex(('localhost', port)) == 0:
        print(port, 'open')
    s.close()

def zk_scan(port):
    zk = KazooClient(hosts="127.0.0.1:2181")
    zk.start()
    print(zk.get_children("/"))
    print(port)
    zk.stop()

def hdfs_scan(port):
    client = HdfsClient(hosts="localhost:50070")
    print(client.listdir('/'))
    print(port)


if __name__ == '__main__':
    start_time = time.time()
    # scan basic
    #list(map(scan, range(1, 65536)))
    # scan multiThread
    # import threading
    #
    # threads = [threading.Thread(target=zk_scan, args=(i,)) for i in range(1, 65536)]
    # list(map(lambda x: x.start(), threads))

    #gevent scan
    from gevent import monkey
    monkey.patch_all()
    from gevent.pool import Pool

    pool = Pool(100)
    pool.map(zk_scan, range(1, 65536))
    pool.join()


    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))