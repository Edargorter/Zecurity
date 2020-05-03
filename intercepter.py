#CLPI ("Clippy") Zachary Bowditch 2020
#!/usr/bin/env python3

import socket
import os
import random
import sys
import re

#Connect to the proxy with these details:
HOST = "localhost"
PORT = 3141

#URL Regex pattern
url_reg = "[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"

#Decoding packets
encoding = "UTF-8"

#Editors
editors = ["vim", "vi", "nano", "pico", "emacs"]
editor = 0

def edit(filename):
    os.system("{} {}".format(editors[editor], filename))

def list_packets():
    pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()

file_string = "request_"
packet_id = 0

print("Listening...")

while 1:
    conn, addr = s.accept()

    with conn:
        print("Connection from: {}".format(addr))
        data = b''

        while True:
            ddata = conn.recv(1024)
            if not ddata:
                break
            data += ddata

        #Decode into variable "encoding"
        data = data.decode(encoding)
        print(data)

        f = open(file_string + str(packet_id), 'w+')
        f.write(data)
        f.close()

        cont = input("Forward [F] Edit [e]: ")
        if cont != "" and cont[0] in ["E", "e"]:
            #Edit packet
            edit(file_string + str(packet_id))

        f = open(file_string + str(packet_id), 'r')
        data = f.readlines()
        print(data)

        dest = data[0].split(" ")[1].split(":")
        if len(dest) > 2:
            dest[0] = ''.join([dest[0], dest[1]])
            dest[1] = dest[2]

        dest_url = dest[0]
        dest_port = int(dest[1])

        print(dest_url)
        print(dest_port)

        #Create socket to communicate with destination server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((dest_url, dest_port))
        client.send(data.encode()) 

        response = b'' #Receive from destination server
        while True:
            ddata = client.recv(1024)
            if not ddata: 
                break
            response += ddata
        
        #Send response back to browser
        conn.send(response)

        #Play nice.
        f.close()
