import socket

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

sk.bind(("127.0.0.1" , 9000) )
sk.listen()

conn,addr = sk.accept()

# 5.收发数据的逻辑
# 接受数据
res = conn.recv(1024)
print(res)
print(res.decode())

# 发送数据
conn.send('好好学习'.encode())

conn.close()
sk.close()
print('-------------1')



# 1 创建socket对象
sk = socket.socket()

# 2 注册主机 
sk.bind(('127.0.0.1',9000))

# 3 监听
sk.listen()

# 4 三次握手
conn,addr = sk.accept()

# 5 收发数据
# 收数据
res1 = conn.recv(1024)
print(res1)
print(res1.decode()) # bytes转str

# 发送数据
conn.send('你好'.encode())


# 6 四次挥手
conn.close()

# 7 退回端口
sk.close()
print('-------------2')

#默写3
# tcp server 7步
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
res = conn.recv(1024)  #参数是字节
print(res)
print(res.decode()) #bytes转str

# 发送数据
conn.send('你好'.encode())  #str转bytes


# 6 四次挥手
conn.close()

# 7 退回端口
sk.close()
print('-------------3')

# 默写4
# tcp server 7步
import socket

# 1 新建socket对象
sk = socket.socket()

# 2 注册主机
sk.bind(('127.0.0.1',9000))

# 3 监听
sk.listen()

# 4 三次握手
conn,addr = sk.accept()

# 5 收发数据
# 接收数据
res = conn.recv(1024)
print(res)
print(res.decode()) # bytes转str


# 发送数据
conn.send('你好'.encode()) #str 转bytes


# 6 四次挥手
conn.close()

# 7 退回端口
sk.close()
print('-------------4')



































































