import hashlib
import socketserver
import json,os

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
	def register(cls,opt_dic):
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
	


class FTPServer(socketserver.BaseRequestHandler):
	def handle(self):
		opt_dic = self.myrecv()
		print(opt_dic)
		#{'user': 'wangwen', 'passwd': '222', 'operate': 'register'}
		
		# Auth.regisrer(opt_dic)  #类名调类方法
		
		# 判断Auth类中是否含有register成员  #反射  字符串反射成员
		if hasattr(Auth,'register'):
			register = getattr(Auth,'register') # 反射方法
			print(register)  
			# <bound method Auth.register of <class '__main__.Auth'>>
			
			res = register(opt_dic) #执行方法
			print(res)
			#{'result': False, 'info': '用户名已经存在'}
			
			self.mysend(res)  #发送注册状态
			
			
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
		
	def mysend(self,send_info):
		str_dic = json.dumps(send_info)  #dic ==> str
		bytes1 = str_dic.encode()  # str ==> bytes
		conn = self.request	
		conn.send(bytes1)
	

ftpserver = socketserver.ThreadingTCPServer(("127.0.0.1",9001),FTPServer)
ftpserver.serve_forever()


































