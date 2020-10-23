import socket
import struct
import time
from datetime import datetime

def socket_():
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)
    dict_ip = dict()

    while True:
        pkt = s.recvfrom(2048)
        ipheader = pkt[0][14:34]
        ip_hdr = struct.unpack("!8sB3s4s4s",ipheader)
        ip_ = socket.inet_ntoa(ip_hdr[3])
        print("The Source of the IP is:", ip_)
    
        # check whether the IP exists in dictionary or not. 
        # If it exists then it will increase it by 1.
        if dict_ip.has_key(ip_):
            dict_ip[ip_] = dict_ip[ip_]+1
            print(dict_ip[IPip_])

        time.sleep(1)

    
    pass