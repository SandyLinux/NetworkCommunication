# Echo client program
import socket
import time

HOST = ''    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(b'Hello, world')
        data = s.recv(1024)
        print('Received-----', repr(data))
        time.sleep(30)
