#!/usr/bin/env python3

'''
Name: CLPI ("Clippy") 
Author: Zachary Bowditch (Edargorter) 
Date: 2020
Description: Command-line (network) packet inspector 
Status: Incomplete

'''

import socket
import os
import random
import sys
import re
import argparse 
import ssl

#Linux command-line editors
EDITORS = ["vim", "vi", "nano", "pico", "emacs"]

#Decoding packets
ENCODING = "utf-8"

#URL Regex pattern
url_reg = "[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"

CERT_PATH = os.path.join(os.getenv("HOME"))
HOST = "127.0.0.1"
PORT = 4443
EDITOR = "vim"
PRIVATE_KEY_FILE = "clpi_key.pem"
CERTIFICATE_FILE = "clpi_cert.pem"
END_OF_PACKET = b"\r\n\r\n"

parser = argparse.ArgumentParser(description="CLPI - Command-line packet inspector\n")
parser.add_argument("-p", "--port", metavar="port", type=int, help="Specify listening port")
parser.add_argument("-c", "--cert", metavar="cert", type=str, help="Folder of certificate and private key (.pem files)")
parser.add_argument("-e", "--editor", metavar="editor", type=str, help="Preferred text editor (e.g. vim)")
args = parser.parse_args()

if args.port:
    PORT = args.port
if args.cert:
    CERT_PATH = args.cert
if args.editor:
    EDITOR = args.editor 

#Display settings
print("[CLPI] Cert folder: {}".format(CERT_PATH))
print("[CLPI] IP: {}".format(HOST))
print("[CLPI] Port: {}".format(PORT))

# open editor if exists (Linux systems)
def edit(filename):
    response = os.system("which {}".format(EDITOR))
    if response:
        return False
    os.system("{} {}".format(EDITOR, filename))

def list_packets():
    pass

'''
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(os.path.join(CERT_PATH, CERTIFICATE_FILE), os.path.join(CERT_PATH, PRIVATE_KEY_FILE)) #Might need seperate files for public and private keys 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind((HOST, PORT))
sock.listen(5)
s = context.wrap_socket(sock, server_side=True)
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

folder_dir = "/tmp/clpi_requests"
if not os.path.isdir(folder_dir):
    os.mkdir(folder_dir)
file_string = "request_"
packet_id = 0


while 1:
    print("\n[CLPI] Listening...\n")
    conn, addr = s.accept()

    with conn:
        print("============================================")
        print("[CLPI] Connection from: {}".format(addr))
        print("============================================")
        print()
        data = b''

        while True:
            ddata = conn.recv(1024)
            if not ddata:
                break
            data += bytes(ddata)
            if data[-4:] == END_OF_PACKET:
                break
        #Decode into variable "encoding"
        request = data.decode(ENCODING, errors="ignore")
        print(request)

        #Write request to file 
        f = open(os.path.join(folder_dir, file_string + str(packet_id)), 'w+')
        f.write(request)
        f.close()

        while True:
            cont = input("[CLPI] Forward [f] Edit [e]: ")
            if cont and cont[0] in ["E", "e"]:
                print("[CLPI] Editing")
                #Edit packet
                edit(os.path.join(folder_dir, file_string + str(packet_id)))

                #Get edited packet
                f = open(os.path.join(folder_dir, file_string + str(packet_id)), 'r')
                request = f.read()
                f.close()
            elif cont and cont[0] in ["F", 'f']:
                print("[CLPI] Forwarding request")

            try:
                host_index = request.find("Host: ") + 5
                end_index = request[host_index:].find('\n') + host_index
                dest = request[host_index:end_index].strip().split(":")
                dest_url = dest[0]
                dest_port = 80
                if len(dest) >= 2:
                    dest_port = int(dest[1])
                print("To: ", dest_url, dest_port)
                break
            except Exception as e:
                print("[CLPI] Incorrect request format.")
                continue

        #Create socket to communicate with destination server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((dest_url, dest_port))
        client.send(bytes(request, encoding=ENCODING, errors="ignore"))

        data = b'' #Receive from destination server
        while True:
            ddata = client.recv(1024)
            if not ddata: 
                break
            data += ddata

        response = data.decode(ENCODING, errors="ignore")
        print("============================================")
        print("[CLPI] Response")
        print("============================================")
        print(response)
        print("============================================")
        
        #Send response back to browser
        conn.send(bytes(response, encoding=ENCODING, errors="encoding"))

        packet_id += 1

client.close()
s.close()
