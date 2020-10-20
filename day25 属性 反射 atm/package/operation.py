import os
import pickle  #json不能存储对象
import random
import re

from .card import Card
from .person import Person

class Operation():
	def __init__(self):
		# 加载user.txt 文件数据
		self.load_user()
		
		# 加载userid.txt 文件数据
		self.load_userid()

	# 加载user.txt文件数据
	def load_user(self):
		if os.path.exists('user.txt'):
			with open('user.txt',mode='rb') as fp:	
				self.user_dict = pickle.load(fp)			
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

	# 0保存退出 --0
	def save(self):
		#存储user_dict 字典
		# self.user_dict = {'1':1}
		# self.user_id_dict = {'2':1}
		with open('user.txt',mode='wb') as fp:
			pickle.dump(self.user_dict,fp)
		
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
		
		## 获取密码
		password = self.get_pwd("请输入您的卡密码:","请确认您的卡密码:")
		# 获取卡号
		cardid = self.get_cardid()
		# 卡内默认余额 10元
		money = 10
		
		# 创建一张卡的对象
		card = Card(cardid,password,money)
		
		# 创建一个用户的对象
		user = Person(name,userid,phone,card)  #card是卡对象
		# print(user)
		
		# 存储数据到 user_dict    卡号:用户对象  cardid:user  
		# 把卡号和用户对象绑定
		# print(self.user_dict)
		# print(type(self.user_dict))
		self.user_dict[cardid] = user
		
		# 存储数据到 user_id_dict 身份证号:卡号  userid:cardid
		# 把身份证号和卡号绑定
		self.user_id_dict[userid] = cardid
		
		print('恭喜{}开卡成功,您的卡号为:{},卡内余额{}元'.
		format(name,cardid,money))


	def get_name(self):
		while True:
			name = input('请输入姓名:')
			if name == '' or ' ' in name:
				print('姓名不能为空')
			elif not name.isalpha():
				print('姓名不是中文或字母')
			elif name.isalpha():
				return name
				
	def get_phone(self):
		while True:
			phone = input('请输入您的手机号:')
			lst = re.findall(r'^1[3456789]\d{9}$',phone)
			if lst:
				return phone
			else:
				print('手机号格式不符合要求')
				
	def get_userid(self):			
		while True:
			userid = input('请输入身份证号:')
			lst = re.findall(r'^\d{6}[12]\d{3}[01]\d{1}[0123]\d{1}\d{3}[\dX]$',userid)
			if lst:
				return userid
			else:
				print('身份证号码格式不符合要求')
				

	# 1-1获取密码
	def get_pwd(self,name1,name2):
		while True:
			pwd1 = input(name1)
			pwd2 = input(name2)
			# 密码长度6位不能空,字母数字下划线 \w (纯数字的密码不允许的)
			lst = re.findall(r'^\w{6}$',pwd1)
			# print(lst)
			if lst and not pwd1.isdecimal():
				if pwd1 == pwd2:
					return pwd1
				else:
					print('两次密码不一致,请重新输入')
			else:
				print('密码长度6位不能空,字母数字下划线 \w (纯数字的密码不允许的)')

	# 1-2 获取卡号  6位卡号
	def get_cardid(self):
		while True:
			cardid = str(random.randrange(100000,1000000))
			# 字典的键推荐用字符串
			# user.txt   => {卡号:用户对象} {"555666": 用户对象}   
			# =>  user_dict
			if cardid not in self.user_dict:
			# 卡号不能相同
				return cardid

	# 2 查询
	def query(self):
		# 1.获取这张卡的相关信息
		card = self.get_card_info()  #获取卡的对象
		if not card:	
			print('抱歉,您的这张卡不存在')
		else:
			if card.islock:
				print('抱歉,你的卡已经被锁了')
			else:
				if self.check_pwd(card):
					# 显示卡内余额
					print('您的卡内余额是{}元'.format(card.money))
					if card.islock:
						print('卡的锁定状态是{}'.format('已锁定'))
					else:
						print('卡的锁定状态是{}'.format('未锁定'))
		
		
	# 2-1 卡的信息
	def get_card_info(self):
		cardid = input('请输入您的卡号:')
		if cardid not in self.user_dict:
			return False
		else:
			# 通过卡号 -> 用户对象 -->卡对象-->卡的cardid属性
			user = self.user_dict[cardid] #用户对象
			return user.card  #获取卡对象

	# 2-2 校验卡的密码 3次锁定  self.islock变成True
	def check_pwd(self,card):  #参数card是卡对象
		times = 1
		for i in range(3):
			pwd = input('请输入您的密码')
			if pwd == card.password:
				return True
			else:
				#剩余次数 = 总次数 - 使用次数
				print('密码错误~ , 您还剩下{}次机会'.format(3-times))
				if times == 3:
					card.islock = True  #锁定状态
					print("抱歉,密码输错三次,卡被锁定,请联系管理员.")		
			times += 1
	
	# 3 存钱
	 # 卡是否存在,是否冻结,存钱金额是否正确
	 # 卡的金额增加
	def sava_money(self):
		# 1.获取这张卡的相关信息
		card = self.get_card_info()  #获取卡的对象
		num = input('请输入你的存钱金额:')
		if num.isdecimal():
			num = int(num)
			if not card:	
				print('抱歉,您的这张卡不存在')
			else:
				if card.islock:
					print('抱歉,你的卡已经被锁了')
				else:
					card.money += num
					print('存款成功,你本次存入了{}元,你的余额是{}元'
					.format(num,card.money))
		else:
			print('请输入数字')

	# 4 取钱
	# 取钱:卡是否存在,是否冻结,取钱金额是否正确
	def withdraw(self):
		# 1.获取这张卡的相关信息
		card = self.get_card_info()  #获取卡的对象
		num = input('请输入你的取钱金额:')
		if num.isdecimal():
			num = int(num)
			if not card:	
				print('抱歉,您的这张卡不存在')
			else:
				if card.islock:
					print('抱歉,你的卡已经被锁了')
				else:
					if num <= card.money:
						if self.check_pwd(card):
							card.money -= num
							print('取款成功,你本次取了{}元,你的余额是{}元'
							.format(num,card.money))
					else:
						print('对不起,余额不足')
		else:
			print('请输入数字')
	
	#6 修改密码
	# 改密:(1)原密码改密  (2)身份证改密
	def change_pwd(self):
		# 1.获取这张卡的相关信息
		card = self.get_card_info()  #获取卡的对象
		while True:
			content = input('修改密码,原密码改密按P,身份证改密按I,退出按Q:')
			if content.upper() == 'P':
				self.old_pwd(card)
				print('密码修改成功')
				break
			elif content.upper() == 'I':
				self.idcard_pwd(card)
				# print('密码修改成功')
				break
			elif content.upper() == 'Q':
				print('退出改密')
				break
			else:
				print('输入选项不对')
	
	# 6-1
	def old_pwd(self,card):
		print('原密码改密')
		if not card:	
			print('抱歉,您的这张卡不存在')
		else:
			if card.islock:
				print('抱歉,你的卡已经被锁了')
			else:
				while True:
					old_pwd1 = input('请输入你的原密码:')
					if old_pwd1 == card.password:
						new_pwd1 = input('请输入你的新密码:')
						new_pwd2 = input('请再次输入你的新密码:')
						if new_pwd1 == new_pwd2:
							print('密码修改成功')
							card.password = new_pwd1  # 替换卡对象的密码
							break
						else:
							print('两次密码不一致,请重新输入')
					else:
						print('对不起密码不对,请重新输入')
	
    # 6-2	
	def idcard_pwd(self,card):
		print('身份证改密')
		if not card:	
			print('抱歉,您的这张卡不存在')
		else:
			if card.islock:
				print('抱歉,你的卡已经被锁了')
			else:
				while True:
					userid1 = input('请输入你的身份证:')
					# user = self.user_dict[self.user_id_dict[userid1]]   #用户对象
					if userid1 in  self.user_id_dict:
						cardid = self.user_id_dict.get(userid1) #获取卡号
						user = self.user_dict.get(cardid)   #用户对象
						if userid1 == user.userid:
						#user_id_dict[userid] 卡号
						# self.user_dict[user_id_dict[userid]]  用户对象
							new_pwd1 = input('请输入你的新密码:')
							new_pwd2 = input('请再次输入你的新密码:')
							if new_pwd1 == new_pwd2:
								print('密码修改成功')
								card.password = new_pwd1  # 替换卡对象的密码
								break
							else:
								print('两次密码不一致,请重新输入')
						else:
							print('对不起身份证不对,请重新输入')
					else:
						print('对不起身份证未开户,请重新输入')


	#7 锁卡:1:使用密码冻结  2:使用身份证号冻结
	def lock_card(self):
		# 1.获取这张卡的相关信息
		card = self.get_card_info()  #获取卡的对象
		while True:
			content = input('锁卡,密码冻结按P,身份证冻结按I,退出按Q:')
			if content.upper() == 'P':
				self.old_pwd2(card)
				break
			elif content.upper() == 'I':
				self.idcard_pwd2(card)
				break
			elif content.upper() == 'Q':
				print('退出锁卡')
				break
			else:
				print('输入选项不对')
	
	# 7-1
	def old_pwd2(self,card):
		print('使用密码冻结')
		if not card:	
			print('抱歉,您的这张卡不存在')
		else:
			if card.islock:
				print('抱歉,你的卡已经被锁了')
			else:
				while True:
					old_pwd1 = input('请输入你的原密码:')
					if old_pwd1 == card.password:
						print('密码冻结成功')
						card.islock = True  # 修改卡对象的锁定状态
						break
					else:
						print('对不起密码不对,请重新输入')
				
	    # 7-2	
	def idcard_pwd2(self,card):
		print('使用身份证号冻结')
		if not card:	
			print('抱歉,您的这张卡不存在')
		else:
			if card.islock:
				print('抱歉,你的卡已经被锁了')
			else:
				while True:
					userid1 = input('请输入你的身份证:')
					# user = self.user_dict[self.user_id_dict[userid1]]   #用户对象
					if userid1 in  self.user_id_dict:
						cardid = self.user_id_dict.get(userid1) #获取卡号
						user = self.user_dict.get(cardid)   #用户对象
						if userid1 == user.userid:
							print('使用身份证号冻结成功')
							card.islock = True  # 修改卡对象的锁定状态
							break
						else:
							print('对不起身份证不对,请重新输入')
					else:
						print('对不起身份证未开户,请重新输入')		
				
	# 8 解卡:判断卡是否存在,使用身份证解卡		
	def unlock_card(self):
		# 1.获取这张卡的相关信息
		card = self.get_card_info()  #获取卡的对象
		while True:
			content = input('身份证解卡按I,退出按Q:')
			if content.upper() == 'I':
				self.idcard_unlock(card)
				break
			elif content.upper() == 'Q':
				print('退出解卡')
				break
			else:
				print('输入选项不对')			
				
		    # 8-1	
	def idcard_unlock(self,card):
		print('使用身份证号解卡')
		if not card:	
			print('抱歉,您的这张卡不存在')
		else:
			if not card.islock:
				print('抱歉,你的卡已经是解锁状态')
			else:
				while True:
					userid1 = input('请输入你的身份证:')
					# user = self.user_dict[self.user_id_dict[userid1]]   #用户对象
					if userid1 in  self.user_id_dict:
						cardid = self.user_id_dict.get(userid1) #获取卡号
						user = self.user_dict.get(cardid)   #用户对象
						if userid1 == user.userid:
							print('使用身份证号解卡成功')
							card.islock = False  # 修改卡对象的锁定状态
							break
						else:
							print('对不起身份证不对,请重新输入')
					else:
						print('对不起身份证未开户,请重新输入')			
				
				
