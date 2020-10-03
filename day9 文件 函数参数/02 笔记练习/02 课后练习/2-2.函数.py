# ### 函数
# 概念:功能(包裹一部分代码  实现某一个功能 达成某一个目的)
# 特点:可以反复调用,提高代码的复用性,提高开发效率,便于维护管理

# 函数基本格式
# 定义一个函数
# def 函数名():
	# code1
	# code2
	
# 调用函数
# 函数名()

#定义函数
def func():
	print('我是一个函数')

#调用函数
func()

# 函数的命名
# 字母数字下划线,首字符不能为数字
# 严格区分大小写,且不能使用关键字
# 函数命名有意义,且不能使用中文


# 输出5个乘法表
# 思路
# 1写一个乘法表函数
#  2 for循环调用函数3次

def cfb_99():
	for i in range(1,10):
		for j in range(1,i+1):
			print("{:d}*{:d}={:2d} ".format(i,j,i*j),end='')
		print()
		
for i in range(3):
	cfb_99()
	print('----------{}'.format(i+1))






















































