# udp  client   
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

while True:
	#发消息
	strvar = input('我是udp client,请输入你要发送的内容:')
	sk.sendto(strvar.encode(),('127.0.0.1',9000))
	
	if strvar == 'q':
		print('本次会话结束')
		break
	
	#收消息
	msg,addr = sk.recvfrom(1024)
	print(msg)
	print(msg.decode())
	

	
sk.close()































