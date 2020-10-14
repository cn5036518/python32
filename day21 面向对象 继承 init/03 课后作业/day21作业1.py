# ### 1.完成下列功能:
	# 1.1创建一个人类Person,再类中创建3个成员属性
		# animal = '高级动物'
		# soul = '有灵魂'
		# language = '语言'
	# 1.2在类中定义三个方法,吃饭,睡觉,工作.
	# 1.3在此类中的__init__方法中,给对象封装5个属性: 国家 , 姓名 , 性别 , 年龄 , 身高.
	# 1.4实例化四个人类对象:
		# 第一个人类对象p1属性为:中国,alex,未知,42,175.
		# 第二个人类对象p2属性为:美国,武大,男,35,160.
		# 第三个人类对象p3属性为:你自己定义.
		# 第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3的身高.
	# 1.5 通过p1对象执行吃饭方法,方法里面打印:alex在吃饭.
	# 1.6 通过p2对象执行吃饭方法,方法里面打印:武大在吃饭.
	# 1.7 通过p3对象执行吃饭方法,方法里面打印:(p3对象自己的名字)在吃饭.
	# 1.8 通过p1对象找到类中成员属性animal
	# 1.9 通过p2对象找到类中成员属性soul
	# 2.0 通过p3对象找到类中成员属性language

# ### 2.通过自己创建类,实例化对象
	#通过调用对象当中的方法,在终端输出如下信息
	#小明，10岁，男，上山去砍柴
	#小明，10岁，男，开车去东北
	#小明，10岁，男，最爱大保健

	#老李，90岁，男，上山去砍柴
	#老李，90岁，男，开车去东北
	#老李，90岁，男，最爱大保健

# ### 3.模拟英雄联盟写一个游戏人物的类
	#要求:
	#(1) 创建一个 Game_role 的类.
	#(2) 构造方法中给对象封装 name,ad(攻击力),hp(血量).三个属性.
	#(3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
	#例: 实例化一个对象 盖伦,ad为10, hp为100
	#实例化另个一个对象 剑豪 ad为20, hp为80
	#盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.
	

# ### 4.请定义一个圆形类,有计算周长和面积的两个方法 (圆的半径通过参数传递给初始化方法)

# ### 5创建AB两个类，A类中有属性abc=5把A类的对象存储在B类对象的成员属性pty中,用B类对象调用出abc这个值.

# ### 简答题
# 1.类或对象是否能做字典的key      
# 2.简述python的私有成员是如何实现的  _
# 3.私有成员能在类的外部使用么?能在子类中使用么?


# ### 1.完成下列功能:
	# 1.1创建一个人类Person,在类中创建3个成员属性
		# animal = '高级动物'
		# soul = '有灵魂'
		# language = '语言'
class Person():
	animal = '高级动物'
	soul = '有灵魂'
	language = '语言'		

	# 1.2在类中定义三个方法,吃饭,睡觉,工作.
class Person():
	animal = '高级动物'
	soul = '有灵魂'
	language = '语言'

	def eat(self):
		pass
		
	def sleep1(self):
		pass
		
	def work(self):
		pass

	# 1.3在此类中的__init__方法中,给对象封装5个属性: 国家 , 姓名 , 性别 , 年龄 , 身高.
class Person():
	animal = '高级动物'
	soul = '有灵魂'
	language = '语言'
	
	def __init__(self,country,name,gender,age,height):
		self.country = country
		self.name = name
		self.gender = gender
		self.age = age
		self.height = height

	def eat(self):
		pass
		
	def sleep1(self):
		pass
		
	def work(self):
		pass	

	# 1.4实例化四个人类对象:
		# 第一个人类对象p1属性为:中国,alex,未知,42,175.
		# 第二个人类对象p2属性为:美国,武大,男,35,160.
		# 第三个人类对象p3属性为:你自己定义.
		# 第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3的身高.
