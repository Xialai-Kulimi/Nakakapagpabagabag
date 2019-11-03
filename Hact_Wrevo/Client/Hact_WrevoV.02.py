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
version = 0.21
host = socket.gethostname()  # "220.135.245.148"

print("[system] Building functions")


class CreateSocket:
    global host

    def __init__(self, port):
        s = socket.socket()
        s.connect((host, port))

    def send(self, msg):
        s.send(bytes(msg, 'utf8'))
        return

    def recv(self):
        data = str(s.recv(2147483647), 'utf8')
        return data

    def disconn(self):
        s.close()


def server_login(server):  # server check user
    now_time = str(time.time())
    server.send(username + '\n' + sha256(username + password + now_time) + '\n' + now_time)


def local_setting():
    global mainNowLine
    local_setting_file = open("setting", "r")
    local_setting_file.seek(0, 0)
    mainNowLine = int(local_setting_file.readline())
    local_setting_file.close()


def setting_update(a, b):
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


print("[system] local version is:", version)
local_setting()

print("[system] local host", host)

print("[system] Checking lastest version")
port = 60001
s.connect((host, port))
s.send(bytes(socket.gethostname(), "utf8"))
lastestvers = float(str(s.recv(1024), "utf8"))
print("[system] Lastest Version is:", lastestvers)

if lastestvers > version:  # 更新
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
    os.system("python " + filename)
    os.system.exit()
    # f.write(lastestContent)


def input_msg():
    global raw_msg, username, mainNowLine
    raw_msg = input("[mainChat]:" + username + ":\r")


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
        t = threading.Thread(target=input_msg)
        t.start()
        main()


def main_chat_recv_cli(port):
    global username, host, mainNowLine, password
    main_chat_recv = CreateSocket(port)
    now_time = str(time.time())
    main_chat_recv.send(username + '\n' + sha256(username + password + now_time) + '\n' + now_time)


def main_chat_cli(port):
    global username, host, mainNowLine, channel, raw_msg, password
    main_chat_send = CreateSocket(port)
    server_login(main_chat_send)
    recv_port = main_chat_send.recv()
    main_chat_recv_cli(recv_port)


def login_chat_server():
    global username, password
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
            print(port, data)
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
