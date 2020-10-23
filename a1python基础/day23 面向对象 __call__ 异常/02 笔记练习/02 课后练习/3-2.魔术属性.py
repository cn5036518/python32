# ### 魔术属性

class Man():
	pass

class Woman():
	pass
	
class Sasuke(Man,Woman):
	'''
描述: 佐助这个的天生属性,技能
成员属性:  __eye skin
成员方法: skylight __moonread
	'''
	__eye = '血轮眼'
	
	skin = '白色'
	
	def skylight(self,myfunc):
		print('使用天照,一团黑色的火焰')
		res = myfunc.__name__
		print(res,type(res))  ## func34 <class 'str'>
		
	def __moonread(self):
		print('月读')
		
obj = Sasuke()
# __dict__ 获取对象或类的内部成员结构

dic = Sasuke.__dict__
print(dic)
# {'__module__': '__main__',
 # '_Sasuke__eye': '血轮眼', 
 # 'skin': '白色',
 # 'skylight': <function Sasuke.skylight at 0x7fde93c31158>, 
 # '_Sasuke__moonread': <function Sasuke.__moonread at 0x7fde93c311e0>,
 # '__doc__': None}

dic = obj.__dict__
print(dic) #{}

# __doc__  获取对象或类的内部文档
print(Sasuke.__doc__)
print(obj.__doc__)

# __name__  获取类名函数名
def func34():
	print('佩恩')

obj.skylight(func34)
# 使用天照,一团黑色的火焰
# func34 <class 'str'>

obj.skylight(Sasuke)
#Sasuke <class 'str'>

# __class__ 获取当前对象所属的类
res = obj.__class__
print(res,type(res)) 
#<class '__main__.Sasuke'><class 'type'>

# __bases__ 获取一个类直接继承的所有父类,返回元组
print(Sasuke.__bases__)
#(<class '__main__.Man'>, <class '__main__.Woman'>)


































