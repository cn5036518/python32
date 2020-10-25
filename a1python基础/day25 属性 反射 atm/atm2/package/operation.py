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

	# 3 存钱
	 # 卡是否存在,是否冻结,存钱金额是否正确
	 # 卡的金额增加  (修改卡对象的余额属性)
	# 卡号--用户对象--卡对象--卡余额属性
	def deposit(self):
		# 1.获取这张卡对象的相关信息
		card = self.get_card_info() #获取卡的对象
		amount = input('请输入你的存钱金额:') 
		if amount.isdecimal():
			amount = int(amount)
			if not card:
				print('您的这张卡不存在')
			else:
				if card.islock:#True是锁了 默认False 没锁
					print('你的卡已经被锁了')
				else:
					print('存款前,你的余额是{}元'.format(card.money))
					card.money += amount
					print('存款成功,你本次存入了{}元,存款后,你的余额是{}元'.format(amount,card.money))				
		else:
			print('请输入数字')
		
		# 4 取钱
	# 取钱:卡是否存在,是否冻结,取钱金额是否正确
	# 取款金额不能超过余额
	def withdraw(self):
		# 1.获取这张卡的相关信息
		card = self.get_card_info() #获取卡的对象
		amount = input('请输入你的取钱金额:')
		if amount.isdecimal():
			amount = int(amount)
			if not card:
				print('您的这张卡不存在')
			else:
				if card.islock:
					print('你的卡已经被锁了')
				else:
					if amount <= card.money:
						if self.check_pwd(card): #取款密码校验  self对象调用
							print('取款前,你的余额是{}元'.format(card.money))
							card.money -= amount
							print('取款成功,你本次取了{}元,取款后,你的余额是{}元'.format(amount,card.money))						
					else:
						print('余额不足')			
		else:
			print('请输入数字')

	# 5转账:把一个卡里的钱转到其他卡内 
# (卡是否存在,是否冻结,对方账户是否存在,转账的金额是否正确)	
	def transfer(self):
		print('转账方:')
		card1 = self.get_card_info()  #获取卡1的对象
		print('接收方:')
		card2 = self.get_card_info() #获取卡2的对象
		if card1 and card2:
			if not card1.islock and not card2.islock:
				if card1.cardid != card2.cardid:
					print('转账方和接受方的卡都存在,且未冻结,也没有给自己转账,可以发起转账')
					amount = input('请输入你的转账金额:')
					if amount.isdecimal():
						amount = int(amount)
						if amount <= card1.money:
							print('转账前,卡号1:{who1}的余额是{money1}元'.format(who1 = card1.cardid,money1 = card1.money))
							print('转账前,卡号2:{who2}的余额是{money2}元'.format(who2 = card2.cardid,money2 = card2.money))
							card1.money -= amount
							card2.money += amount
							print('转账成功,卡号1:{who1}本次给卡号2:{who2}转账了{amount1}元,转账后,卡号1:{who1}的余额是{money1}元,卡号2:{who2}的余额是{money2}元'.format(who1 = card1.cardid,who2 = card2.cardid,amount1 = amount,money1 = card1.money,money2 = card2.money))						
						else:
							print('你的转账金额超过了你的余额,不能转出')					
					else:
						print('请输入数字')		
				else:
					print('不能给自己转账')
			else:
				if card1.islock and card2.islock:
					print('转账双方的卡号都被冻结了')
				elif card1.islock:
					print('卡号{}被冻结了'.format(card1.cardid))
				elif card2.islock:
					print('卡号{}被冻结了'.format(card2.cardid))
		else:
			if not card1 and not card2:
				print('转账双方的卡号都不存在')
			elif not card1:
				print('卡号{}不存在'.format(card1.cardid))
			elif not card2:
				print('卡号{}不存在'.format(card2.cardid))

	#6 修改密码
	# 改密:(1)原密码改密  (2)身份证改密
	def change_pwd(self):
		# 1.获取这张卡的相关信息
		card = self.get_card_info()
		while True:
			content = input('修改密码,原密码改密按P,身份证改密按I,退出按Q:')
			if content.upper() == 'P':
				self.old_pwd(card)
				print('密码修改成功')
				break
			elif content.upper() == 'I':
				self.idcard_pwd(card)
				break
			elif content.upper() == 'Q':
				print('退出改密')
				break
			else:
				print('输入选项不对')

	def old_pwd(self,card):
		print('原密码改密')
		if not card:
			print('您的这张卡不存在')
		else:
			if card.islock:
				print('你的卡已经被锁了')
			else:
				while True:
					old_pwd1 = input('请输入你的原密码:')
					if old_pwd1 == card.password:
						new_pwd1 = input('请输入你的新密码:')
						new_pwd2 = input('请再次输入你的新密码:')
						if new_pwd1 == old_pwd1 or new_pwd2 == old_pwd1:
							print('新密码不能和原密码一样')
						else:
							if new_pwd1 == new_pwd2:
								print('密码修改成功')
								card.password = new_pwd1 #修改卡对象的密码
								break
							else:
								print('两次密码不一致,请重新输入')
						self.input_pwd()
					else:
						print('对不起密码不对,请重新输入')

	def idcard_pwd(self,card):
		print('身份证改密')
		if not card:
			print('您的这张卡不存在')
		else:
			if card.islock:
				print('你的卡已经被锁了')
			else:
				while True:
					userid1 = input('请输入你的身份证号:')
					if userid1 in self.user_id_dict:
						cardid = self.user_id_dict.get(userid1) #获取卡号
						# 身份证号==>卡号  字典2
						user = self.user_dict.get(cardid) #用户对象
						# 卡号==>用户对象  字典1
						if userid1 == user.userid:
							# self.input_pwd()	
							new_pwd1 = input('请输入你的新密码:')
							new_pwd2 = input('请再次输入你的新密码:')
							old_pwd1 = card.password #老卡的密码
							if new_pwd1 == old_pwd1 or new_pwd2 == old_pwd1:
								print('新密码不能和原密码一样')
							else:
								if new_pwd1 == new_pwd2:
									print('密码修改成功')
									card.password = new_pwd1 #修改卡对象的密码
									break  
									#SyntaxError: 'break' outside loop
									# return
								else:
									print('两次密码不一致,请重新输入')	
						else:
							print('对不起,身份证号不对,请重新输入')
					else:
						print('对不起,该身份证号未开户,请重新输入')

	# def input_pwd(self):
		# new_pwd1 = input('请输入你的新密码:')
		# new_pwd2 = input('请再次输入你的新密码:')
		# if new_pwd1 == old_pwd1 or new_pwd2 == old_pwd1:
			# print('新密码不能和原密码一样')
		# else:
			# if new_pwd1 == new_pwd2:
				# print('密码修改成功')
				# card.password = new_pwd1 #修改卡对象的密码
				# break  
				# SyntaxError: 'break' outside loop
				# return
			# else:
				# print('两次密码不一致,请重新输入')	

