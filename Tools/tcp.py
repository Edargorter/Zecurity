#!/usr/bin/env python3 

from sys import argv
import os
import struct 
import socket

TCP_IP = argv[1]
TCP_PORT = int(argv[2])

print("IP: {}".format(TCP_IP))
print("PORT: {}".format(TCP_PORT))

BUFFER_SIZE = 1024

os.system("ls -l")
cwd = os.getcwd() + "\n"

MESSAGE = cwd.encode()
MESSAGE = struct.pack('{}s'.format(len(MESSAGE)), MESSAGE)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
data = data.decode()
s.close()
