# tcp client 4步 循环收发
import socket

# 1 新建socket对象
sk = socket.socket()

# 2 建立连接到服务端
sk.connect(('127.0.0.1',9000)) #元组

while True:
	# 3 收发数据
	# 发送数据
	strvar = input('客户端,请输入你要发送的数据:')
	sk.send(strvar.encode()) #str转bytes

	# 接收数据
	res = sk.recv(1024)
	print(res)
	print(res.decode()) #bytes转str
	if res.decode() == 'q':
		print('本次会话结束')
		break


# 4 关闭连接
sk.close()











































