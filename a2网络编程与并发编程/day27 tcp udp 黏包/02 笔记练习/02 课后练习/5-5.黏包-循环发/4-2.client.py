# tcp client  4步  黏包
import socket
import struct

# 1 新建socket对象
sk = socket.socket()

# 2 建立连接到服务端
sk.connect(('127.0.0.1',9001)) #元组

while True:
	# 3 收发数据
	# 1 得到数据的长度
	bytes2 = sk.recv(4)
	tup = struct.unpack('i',bytes2)
	length = tup[0]

	# 2 接受第一个数据的内容
	res = sk.recv(length)
	print(res.decode())

	# 3 接受第二个数据的内容
	# res2 = sk.recv(1024)
	# print(res2.decode())
	if res.decode() == 'q':
		print('当前会话停止')
		break

# 4 关闭连接
sk.close()



















