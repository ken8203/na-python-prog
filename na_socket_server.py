#! /usr/bin/env python
# -*-coding: utf-8 -*-
# file: na_socket_server.py

import socket

HOST = ''
PORT = 50007

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
while True:
	data = conn.recv(1024)
	if not data:
		break
	conn.sendall(data)
conn.close()