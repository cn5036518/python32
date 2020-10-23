# udp server 4步 
import socket

# 1 新建socket对象
sk = socket.socket(type = socket.SOCK_DGRAM)

# 2 注册主机
sk.bind(('127.0.0.1',9000)) #元组

# 3 收发数据  先收后发  
# 收
msg,addr = sk.recvfrom(1024)
print(msg)
print(msg.decode())
# b'\xe6\x88\x91\xe6\x98\xafudp client'
# 我是udp client

# 发
sk.sendto('我是udp server'.encode(),addr)

# 4 关闭连接
sk.close()
































