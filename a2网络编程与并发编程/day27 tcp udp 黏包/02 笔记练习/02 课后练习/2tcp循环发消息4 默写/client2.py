# tcp client 4步 循环发消息
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000)) #元组

while True:
	#收发数据
	strvar = input('我是tcp client,请输入你要发送的内容:')
	sk.send(strvar.encode())

	res = sk.recv(1024)
	print(res)
	print(res.decode())
	
	if res.decode() == 'q':
		print('本次会话结束')
		break

sk.close()






















