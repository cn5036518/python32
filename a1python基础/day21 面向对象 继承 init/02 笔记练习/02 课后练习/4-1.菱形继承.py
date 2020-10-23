# ### 菱形继承 (钻石继承)
# """
	 # Human
# Man		    Woman
	# Children
# 

class MyClass():
	pass
	
class Human():
	# pty = 1
	def feelT(self):
		print('古代人类,天热了1')
		# print(self.pty)
		print('古代人类,天冷了2')

class Man(Human):
	# pty = 2
	def feelT(self):
		# print(self)
		print('男人,天热了,光膀子3')
		print(super(),'----------2')
		super().feelT()
		print('男人,天冷了4')
		
class Woman(Human):
	# pty = 3
	def feelT(self):
		print('女人,天热了5')
		print(super(),'--------3')
		super().feelT()
		print('女人,天冷了,穿貂6')

class Children(Man,Woman):
	# pty = 4
	def feelT(self):
		print('小孩,天热了7')
		print(super(),'--------1')
		#<super: <class 'Children'>, <Children object>> --------1
		super().feelT()
		print('小孩,天冷了,多喝热水8')
		
obj = Children()
obj.feelT()  ## 73512648

# 小孩,天热了7
# <super: <class 'Children'>, <Children object>> --------1
# 男人,天热了,光膀子3
# <super: <class 'Man'>, <Children object>> ----------2
# 女人,天热了5
# <super: <class 'Woman'>, <Children object>> --------3
# 古代人类,天热了1
# 古代人类,天冷了2
# 女人,天冷了,穿貂6
# 男人,天冷了4
# 小孩,天冷了,多喝热水8

# ### super的深层理解
# mro: 方法解析顺序 (c3算法计算的)
# 语法: 类.mro() => 列表
# m :method
# r :resolution 
# o :order
# super 会自动根据mro列表返回出来的顺序关系,依次调用 
# super作用:专门用于解决复杂的多继承调用顺序关系;依照mro返回的列表顺序,依次调用;
# super调用的顺序:会按照c3算法的广度优先原则进行调用
# super传参:会默认在调用方法时,传递该对象参数;
lst = Children.mro()
print(lst)
#[<class '__main__.Children'>, 
# <class '__main__.Man'>, 
# <class '__main__.Woman'>,
 # <class '__main__.Human'>,
 # <class 'object'>]

# ### issubclass与isinstance
# issubclass 判断类的子父关系(应用在类与类之间)
# """只要在一条继承链上(后代)满足关系即可"""
res = issubclass(Children,Man)
print(res)  #True

res = issubclass(Children,Human)
print(res) #True

res = issubclass(Children,MyClass)
print(res) #False

# 如果元组当中有一个父类满足,即返回真
res = issubclass(Children,(Man,Human,MyClass))
print(res) #True

# isinstance 判断对象的类型  (应用在类与对象之间)
# """只要在一条继承链(后代)上满足关系即可"""
res = isinstance(obj,Children)
print(res) #True

res = isinstance(obj,Human)
print(res)  #True

res = isinstance(obj,MyClass)
print(res)  #False

# 如果元组当中有一个类满足,即返回真
res = isinstance(obj,(Man,Human,MyClass))
print(res)  #True



















