#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/11/19 17:34

import socket
import time
from threading import  Thread
from urls import  urlpatterns

def run():
	server = socket.socket()

	IP_PORT = ('127.0.0.1',8001)  #http://127.0.0.1:8001/index 页面输入访问
	server.bind(IP_PORT)
	server.listen()

	while True:
		conn,addr = server.accept()
		from_client_msg = conn.recv(1024)
		from_browser_msg = from_client_msg.decode()
		print(from_browser_msg)
		path = from_browser_msg.split()[1]
		conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
		for item in urlpatterns:
			if item[0] == path:
				# t = Thread(target=item[1],args=(conn,))
				# t.start()
				data = item[1](conn)
				break


# server.close()
# server = socket.socket()
#
# IP_PORT = ('127.0.0.1',8001)  #http://127.0.0.1:8001/index 页面输入访问
# server.bind(IP_PORT)
# server.listen()
#
# while True:
# 	conn,addr = server.accept()
# 	from_client_msg = conn.recv(1024)
# 	from_browser_msg = from_client_msg.decode()
# 	print(from_browser_msg)

import socket
server = socket.socket()  # TCP协议
ip = ('127.0.0.1', 8000)
server.bind(ip)
server.listen()

while True:

    conn, addr = server.accept()
    from_client_msg = conn.recv(1024)
    print(from_client_msg.decode())
    conn.send(b'i miss you')
    conn.close()












