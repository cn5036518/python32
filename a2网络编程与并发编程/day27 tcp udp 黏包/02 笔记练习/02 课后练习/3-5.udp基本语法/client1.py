# udp client 3步

import socket

# 1 新建socket对象
sk = socket.socket(type = socket.SOCK_DGRAM)

# 2 收发数据  先发后收
# 发送数据
sk.sendto('你好,我是udp client'.encode(),('127.0.0.1',9000))

# 接收数据
msg,addr = sk.recvfrom(1024)
print(msg)
print(msg.decode())
print(addr)

# 3 关闭连接
sk.close()























