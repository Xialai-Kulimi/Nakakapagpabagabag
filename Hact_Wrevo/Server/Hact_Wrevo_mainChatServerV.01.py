import sys
import socket
import math as m
import hashlib
import threading
import time
import os


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
        data = str(s.recv(2147), 'utf8')
        data = data.split('\n')
        f = open('./player/' + data[0], 'r')
        password = f.readlines()[0].split(': ')[1]
        if data[4] != sha256(data[0] + data[1] + data[2] + password + data[3]):
            return 1

    # def disconn(self):
        # conn.close()


port = 60010
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(0)


def server_send():
    print('s=Send server start')
    global port
    send_port = port + 100
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, send_port))
    s.listen(0)

    conn, addr = s.accept()
    print('Send server connect with:', addr)

    data = str(conn.recv(2147), 'utf8')
    data = data.split('\n')
    username = data[0]
    f = open('./player/' + username, 'r')
    password = f.readlines()[0].split(': ')[1].replace('\n', '')
    if data[2] != sha256(data[0] + password + data[1]):
        print('bad user')
        conn.close()
    f.close()
    # while True:
    gist = 'checking'
    msg = 'Get!'
    strings = gist + '\n' + msg + '\n' + str(time.time()) + sha256(
        gist + msg + password + str(time.time()))
    conn.send(bytes(strings, 'utf8'))
    data = str(conn.recv(1024), 'utf8')
    #     if data != '':
    #         break

    print('aaaa')
    print(data)
    cli_now_line = int(data.split('\n')[2])
    # read_line = cli_now_line
    f = open('./player_mail/'+username, 'r')
    read_line = len(f.readlines())-1

    while True:
        if read_line > cli_now_line:
            f = open('./player_mail/' + username, 'r')
            gist = 'real_now_line: ' + str(cli_now_line+1)
            msg = f.readlines()[cli_now_line]
            strings = gist + '\n' + msg + '\n' + str(time.time()) + sha256(
                gist + msg + password + str(time.time()))
            s.send(bytes(strings, 'utf8'))
            cli_now_line += 1
            f.close()
        else:
            f = open('./player_mail/' + username, 'r')
            read_line = len(f.readlines())-1


print('Main chat Server start')
print(port)
#chathis = open("mainchathis", "r")
#nowLine = len(chathis.readlines())
#print("Now line:", nowLine)
#chathis.close()
while True:
    #try:
        conn, addr = s.accept()
        print('connect with', addr)
        t = threading.Thread(target=server_send)
        t.start()
        print('start server_send')
        data = str(conn.recv(21474), 'utf8')
        print(data)
        data = data.split('\n')
        username = data[0]
        f = open('./player/' + username, 'r')
        password = f.readlines()[0].split(': ')[1].replace('\n', '')
        f.close()
        print(password)
        print(data[2])
        print(sha256(data[0] + password + data[1]))
        if data[2] != sha256(data[0] + password + data[1]):
            conn.close()
            print('bad user')

            continue

        print('Recv server connect with', addr)
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
            data = str(conn.recv(21470), 'utf8')
            if data != '':
                data = data.split('\n')
                print(data)
                username = data[0]
                f = open('./player/'+username, 'r')
                password = f.readlines()[0].split(': ')[1]
                if data[4] != sha256(data[0] + data[1] + data[2] + password + data[3]):
                    conn.close()
                    break
                else:
                    if data[1] == 'main_chat':
                        for file in os.listdir('./player_mail/'):
                            f = open('./player_mail/' + file, 'a')
                            f.write('['+username+']:'+data[2]+'\n')
    #except:
    #    f = open('AvaList', 'r')
    #    availist = list(f.read())
    #    f.close()
    #    availist[port - 60010] = '0'
    #    f = open('AvaList', 'w')
    #    for numinlist in availist:
    #        f.write(numinlist)
    #    f.close()
    # try:
    #     conn, addr = s.accept()
    #     print('connect with', addr)
    #     f = open('AvaList', 'r')
    #     availist = list(f.read())
    #     print(availist)
    #     f.close()
    #     availist[port - 60010] = '1'
    #     f = open('AvaList', 'w')
    #     for numinlist in availist:
    #         f.write(numinlist)
    #     f.close()
    #     while True:

    #         text = str(nowLine) + ":"
    #         chathis = open("mainchathis", "r")

    #         data = str(conn.recv(32767), "utf8")
    #         print('Server received:\n'+data)
    #         histext = chathis.readlines()
    #         # print(str(histext)+":"+str(len(histext)))
    #         print("Organizing unread MSG")

    #         for i in range(int(data.split(":")[0])+1, nowLine+1):
    #             print(str(i)+"/"+str(nowLine))

    #             try:
    #                 text = text + histext[i-1]
    #             except:
    #                 pass
    #         print("Organize complete")

    #         print("Sending:")
    #         print(text)

    #         conn.send(bytes(text, "utf8"))
    #         print('Done sending')
    #         chathis.close()
    #         # print("Disconnect with ", addr)
    #         # conn.close()

    #         chathis = open("mainchathis", "a")
    #         try:
    #             player = open("./player" + data.split(":")[1], "r")
    #             # mainNowLine+":"+username+":"+channel+":"+msg+":"+int(time.time())+":"+sha256(username+":"+channel+":"+msg+":"+int(time.time())+":"+password)
    #             if sha256(data[len(data.split(":")[0])+1:-64]+player.readline()) == data.split(":")[5]:
    #                 chathis.write("\n"+data)
    #                 nowLine += 1
    #             else:
    #                 conn.send(bytes('deny', 'utf8'))
    #         except:
    #             pass
    #         chathis.close()
    # except:
    #     f = open('AvaList', 'r')
    #     availist = list(f.read())
    #     f.close()
    #     availist[port - 60010] = '0'
    #     f = open('AvaList', 'w')
    #     for numinlist in availist:
    #         f.write(numinlist)
    #     f.close()