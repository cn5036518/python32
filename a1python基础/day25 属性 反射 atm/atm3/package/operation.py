import os
import pickle  #json不能存储对象
import random
import re

# 思路
# 1修改对象属性
# 2把修改后的对象存储到字典
# 3把字典清空写入文件--save保存退出
# 4新建operation对象的时候,读取文件到字典(放init 构造方法中)

from .card import Card     #相对路径的导包
from .person import Person

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
		# 一 用户对象的信息
		# 获取用户名
		# name = input('请输入姓名:')
		name = self.get_name()
		
		# 获取身份证号
		# userid = input('请输入身份证号:')
		userid = self.get_userid()
		
		# 获取手机号
		# phone = input('请输入您的手机号:')
		phone = self.get_phone()
		
		# 二 卡对象的信息
		## 获取密码-卡取款密码
		password = self.get_pwd('请输入您的卡取款密码:','请确认您的卡取款密码:')
		
		# 获取卡号
		cardid = self.get_cardid()
		
		# 卡内默认余额 10元
		money = 10  #也可以在卡对象的构造方法中定义
		
		#  三 创建对象(卡和用户)
		# 创建一张卡的对象
		card = Card(cardid,password,money)
		
		# 创建一个用户的对象
		user = Person(name,userid,phone,card)  #card是卡对象 关键点1
		
		#  四 存储数据到字典  (把用户对象存入字典)
		# 存储数据到 user_dict    卡号:用户对象  cardid:user  
		# 把卡号和用户对象绑定
		self.user_dict[cardid] = user
		
		# 存储数据到 user_id_dict 身份证号:卡号  userid:cardid
		# 把身份证号和卡号绑定
		self.user_id_dict[userid] = cardid
		
		# 打印卡的基本信息(卡的用户姓名,卡号,卡余额)
		print('恭喜{}开卡成功,您的卡号为:{},卡内余额{}元'.format(name,cardid,money))
		
		
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
			lst = re.findall(r'^\d{6}[12]\d{3}[01]\d[0123]\d\d{3}[\dX]$',userid)
			# lst = re.findall(r'^\d{6}[12]\d{3}[01]\d{1}[0123]\d{1}\d{3}[\dX]$',userid)
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

	# 1-2 获取卡号  6位随机卡号
	def get_cardid(self):
		while True:
			cardid = str(random.randrange(100000,1000000))
			# 字典的键推荐用字符串
			# user.txt   => {卡号:用户对象} {"555666": 用户对象}   
			# =>  user_dict
			if cardid not in self.user_dict:
			# 卡号不能相同
				return cardid  #死循环的终止条件

	# 2 查询   卡余额和卡的锁定状态
	def query(self):
		# 1.获取这张卡的相关信息
		card = self.get_card_info()  #获取卡的对象
		if not card:
			print('您的这张卡不存在')
		else:
			if card.islock:  #卡对象.锁定属性
				print('你的卡已经被锁了')
			else:
				if self.check_pwd(card):
					# 显示卡内余额
					print('您的卡内余额是{}元'.format(card.money))
					if card.islock:
						print('卡的锁定状态是{}'.format('已锁定'))
					else:
						print('卡的锁定状态是{}'.format('未锁定'))
				


	# 2-1 卡的信息   获取卡对象
	def get_card_info(self):
		cardid = input('请输入您的卡号:')
		if cardid not in self.user_dict:
			return False
		else:
			# 通过卡号 -> 用户对象 -->卡对象-->卡的cardid属性
			user = self.user_dict[cardid] #用户对象
			return user.card   #获取卡对象

	# 2-2 校验卡的密码 3次锁定  self.islock变成True
	def check_pwd(self,card): #参数card是卡对象
		times = 0
		for i in range(3):
			pwd = input('请输入您的密码:')
			if pwd == card.password:
				return True
			else:
				#剩余次数 = 总次数 - 使用次数
				print('密码错误~ , 您还剩下{}次机会'.format(2-times))
				if times == 3:
					card.islock = True  #锁定状态 锁卡的动作
					print('抱歉,密码输错三次,卡被锁定,请联系管理员.')
			times += 1




















































