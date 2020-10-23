# udp client 3步
import socket

# 1 新建socket对象
sk = socket.socket(type = socket.SOCK_DGRAM)

# 2 收发数据 先发后收
sk.sendto('我是udp client'.encode(),('127.0.0.1',9000))

msg,addr = sk.recvfrom(1024)
print(msg)
print(msg.decode())
# b'\xe6\x88\x91\xe6\x98\xafudp server'
# 我是udp server

# 3 关闭连接
sk.close()






















