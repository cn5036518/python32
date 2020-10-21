# ### 操作类 operation
import os
import pickle
import random

from .card import Card  
    #单入口模式的相对路径导包  必须从单入口文件执行,不能从当前文件执行
from .person import Person

class Operation():
	def __init__(self):
	
		# 加载user.txt文件数据   {卡号:用户对象}  user_dict
		self.load_user()
		
		# 加载userid.txt文件数据  (身份证号:卡号)  user_id_dict
		self.load_userid()

	# 1 开户注册
	def register():
		pass
		
	# 2 查询    卡余额 锁定状态
	def query():
		pass
		
	
	# 0-1 加载user.txt文件数据
	def load_user(self):
		if os.path.exists(r'user.txt'):
			with open(r'user.txt',mode='rb') as fp:
				self.user_dict = pickle.load(fp)
				# 把字节流转成字典
		else:
			# 设置空字典属性
			self.user_dict = {}
			
		print(self.user_dict)	#{}
		
	# 0-2 加载userid.txt文件数据
	def load_userid(self):
		if os.path.exists(r'userid.txt'):
			with open(r'userid.txt',mode='rb') as fp:
				self.user_id_dict = pickle.load(fp)
		else:
			# 设置空字典属性
			self.user_id_dict = {}
			
		print(self.user_id_dict)
	
	
	# 0 保存退出
	def save(self):
		# 存储user_dict 字典
		with open(r'user.txt',mode='wb') as fp:
			pickle.dump(self.user_dict,fp)
			# 第一次会把空字典转成字节流bytes 写入到文件 ,新建文件user.txt

		# 存储user_id_dict 字典
		with open(r'userid.txt',mode='wb') as fp:
			pickle.dump(self.user_id_dict,fp)

	# 1 注册用户
	def register(self):
		# 一 用户信息
		# 1获取用户-姓名
		name = input('请输入您的姓名:')
		
		# 2获取用户-身份证号
		userid = input('请输入您的身份证号:')
		
		# 3获取用户-手机号
		phone = input('请输入您的手机号:')
		
		# 二 卡信息
		# 1获取卡号
		cardid = self.get_cardid()
		
		# 2获取卡余额  卡内默认余额 10元  也可以写在卡的init中
		money = 10
		
		# 3获取卡取款密码
		password = self.get_pwd('请输入您的密码:','请确认您的密码:')
		
		# 三 创建对象
		# 1创建一张卡对象
		card = Card(cardid,password,money)
		
		# 2创建一个用户对象
		user = Person(name,userid,phone,card)  #card是对象
		
		# 四 存储数据到文件
		# 1存储数据到 user_dict    卡号:用户对象
		self.user_dict[cardid] = user   #user是对象
		# 0把用户对象存入到字典中
		# 1用户对象可以获取用户的属性和card对象
		# 2card对象可以获取card的属性
		
		# 2存储数据到 user_id_dict 身份证号:卡号
		self.user_id_dict[userid] = cardid
		
		print('恭喜{}开卡成功,您的卡号为:{},卡内余额{}元'
		.format(name,cardid,money))
		
		
	
	#1-1 获取卡取款密码
	def get_pwd(self,name1,name2):
		while True:
			pwd1 = input(name1)
			pwd2 = input(name2)
			if pwd1 == pwd2:
				return pwd1
			else:
				print('两次密码不一致,请重新输入')
		
	#1-2 获取卡号  #卡号6位随机数字的字符串
	def get_cardid(self):
		while True:
			cardid = str(random.randrange(100000,1000000))
			if cardid not in self.user_dict:
				return cardid

	#2 查询  根据卡号,查询卡的余额和锁定状态
	def query(self):
		# 1.获取这张卡对象的相关信息
		card = self.get_card_info()
		if not card:
			print('抱歉,您的这张卡不存在,未注册')
		else:
			if card.islock:  #
				print('抱歉,您的卡已经被锁了')
			else:
				if self.check_pwd(card): #取款密码校验通过
					# 显示卡内余额和锁定状态
					print('您的卡内余额是{}元'.format(card.money))
					if card.islock:
						print('您的卡的状态是{}'.format('锁定'))
					else:
						print('您的卡的状态是{}'.format('未锁定'))
		
		
	#2-1 获取卡对象的信息(属性)  密码 余额 锁定状态
	def get_card_info(self):
		cardid = input('请输入您的卡号:')
		if cardid not in self.user_dict:
			return False
		else:
			# 通过卡号 -> 用户对象
			user = self.user_dict[cardid] #获取用户对象
			return user.card  #获取card对象

	#2-2 查询的时候,需要输入校验取款密码
	def check_pwd(self,card): #参数是卡的对象
		times = 1
		for i in range(3):
			pwd = input('请输入您的密码:')
			if pwd == card.password:
				return True
			else:
				#剩余次数 = 总次数 - 使用次数
				print('密码错误~ , 您还剩下{}次机会'.format(3-times))
				if times == 3:
					card.islock = True  # 修改卡对象的属性
					# 卡对象的属性修改了,卡对象就修改了,self.user_dict这个字典就修改了
					# self.user_dict这个字典写入文件user.txt后,文件就修改了
					# user.txt文件数据   {卡号:用户对象}  user_dict
					
					# 下次读取文件后,读取字典,读取到的卡对象的属性是修改后的
					print('抱歉,密码输错三次,卡被锁定,请联系管理员.')			
			times += 1

































