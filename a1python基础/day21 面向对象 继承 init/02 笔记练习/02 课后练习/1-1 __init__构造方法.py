# ### __init__ 构造方法
	# 触发时机：实例化对象,初始化的时候触发
	# 功能：为对象添加成员
	# 参数：参数不固定,至少一个self参数
	# 返回值：无

# (1) 基本语法
class MyClass():
	def __init__(self):
		print('构造方法被触发 ... ')
		self.color = 'yellow'

# 实例化对象
obj = MyClass()
print(obj.__dict__) #{'color': 'yellow'}
print(obj.color) #yellow

# (2) 带有多个参数的构造方法
class MyClass():
	def __init__(self,color):
		self.color = color

# 实例化对象
obj1 = MyClass('green')
print(obj1.color) #green
obj2 = MyClass('red')
print(obj2.color) #red

# (3)类可以是一个,对象可以是多个,创造的对象彼此是独立的;
class Children():
	def __init__(self,name,skin):
		self.name = name
		self.skin = skin
		
	def cry(self):
		print('小孩一下生久哇哇哇的哭')
		
	def la(self):
		print('小孩一下生久拉粑粑')
		
	def __eat(self):
		print('小孩一下生就要吃奶奶')
		
	def info(self):
		print('小孩的名字:{},小孩的肤色{}'.format(self.name,self.skin))

	def info2(self,name,skin):
		print('小孩的名字:{},小孩的肤色{}'.format(name,skin))

# 实例化对象
afanda = Children("阿凡达","深蓝色")
afanda.cry() #小孩一下生久哇哇哇的哭
afanda.info()#小孩的名字:阿凡达,小孩的肤色深蓝色

haoke = Children("绿巨人","绿色的")
haoke.la() #小孩一下生久拉粑粑
haoke.info() #小孩的名字:绿巨人,小孩的肤色绿色的

wangbaoqiang = Children("王宝强","亮绿色")
wangbaoqiang.info() #小孩的名字:王宝强,小孩的肤色亮绿色
# wangbaoqiang.__eat()
#AttributeError: 'Children' object has no attribute '__eat'

wangbaoqiang.info2("张保张","黄色")  #这里的参数会覆盖init的参数
#小孩的名字:张保张,小孩的肤色黄色









































