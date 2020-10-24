# ### 客户端
import socket
import json

# pickle => 字节流( 存储数据 )
# json   => 字符串( 数据交互 )

sk = socket.socket()
sk.connect(("127.0.0.1" , 9001))

# 处理收发数据的逻辑
# 1 用户输入用户名和密码.通过字典-json(dict-str-bytes),发送给服务端
user = input('请输入登录用户名:')
pwd = input('请输入登录密码:')
dic = {'username':user,'password':pwd,'operate':'login'}

strvar = json.dumps(dic)
bytes1 = strvar.encode()

sk.send(bytes1)

# 5 接受服务端发来的校验结果  bytes-str-dict
strvar = sk.recv(1024).decode()
dic = json.loads(strvar)
print(dic,type(dic))
#{'code': 1, 'msg': '登录成功'} <class 'dict'>


sk.close()
























