# 9补卡:将旧用户的所有信息和新卡绑定 即除了卡号变了.其余卡对象信息和用户对象信息都不变
# (包括名字,余额等所有卡信息和用户信息,数据重新绑定)[user_id_dict]
# 通过身份证 => 卡号  => 用户对象 	
	def supplment_card(self):
		print('补卡了')
		while True:
			userid1 = input('请输入你的身份证:')
			if userid1 in self.user_id_dict:
				cardid = self.user_id_dict.get(userid1)  ##获取老卡号
				# 身份证号 ==> 卡号
				user = self.user_dict.get(cardid) # 用户对象
				# 卡号 ==> 用户对象
				if userid1 == user.userid: #校验身份证
					old_pwd = user.card.password  #老卡的密码
					# 用户对象.卡对象.卡取款密码  
					old_money = user.card.money  #老卡的余额
					old_islock = user.card.islock  #老卡的锁定状态
					
					old_name = user.name   #老卡号所在用户的姓名
					old_userid = user.userid #老卡号所在用户的身份证
					old_phone = user.phone  # 老卡号所在用户的手机
					
					cardid11 = self.get_cardid() #获取新卡的卡号
					card11 = Card(cardid11,old_pwd,old_money)
					card11.islock = old_islock
					#新卡的对象
					
					user11 = Person(old_name,old_userid,old_phone,card11) #卡对象是参数4  重新绑定卡对象和用户对象
					#新卡所在的用户对象
					
					#将 新卡号的id:user11(用户对象)  作为键值对,添加到字典1
					self.user_dict[card11.cardid] = user11
					
					# 将 老卡号的id 从字典1删除   #删除老卡的cardid
					self.user_dict.pop(cardid)
					
					#将 老卡身份证和新卡号的id: 作为键值对,添加到字典2  
					# 修改老卡身份证和老卡号的id
					self.user_id_dict[old_userid] = card11.cardid
					print('补卡成功')
					print('新卡的卡号是{}'.format(card11.cardid))
					break
				else:
					print('对不起身份证不对,请重新输入')				
			else:
				print('对不起身份证未开户,请重新输入')












































