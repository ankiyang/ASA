import socket
import time

def Send_Container_a():

    HOST = '172.19.0.21'
    # HOST = "localhost"
    PORT = 50000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    while True:
        user_input = str(int(time.time()))  
        for i in range(20):     
            s.sendall(user_input.encode())
            data = s.recv(1024)
            print ('Received', repr(data))
    
        
        time.sleep(5)

        # s.close()

if __name__ == "__main__":
    Send_Container_a()