import sys
import socket
import os
import math as m
import hashlib

host = socket.gethostname()
remote_ip = socket.gethostbyname(host)
print(remote_ip)
