# udp server 4步 循环发消息
import socket

# 1 新建socket对象
sk = socket.socket(type = socket.SOCK_DGRAM)

# 2 注册主机
sk.bind(('127.0.0.1',9000)) #元组

# 3 收发数据 先收后发 没有三次握手
while True:
#收数据
	msg,addr = sk.recvfrom(1024)
	print(msg)
	print(msg.decode())
	print(addr)
	# b'1'
# 1
# ('127.0.0.1', 50556)

# 发送数据
	strvar = input('服务端,请输入你要发送的内容:')
	sk.sendto(strvar.encode(),addr)
	
	if strvar == 'q':
		break


# 4 关闭连接
sk.close()

















