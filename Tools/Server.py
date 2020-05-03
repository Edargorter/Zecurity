#!/usr/local/env python3 

import socket 
import hexdump as hd
import binascii as ba

HOST = '127.0.0.1'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

#Sequence packet
print(type(socket.SOCK_SEQPACKET))

#Test hexdump
test_str = ba.hexlify(bytes("Test string", "utf-8"))

print(hd.hexdump(test_str))

while 1:
    s.listen()
    conn, addr = s.accept()
    while conn:
        pkt = (conn.recv(1024))
        print(hd.hexdump(pkt))
        #print(ba.hexlify(bytes(pkt, "utf-8")))
        print("Received connection from: {}".format(addr))
