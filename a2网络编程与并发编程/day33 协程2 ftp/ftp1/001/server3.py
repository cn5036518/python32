import hashlib
import socketserver
import json,os,struct

# print(__file__)
# #/mnt/hgfs/ubuntu_gx/python32/a2网络编程与并发编程/day33 协程2 ftp/ftp1/server1.py
#
# print(os.getcwd())
# # /mnt/hgfs/ubuntu_gx/python32/a2网络编程与并发编程/day33 协程2 ftp/ftp1
#
# print(os.path.dirname(__file__))
# # /mnt/hgfs/ubuntu_gx/python32/a2网络编程与并发编程/day33 协程2 ftp/ftp1

base_path = os.path.dirname(__file__)
userinfo = os.path.join(base_path,'db','userinfo.txt')
# print(userinfo)
#/mnt/hgfs/ubuntu_gx/python32/a2网络编程与并发编程/day33 协程2 ftp/ftp1/db/userinfo.txt

class Auth():
	@staticmethod   #类和对象都可以调,不会额外传递类或者对象
	def md5(usr,pwd):
		hs = hashlib.md5(usr.encode())
		hs.update(pwd.encode())
		return hs.hexdigest()		
		
	@classmethod   #类方法 自动把类传入
	def register(cls,opt_dic):   #注册
		# {'user': 'wangwen', 'passwd': '111', 'operate': 'register'}
		# 1.检测注册用户名是否存在
		with open(userinfo,mode='r',encoding='utf-8') as fp:
			for line in fp:
				username = line.strip().split(':')[0]
				if opt_dic['user'] == username:
					# 失败结果
					dic1 = {'result':False,'info':'用户名已经存在'}
					return dic1		#函数终止	
	
		# 2.当前用户可以注册
		with open(userinfo,mode='a+',encoding='utf-8') as fp:
			user = opt_dic['user']
			pwd_mi = cls.md5(opt_dic['user'],opt_dic['passwd']) #类方法
			strvar = '{}:{}{}'.format(user,pwd_mi,'\n')
			print(strvar) #jack:e850e9ed98871dd9deed15889e29d705
			fp.write(strvar)			
		
		# 成功注册
			dic2 = {'result':True,'info':'注册成功'}
			return dic2
			
	@classmethod
	def login(cls,opt_dic):  #2 登录
		# 打开文件检测账号密码是否一致,如果成功直接返回,终止函数
		with open(userinfo,mode='r',encoding='utf-8') as fp:
			for i in fp:
				username,password = i.strip().split(':')
				user = opt_dic['user']
				pwd_mi = cls.md5(opt_dic['user'],opt_dic['passwd']) #类方法
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
		print(opt_dic)
		#{'user': 'wangwen', 'passwd': '222', 'operate': 'register'}
		
		# Auth.regisrer(opt_dic)  #类名调类方法
		
		# 判断Auth类中是否含有register成员  #反射  字符串反射成员
		# if hasattr(Auth,'register'):
		if hasattr(Auth,opt_dic['operate']):
			# register = getattr(Auth,'register') # 反射方法
			func = getattr(Auth,opt_dic['operate']) # 反射方法
			# print(register)  
			# <bound method Auth.register of <class '__main__.Auth'>>
			
			res = func(opt_dic) #执行方法
			print(res)
			#{'result': False, 'info': '用户名已经存在'}
			
			if res['result'] == 'myexit':
				# 终止当前这个线程和客户端的连接
				return
			
			self.mysend(res)  #发送注册/登录状态	
			# res = {'result': True, 'info': '登录成功'}
			
			if res['result']:
				while True:
					opt_dic = self.myrecv()
					print(opt_dic)
					#{'operate': 'download', 'filename': 'study_into1.mp4'}
					
					# 如果接受的数据是myexit , 直接退出,终止连接
					if opt_dic['operate'] == 'myexit':
						return
						
					# 通过download方法进行下载
					if hasattr(self,opt_dic['operate']):  #反射
						# download()  upload() ...
						func = getattr(self,opt_dic['operate'])
						func(opt_dic)
					
			
		else:
			dic = {'result':False,'info':'类中没有该成员,没有该操作'}
			# 发送状态
			self.mysend(dic)
		
	def myrecv(self):	
		# 字节流
		conn = self.request		
		opt_bytes = conn.recv(1024)
		
		# 字典
		opt_dic = json.loads(opt_bytes.decode())
		return opt_dic	
		
	def mysend(self,send_info,sign = False):
		str_dic = json.dumps(send_info)  #dic ==> str
		bytes1 = str_dic.encode()  # str ==> bytes
		conn = self.request

		if sign == True:  #避免黏包
			# 计算大小 (文件的大小就是字节的个数)
			res = struct.pack('i',len(send_info))
			conn.send(res)  #01 发送内容的长度
			
		conn.send(bytes1)  # 02 发送内容
		
	def download(self,opt_dic):
		#{'operate': 'download', 'filename': 'studey_info1.mp4'}
		print(opt_dic)
		
		# 获取文件名
		filename = opt_dic['filename']
		
		# 要下载的文件绝对路径
		file_abs = os.path.join(base_path,'video',filename)
		print(file_abs)
		#/mnt/hgfs/ubuntu_gx/python32/a2网络编程与并发编程/day33 协程2 ftp/ftp1/video/study_into1.mp4
	
		# 判断文件是否存在,存在的情况下发数据
		if os.path.exists(file_abs):
			# 1.告诉用户,文件存在,可以操作
			dic = {'result': True, 'info': '文件可以下载'}
			self.mysend(dic,sign=True)  #避免黏包
			
			# 2.把对应的文件名和文件大小发过去
			# 文件的大小
			filesize = os.path.getsize(file_abs)
			dic = {'filename':filename,'filesize':filesize}
			self.mysend(dic,sign=True)  #避免黏包
			
			# 3.真实文件内容发送
			with open(file_abs,mode='rb') as fp:
				while filesize:
					content = fp.read(1024000)
					self.request.send(content)
					filesize -= len(content)
			print('服务端传输完毕')
			
			
		else:
			# 额外增加功能
			dic = {'result': True, 'info': '文件不存在'}
			self.mysend(dic,sign=True)
		

ftpserver = socketserver.ThreadingTCPServer(("127.0.0.1",9000),FTPServer)
ftpserver.serve_forever()


