class Person():
#   成员属性
	animal = '高级动物'
	soul = '有灵魂'
	language = '语言'

# 构造方法	
	def __init__(self,country,name,gender,age,height):
		self.country = country
		self.name = name
		self.gender = gender
		self.age = age
		self.height = height

# 成员方法
	def eat(self):
		print('{}在吃饭'.format(self.name))
		
	def sleep1(self):
		pass
		
	def work(self):
		pass	

p1 = Person('中国','alex','未知',42,175)		
p2 = Person('美国','武大','男',35,160)		
p3 = Person('中国','lucy','女',18,165)		
p4 = Person('中国','武大','女',35,165)		

	# 1.5 通过p1对象执行吃饭方法,方法里面打印:alex在吃饭.
p1.eat()  #alex在吃饭
	
	# 1.6 通过p2对象执行吃饭方法,方法里面打印:武大在吃饭.
p2.eat() #武大在吃饭
	
	# 1.7 通过p3对象执行吃饭方法,方法里面打印:(p3对象自己的名字)在吃饭.
p3.eat() #lucy在吃饭
	
	# 1.8 通过p1对象找到类中成员属性animal
print(p1.animal)  #高级动物
	
	# 1.9 通过p2对象找到类中成员属性soul
print(p2.soul)	  #有灵魂

	# 2.0 通过p3对象找到类中成员属性language
print(p3.language) #语言
print('---------------------------1')

# ### 2.通过自己创建类,实例化对象
	#通过调用对象当中的方法,在终端输出如下信息
	#小明，10岁，男，上山去砍柴
	#小明，10岁，男，开车去东北
	#小明，10岁，男，最爱大保健

	#老李，90岁，男，上山去砍柴
	#老李，90岁，男，开车去东北
	#老李，90岁，男，最爱大保健


class Person():
# 构造方法	
	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender
		# self.hobby = hobby

# 成员方法
	def work(self):
		print('{},{}岁,{},上山去砍柴'.format(self.name,self.age,self.gender))	
		
	def go(self):
		print('{},{}岁,{},开车去东北'.format(self.name,self.age,self.gender))

	def hobby(self):
		print('{},{}岁,{},最爱大保健'.format(self.name,self.age,self.gender))

p1 = Person('小明','10','男')		
p2 = Person('老李','90','男')		

p1.work()
p1.go()
p1.hobby()

p2.work()
p2.go()
p2.hobby()
print('---------------------------2')

# ### 3.模拟英雄联盟写一个游戏人物的类
	#要求:
	#(1) 创建一个 Game_role 的类.
	#(2) 构造方法中给对象封装 name,ad(攻击力),hp(血量).三个属性.
	#(3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
	#例: 实例化一个对象 盖伦,ad为10, hp为100
	#实例化另个一个对象 剑豪 ad为20, hp为80
	#盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.

class Game_role():
	def __init__(self,name,ad,hp):
		self.name = name
		self.ad = ad
		self.hp = hp

	def attack(self,who,hp):
		print('{}攻击{},{}掉了{}点血,还剩{}点血'.format(self.name,who,who,self.ad,hp-self.ad))

r1 = Game_role('盖伦',10,100)
r2 = Game_role('剑豪',20,80)

r1.attack(r2.name,r2.hp)
# 盖伦攻击剑豪,剑豪掉了10点血,还剩70点血
# 2个对象如何在一个方法中使用?--nok
print('---------------------------3')

# ### 4.请定义一个圆形类,有计算周长和面积的两个方法 (圆的半径通过参数传递给初始化方法)
import math
class Circle():
	def __init__(self,r):
		self.r = r
		
	def area(self):
		return math.pi*self.r**2
		
	def perimeter(self):
		return 2*math.pi*self.r

obj = Circle(10)
area1 = obj.area()
print(area1) #314.1592653589793

perimeter1 = obj.perimeter()
print(perimeter1) #62.83185307179586
print('---------------------------4')