# 5转账:把一个卡里的钱转到其他卡内 
# (卡是否存在,是否冻结,对方账户是否存在,转账的金额是否正确)				
	def transfer(self):
		print('转账方:')
		card1 = self.get_card_info()  #获取卡的对象	
		# print(card1)
		# print(card1.islock)
		print('接受方:')
		card2 = self.get_card_info()  #获取卡的对象	
		# print(card2)
		# print(card2.islock)	
		if card1 is not False or card2 is not False:
			if (card1 and card2) and (not card1.islock and not card2.islock) and card1.cardid != card2.cardid:
			# 不能给自己转账
				print('转账方和接受方的卡都存在,且未冻结,可以发起转账')
				num = input('请输入你的转账金额:')
				if num.isdecimal():
					num = int(num)
					if num <= card1.money:
						card1.money -= num
						card2.money += num
						print('转账成功,卡号1:{who1}本次给卡号2:{who2}转账了{num1}元,卡号1:{who1}的余额是{money1}元,卡号2:{who2}的余额是{money2}元'
								.format(who1 = card1.cardid, who2 = card2.cardid,
										num1 = num,
										money1 = card1.money,money2 = card2.money))
										# card1.cardid,card1.money,
										# card2.cardid,card2.money))
						# print('接受成功,卡号{}本次接受了{}元,余额是{}元'
								# .format(card2.cardid,num,card2.money))		
								
					else:
						print('你的转账金额超过了你的余额,不能转出')
				else:
					print('请输入数字')	
			
			else:
				print('转账方和接受方的卡,至少有一个不存在,或被冻结,或给自己转账,不能转账')
		else:
			print('卡号不存在')
		
