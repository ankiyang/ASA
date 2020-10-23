import socket
import struct

from datetime import datetime

def socket_():
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)

    dict_ = dict()

    file_ = open("attac_ddos.txt", "a")
    time1 = str(datetime.now())

    # record the current time
    file_.writelines(time1)
    file_.writelines("\n")

    # assume the particular IP is hitting for more than 15 times
    # then it would be an attack
    no_of_ips = 15
    r_no_of_ips = no_of_ips + 10
    while True:
        pkt = s.recvfrom(2048)
        ipheader = pkt[0][14:34]
        ip_hdr = struct.unpack("!8sB3s4s4s",ipheader)
        ip_ = socket.inet_ntoa(ip_hdr[3])
        print("The Source of the IP is:", ip_)
    
        # check whether the IP exists in dictionary or not. If it exists then it will increase it by 1.
        if dict_.has_key(IP):
            dict_[IP] = dict_[IP]+1
            print(dict_[IP])

    
    pass