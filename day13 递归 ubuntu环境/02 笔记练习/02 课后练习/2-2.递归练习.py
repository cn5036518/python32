# ### 1使用递归实现任意数n的阶乘

# 方法1 普通实现
# 5! = 5*4*3*2*1

def jiecheng1(n):
	total = 1
	for i in range(n,0,-1):
		total *= i  #累加的初始值是0  累乘的初始值是1
	print(total)

jiecheng1(5)  #120

# 方法2 递归实现
def jiecheng(n):
	if n == 1:
		return 1
	return jiecheng(n-1)*n
print(jiecheng(3))  #6
#顺序来看
# jiecheng(1)  ==> 1
# jiecheng(2)  ==> jiecheng(1)*2==>1 * 2
# jiecheng(3)  ==> jiecheng(2)*3==>1 * 2 *3

# 代码解析
# 去的过程:   新建了3个空间
# n = 3 return jiecheng(n-1) * n ==> jiecheng(2) * 3
# n = 2 return jiecheng(n-1) * n ==> jiecheng(1) * 2
# n = 1 return 1 #到此,得到值了,去的过程结束
# #这里的1返回给n=2这个空间 然后n=1(空间1)释放
#
# 回的过程:   依次释放这3个空间
# n=2 return jiecheng(1)*2  ==>1 * 2  #这里的1*2返回给n=3这个空间(空间3) 然后n=2(空间2)释放
# n=3 return jiecheng(2)*3  ==>1 * 2 * 3
#
# 到此程序结束
# 返回  1*2*3
print('-------------------------------------1')

# ### 3.使用递归来完成斐波那契数列
# 1 1 2 3 5 8 13

def feib(n):  #这里的n表示数列中第几个数  比如:请问第5个数是多少?
	if n == 1 or n == 2:
		return 1
	# 上一个结果 + 上上个结果
	return feib(n-1) + feib(n-2)
res = feib(4)	
print(res)  #3  #即斐波那契数列中,第n=4个数是4

# 代码解析
# 这里返回的是一个表达式.有去有回
# 如果返回的不是一个表达式,而是返回的是函数自己,就是尾递归
# 尾递归的特点:
# 	有去有回
# 	回的过程中,由于返回的是函数自己.
# 	所以第一层返回,第二层返回..最后一层返回的值是相同的
#
# 去的过程  依次新建内存空间
# n=4 return feib(n-1) + feib(n-2) ==> feib(3) + feib(2) ==> 2 + 1 =3
# n=3 return feib(n-1) + feib(n-2) ==> feib(2) + feib(1)
# n=2 return 1
# n=1 return 1
# 到此,去的过程结束
#
# 回的过程  依次回收内存空间
# n=1 return 1   空间1
# n=2 return 1   空间2
# n=3 return feib(2) + feib(1)    1+1 =2   空间1和空间2将结果返回给 空间3
# n=4 return feib(3) + feib(2)    2+1 =3   空间3将结果返回给 空间4
# 到此,回的过程结束
# 到此,整个过程结束
print('-------------------------------------3')

# ### 2.使用尾递归来实现任意数的阶乘
# return 在哪调用,在哪返回
# 尾递归的概念:
	# 自己调用自己,且返回是非运算表达式,只是函数本身
# 特点:
	# 尾递归只开辟一个空间,不会无限的开辟,在一个空间里面去计算最后的结果
	# 进行返回,比较节省空间,有的解释器支持尾递归的调用特点
	# 但是cpython解释器目前不支持
# 写法:
	# 所有运算的值都在函数的参数中计算完毕,最后返回运算的参数

def jiecheng(n,endval):
	if n == 1:
		return endval
	return jiecheng(n-1,n * endval)
res = jiecheng(3,1) # 3*2*1
print(res) #6

# 代码解析
# 去的过程
# n=3 endval=1 return jiecheng(n-1,n * endval) ==>jiecheng(2,3*1)
# n=2 endval=3*1 return jiecheng(n-1,n * endval) ==>jiecheng(1,3*1*2)
# n=1 endval=3*2*1 if n==1 成立 return endval  3*2*1
# endval = 3*2*1
# 最下层空间的返回值是 3*2*1
# 最上层空间的返回值是 3*2*1
# 最下层和最上层返回的结果是一致的,所以对于尾递归来说,只需要考虑去的过程
# 无需考虑回的过程即可完成


# 优化代码1
def jiecheng(n,endval=1):  #默认参数
	if n == 1:
		return endval
	return jiecheng(n-1,n*endval)
res = jiecheng(5)  # 5*4*3*2*1  #只需要传递一个参数即可
# res = jiecheng(5,100)  # 如果第二参数是100.就会有问题
print(res)  #120

# 优化代码2  #把尾递归需要的参数值隐藏起来,避免篡改
def outer(n):
	def jiecheng(n,endval=1):
		if n == 1:
			return endval
		return jiecheng(n-1,n * endval)
	return jiecheng(n)
print(outer(5))  #120
# print(outer(5,1))  #120  #用户只能传一个参数,传2个,就会报错
#TypeError: outer() takes 1 positional argument but 2 were given

# 优化代码3(扩展)
# 闭包实现
def outer(n):
	endval = 1
	def jiecheng(n):  # n =5
		nonlocal endval
		if n == 1:
			return endval
		endval *= n  #累乘
		return jiecheng(n-1)
	return jiecheng
func = outer(5)
print(func(5))

# 代码解析
# n=5 endval = 1 * 5  return jiecheng(4)
# n=4 endval = 1 * 5 *4  return jiecheng(3)
# n=3 endval = 1 * 5 *4 *3   return jiecheng(2)
# n=2 endval = 1 * 5 *4 *3 *2    return jiecheng(1)
# n=1 endval = 1 * 5 *4 *3 *2 















