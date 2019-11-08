import sys
import socket
import math as m
import hashlib
import threaing


def sha256(input):
    sha_signature = \
        hashlib.sha256(input.encode()).hexdigest()
    return sha_signature


class CreateSocket:
    global host, password

    def __init__(self, port, listen):
        s = socket.socket()
        s.bind((host, port))
        s.listen(listen)


    def send(self, gist, msg):
        strs = gist + '\n' + msg + '\n' + str(time.time()) + sha256(
               gist + msg + password + str(time.time()))
        s.send(bytes(strs, 'utf8'))

    def recv(self):
        data = str(s.recv(2147483647), 'utf8')
        data = data.split('\n')
        f = open('./player/' + data[0], 'r')
        password = f.readlines[0].split(': ')
        if data[4] != sha256(data[0] + data[1] + data[2] + password + data[3]):
            return 1

    def disconn(self):
        conn.close()


port = 60010
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(0)


def server_send():
    global port
    send_port = port + 100
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, sedn_port))
    s.listen(0)
    conn, addr = s.accept()
    print('connect with:', addr)
    data = s.recv(1024)
    data = str(s.recv(1024), 'utf8')
    cli_now_line = int(data.split('\n')[2])
    read_line = cli_now_line
    while True:
        if read_line > cli_now_line :




print('Main chat Server start')
chathis = open("mainchathis", "r")
nowLine = len(chathis.readlines())
print("Now line:", nowLine)
chathis.close()
while True:
    try:
        conn, addr = s.accept()
        print('connect with', addr)
        f = open('AvaList', 'r')
        availist = list(f.read())
        print(availist)
        f.close()
        availist[port - 60010] = '1'
        f = open('AvaList', 'w')
        for numinlist in availist:
            f.write(numinlist)
        f.close()
        while True:

            text = str(nowLine) + ":"
            chathis = open("mainchathis", "r")

            data = str(conn.recv(32767), "utf8")
            print('Server received:\n'+data)
            histext = chathis.readlines()
            # print(str(histext)+":"+str(len(histext)))
            print("Organizing unread MSG")

            for i in range(int(data.split(":")[0])+1, nowLine+1):
                print(str(i)+"/"+str(nowLine))

                try:
                    text = text + histext[i-1]
                except:
                    pass
            print("Organize complete")

            print("Sending:")
            print(text)

            conn.send(bytes(text, "utf8"))
            print('Done sending')
            chathis.close()
            # print("Disconnect with ", addr)
            # conn.close()

            chathis = open("mainchathis", "a")
            try:
                player = open("./player" + data.split(":")[1], "r")
                # mainNowLine+":"+username+":"+channel+":"+msg+":"+int(time.time())+":"+sha256(username+":"+channel+":"+msg+":"+int(time.time())+":"+password)
                if sha256(data[len(data.split(":")[0])+1:-64]+player.readline()) == data.split(":")[5]:
                    chathis.write("\n"+data)
                    nowLine += 1
                else:
                    conn.send(bytes('deny', 'utf8'))
            except:
                pass
            chathis.close()
    except:
        f = open('AvaList', 'r')
        availist = list(f.read())
        f.close()
        availist[port - 60010] = '0'
        f = open('AvaList', 'w')
        for numinlist in availist:
            f.write(numinlist)
        f.close()