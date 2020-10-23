# 1.结果
def extendList(val,list=[]):
    list.append(val)
    return list
list1 = extendList(10)   
print(list1)    #[10]  #这里的[10]作为默认形参,提前驻留内存
list2 = extendList(123 , [])   #这里的[]和默认形参的id不同  新开辟了一个空间
print(list2)  # [123]
list3 = extendList('a')   
print(list3)  # [10,'a']
print('------------------1')

# 2.res是多少?
def func():
	return [lambda x : i*x    for i in range(4)]  #循环完毕后,才调用函数
res = [m(2) for m in func()]
print(res)  #[6, 6, 6, 6]
print('------------------2-1')

#1先判断,下面的是列表推导式,还是lambda函数
[lambda x : i*x    for i in range(4)]

# lambda x : i*x    for i in range(4)  #SyntaxError: invalid syntax  说明不是lambda函数
lambda x : [i*x    for i in range(4)]  #这个才是lambda的正确写法

[lambda x : i*x    for i in range(4)]  #是列表推导式  该列表的元素是4个匿名函数(id不同)

# 2  将列表推导式改写成普通的函数
# 2-1  lambda x : i*x改写成普通函数
def func(x):
	return i*x
	
# 2-2  [lambda x : i*x    for i in range(4)] 改写如下
lst = []
for i in range(4):
	def func(x):
		return i*x  #i的取值 0 1 2 3
	lst.append(func)

# 3  res = [m(2) for m in func()]  改写如下
# res = [i(2) for i in func()]  将列表推导是改写成普通函数
# func()是上述2-2

def outer():
	lst = []
	for i in range(4):#关键点 i遍历完了,i=3的时候,4个匿名函数定义完毕(函数定义的时候,是不执行代码的,只有函数调用的时候,才执行代码,函数调用在49行)
		def func(x): #即i = 0 1 2的时候,是无法传入到45行的内函数的   #x=2 i=3(关键点:i在4个匿名函数的值都是3,而不是0 1 2 3)
			return i*x  #i的取值 0 1 2 3  #i是嵌套层的局部变量 ,生命周期会延长  
		lst.append(func)
	return lst  #外函数返回的是列表,列表里面的元素是4个匿名函数的内存地址,闭包(因为间距返回了内函数)
lst = outer()
print(lst) #lst里面是4个匿名函数,匿名函数的参数x是2,返回值是i*x = 3*2  即4个6  [6,6,6,6]  而不是[0,2,4,6]

#4个匿名函数的写法一样,但是id不同
# [<function outer.<locals>.func at 0x7f55b1c89378>, 
# <function outer.<locals>.func at 0x7f55b1c89598>,
 # <function outer.<locals>.func at 0x7f55b1c89620>,
 # <function outer.<locals>.func at 0x7f55b1c896a8>]


print('------------------2')

# 3.打印结果是多少?
def add(a,b):                     
    return a + b
def test():                       
    for r in range(4): 
        yield r
g=test()   #生成器(0,1,2,3)
for n in [2,10]: #n=2的时候,是不能传递到26行的,因为27行没有调用.等27行调用的时候,for循环结束了,n的值是10,而不是2(关键点1)
	g=(add(n,i) for i in g)    #24行的g是26行右边的g.从右往左看
print(list(g))

# g=(add(n,i) for i in g)  

# g= (add(10,i) for i in (0,1,2,3)))  (10,11,12,13)  #第一个g计算后是(10,11,12,13),替换到32行的in后面的g
# g= (add(10,i) for i in (10,11,12,13))) (20,21,22,23)

# 生成器(函数也是)定义的时候,代码是不执行的,只有调用的时候(list强转)的时候,才执行
print('------------------3')



	
# 4.如何判断输入的数是质数( 1.通用方法完成 2.使用for .. else 完成 )
# 规律:质数只能被1和自己整除(取余是0)的数,不能被2~n-1整除(取余是0)
# n = 5
#方法1  使用for .. else 完成    python特有
def prime(n):
	if n > 1:
		for i in range(2,n):
			if n % i == 0: 
				print('{:d}不是质数'.format(n))
				break
		else:
			print('{:d}是质数'.format(n))				
	else:
		print('{:d}不是质数'.format(n))
prime(-1)

#方法2  使用通用方法完成 完成 
sign = True
def prime_num(n):
	if n > 1:
		for i in range(2,n):
			if n % i == 0:
				# print('{:d} 不是质数'.format(n))
				sign = False  #不是质数,sign就是False
				break
			# else:
				# sign = True
				
		if sign == False:  #不是质数
			print('{:d}不是质数'.format(n))
		elif sign == True: #是质数
			print('{:d}是质数'.format(n))
	else:
		print('{:d}  不是质数'.format(n))
prime_num(6)
print('------------------4')

# 5 计算文件夹的大小
#思路   
# 1 找到文件夹的绝对路径  os.getcwd()  os.path.join()
# 2 列出文件夹的内容  os.listdir
# 3 遍历文件夹
# 4 判断是否是文件夹
  # 如果是文件,os.path.getsize  参数是新的文件的绝对路径
	#os.path.isdir()
  # 如果是文件夹,调用自己        参数是新文件夹的绝对路径
  # os.path.isfile()
# 5 size += 累加

# 1 找到文件夹的绝对路径  os.getcwd()  os.path.join()
import os
pathvar = os.getcwd()
print(pathvar)  
#/mnt/hgfs/ubuntu_gx/python32/day14 ubuntu环境2 内置函数 随机模块 数学模块/03 课后作业

pathvar_new = os.path.join(pathvar,'001')
print(pathvar_new)
#/mnt/hgfs/ubuntu_gx/python32/day14 ubuntu环境2 内置函数 随机模块 数学模块/03 课后作业/001

# 2 列出文件夹的内容  os.listdir
content = os.listdir(pathvar_new)
print(content)
# ['002', 'day14作业面试题1.py', 'day14作业面试题2.py']

# 3 遍历文件夹

def getdirsize(pathvar_new):
	size = 0  #位置在函数内,for外 关键点2
	for i in os.listdir(pathvar_new):
		#拼接绝对路径
		path1 = os.path.join(pathvar_new,i)
		# print(path1)
		# /mnt/hgfs/ubuntu_gx/python32/day14 ubuntu环境2 内置函数 随机模块 数学模块/03 课后作业/001/002
	# /mnt/hgfs/ubuntu_gx/python32/day14 ubuntu环境2 内置函数 随机模块 数学模块/03 课后作业/001/day14作业面试题1.py
	# /mnt/hgfs/ubuntu_gx/python32/day14 ubuntu环境2 内置函数 随机模块 数学模块/03 课后作业/001/day14作业面试题2.py	
		if os.path.isdir(path1):
			size += getdirsize(path1)   #关键点
		elif os.path.isfile(path1):
			size += os.path.getsize(path1)
	return size

res = getdirsize(pathvar_new)
print(res)

# 4 判断是否是文件夹
  # 如果是文件,os.path.getsize  参数是新的文件的绝对路径
  # 如果是文件夹,调用自己        参数是新文件夹的绝对路径
# 5 size += 累加

print('-----------------------5')













