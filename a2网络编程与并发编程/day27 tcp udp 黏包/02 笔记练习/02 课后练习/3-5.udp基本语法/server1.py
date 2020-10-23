# udp server 4步
import socket

# 1 新建socket对象
sk = socket.socket(type=socket.SOCK_DGRAM)

# 2 注册主机
sk.bind(('127.0.0.1',9000)) #元组

# 3 收发数据  默认第一只只能接收数据,没有三次握手,不知道对方的ip
# 接收数据
msg,addr = sk.recvfrom(1024)
print(msg)
print(msg.decode())
print(addr)

# 发送数据
sk.sendto('我是服务端,udp'.encode(),addr)


# 4 关闭连接
sk.close()
print('------------------------1')


























































