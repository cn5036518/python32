# ### 魔术属性

class Man():
	pass

class Woman():
	pass

class Sasuke(Man,Woman):
	# """
# 描述: 佐助这个的天生属性,技能
# 成员属性:  __eye skin
# 成员方法: skylight __moonread
	# """
	__eye = "血轮眼"
	
	skin = "白色"
	
	def skylight(self , myfunc):
		print("使用天照")
		res = myfunc.__name__
		print(res , type(res) ) #func343434 <class 'str'>
		print(myfunc)  #<function func343434 at 0x7f59affe7e18>

	def moonread(self,class1):
		print("使用月读")
		print(class1.__name__)  #Sasuke
		print(class1)  #<class '__main__.Sasuke'>
		res = Sasuke.__name__
		print(res,type(res))  #Sasuke <class 'str'>  可以直接打印类名

obj = Sasuke()
# __dict__ 获取对象或类的内部成员结构
print(Sasuke.__dict__) 
#{'__module__': '__main__',
 # '_Sasuke__eye': '血轮眼->万花筒->轮回眼',
 # 'skin': '白色',
 # 'skylight': <function Sasuke.skylight at 0x7f1085678158>,
 # '_Sasuke__moonread': <function Sasuke.__moonread at 0x7f10856781e0>,
 # '__doc__': None}
print(obj.__dict__)  #{}


# __doc__  获取对象或类的内部文档
# print(Sasuke.__doc__)
# print(obj.__doc__)


# __name__  获取类名函数名
# 1 获取函数名
def func34():
	print("佩恩出场")
obj.skylight(func34)
print('-----------------3-1  name 获取函数名')

# 当把函数作为实参传递到类的方法中,直接打印形参,会显示函数的内存地址,而不是名字
# 如何在类的方法中获取实参-函数的名字呢?   --答案是   形参.__name__    myfunc.__name__  即第21行

# 2 获取类名
obj.moonread(Sasuke)
print('-----------------3-2  name 获取类名')


# __class__ 获取当前对象所属的类
print(obj.__class__)  
#<class '__main__.Sasuke'>

# __bases__ 获取一个类直接继承的所有父类,返回元组
print(Sasuke.__bases__)
# (<class '__main__.Man'>, <class '__main__.Woman'>)


#小结:
# __name__  获取类名函数名
# 在类中直接打印类名,返回的是 <class '__main__.Sasuke'>
# 如果要在类中获取类名字符串 print(类名.__name__) 就是类名的字符串

# 函数无法直接在类中打印,可以通过实参传递到类的方法中
  # 打印函数名,会显示函数的地址 <function func343434 at 0x7f59affe7e18>
# 如果要在类中获取函数名字符串 print(函数名.__name__) 就是函数名的字符串


#魔术小结
# __call__   对象() 当做函数来调用
# __bool__ int float complex   将对象转成bool int float complex类型
# __add__ radd sub mul truediv 对象的计算
# __len__ 计算类或者对象的成员
# __dict__  获取类或者对象的成员 字典
# __doc__    帮助文档
# __class__  对象的所属类
# __bases__  类的所有父类
# __name__  获取类或者对象的名字
































