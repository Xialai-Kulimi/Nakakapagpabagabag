import sys
import socket
import os
import math as m

filename = os.path.basename(__file__)

port = 60002                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)
print(filename+' Server start')
filename = '0.21.txt'
f = open(filename, 'rb')
l = f.read(1024)
while l:
   print(l)
   l = f.read(1024)


while True:

    conn, addr = s.accept()
    print('update with', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename = '0.21.txt'
    f = open(filename, 'rb')
    l = f.read(1024)
    while l:
       conn.send(l)
       l = f.read(1024)
    f.close()
    print('Done sending')
    conn.close()

