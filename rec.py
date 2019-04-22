import socket
import time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print(conn, addr)
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print('---',data)
            data1 = b'update '
            if not data: 
                break
            conn.sendall(data1)
