# ### 客户端
import socket

# 1.创建一个socket对象
sk = socket.socket()

# 2.与服务端建立连接
sk.connect(("127.0.0.1" , 9000))  #一个元组参数 不能是2个参数
# sk.connect(("localhost" , 9000))
# sk.connect(("192.168.235.128" , 9000))

# 3.收发数据的逻辑
# """发送的数据类型是二进制字节流"""
# """b开头的字符串是二进制字节流格式,要求字符类型必须是ascii编码"""
sk.send('今天我们学习网络编程'.encode())

# 接受数据
res = sk.recv(1024)
print(res.decode())
#好好学习,天天向上

# 4.关闭连接
sk.close()


























