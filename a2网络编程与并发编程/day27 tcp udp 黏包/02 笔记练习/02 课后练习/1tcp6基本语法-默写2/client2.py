# tcp client 4步
import socket

# 1 新建socket对象
sk = socket.socket()

# 2 建立连接到服务端
sk.connect(('127.0.0.1',9000)) # 元组

# 3 收发数据
# 发送数据
sk.send('我是tcp client'.encode())

#接收数据
res = sk.recv(1024)
print(res)
print(res.decode())
# b'hello'
# hello

# 4 关闭连接
sk.close()










































