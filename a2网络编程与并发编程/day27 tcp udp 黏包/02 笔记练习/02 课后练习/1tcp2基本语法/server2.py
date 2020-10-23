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
sk.bind(("127.0.0.1" , 9000))  #一个元组参数 不能是2个参数
# sk.bind(("localhost" , 9000))
# sk.bind(("192.168.235.128" , 9000))

# 3.开启监听
sk.listen()

# 4.三次握手
conn,addr = sk.accept()  #

# 5.收发数据的逻辑

# 接受数据
res = conn.recv(1024)
print(res)
#b'\xe4\xbb\x8a\xe5\xa4\xa9\xe6\x88\x91\xe4\xbb\xac\xe5
# \xad\xa6\xe4\xb9\xa0\xe7\xbd\x91\xe7\xbb\x9c\xe7\xbc\x96\xe7\xa8\x8b'
print(res.decode()) #把字节流bytes(b开头)转换成字符串
#今天我们学习网络编程


# 发送数据
conn.send('好好学习,天天向上'.encode())  #把字符串变成字节流传输

# 6.四次挥手
conn.close()

# 7.退还端口
sk.close()










































