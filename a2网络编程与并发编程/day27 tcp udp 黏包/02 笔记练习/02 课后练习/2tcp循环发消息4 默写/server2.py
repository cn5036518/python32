# tcp server 7步 循环发消息
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000)) #元组
sk.listen()

while True:
	conn,addr = sk.accept()
	
	while True:
		#收发数据
		res = conn.recv(1024)
		print(res)
		print(res.decode())

		strvar = input('我是tcp server,请输入你要发送的内容:')
		conn.send(strvar.encode())
		
		if strvar == 'q':
			print('本次会话结束')
			break

	conn.close()
	
sk.close()































