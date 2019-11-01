import sys
import socket
import math as m
import hashlib


def sha256(input):
    sha_signature = \
        hashlib.sha256(input.encode()).hexdigest()
    return sha_signature


port = 60003
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(1024)
print('Server start')

while True:
    conn, addr = s.accept()
    # recvdata = ""
    print('Login with', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))
    try:
        player.close()
    except:
        pass
    try:
        player = open(r"D:\Nakakabagpabagabag\Hact_Wrevo\Server\player\\"+str(data, "utf8").split(":")[0], "r")
        corrpassword = sha256(player.readline())
        if corrpassword == str(data, "utf8").split(":")[1]:
            conn.sendall(bytes("accept", "utf8"))
            print(str(data, "utf8")+" Log in")
        else:
            conn.sendall(bytes("no", "utf8"))
            print("User not exist" + data)
            player.close()
    except:
        pass

    print('Done')
    conn.close()