# 9补卡:将旧用户的所有信息和新卡绑定
# (包括名字,余额等所有卡信息和用户信息,数据重新绑定)[user_id_dict]
# 通过身份证 => 卡号  => 用户对象 		
	def	supplment_card(self):
		print('补卡了')
		while True:
			userid1 = input('请输入你的身份证:')
			# user = self.user_dict[self.user_id_dict[userid1]]   #用户对象
			if userid1 in  self.user_id_dict:
				cardid = self.user_id_dict.get(userid1) #获取老卡号
				user = self.user_dict.get(cardid)   #用户对象
				# user.card  #卡的对象
				if userid1 == user.userid:
					old_pwd = user.card.password  #老卡的密码
					old_money = user.card.money  #老卡的余额
					old_islock = user.card.islock  #老卡的锁定状态
					
					old_name = user.name   #老卡号所在用户的姓名
					old_userid = user.userid #老卡号所在用户的身份证
					old_phone = user.phone  # 老卡号所在用户的手机
					
					# card11 = Card('111',old_pwd,old_money,old_islock)
					cardid11 = self.get_cardid()
					# card11 = Card('111',old_pwd,old_money)
					card11 = Card(cardid11,old_pwd,old_money)
					card11.islock = old_islock
					#新卡的对象
					
					user11 = Person(old_name,old_userid,old_phone,card11)
					#新卡所在的用户对象
					
					#将 新卡号的id:user11  作为键值对,添加对字典1
					self.user_dict[card11.cardid] = user11
					
					# 将 老卡号的id 从字典1删除   #llw
					self.user_dict.pop(cardid)
					
					#将 老卡身份证和新卡号的id: 作为键值对,添加对字典2  
					# 修改老卡身份证和老卡号的id
					self.user_id_dict[old_userid] = card11.cardid
					print('补卡成功')
					break
					
				else:
					print('对不起身份证不对,请重新输入')
			else:
				print('对不起身份证未开户,请重新输入')	

				
				
			






































			
				
				
				
				
				
				
				
				












