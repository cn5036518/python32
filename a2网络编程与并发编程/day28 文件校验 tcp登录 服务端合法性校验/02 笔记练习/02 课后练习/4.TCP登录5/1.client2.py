# ### 客户端
import socket
import json

# pickle => 字节流( 存储数据 )
# json   => 字符串( 数据交互 )

sk = socket.socket()
sk.connect(("127.0.0.1" , 9000))

# 处理收发数据的逻辑
user = input('请输入用户名:')
pwd = input('请输入密码:')
dic = {'username':user,'password':pwd,'operate':'login'}

# 通过json,把字典变成字符串
strvar = json.dumps(dic)
print(strvar)

# 转化成字节流发送给服务端
sk.send(strvar.encode())

# 接受服务端响应的数据
strvar = sk.recv(1024).decode()
dic = json.loads(strvar)
print(dic)
# {'code':1,'msg':'登录成功'}
print(dic['msg'])

# 把字符串转化成字典
# if res == 'True':
	# print('登录成功')
# else:
	# print('登录失败')

sk.close()
























































