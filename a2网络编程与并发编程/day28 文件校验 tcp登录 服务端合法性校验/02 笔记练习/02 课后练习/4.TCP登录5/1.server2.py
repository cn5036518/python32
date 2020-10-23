# ### 服务端
from collections import Iterator,Iterable
import socketserver
import hashlib
import json

class MyServer(socketserver.BaseRequestHandler):
	# 默认没有登录
	sign = False
	
	def get_md5_code(self,usr,pwd):
		hs = hashlib.md5(usr.encode())
		hs.update(pwd.encode())
		return hs.hexdigest()
		
	def auth(self):
		conn = self.request
		
		# 接受客户端发送过来的数据(字节流),通过decode反解成字符串
		strvar = conn.recv(1024).decode()
		
		# 通过json把字符串 转换成 字典
		dic = json.loads(strvar)
		print(dic,type(dic))

		# {'username': 'caijingguan', 'password': '8888', 'operate': 'login'} 
		
		with open("userinfo.data",mode="r",encoding="utf-8") as fp:
			for i in fp:
				user,pwd = i.strip().split(':')
				if user == dic['username'] and pwd == self.get_md5_code(dic['username'],dic['password']):
					# print('登录成功')
					self.sign = True
					return True
					
			# 没有找到对应合法的用户名和密码,登录失败
			# if self.sign == False:
			else:
				return False	
		
	def handle(self):
		if self.auth():
			print('登录成功')
			dic = {'code':1,'msg':'登录成功'}
			# strvar = json.dumps(dic)
			# self.request.send(strvar.encode())
		else:
			print('登录失败')
			dic = {'code':0,'msg':'登录失败'}
		strvar = json.dumps(dic)
		self.request.send(strvar.encode())
		
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

# 二 客户端
# 1 用户输入用户名和密码.通过字典-json,发送给服务端


# 三 文件
# wangwen:加密串





































