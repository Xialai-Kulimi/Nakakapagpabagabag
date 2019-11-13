import socket
import os
import hashlib
import time
import threading
import pygame

print("[system] Reset variable")

mainNowLine = 0
channel = ""
username = ""
password = ""
s = socket.socket()
raw_msg = ""
__version__ = 0.21
host = socket.gethostname()  # "220.135.245.148"
global_data: dict = {}

print('[system] checking core files')

path = "./data/"
if not os.path.isdir(path):
    os.mkdir(path)
path = "./asset/"
if not os.path.isdir(path):
    os.mkdir(path)
f = open('./data/log', 'a')
f.close()
f = open('./data/chat_log', 'a')
f.close()
f = open('./data/main_chat', 'a')
f.close()


print("[system] Building functions")


class CreateSocket:
    global host, username, password

    def __init__(self, port):
        s = socket.socket()
        s.connect((host, port))

        strs = username + '\n' + str(time.time()) + '\n' + sha256(
            username + password + str(time.time()))
        s.send(bytes(strs, 'utf8'))

    def send(self, gist, msg):
        strs = username + '\n' + gist + '\n' + msg + '\n' + str(time.time()) + sha256(
            username + gist + msg + password + str(time.time()))
        s.send(bytes(strs, 'utf8'))

    def recv(self):
        data = str(s.recv(32767), 'utf8')
        print(data)
        if data.split('\n')[3] == sha256(data.split('\n')[0]+data.split('\n')[1]+data.split('\n')[2]):
            if (time.time()-float(data.split('\n')[2])) > 1:
                return 'Timed out'
            local_msg_log = open(data.split('\n')[0], 'a')
            local_msg_log.write(data.split(data.split('\n')[1] + ' ' + data.split('\n')[2]))
            return data.split('\n')[0], data.split('\n')[1], data.split('\n')[2]
        else:
            return 'Server be hacked'

    def disconn(self):
        s.close()


# def server_login(server):  # server check user
#     now_time = str(time.time())
#     server.send(username + '\n' + sha256(username + password + now_time) + '\n' + now_time)


def local_setting():
    global mainNowLine
    local_setting_file = open("setting", "r")
    local_setting_file.seek(0, 0)
    mainNowLine = int(local_setting_file.readline())
    local_setting_file.close()


def setting_update(a, b):  # edit setting file
    try:
        local_setting_file = open("setting", "r")
    except:
        local_setting_file = open("setting", "w")
    content = local_setting_file.readlines()
    text = ""
    for string in content:
        if string == content[a - 1]:
            try:
                text = text + str(b) + "\n"
            except:
                text = text + b + "\n"
        else:
            text = text + string
    local_setting_file.seek(0, 0)
    local_setting_file.close()
    local_setting_file = open("setting", "w")
    local_setting_file.write(text)


def sha256(str):
    sha_signature = hashlib.sha256(str.encode()).hexdigest()
    return sha_signature


print("[system] local version is:", __version__)
local_setting()

print("[system] local host:", host)

print("[system] Checking lastest version")
port = 60001
s.connect((host, port))
s.send(bytes(socket.gethostname(), "utf8"))
lastestvers = float(str(s.recv(1024), "utf8"))
print("[system] Lastest Version is:", lastestvers)

if lastestvers > __version__:  # 更新
    print("[system] Start update")
    print("[system] Reveiving lastest version...\a")
    filename = os.path.basename(__file__)
    lastestContent = bytes("", "utf8")
    s = socket.socket()
    port = 60002
    s.connect((host, port))
    s.send(bytes(socket.gethostname(), "utf8"))
    # f = open("recvfile", "wb")

    while True:

        data = s.recv(1024)
        print('data=' + str(data, "utf8"))
        if not data:
            break
        # f.write(data)
        lastestContent = lastestContent + data
    print("[system] Reveiving lastest version...Complete")
    s.close()
    # f.close()
    print('[system] Replacing old version...')
    f = open(filename, "wb")
    f.write(lastestContent)
    f.close()
    print("[system] Restart program")
    os.system(filename)
    exit()
    # f.write(lastestContent)


# def input_msg():
#     global raw_msg, username, mainNowLine
#     raw_msg = input("[mainChat]:" + username + ":\r")


def login():
    global username, password, host
    os.system('cls')
    username = input("name?")
    password = input("password?")

    s = socket.socket()  # login
    port = 60003

    s.connect((host, port))
    s.send(bytes(username + ":" + sha256(password), "utf8"))
    data = str(s.recv(1024), "utf8")
    if (data == "") or (data == "no"):
        print(data)
        print("User not exist")
        s.close()
        login()
    if data == "accept":
        os.system('cls')
        print("[system] Log in")
        # t = threading.Thread(target=input_msg)
        # t.start()
        main()


def main_chat_recv_cli():
    global username, host, mainNowLine, password
    mainNowLine = 0
    main_recv_port = global_data['main_chat_recv_port']
    print(main_recv_port)
    main_chat_recv = CreateSocket(main_recv_port)
    data = main_chat_recv.recv()
    main_chat_recv.send('now_line', '0')
    #now_line = int(main_chat_recv.recv()[1])
    #for i in range(1, now_line + 1):
    #    print(main_chat_recv.recv()[1], time.asctime(time.localtime(time.time())))

    while True:
        print(main_chat_recv.recv())


def main_chat_cli(port):
    global username, host, mainNowLine, channel, password, recv_port
    #try:
    main_chat_send = CreateSocket(port)
    global_data['main_chat_recv_port'] = port + 100
    main_chat_recv_cli_threading = threading.Thread(target=main_chat_recv_cli)
    main_chat_recv_cli_threading.start()
    while True:
        raw_msg = input()
        strs_msg = ''
        for i in raw_msg.split(' '):
            strs_msg += i
        if strs_msg != '':
            main_chat_send.send('main_chat', raw_msg)
    #except:
    #    main_chat_cli(port)


def login_chat_server():
    global username, password
    main_chat_cli(60010)
    s = socket.socket()
    s.connect((host, 60005))
    s.send(bytes(username + ":" + sha256(password), 'utf8'))
    data = str(s.recv(1024), 'utf8')
    if data == "deny":
        print('illegal user')
        s.close()
        login()
    else:
        try:
            port = 60010 + int(data)
            main_chat_cli(port)
        except:
            print('Connection exception')
            # print(port, data)
            login_chat_server()


def main():
    global channel
    # try:
    channel = "mainChat"
    login_chat_server()
    # f = open("mainchathis", "r")
    # print(f.read())
    # except:
    main()


login()

# mainNowLine = 1

# mainNowLine = 0

f = open("mainchathis", "r")
print(f.read())
