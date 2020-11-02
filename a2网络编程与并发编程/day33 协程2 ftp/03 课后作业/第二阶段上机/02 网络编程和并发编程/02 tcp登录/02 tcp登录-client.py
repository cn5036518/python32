import socket
import json

sk = socket.socket()
sk.connect(("127.0.0.1" , 9001))

# 处理收发数据的逻辑
usr = input('请输入您的用户名:')
pwd = input('请输入您的密码:')
dic = {'username':usr,'password':pwd,'operate':'login'}

res = json.dumps(dic)
sk.send(res.encode())

res_str = sk.recv(1024).decode()
dic = json.loads(res_str)
print(dic)
print(dic['msg'])



sk.close()













































