import socket

sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9000)) #元组

while True:
	#先收后发
	msg,addr = sk.recvfrom(1024)
	print(msg)
	print(msg.decode())
	if msg.decode() == 'q':
		print('本次会话结束')
		break

	strvar = input('我是udp server,请输入你要发送的内容:')
	sk.sendto(strvar.encode(),addr)
	


sk.close()
















