import os
import sys
import time
import socket


def send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    command = "bridge test!"
    sock.connect(('172.168.1.2', 4000))
    sock.sendall(command.encode())
    sock.close()
    pass

def receiver():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('172.168.1.3', 4000))
    s.listen(3)

    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        conn.close()
        print "received data from sender: %s" % (data)

    pass

if __name__ == "__main__":
    print("CONTAINER AAA")