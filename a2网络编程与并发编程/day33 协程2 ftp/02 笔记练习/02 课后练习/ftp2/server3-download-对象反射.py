import hashlib
import socketserver
import json
import os,struct

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
			
	@classmethod
	def myexit(cls,opt_dic):
		dic5 = {"result":"myexit"}
		return dic5
		
		

class FTPServer(socketserver.BaseRequestHandler):
	def handle(self):
		opt_dic = self.myrecv()
		print(opt_dic)  #{'operate': 'myexit'}
		# {'operate': 'download', 'filename': 'studey_info1.mp4'}
		#{'user': 'wangwen', 'passwd': '111', 'operate': 'register'}
		
		# 判断Auth类中是否含有register成员 --类的反射
		if hasattr(Auth,opt_dic['operate']):
			func = getattr(Auth,opt_dic['operate']) # 方法的内存地址  # 反射方法
			res = func(opt_dic)  ##直接加小括号调用即可, # 执行方法
			# 不用obj.register(opt_dic) 不用Auth.register(opt_dic)
			print(res,type(res))  #{'result': 'myexit'}
			#{'result': False, 'info': '用户名存在'}
		
			if res['result'] == 'myexit':
				# 终止当前这个线程和客户端的连接
				return
		
			self.mysend(res)  # 发送状态
			
		# 通过download方法进行下载   对象的反射
		elif hasattr(self,opt_dic['operate']): #绑定方法的反射  也可以把self的反射改成cls的放在Auth中
			func = getattr(self,opt_dic['operate'])
			func(opt_dic)
		
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
		
	def mysend(self,send_info,sign=False):
		# 字符串
		send_str = json.dumps(send_info) # dict-->str
		# print(send_str,1)
		
		# 字节流
		send_info = send_str.encode()  # str-->bytes
		
		if sign == True: #防止黏包
			# 计算文件大小 (文件的大小就是字节的个数)
			res = struct.pack('i',len(send_info))
			conn = self.request
			conn.send(res)
			

		# 发送字节流
		conn = self.request
		conn.send(send_info)
		

		
	def download(self,opt_dic):
		# {'operate': 'download', 'filename': 'studey_info.mp4'}
		print(opt_dic)
		
		# 获取文件名
		filename = opt_dic['filename']
		
		# 要下载的文件绝对路径
		file_abs = os.path.join(base_path,'video',filename)
		print(file_abs)
		#/mnt/hgfs/ubuntu_gx/python32/a2网络编程与并发编程/day33 协程2 ftp/02 笔记练习/02 课后练习/ftp2/video/studey_info1.mp4
		
		# 判断文件是否存在,存在的情况下发数据
		if os.path.exists(file_abs):
			# 1.告诉用户,文件存在,可以操作
			dic = {'result':True,'info':'文件可以下载'}
			self.mysend(dic,sign= True)		
			
			# 2.把对应的文件名和文件大小发过去			
			# 文件的大小
			filesize = os.path.getsize(file_abs)
			dic = {'filename':filename,'filesize':filesize}
			print(dic)
			# {'filename': 'studey_info.mp4', 'filesize': 72274155}
			self.mysend(dic,sign= True)
			
			# 3.真实文件内容发送
			with open(file_abs,mode='rb') as fp:
				while filesize:
					content = fp.read(102400)
					self.request.send(content)
					filesize -= len(content)
				print('服务端传输完毕') #
				# 服务端发送,客户端必须同时接受才行.否则报错
				#BrokenPipeError: [Errno 32] Broken pipe
			
			
		else:
			dic = {'result':True,'info':'文件不存在'}
			self.mysend(dic,sign= True)
	
	
ftpserver = socketserver.ThreadingTCPServer(("127.0.0.1",9002),FTPServer)
ftpserver.serve_forever()
	

# 一 注册思路
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


# 二 登录思路
# client
# 1 用户输入用户名和密码
  # 构造成字典,发送给server

# server
# 2 接受数据
# 3 通过反射,调login方法
# 4 把用户输入的密文密码加密成密文,和用户名输入的用户名一起
     # 和用户名密码文件比对,相等就登录成功
	 # 否则,登录失败
# 5 把{'result':True,'info':'登录成功'}或者
      # {'result':True,'info':'登录失败'}字典发送给client

# 三 下载思路
# client
# 1 用户把要下载的请求	operate_dict = {"operate":"download","filename":"studey_info.mp4"	}
  # 构造成字典,发送给server
# 2 接受server发来的连续3个信息(2个字典,1个文件真实内容)
# 	字典1:文件存在,可以下载的通知
# 	字典2:文件名和文件大小 (单独新建一个下载文件夹)
# 	真实文件内容接收  wb模式
#
# # server
# 1 获取要下载的文件名,获取文件名的绝对路径,判断文件是个存在
#   如果存在,告诉用户client,文件存在,可以下载,构造字典发给client  (处理黏包--重点)
#   如果不存在,告诉用户client,文件不存在,无法下载
# 2 如果文件存在,把对应的文件名和文件大小,构造字典发给client  (处理黏包)
# 3 真实文件内容发送  rb模式

























