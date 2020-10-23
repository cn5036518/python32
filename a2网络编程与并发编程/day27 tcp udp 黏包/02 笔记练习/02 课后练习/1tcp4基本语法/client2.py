# tcp client 4步
# 默写1

import socket

# 1 新建socket对象
sk = socket.socket()

# 2 建立连接到服务端
sk.connect(('127.0.0.1',9000)) #元组

# 3 收发数据
# 发数据
sk.send('你好,我是client'.encode())  #str转bytes

# 接收数据
res = sk.recv(1024)
print(res)
print(res.decode()) #bytes转str

# 4 关闭连接
sk.close()























