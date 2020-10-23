# tcp client  4步  黏包
import socket
import struct

# 1 新建socket对象
sk = socket.socket()

# 2 建立连接到服务端
sk.connect(('127.0.0.1',9000)) #元组

# 3 收发数据
# 接受数据
# 1 先计算数据的字节数据
res = sk.recv(4)  #长度是4的字节流
tup = struct.unpack('i',res)
# 把4个字节长度的值恢复成原来的数字,返回元组
length = tup[0]

# 2 接受数据内容
res = sk.recv(length)
print(res.decode())

# 3 接受数据内容2
res = sk.recv(1024)
print(res.decode())


# 4 关闭连接
sk.close()



















