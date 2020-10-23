import time
import numpy as np
from threading import Thread, Event

from scipy.fft import fft, ifft
import socket 

class TrafficCapture(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        pass

    def run(self):
        s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)

        ip_packet = dict()
        time_init = time.time()

        while true:
            pkt = s.recvfrom(2048)
            ip_ = self.capture_ip(pkt)
            time_end = time.time()

            if ip_packet.has_ley(ip_):
                ip_packet[ip_].append(time_end)
            else:
                ip_packet[ip_] = [time_end]

            if time_end - time_init > 10:
                self.queue.put(ip_packet)
                ip_packet = dict()
                time_init = time.time()
                time.sleep(1)
                pass

    def capture_ip(self, pkt):
        ip_header = pkt[0][14:34]
        ip_hdr = struct.unpack("!8sB3s4s4s", ip_header)
        ip_ = socket.inet_ntoa(ip_hdr[3])
        return ip_


class DAF(Thread):
    """ Detection with Average Filter"""

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.time_period = 30000
        self.total_packets_per_ip = dict()
        self.attackers = list()
        pass

    def run(self):
        time_start = time.time()
        count = 0
        while True:
            item = self.queue.get()
            for k,v in item.items():
                if self.total_packets_per_ip.has_key(k):
                    self.total_packets_per_ip[k].append(len(k))
                else:
                    self.total_packets_per_ip[k] = len(v)
                pass

            count += 1
            if time.time() - time_start > self.time_period:
                break

        total_packets = sum(self.total_packets_per_ip.values())
        # calculate averages
        average_for_all_ips = total_packets / count

        for k, v in self.total_packets_per_ip:
            average_per_ip = sum(v)/count
            if average_per_ip > average_for_all_ips:
                self.attackers.append(k)

        self.log_(",".join(self.attackers))

    def log_(self, content):
        with open("attackers.txt") as f_:
            f_.writelines(content)


class DDFT(Thread):
    """Detection with Discrete Fourier Transform"""

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.ip_time = dict()

    def run(self):
        # T
        # sampling_duration = 5
        threshold = 15
        sample_number_threshold = 5

        time_start = time.time()
        count = 0
        while True:
            item = self.queue.get()

            for k, v in item.items():
                time_difference = list()
                for index, each_ in enumerate(v):
                    if index == 0:
                        continue
                    difference_ = each_ - v[index-1]
                    time_difference.append(difference_)
                    # if index == len(v)-1:
                    #     continue
                y = fft(np.array(time_difference))
                pass

        # calculate the differences between the reception times
        # of the packets for each IP source


if __name__ == '__main__':
    pass