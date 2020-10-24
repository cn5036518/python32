# ### 服务端
from collections import Iterator,Iterable
import socketserver
import hashlib
import hmac
import json

class MyServer(socketserver.BaseRequestHandler):

	def get_pwd(self,user,pwd):
		hm = hmac.new(user.encode(),pwd.encode()) 
   		#参数1:key-盐-bytes 参数2:要加密的内容-bytes
		strvar = hm.hexdigest()
		print(strvar)  #32位字符串
		#49e00e36d304de871b64810697767a24
		return strvar	
		
	def auth(self):
		# 2 收到字节流后,先转字符串,再json转成字典
		conn = self.request
		
		strvar = conn.recv(1024).decode()
		dic = json.loads(strvar)
		print(dic,type(dic))
		#{'username': 'wangwen', 'password': '111', 'operate': 'login'} <class 'dict'>
		
		# 3 拿用户名做key  hmac md5 sha加密算法  将用户的明文密码加密成密文
		pwd_mi = self.get_pwd(dic['username'],dic['password'])
		
		# 4 用户输入的密码的密文和文件中密码的密文对比
		#   用户输入的用户名和文件中用户名对比
		with open('userinfo.data',mode='r',encoding='utf-8') as fp:
			for i in fp:
				user,pwd = i.strip().split(':')
				if dic['username'] == user and pwd_mi == pwd:
					print('登录成功')
					return True
			else:
				print('登录失败')
				return False	
		
		
	def handle(self):
		# 5 将校验结果发给客户端 dict-str-bytes
		if self.auth():
			dic = {'code':1,'msg':'登录成功'}			
		else:
			dic = {'code':0,'msg':'登录失败'}
		strvar = json.dumps(dic)
		bytes1 = strvar.encode()
		self.request.send(bytes1)
	
		
server = socketserver.ThreadingTCPServer(("127.0.0.1" , 9001),MyServer)
# 开启,让一个端口绑定多个程序;  模块.类.属性 = True
socketserver.TCPServer.allow_reuse_address = True
server.serve_forever()


# """
# 课后作业: 完成FTP服务器
# (1) 登录 (2) 注册 (3) 上传 (4) 下载
# """

# 思路
# 一 服务端
# 2 收到字节流后,先转字符串,再json转成字典
# 3 拿用户名做key  hmac md5 sha加密算法  将用户的明文密码加密成密文
# 4 用户输入的密码的密文和文件中密码的密文对比
#   用户输入的用户名和文件中用户名对比
  # 一致,登录成功
  # 不一致,登录失败
# 5 将校验结果发给客户端 dict-str-bytes
#   1 字符串 True
#   2 dict

# 二 客户端
# 1 用户输入用户名和密码.通过字典-json(dict-str-bytes),发送给服务端
# 5 接受服务端发来的校验结果 bytes-str-dict


# 三 文件
# wangwen:加密串





































