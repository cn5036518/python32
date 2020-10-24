# ### 客户端
import socket
import json

# pickle => 字节流( 存储数据 )
# json   => 字符串( 数据交互 )

sk = socket.socket()
sk.connect(("127.0.0.1" , 9000))

# 处理收发数据的逻辑
# 1 用户输入用户名和密码.通过字典-json(转str 转bytes),发送给服务端
user = input('请输入用户名:')
pwd = input('请输入密码:')
dic = {'user':user,'pwd':pwd,'operate':'login'}

strvar = json.dumps(dic)
bytes1 = strvar.encode()

sk.send(bytes1)

# 5 接受服务端发来的校验结果
strvar = sk.recv(1024).decode()
# if res == 'True':
	# print('登录成功')
# elif res == 'False':
	# print('登录失败')
# else:
	# print('其他')
	
dic = json.load(strvar)
print(dic)
print(dic['msg'])


sk.close()
























































