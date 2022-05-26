import socket
import threading
from queue import Queue

# Set to local host
target = '127.0.0.1'
que = Queue()
open_ports = []

def portscan(port):
    try:
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.connect((target, port))
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        que.put(port)

def worker():
    while not que.empty():
        port = que.get()
        if portscan(port):
            print("Port {} is open".format(port))
            open_ports.append(port)

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)