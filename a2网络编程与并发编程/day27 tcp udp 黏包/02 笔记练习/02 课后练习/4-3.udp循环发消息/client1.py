# udp  client   3步  循环发消息
import socket

# 1 新建socket对象
sk = socket.socket(type = socket.SOCK_DGRAM)

# 2 收发消息  先发后收
while True:
#发送消息
	strvar = input('我是udp client 请输入你要发送的内容:')
	sk.sendto(strvar.encode(),('127.0.0.1',9000))

#接受消息
	msg,addr = sk.recvfrom(1024)
	print(msg)
	print(msg.decode())
	print(addr)
	
	# b'2'
# 2
# ('127.0.0.1', 9000)
	if msg.decode() == 'q':
		break


# 3 关闭连接
sk.close()





















