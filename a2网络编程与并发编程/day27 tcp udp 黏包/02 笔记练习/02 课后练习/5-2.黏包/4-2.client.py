# ### 客户端
import socket
import time
import struct

sk = socket.socket()
sk.connect(("127.0.0.1",9001))

time.sleep(2)
# 收发数据的逻辑

# 第一次接受数据 (数据长度)
num = sk.recv(4) #4位字节流
tup = struct.unpack('i',num) #元组
print(tup[0])  #数据的长度-字节数

# 第二次接受数据 (真实数据的内容)
res = sk.recv(tup[0])
print(res.decode())
# 4  数据长度
# 1111  数据内容

# 第三次接受数据 (真实数据)
res = sk.recv(1024)
print(res.decode())

# 3
# 111
# world,hello

sk.close()



























