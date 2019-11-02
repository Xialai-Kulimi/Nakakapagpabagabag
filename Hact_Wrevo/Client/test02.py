import socket
import os
import hashlib
import time
import threading
import pygame

mainNowLine = 0
channel = ""

def localSetting():
    global mainNowLine
    f = open("setting", "r")
    f.seek(0, 0)
    mainNowLine = int(f.readline())
    f.close


def settingUpdate(a, b):
    try:
        f = open("setting", "r")
    except:
        f = open("setting", "w")
    content = f.readlines()
    text = ""
    for string in content:
        if string == content[a-1]:
            try:
                text = text + str(b) + "\n"
            except:
                text = text + b + "\n"
        else:
            text = text + string
    f.seek(0, 0)
    f.close()
    f = open("setting", "w")
    f.write(text)


def sha256(input):
    sha_signature = \
        hashlib.sha256(input.encode()).hexdigest()
    return sha_signature

# try:
#     filename = os.path.basename(__file__)
#     for root, dirs, files in os.walk('./'):
#         for name in files:
#             if name.endswith(".exe"):
#                 if "./" + filename != os.path.join(root, name):
#                     # os.remove(os.path.join(root, name))
#                     print(os.path.join(root, name))
# except:
#     pass


vers = 0.21

localSetting()

host = socket.gethostname()  # "220.135.245.148"
print(host)
username = ""
password = ""
s = socket.socket()
raw_msg = ""

port = 60001
s.connect((host, port))
s.send(bytes(socket.gethostname(), "utf8"))
print("receiving lastest vers")
lastestvers = s.recv(1024)
print("done...lastest vers:" + str(lastestvers, "utf8"))


if float(str(lastestvers, "utf8")) > vers:  # 更新
    lastestContent = ""
    s = socket.socket()
    port = 60002
    s.connect((host, port))
    s.send(bytes(socket.gethostname(), "utf8"))

    while True:
        print('receiving lastest version...')
        data = s.recv(1024)
        print('data=%s', str(data, "utf8"))
        if not data:
            break
        lastestContent = lastestContent + str(data, "utf8")

    print('Successfully get the file')
    s.close()
    print('connection closed\nReplacing old version...')
    filename = os.path.basename(__file__)
    f = open(filename, "w")
    f.write(lastestContent)


def login():
    global username, password, host
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
        print("Log in")
        pass


login()

def inputMsg():
    global raw_msg
    rawmsg = input("[mainChat]:")
    print("i")
    inputMsg()

def mainchat():
    global username, host, mainNowLine, channel, raw_msg
    channel = "mainChat"
    while True:
        # mainNowLine = localSetting()
        if rawmsg == "":
            try:
                s = socket.socket()
                s.connect((host, 60004))
                s.send(bytes(str(mainNowLine)+":pass", "utf8"))
                data = str(s.recv(32768), "utf8")
                s.close()
                f = open("mainchathis", "a")
                print("asdfasdf")
                print(data)
                print("asdfasdf")
                for text in (data + "_")[len(data.split(":")[0]) + 1:-1].split("\n"):
                    print("[" + text.split(":")[2] + "]:" + text.split(":")[1] + ":" + text.split(":")[3])
                    f.write(text.split(":")[1] + ":" + text.split(":")[3] + "\n")
                print("[mainChat]:" + username + ":" + rawmsg)
                print(data.split(":")[0])
                mainNowLine = int(data.split(":")[0])
                settingUpdate(1, mainNowLine)
            except:
                pass
        else:
            msg = str(mainNowLine)+":"+username+":"+channel+":"+rawmsg+":"+str(int(time.time()))+":"+sha256(username+":"+channel+":"+rawmsg+":"+str(int(time.time()))+":"+password)
            rawmsg = ""
            s = socket.socket()
            s.connect((host, 60004))
            s.send(bytes(msg, "utf8"))
            data = str(s.recv(32768), "utf8")
            s.close()
            f = open("mainchathis", "a")
            print(data)
            for text in (data+"_")[len(data.split(":")[0])+1:-1].split("\n"):
                print("["+text.split(":")[2]+"]:"+text.split(":")[1]+":"+text.split(":")[3])
                f.write(text.split(":")[1]+":"+text.split(":")[3]+"\n")
            print("[mainChat]:"+username+":"+rawmsg)
            mainNowLine = int(data.split(":")[0])
            settingUpdate(1, mainNowLine)
        print("mainNowLine:"+str(mainNowLine))


def main():

    #try:
    channel = "mainChat"
    mainchat()
    f = open("mainchathis", "r")
    print(f.read())
    #except:
    main()


mainNowLine = 1
t = threading.Thread(target=inputMsg)

# 執行該子執行緒
t.start()
main()
#0.21