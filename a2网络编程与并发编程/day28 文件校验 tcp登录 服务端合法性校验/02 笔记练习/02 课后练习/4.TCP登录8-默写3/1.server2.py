# ### 服务端
from collections import Iterator,Iterable
import socketserver
import hashlib
import json

class MyServer(socketserver.BaseRequestHandler):

	def get_pwd(self,user,pwd):
		hs = hashlib.md5(user.encode())  #参数是bytes
		hs.update(pwd.encode())  #参数是bytes
		res = hs.hexdigest()  #获取十六进制的字符串
		# AttributeError: '_hashlib.HASH' object has no attribute 'hexdegist'
		# print(res)
		return res
	
		
	def auth(self):
		# 2 收到字符串后,json转成字典
		conn = self.request
		strvar = conn.recv(1024).decode()
		
		dic = json.loads(strvar)
		print(dic,type(dic))
		# {'user': 'wangwen', 'pwd': '111', 'operate': 'login'} <class 'dict'>
		
		# 3 拿用户名做key  md5加密算法(加盐)  将用户的明文密码加密成密文
		pwd_mi = self.get_pwd(dic['user'],dic['pwd'])
		# print(pwd_mi)
		
		# 4 用户输入的明文密码转换成的密码密文和文件的密文对比,用户输入的用户名和和文件中的用户名对比
		with open('userinfo.data',mode='r',encoding= 'utf-8') as fp:
			for i in fp:
				user,pwd = i.strip().split(':')
				if dic['user'] == user and pwd_mi == pwd:					
					return True
					
			else:				
				return False		
		
		
	def handle(self):
		if self.auth():
			print('登录成功')
			# self.request.send('True'.encode)
			# TypeError: a bytes-like object is required, not 'builtin_function_or_method'
			dic = {'code':1,'msg':'登录成功'}			
			# self.request.send('True'.encode())		
		else:
			print('登录失败')
			dic = {'code':0,'msg':'登录失败'}
			# self.request.send('False'.encode())
		strvar = json.dumps(dic)  #dict转str
		bytes1 = strvar.decode()  #str 转bytes
		self.request.send(bytes1)
		
server = socketserver.ThreadingTCPServer(("127.0.0.1" , 9000),MyServer)
# 开启,让一个端口绑定多个程序;  模块.类.属性 = True
socketserver.TCPServer.allow_reuse_address = True
server.serve_forever()


# """
# 课后作业: 完成FTP服务器
# (1) 登录 (2) 注册 (3) 上传 (4) 下载
# """

# 思路
# 一 服务端
# 2 收到字符串后,json转成字典
# 3 拿用户名做key  hmac加密算法  将用户的明文密码加密成密文
# 4 密文和文件的密文对比
  # 一致,登录成功
  # 不一致,登录失败
# 5 将校验结果发给客户端
#   1 字符串 True
#   2 dict

# 二 客户端
# 1 用户输入用户名和密码.通过字典-json,发送给服务端
# 5 接受服务端发来的校验结果


# 三 文件
# wangwen:加密串





































