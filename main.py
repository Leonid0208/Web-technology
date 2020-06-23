import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    pid = os.fork()
    if pid == 0 and not data:
        data = conn.recv(1024)
        conn.send(data)
        conn.close()
    else:
        conn.close()
s.close()
