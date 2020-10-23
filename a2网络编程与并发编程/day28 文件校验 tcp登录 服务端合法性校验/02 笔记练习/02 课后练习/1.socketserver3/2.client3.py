# ###  客户端
import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1",9001)) #元组


# 处理收发数据逻辑
while True:
	time.sleep(1)
	sk.send(b'give me five')
	res = sk.recv(1024)
	print(res.decode())
	
sk.close()



















