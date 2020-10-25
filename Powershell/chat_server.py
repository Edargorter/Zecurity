#!/usr/bin/env python3

import socket
import sys
import select 

HEADER_LEN = 10

server_addr = ("127.0.0.1", 5555)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(server_addr)
sock.listen(1)

print("Started listening with port: {}...".format(server_addr[1]))

sockets_list = [sock]

clients = {}

def receive_msg(cli):
    try:
        msg = cli.recv(HEADER_LEN)
        print("MSG HEADER: {}".format(msg))

        if not len(msg):
            return False

        msg_len = int(msg.decode('utf-8').strip())

        return {'header': msg, 'data': cli.recv(msg_len)}

    except Exception as e:
        return False

while True:
    read_sockets, temp, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:

        if notified_socket == sock:

            cli, addr = sock.accept()
            user = receive_msg(cli)

            if not user:
                continue 

            sockets_list.append(cli)
            clients[cli] = user 

            print("Accepted connection from {}:{}, username: {}".format(addr, user['data'].decode('utf-8')))

        else:
            
            msg = receive_msg(notified_socket)

            if not msg:
                print("Closed connection from: {}".format(clients[notified_socket]['data'].decode('utf-8')))

                sockets_list.remove(notified_socket)

                del clients[notified_socket]

                continue 

            user = clients[notified_socket]

            print(f"Received message from {user['data'].decode('utf-8')}: {msg['data'].decode('utf-8')}")

            for cli in clients:
                
                if cli != notified_socket:

                    client_socket.send(user['header'] + user['data'] + msg['header'] + msg['data'])

    for notified_socket in exception_sockets:
        
        sockets_list.remove(notified_socket)
        
        del clients[notified_socket]
