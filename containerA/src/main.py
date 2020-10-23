import os
import sys
import time
import socket
import json
import socketserver
from socketserver import BaseRequestHandler
import logging
from logging import handlers
from threading import Thread
from threading import Lock

container_b_ip = "172.19.0.22"
container_c_ip = "172.19.0.23"


class MySockServer(BaseRequestHandler):    #定义一个类
 
    # def __init__(self):
    #     # BaseRequestHandler.__init__(self)
    #     self.req_records = dict()
    #     # self.lock = lock
    #     self.timenow = time.time()
        
    def handle(self):      #handle(self)方法是必须要定义的，可以看上面的说明
        req_records = dict() 
        timenow = time.time()

        # logger = log()
        print ('Got a new connection from', self.client_address)
        while True:
            data = self.request.recv(1024)    #需要通过self的方法调用数据接收函数
            if not data:
                break
            print ('recv:', data, time.time())
            if self.client_address in req_records.keys():
                req_records[self.client_address].append(time.time())
            else:
                req_records[self.client_address] = [time.time()]
            # self.req_records[self.client_address] = 
            # logger.info(self.client_address, time.time())
            print("req::::", req_records)
 
            self.request.send(data.upper())   #需要通过self的方法调用数据接收函数
            
            if time.time() - timenow >300:
                self.write(req_records)
                timenow = time.time()

    def write(self, req_records):
        # self.lock.acquire()
        if not req_records:
            return 
        with open("ip_log.json", 'a', encoding='utf8') as f_:
            # tranfer json
            json.dump(req_records, f_, ensure_ascii=False)
            pass
        # self.lock.release()

def startRec():
    HOST = ''             #定义侦听本地地址口（多个IP地址情况下），这里表示侦听所有
    PORT = 50000         #Server端开放的服务端口
    s = socketserver.ThreadingTCPServer((HOST, PORT), MySockServer)
                              #调用SocketServer模块的多线程并发函数
    s.serve_forever()     #持续接受客户端的连接
    pass

def analysis_file(lock):
    file_path = "ip_log.json"
    if not os.path.exists(file_path):
        return
    
    while True:

        lock.acquire()
        with open(file_path, 'r', encoding='utf8') as f_:
            content = json.load(f_)
        
        lock.release()

        for k_, v_ in content.values():
            
            pass
        time.sleep(60)
    pass

def main():
    mutex = Lock()
    t_server = Thread(target=startRec, args=(mutex,))
    t_server.start()
    t_server.join()
    pass


class Reveiver(Thread):

    def __init__(self, target_ip):
        Thread.__init__(self)
        self.target_ip = target_ip

    def log(self, message):
        print(message)
    
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.target_ip, 80))
        s.listen(3)

        while True:
            conn, addr = s.accept()
            data = conn.recv(1024)
            conn.close()
            print("received data from sender: %s" % (data))

def send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    command = "bridge test!"
    sock.connect(('172.17.0.3', 4000))
    sock.sendall(command.encode())
    sock.close()
    pass

def receiver():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(container_b_ip)
    s.listen(5)

    while True:
        conn, _ = s.accept()
        data = conn.recv(1024)
        conn.close()
        print("received data from sender: %s" % (data))

    pass


def log():
    # 创建一个logger 
    logger = logging.getLogger('mylogger') 
    logger.setLevel(logging.DEBUG) 
    
    # 创建一个handler，用于写入日志文件 
    fh = logging.FileHandler('test.log') 
    fh.setLevel(logging.DEBUG) 
    
    # 再创建一个handler，用于输出到控制台 
    ch = logging.StreamHandler() 
    ch.setLevel(logging.DEBUG) 
    
    # 定义handler的输出格式 
    formatter = logging.Formatter('[%(created)f][%(thread)d][%(levelname)s] ## %(message)s')
    fh.setFormatter(formatter) 
    ch.setFormatter(formatter) 
    
    # 给logger添加handler 
    logger.addHandler(fh) 
    logger.addHandler(ch) 
    
    # 记录一条日志 
    # logger.info('foorbar') 
    return logger


if __name__ == "__main__":
    # receiver()
    startRec()
    # main()

    pass