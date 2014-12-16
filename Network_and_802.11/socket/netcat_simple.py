#!/usr/bin/env python

__author__ = "bt3"


import socket

# Defining constants
PORT = 12345
HOSTNAME = '54.209.5.48'


def netcat(text_to_send):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(( HOSTNAME, PORT))
    s.sendall(text_to_send)
    s.shutdown(socket.SHUT_WR)

    adata = []
    while 1:
        data = s.recv(1024)
        if data == "":
            break
        adata.append(data)

    s.close()
    return adata



if __name__ == '__main__':

    text_to_send = ''
    text_recved = netcat(text_to_send))
    print text_recved[1]