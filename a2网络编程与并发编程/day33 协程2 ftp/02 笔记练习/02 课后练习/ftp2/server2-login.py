import hashlib
import socketserver
import json
import os

# print(__file__) #当前文件的全路径
# /mnt/hgfs/ubuntu_gx/python32/a2网络编程与并发编程/day33 协程2 ftp/02 笔记练习/02 课后练习/ftp2/server1.py

# print(os.getcwd())  #当前文件所在目录的绝对路径
# /mnt/hgfs/ubuntu_gx/python32/a2网络编程与并发编程/day33 协程2 ftp/02 笔记练习/02 课后练习/ftp2

print(os.path.dirname(__file__))
# /mnt/hgfs/ubuntu_gx/python32/a2网络编程与并发编程/day33 协程2 ftp/02 笔记练习/02 课后练习/ftp2

base_path = os.path.dirname(__file__)  #当前文件所在目录的绝对路径
userinfo = os.path.join(base_path,'db','userinfo.txt')

class Auth():
	@staticmethod
	def md5(usr,pwd):
		hs = hashlib.md5(usr.encode())  #盐是用户名的字节流
		hs.update(pwd.encode())
		return hs.hexdigest()
		
	@classmethod
	def register(cls,opt_dic):
		# {'user': 'wangwen', 'passwd': '111', 'operate': 'register'}
		# 1.检测注册用户名是否存在
		with open(userinfo,mode='r',encoding='utf-8') as fp:
			for i in fp:
				username = i.strip().split(':')[0]
				if opt_dic['user'] == username:
					# 失败结果
					dic1 = {'result':False,'info':'用户名存在'}
					return dic1
	
		# 2.当前用户可以注册
		with open(userinfo,mode='a+',encoding='utf-8') as fp:
			user = opt_dic['user']
			pwd_mi = cls.md5(user,opt_dic['passwd'])
			strvar = '{}:{}{}'.format(user,pwd_mi,'\n')
			fp.write(strvar)
			
			dic2 = {'result':True,'info':'注册成功了'}
			return dic2
			
	@classmethod
	def login(cls,opt_dic):
		# 打开文件检测账号密码是否一致,如果成功直接返回,终止函数
		with open(userinfo,mode='r',encoding='utf-8') as fp:
			for i in fp:
				username,password = i.strip().split(':')
				user = opt_dic['user']
				pwd_mi = cls.md5(user,opt_dic['passwd'])
				if user == username and pwd_mi == password:
					dic3 = {'result':True,'info':'登录成功'}
					return dic3
			dic4 = {'result':False,'info':'登录失败'}
			return dic4
		
		

class FTPServer(socketserver.BaseRequestHandler):
	def handle(self):
		opt_dic = self.myrecv()
		print(opt_dic)
		#{'user': 'wangwen', 'passwd': '111', 'operate': 'register'}
		
		# 判断Auth类中是否含有register成员 --反射
		if hasattr(Auth,opt_dic['operate']):
			func = getattr(Auth,opt_dic['operate']) # 方法的内存地址  # 反射方法
			res = func(opt_dic)  ##直接加小括号调用即可, # 执行方法
			# 不用obj.register(opt_dic) 不用Auth.register(opt_dic)
			print(res)
			#{'result': False, 'info': '用户名存在'}
			self.mysend(res)  # 发送状态
			
		else:
			dic1 = {'result':False,'info':'没有该操作'}
			# 发送状态
			self.mysend(dic1)
	
	
	def myrecv(self):
		conn = self.request
		
		# 接收字节流
		opt_bytes = conn.recv(1024)
		
		# 字符串
		opt_str = opt_bytes.decode()  #bytes-->str
		
		# 字典
		opt_dic = json.loads(opt_str)  #str-->dict
		
		return opt_dic		
		
	def mysend(self,send_info):
		# 字符串
		send_str = json.dumps(send_info) # dict-->str
		
		# 字节流
		send_info = send_str.encode()  # str-->bytes
		
		# 发送字节流
		conn = self.request
		conn.send(send_info)
		
	
	
ftpserver = socketserver.ThreadingTCPServer(("127.0.0.1",9001),FTPServer)
ftpserver.serve_forever()
	

# 注册思路
# client
# 1 用户输入用户名和密码
  # 构造成字典,发送给server
# 6 接收server端发送的字典
	# {'result': False, 'info': '用户名存在'}或
	# {'result':True,'info':'注册成功了'}

# server
# 2 接受数据
# 3 通过反射,调register方法
# 4 检测用户名是否已经存在,
	# 如果存在,将{'result': False, 'info': '用户名存在'}字典发送给client
	# 如果不存在
# 5 把用户输入的密文密码加密成密文,和用户名输入的用户名一起写入到userinfo文件
	# 把{'result':True,'info':'注册成功了'}字典发送给client

































