# tcp server 7步  默写1
import socket

# 1 新建socket对象
sk = socket.socket()

# 2 注册主机
sk.bind(('127.0.0.1',9000)) #元组

# 3 监听
sk.listen()

# 4 三次握手
conn,addr = sk.accept()

# 5 收发数据
# 接收数据
res = conn.recv(1024)
print(res)
print(res.decode()) # bytes转str
# b'\xe4\xbd\xa0\xe5\xa5\xbd,\xe6\x88\x91\xe6\x98\xafclient'
# 你好,我是client

# 发送数据
conn.send('你好.我是server'.encode()) #str转bytes


# 6 四次挥手
conn.close()


# 7 退换端口
sk.close()























