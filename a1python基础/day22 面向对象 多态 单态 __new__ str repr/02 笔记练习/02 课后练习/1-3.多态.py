# 多态
 # __new__ 
 # 单态  
 # __del__ 
 # __str__
 # __repr__

# 01多态
# ### 多态: 不同的子类对象调用相同的父类方法,得到不同的执行结果
# """继承   子类和父类
# 重写 """   子类重新父类的同名公有方法
 # 调用方: 不同的子类
 # 调用方法:调用相同的父类方法
 # 结果:得到不同的执行结果

# 父类
# soldier
# 方法 attack
	 # back
     
# 子类
# army
# navy
# airforce

#要求
# 1.全体出击
# 2.全体撤退
# 3.海军上,其他兵种撤退

class Soldier():
	def attack(self):
		pass
	def back(self):
		pass
		
class Army(Soldier):
	def attack(self):
		print('陆军进攻')
	def back(self):
		print('陆军撤退')

class Navy(Soldier):
	def attack(self):
		print('海军进攻')
	def back(self):
		print('海军撤退')

class Airforce(Soldier):
	def attack(self):
		print('空军进攻')
	def back(self):
		print('空军撤退')

obj1 = Army()
# obj1.attack()

obj2 = Navy()
obj3 = Airforce()

lst = [obj1,obj2,obj3]  #列表里面是3个对象

# 1.全体出击
for i in lst:
	i.attack()
# 陆军进攻
# 海军进攻
# 空军进攻
print('--------------1 全体出击')

# 2.全体撤退
for i in lst:
	i.back()
# 陆军撤退
# 海军撤退
# 空军撤退
print('--------------2 全体撤退')

# 3.海军上,其他兵种撤退
for i in lst:
	if isinstance(i,Navy):
		i.attack()  # 海军进攻
	else:
		i.back()  # 陆军撤退  # 空军撤退
# 陆军撤退
# 海军进攻
# 空军撤退
print('--------------3 海军上,其他兵种撤退')

obj1 = Army()
# obj1.attack()

obj2 = Navy()
obj3 = Airforce()

lst = [obj1,obj2,obj3]  #列表里面是3个对象

strvar = '1全体出击 2.全体撤退 3.海军上,其他兵种撤退'
num = input(strvar)
if num.isdecimal():
	for i in lst:
		if num == '1':
			i.attack()
		elif num == '2':
			i.back()
		elif num == '3':  #多态体现
		# 调用方:  不同的子类对象
		# 调用方法:调用同一个父类方法
		# 返回:	    得到不同的结果
			if isinstance(i,Navy):
				i.attack()   # 海军进攻
			else:
				i.back() # 陆军撤退 # 空军撤退
		else:
			print('请输入1~3')
else:
	print('请输入数字')

# 1全体出击 2.全体撤退 3.海军上,其他兵种撤退3
# 陆军撤退
# 海军进攻
# 空军撤退



























