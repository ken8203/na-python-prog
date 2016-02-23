#! /usr/bin/env python
# -*-coding: utf-8 -*-
# file: na_socket_client.py

import socket

HOST = ''
PORT = 50007

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.sendall('Hello, world')
data = sock.recv(1024)
sock.close()

print "Received: " + str(data)