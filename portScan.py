import socket


def scan(port):
    s = socket.socket()
    s.settimeout(0.1)
    print('scanning :',port)
    if s.connect_ex(('localhost', port)) == 0:
        print(port, 'open')
    s.close()


if __name__ == '__main__':
    list(map(scan, range(1, 65536)))
