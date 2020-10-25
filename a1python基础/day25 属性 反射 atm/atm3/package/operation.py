import os
import pickle  #json不能存储对象
import random
import re

# from .card import Card     #相对路径的导包
# from .person import Person

class Operation():
	def __init__(self): #每次新建对象都会加载文件到字典
		# 加载user.txt 文件数据
		self.load_user()   #卡号:用户对象
		
		# 加载userid.txt 文件数据
		self.load_userid()  #身份证号:卡号

	# 加载user.txt文件数据
	def load_user(self):
		if os.path.exists('user.txt'):
			with open('user.txt',mode='rb') as fp: #存了用户对象,rb模式
				self.user_dict = pickle.load(fp)
				# 把bytes从文件中读出来,转成字典
		else:
			#设置空字典
			self.user_dict = {}
		print(self.user_dict)
		
	# 加载userid.txt文件数据
	def load_userid(self):
		if os.path.exists('userid.txt'):
			with open('userid.txt',mode='rb') as fp:
				self.user_id_dict = pickle.load(fp)
		else:
			#设置空字典
			self.user_id_dict = {}
		print(self.user_id_dict)
		
	

	# 0保存退出
	def save(self):
		#存储user_dict 字典
		with open('user.txt',mode='wb') as fp: #清空重写
			pickle.dump(self.user_dict,fp)
			# 把字典转成bytes,存到文件中
	
		#存储user_id_dict 字典
		with open('userid.txt',mode='wb') as fp:
			pickle.dump(self.user_id_dict,fp)

	# 1开户注册
	def register(self):
		# 获取用户名
		# name = input('请输入姓名:')
		name = self.get_name()
		
		# 获取身份证号
		# userid = input('请输入身份证号:')
		userid = self.get_userid()
		
		# 获取手机号
		# phone = input('请输入您的手机号:')
		phone = self.get_phone()
		
		## 获取密码-卡取款密码
		password = self.get_pwd('请输入您的卡取款密码:','请确认您的卡取款密码:')
		
		
		
	def get_name(self):
		while True:
			name = input('请输入姓名:')
			if name == '' or ' ' in name:
				print('姓名不能为空')
			elif not name.isalpha():
				print('姓名不是中文或字母')
			elif name.isalpha():
				return name
	
	def get_userid(self):
		while True:
			userid = input('请输入身份证号:')
			lst = re.findall(r'^\d{6}[12]\d{}3[01]\d[0123]\d\d{3}[\dX]$',userid)
			if lst:
				return userid
			else:
				print('身份证号码格式不符合要求')

	def get_phone(self):
		while True:
			phone = input('请输入您的手机号:')
			lst = re.findall(r'^1[3-9]\d{9}$',phone)
			if lst:
				return phone
			else:
				print('手机号格式不符合要求')

	# 1-1获取密码
	def get_pwd(self,name1,name2):
		while True:
			pwd1 = input(name1)
			pwd2 = input(name2)
			# 密码长度6位不能空,字母数字下划线 \w (纯数字的密码不允许的)
			lst = re.findall(r'^\w{6}$',pwd1)
			if lst and not pwd1.isdecimal():
				if pwd1 == pwd2:
					return pwd1
				else:
					print('两次密码不一致,请重新输入')
			else:
				print('密码长度6位不能空,字母数字下划线 \w (纯数字的密码不允许的)')





























