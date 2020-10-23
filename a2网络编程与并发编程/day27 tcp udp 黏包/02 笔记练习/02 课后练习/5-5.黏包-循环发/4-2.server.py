# tcp server 黏包  7步

import socket
import struct
import time

# 1 新建socket对象
sk = socket.socket()

# 2 注册主机
sk.bind(('127.0.0.1',9001)) #元组

# 3 监听
sk.listen()

while True:
	# 4 三次握手
	conn,addr = sk.accept()
	while True:
		# 5 收发数据
		# 01 发送数据的长度
		strvar = input('我是tcp server,请输入你要发送的内容:')
		bytes1 = strvar.encode() #1 str转成bytes
		length = len(bytes1) #2 字节数--数据的长度

		bytes2 = struct.pack('i',length)  #把任意长度int转成字节流(长度固定是4)

		conn.send(bytes2)

		# 02 发送数据的内容
		conn.send(bytes1)

		# 03 发送数据的内容2
		# conn.send('hello'.encode())
		if strvar == 'q':
			print('当前会话停止')
			break


	# 6 四次挥手
	conn.close()

# 7 退还端口
sk.close()





# 黏包的思路
# 1 写死
# 2 写活

# 写死
# 1 server
# 1 发送数据的长度
	# 123  字节数是3

# 2 发送数据的内容


# 2 client
# 1 拿到数据的长度
# 2 sk.recv(数据的长度)
  # sk.recv(3)

# 写活
# 1 server
# 1 发送数据的长度
	# 123  字节数是3
	# 通过struct.pack('i',3)转换成4个字节

# 2 发送数据的内容


# 2 client
# 1 拿到数据的长度
# 2 sk.recv(4)
  # 得到4个字节的变量res
  # 通过struct.unpack('i',res) 得到元组 tup[0]
























