import socket
import sys

vers = 0.21

port = 60001
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(1024)

print("check vers server start")

while True:
    try:
        conn, addr = s.accept()
        print('check with', addr)
        data = conn.recv(1024)
        print('Server received', repr(data))
        conn.send(bytes(str(vers), "utf8"))
        print('Done')
        conn.close()
    except:
        pass
