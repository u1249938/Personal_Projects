import socket

# Set to local host
target = '127.0.0.1'

def portscan(port):
    try:
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.connect((target, port))
        return True
    except:
        return False

for port in range(1, 1024):
    print("Port {} is open: ".format(port) + "{}".format(portscan(port)))
