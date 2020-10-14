# ### 多继承

# (1) 基本语法
class Father():
	property = '风流倜傥'
	def f_hobby(self):
		print('烫头')

class Mother():
	property = '倾国倾城'
	def m_hobby(self):
		print('网红直播')
		
class Daughter(Father,Mother):
	pass
	
obj = Daughter()
print(obj.property) #风流倜傥
obj.m_hobby() #网红直播

# (2) 多继承的成员调用
class Father():
	property = '风流倜傥'
	def f_hobby(): #无参方法 类调用
		print('烫头')

class Mother():
	property = '倾国倾城'
	def m_hobby(self):
		print('------------1')
		print(self) #<__main__.Son object at 0x7f73f30de978> #对应第60行的super
		print(self.property) #吃小零食  
		print('网红直播')

# (1)super本身是一个类 super()是一个对象 用于调用父类的绑定方法
# (2)super() 只应用在绑定方法中,默认自动传递self对象 (前提:super所在作用域存在self)
# (3)super用途: 解决复杂的多继承调用顺序

class Son(Father,Mother):
	property = '吃小零食'
	
	def m_hobby(self):
		print('son中m_hobby方法')

	# 用类调用成员
	def skill1(self):
		Father.f_hobby() ##烫头
		print(Mother.property)  #倾国倾城
		
	# 用对象调用成员
	# """self按照顺序找: 对象本身 => 自己的类 => 父类1 ==> 父类2 对应的成员 """
	def skill2(self):
		print(self.property)	 #喜欢跑跑卡丁车
		
	# 用super调用成员
	# """super()只调用父类的相关成员,顺带传递对象参数"""
	# 谁调,把谁当对象传递
	def skill3(self):
		print(super()) #<super: <class 'Son'>, <Son object>>
		print(super().property) #风流倜傥
		super().m_hobby() #网红直播
	
obj2 = Son()
obj2.skill1() #烫头

# obj2.property = '喜欢跑跑卡丁车'
obj2.skill2()

obj2.skill3()

































