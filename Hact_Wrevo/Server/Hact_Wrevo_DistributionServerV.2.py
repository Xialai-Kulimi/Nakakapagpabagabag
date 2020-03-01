import sys
import socket
import os
import math as m
import hashlib


def sha256(input):
    sha_signature = hashlib.sha256(input.encode()).hexdigest()
    return sha_signature


filename = os.path.basename(__file__)
print(filename+' Server start')

ServerAmount = 100
BasePort = 60010

f = open('Hact_Wrevo_mainChatServerV.01.py', 'r')
content = f.readlines()
f.close()
# print(content)
for i in range(0, ServerAmount):
    f = open('./chatServers/No.'+str(i+1)+'ChatServer.py', 'w')
    content[13] = 'port = ' + str(BasePort + i) + '\n'
    print(str(BasePort + i))
    for l in content:
        f.writelines(l)
    f.close()
    #os.system('start ./chatServers/No.'+str(i+1)+'ChatServer.py')
f = open('./ChatServers/AvaList', 'w')
for i in range(1, ServerAmount+1):
    f.write('0')
    print('0', end='')

f.close()
print('\nServers generation complete')


port = 60005
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(1024)

while True:
    try:
        conn, addr = s.accept()
        print('Connect with', addr)
        data = str(conn.recv(1024), 'utf8')
        print('Server received', data)
        f = open('./player/'+data.split(':')[0], 'r')
        if sha256(f.readlines()[0].split(': ')[1].replace('\n', '')) == data.split(':')[1]:
            f.close()
            f = open('./ChatServers/AvaList', 'r')
            AvailableServersList = f.read()
            f.close()
            n = -1
            for i in list(AvailableServersList):
                n += 1
                if i == '0':
                    conn.sendall(bytes(str(n), 'utf8'))
                    print('Available Server:No.', str(n+1))
                    conn.close()
                    continue
            conn.sendall(bytes('server fulled'))
            print('Done sending')
        else:
            conn.sendall(bytes('Deny', 'utf8'))
        conn.close()
    except:
        pass
