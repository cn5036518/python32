import pickle
import os
import random
import re
import time
from .card import Card
from .person import Person
from .view import View


class Operation:
	login_card = None  # card obj

	# 写日志
	def write_log(self,cardid,strvar):
		t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		self.log_data[cardid][t] = strvar

	# 登录卡对象装饰器
	def card_login(func):
		def inner(self, *args, **kwargs):
			if self.login_card:
				return func(self, *args, **kwargs)
			else:
				print(' 登录界面 '.center(30, '*'))
				cardid = input("请输入您的卡号:")
				if cardid not in self.user_dict:
					print("抱歉,此卡号不存在")
				else:
					user = self.user_dict[cardid]
					card = user.card
					if card.islock:
						print("抱歉,您的卡已被锁定")
					else:
						times = 1
						while times <= 3:
							pwd = input("请输入您的密码").strip()
							if pwd.upper() == 'Q':
								break
							elif pwd == card.password:
								self.login_card = card
								print(f' 欢迎登录:{card.cardid} '.center(30, '*'))
								return func(self, *args, **kwargs)
							else:
								print("密码错误,还剩下{}次机会".format(3 - times))
								if times == 3:
									card.islock = True
									self.write_log(cardid, '卡号锁定')
									print("密码输错三次,卡被锁定,请联系管理员.")
							times += 1
		return inner

	# 1 注册
	def register(self):
		userid = self.get_userid()
		if not userid:
			return
		name = self.get_name()
		if not name:
			return
		password = self.get_pwd()
		if not password:
			return
		phone = self.get_phone()
		if not phone:
			return
		cardid = self.get_cardid()
		money = 10
		card = Card(cardid, password, money)
		user = Person(name, userid, phone, card)
		self.user_dict[cardid] = user
		self.userid_dict[userid] = [cardid]
		self.log_data[cardid] = {}
		self.write_log(cardid, '开卡成功')
		print('{}开卡成功,卡号:{},卡内余额{}'.format(name, cardid, money))

	# 1.1 用户名
	def get_name(self):
		while True:
			name = input('输入用户名>>>').strip()
			if name.upper() == 'Q':
				return
			elif name.isalpha():
				return name
			else:
				print('用户名输入有误')

	# 1.2 密码
	def get_pwd(self):
		while True:
			pwd1 = input('输入密码>>>').strip()
			if pwd1.upper() == 'Q':
				return
			res = re.search(r'^\w{6}$', pwd1)
			if res:
				if not res.group().isdecimal():
					pwd2 = input('确认密码>>>').strip()
					if pwd2.upper() == 'Q':
						return
					elif pwd1 == pwd2:
						return pwd1
					else:
						print('两次密码输入不一致')
				else:
					print('密码不可为纯数字')
			else:
				print('密码必须为6位,可用字符: 字母,数字,下划线')

	# 1.3 身份证
	def get_userid(self):
		while True:
			userid = input('输入身份证号>>>').strip().upper()
			if userid == 'Q':
				return
			elif userid not in self.userid_dict:
				res = re.search(r'^([1-9]\d)(\d[1-9])(\d[1-9])'
				                r'(19\d{2}|20[01]\d|2020)(0[1-9]|1[012])([012]\d|3[01])'
				                r'(\d[1-9])(\d)(\d|X)$', userid)
				if res:
					userid = res.group()
					if userid[10:12] == '02':
						if int(userid[12:14]) < 30:
							return userid
						else:
							print('身份证输入错误!')
					else:
						return userid
				else:
					print('身份证输入错误!')
			else:
				cmd = input('该身份证已存在用户,[Q]返回主界面,任意键使用其他身份证注册>>>').strip().upper()
				if cmd == 'Q':
					return

	# 1.4 手机号
	def get_phone(self):
		while True:
			phone = input('输入手机号>>>').strip()
			if phone.upper() == 'Q':
				return
			res = re.search(r'^[1-9][3-9]\d{9}$', phone)
			if res:
				phone = res.group()
				return phone
			else:
				print('手机号输入错误!')

	# 1.5 卡号
	def get_cardid(self):
		while True:
			cardid = str(random.randrange(100000, 1000000))
			if cardid not in self.user_dict:
				return cardid

	# 2 查询
	@card_login
	def query(self):
		View.query_choice()
		choice = input('>>>').strip()
		if choice == '1':
			print("您的卡内余额是{}元".format(self.login_card.money))
		elif choice == '2':
			View.query_logs(self.log_data[self.login_card.cardid])
		else:
			print('输入有误')

	# 3 存钱
	@card_login
	def save_money(self):
		money = input('输入存入金额>>>').strip()
		if money.isdecimal():
			money = int(money)
			if money % 100 == 0:
				self.login_card.money += money
				self.write_log(self.login_card.cardid, f'存入金额:{money}元')
				print(f'存入成功,金额:[{money}]元')
			else:
				print('错误,请输100的倍数')
		else:
			print('错误,请输入整数数字')

	# 4 取钱
	@card_login
	def get_money(self):
		money = input('输入提现金额>>>').strip()
		if money.isdecimal():
			money = int(money)
			if money % 100 == 0:
				if money <= self.login_card.money:
					self.login_card.money -= money
					self.write_log(self.login_card.cardid, f'提现金额:{money}元')
					print(f'提现成功,金额:[{money}]元')
				else:
					print('余额不足')
			else:
				print('错误,请输100的倍数')
		else:
			print('错误,请输入整数数字')

	# 5 转账
	@card_login
	def trans_money(self):
		other_cardid = input('输入转账目标卡号>>>').strip()
		if other_cardid.upper() == 'Q':
			return
		elif other_cardid not in self.user_dict:
			print('抱歉,此卡号不存在')
		else:
			other_card = self.user_dict[other_cardid].card  # 对方卡 obj
			if other_card.islock:
				print('对方账户已被冻结')
			else:
				money = input('输入转账金额>>>').strip()
				if money.upper() == 'Q':
					return
				elif money.isdecimal():
					money = int(money)
					if money <= self.login_card.money:
						self.login_card.money -= money
						other_card.money += money
						self.write_log(self.login_card.cardid, f'向{other_card.cardid}转账:{money}元')
						self.write_log(other_card.cardid, f'由账户{self.login_card.cardid}转入:{money}元')
						print(f'向用户[{self.user_dict[other_card.cardid].name}]的卡号[{other_card.cardid}]转账成功,金额:[{money}]元')
					else:
						print('余额不足')
				else:
					print('错误,请输入整数数字')

	# 6 改密
	def change_pwd(self):
		View.mode_choice('改密')
		choice = input('>>>').strip()
		if choice == '1':
			self.pwd_change_pwd()
		elif choice == '2':
			self.userid_change_pwd()
		else:
			print('输入有误')

	# 6.1 密码改密
	@card_login
	def pwd_change_pwd(self):
		old_pwd = input('输入原密码>>>').strip()
		if old_pwd == self.login_card.password:
			new_pwd = self.get_pwd()
			if not new_pwd:
				return
			elif new_pwd != self.login_card.password:
				self.login_card.password = new_pwd
				self.write_log(self.login_card.cardid, '更改密码')
				print(f'卡号:{self.login_card.cardid}已完成改密操作')
				self.login_card = None
			else:
				print('不可与原密码一致')
		else:
			print('密码输入有误')

	# 6.2 身份证改密
	def userid_change_pwd(self):
		cardid = input('输入需要改密卡号>>>').strip()
		if self.check_userid(cardid):
			if self.user_dict[cardid].card.islock:
				print('该卡已被锁定')
			else:
				new_pwd = self.get_pwd()
				if not new_pwd:
					return
				elif new_pwd != self.user_dict[cardid].card.password:
					self.user_dict[cardid].card.password = new_pwd
					self.write_log(cardid, '更改密码')
					print(f'卡号:{self.user_dict[cardid].card.cardid}已完成改密操作')
					if self.login_card:
						if cardid == self.login_card.cardid:
							self.login_card = None
				else:
					print('不可与原密码一致')

	# 身份证号验证
	def check_userid(self, cardid):
		if cardid in self.user_dict:
			user = self.user_dict[cardid]
			userid = input('输入身份证号>>>').strip()
			if userid == user.userid:
				return True
			else:
				print('身份证号输入错误')
		else:
			print("抱歉,此卡号不存在")

	# 7 锁卡
	def lock(self):
		View.mode_choice('锁卡')
		choice = input('>>>').strip()
		if choice == '1':
			self.pwd_lock_card()
		elif choice == '2':
			self.userid_lock_card()
		else:
			print('输入有误')

	# 7.1 密码锁卡
	@card_login
	def pwd_lock_card(self):
		old_pwd = input('输入密码>>>').strip()
		if old_pwd == self.login_card.password:
			self.login_card.islock = True
			self.write_log(self.login_card.cardid, '卡号锁定')
			print(f'卡号:{self.login_card.cardid}已完成锁定')
			self.login_card = None
		else:
			print('密码输入有误')

	# 7.2 身份证锁卡
	def userid_lock_card(self):
		cardid = input('输入需要锁定卡号>>>').strip()
		if self.check_userid(cardid):
			if self.user_dict[cardid].card.islock:
				print(f'卡号:{self.user_dict[cardid].card.cardid}已处于锁定状态')
			else:
				self.user_dict[cardid].card.islock = True
				self.write_log(cardid, '卡号锁定')
				print(f'卡号:{self.user_dict[cardid].card.cardid}已完成锁定')
				if self.login_card:
					if cardid == self.login_card.cardid:
						self.login_card = None

	# 8 解冻
	def unlock(self):
		cardid = input('输入需要解锁卡号>>>').strip()
		if self.check_userid(cardid):
			if not self.user_dict[cardid].card.islock:
				print(f'卡号:{self.user_dict[cardid].card.cardid}未处于锁定状态')
			else:
				self.user_dict[cardid].card.islock = False
				self.write_log(cardid, '卡号解锁')
				print(f'卡号:{self.user_dict[cardid].card.cardid}已完成解锁')

	# 9 补卡
	def new_card(self):
		userid = input('输入身份证号>>>').strip()
		if userid in self.userid_dict:
			lst = self.userid_dict[userid]
			View.lst_show(lst)
			choice = input('选择补办卡序号>>>').strip()
			if choice.isdecimal():
				choice = int(choice)
				if 0 < choice <= len(lst):
					cardid = lst[choice-1]
					new_cardid = self.get_cardid()
					new_pwd = self.get_pwd()
					if not new_pwd:
						return
					self.user_dict[cardid].card.password = new_pwd
					self.user_dict[cardid].card.cardid = new_cardid
					self.user_dict[cardid].card.islock = False
					self.user_dict[new_cardid] = self.user_dict[cardid]
					self.user_dict.pop(cardid)
					self.userid_dict[userid].remove(cardid)
					self.userid_dict[userid].append(new_cardid)
					self.log_data[new_cardid] = self.log_data[cardid]
					self.log_data.pop(cardid)
					self.write_log(new_cardid, f'补卡成功,原卡作废')
					print(f'补卡成功,新卡号为{new_cardid}')
				else:
					print('超出选择范围')
			else:
				print('请输入数字')
		else:
			print('身份证号输入错误')

	# N 开新卡
	def append_card(self):
		userid = input('输入身份证号>>>').strip()
		if userid in self.userid_dict:
			print('*- 现将创建新卡')
			user = self.user_dict[self.userid_dict[userid][0]]  # 用户对象
			name = user.name
			password = self.get_pwd()
			if not password:
				return
			phone = user.phone
			cardid = self.get_cardid()
			money = 10
			card = Card(cardid, password, money)
			user = Person(name, userid, phone, card)
			self.user_dict[cardid] = user
			self.userid_dict[userid].append(cardid)
			self.log_data[cardid] = {}
			self.write_log(cardid, '开卡成功')
			print('{}开卡成功,卡号:{},卡内余额{}'.format(name, cardid, money))
		else:
			print('该身份证尚未开户,请先进行开户操作')

	# X 登出
	def signout(self):
		if self.login_card:
			print(f'卡号{self.login_card.cardid}已登出')
			self.login_card = None
		else:
			print('尚未登录')

	# Z 身份证登录入口
	def userid_login(self):
		print(' 登录界面 '.center(30, '*'))
		userid = input('输入身份证号>>>').strip()
		if userid in self.userid_dict:
			lst = self.userid_dict[userid]
			View.lst_show(lst)
			choice = input('选择登录卡序号>>>').strip()
			if choice.isdecimal():
				choice = int(choice)
				if 0 < choice <= len(lst):
					cardid = lst[choice-1]
					user = self.user_dict[cardid]
					card = user.card
					if card.islock:
						print("抱歉,您的卡已被锁定")
					else:
						times = 1
						while times <= 3:
							pwd = input("请输入您的密码").strip()
							if pwd.upper() == 'Q':
								break
							if pwd == card.password:
								self.login_card = card
								print(f' 欢迎登录:{card.cardid} '.center(30, '*'))
								break
							else:
								print("密码错误,还剩下{}次机会".format(3 - times))
								if times == 3:
									card.islock = True
									self.write_log(card.cardid, '卡号锁定')
									print("密码输错三次,卡被锁定,请联系管理员.")
							times += 1
				else:
					print('超出选择范围')
			else:
				print('请输入数字')

	# C 卡号登录入口
	@card_login
	def cardid_login(self):
		pass

	# 0 存储退出
	def save(self):  # 存回字典
		with open("user.pkl", mode="wb") as fp:
			pickle.dump(self.user_dict, fp)
		with open("userid.pkl", mode="wb") as fp:
			pickle.dump(self.userid_dict, fp)
		with open("log.txt", mode="wb") as fp:
			pickle.dump(self.log_data, fp)
		print('再见')

	# 加载字典
	def __init__(self):
		self.user_dict = {}
		self.userid_dict = {}
		self.log_data = {}
		self.load_user()
		self.load_userid()
		self.load_log()

	def load_user(self):  # 加载字典user_dict
		if os.path.exists("user.pkl"):
			with open("user.pkl", mode="rb") as fp:
				self.user_dict = pickle.load(fp)

	def load_userid(self):  # 加载字典userid_dict
		if os.path.exists("userid.pkl"):
			with open("userid.pkl", mode="rb") as fp:
				self.userid_dict = pickle.load(fp)

	def load_log(self):  # 加载字典log_data
		if os.path.exists("log.txt"):
			with open("log.txt", mode="rb") as fp:
				self.log_data = pickle.load(fp)