# ### 5创建AB两个类，A类中有属性abc=5把A类的对象存储在B类对象的成员属性pty中,用B类对象调用出abc这个值.
class A():
	abc = 5
	
a1 = A()
	
class B():
	pty = a1
	
b1 = B()
print(b1.pty.abc) #5
print('---------------------------5')

# ### 简答题
# 1.类或对象是否能做字典的key   
# 字典的key需要是不可变的类型 Numbers(int float bool complex) tuple str
# 可变类型  list dict set
   
# 2.简述python的私有成员是如何实现的  _
#  改名   _类__私有成员

# 3.私有成员能在类的外部使用么?能在子类中使用么?
# 方法1  _类__私有成员  不推荐
# 方法2 obj通过公有方法,来获取私有成员 推荐
#  私有成员可以在子类中使用,子类的对象通过调用父类的公有方法来获取父类的私有成员

# ### 读代码,写答案
# 1.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print('666')
		
# 创建了一个列表,列表中有三个对象(实例)
config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
for item in config_obj_list:
    print(item.num)	 # 1 2 3
print('-----------------1')		
		
# 2.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):
    pass
	
# 创建了一个列表,列表中有三个对象(实例)
config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
for item in config_obj_list:
    item.changelist(168)
print(config_obj_list[0].num)
# 1 168
# 2 168
# 3 168
# 1		
print('-----------------2')			
		
# 3.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print(666,self.num)

config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
for item in config_obj_list:
    item.changelist(168)
# 1 168
# 2 168
# 666 3
print('-----------------3')			
	
# 4.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)
    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print(666,self.num)

config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
config_obj_list[1].run()  
config_obj_list[2].run()	
# 2 999
# 666 3		
print('-----------------4')			
		
# 5.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)
    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print(666,self.num)

class AdminSite(object):
    def __init__(self):
        self._registry = {}
    def register(self,k,v):
        self._registry[k] = v

site = AdminSite()
print(len(site._registry))  #0  
site.register('range',666)
site.register('shilei',438)
print(len(site._registry)) #2 

site.register('lyd',StarkConfig(19))
site.register('yjl',StarkConfig(20))
site.register('fgz',RoleConfig(33))
print(len(site._registry))  #5  
print(site._registry)	
#{'range': 666, 'shilei': 438, 'lyd': <__main__.StarkConfig object at 0x7fee9786fe48>, 
# 'yjl': <__main__.StarkConfig object at 0x7fee9786fe80>, 'fgz': <__main__.RoleConfig object at 0x7fee9786feb8>}	
print('-----------------5')	
		
# 6.读程序写结果.(不执行)
class StarkConfig():
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)
    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print(666,self.num)

class AdminSite():
    def __init__(self):
        self._registry = {}
    def register(self,k,v):
        self._registry[k] = v

site = AdminSite()
site.register('lyd',StarkConfig(19))
site.register('yjl',StarkConfig(20))
site.register('fgz',RoleConfig(33))

for k,row in site._registry.items():
    row.changelist(5)
for k,row in site._registry.items():
    row.run()	
# 19 5
# 20 5
# 666 33

# 19 999
# 20 999
# 666 33	
print('-----------------6')			
		
# 7.读程序写结果.(不执行)
class JustCounter:
	__secretCount = 0
	def count(self):
		print(self.__secretCount) # 获取
		self.__secretCount += 1

	def count3():
		print(JustCounter.__secretCount)
		JustCounter.__secretCount += 1
		print(JustCounter.__secretCount)

class Bars(JustCounter):
	def count2(self):
		print(self.__secretCount)

#  情况一
counter1 = JustCounter()
counter1.count() #0
counter1.count()  #1
JustCounter.count3()  #0 1
#  情况二
counter2 = Bars() #1
counter2.count() 
counter2.count()
#  情况三
JustCounter.count3()		
print('-----------------7')			
		
		
		
		
		
		
		
		
		
		
		



















