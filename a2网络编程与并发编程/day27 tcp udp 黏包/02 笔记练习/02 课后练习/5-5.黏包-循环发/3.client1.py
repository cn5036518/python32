# ### 客户端
import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1",9001) )

time.sleep(2)
# 收发数据的逻辑
# 第一步,先接受接下来要发送的数据的总大小
# res = sk.recv(7)  #接受7个字节 '0000018'对应7个字节
res = sk.recv(2)  #接受7个字节 '0000018'对应7个字节
num = int(res.decode()) #18  int

# 第二部,在接受真实的数据内容
res1 = sk.recv(num) #18
print(res1.decode(),'--------------1')
res2 = sk.recv(1024)
print(res2.decode(),'-------------2')

# world,world,world, --------------1
# hello -------------2

sk.close()






































