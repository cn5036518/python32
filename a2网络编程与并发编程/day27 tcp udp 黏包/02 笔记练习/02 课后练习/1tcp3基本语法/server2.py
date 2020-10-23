# ### socket 服务端

# 一发一收是一对,否则会导致数据异常
# send 发送 recv 接受

import socket

# 1.创建一个socket对象
sk = socket.socket()

# 一个端口绑定多个程序(仅在测试时使用,偶尔会失效,修改端口即可)
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 2.在网络中注册该主机(绑定对应的ip和端口号)
# """ 默认本地ip : 127.0.0.1  => localhost """
sk.bind(("127.0.0.1" , 9000))

# 3.开启监听
sk.listen()

# 4.三次握手
conn,addr = sk.accept()
print(conn)
# <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0,
 # laddr=('127.0.0.1', 9000), raddr=('127.0.0.1', 49918)>
print(addr)  
#('127.0.0.1', 49918)

# 5.收发数据的逻辑

# 接受数据
res = conn.recv(1024)  #接受到的是字节流
print(res)
#b'\xe4\xbb\x8a\xe5\xa4\xa9\xe6\x88\x91\xe4\xbb\xac\xe5\xad\xa6\xe4\xb9\xa0\xe7\xbd\x91\xe7\xbb\x9c\xe7\xbc\x96\xe7\xa8\x8b'
print(res.decode())
#今天我们学习网络编程

# 发送数据

# 6.四次挥手
conn.close()

# 7.退还端口
sk.close()












































