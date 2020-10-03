# 1 局部变量
def func():
	a = 1  #定义
	print(a) #获取
	a = 2  #修改
	print(a)
func()
print('-----------------1')

# 2 全局变量
b = 10  #定义
print(b) #获取
b = 20  #修改
print(b)
print('-----------------2')

def func():
	print(b)  #全局变量可以在函数内获取
func()  #20



























