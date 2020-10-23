# tcp client  4步  黏包
import socket
import struct

# 1 新建socket对象
sk = socket.socket()

# 2 建立连接到服务端
sk.connect(('127.0.0.1',9000)) #元组

# 3 收发数据
# 2 接受数据内容
res = sk.recv(1024)
print(res.decode())

# 3 接受数据内容2
res2 = sk.recv(1024)
print(res2.decode())

#hellohello2


# 4 关闭连接
sk.close()



















