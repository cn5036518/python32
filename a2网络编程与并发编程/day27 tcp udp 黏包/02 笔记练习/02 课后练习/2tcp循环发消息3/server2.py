# tcp server 7步 循环发
import socket

# 1 新建socket对象
sk = socket.socket()

# 2 注册主机
sk.bind(('127.0.0.1',9000))  #元组

# 3 监听
sk.listen()

while True:
	# 4 三次握手
	conn,addr = sk.accept()

	while True:		
		# 5 收发数据
		# 接收数据
		res = conn.recv(1024)
		print(res)
		print(res.decode()) #bytes转str
		
		# 发送数据
		strvar = input('服务端,请输入你要发送的内容:')
		conn.send(strvar.encode())		
		
		if strvar == 'q':
			print('本次会话结束')
			break

	# 6 四次挥手
	conn.close()

# 7 退还端口
sk.close()



















