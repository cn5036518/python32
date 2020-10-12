# ### reduce
# reduce(func,iterable)
# 功能:
	# 计算数据
	# 把iterable中的前两个数据扔到func函数中做计算,
	# 把计算的结果和iterable中第三个值再继续放到func中做计算,
	# 以此类推...
	# 最后返回计算的结果

# 参数:
	# func:自定义函数
	# iterable:可迭代对象(容器数据类型,range对象,迭代器)
# 返回值:
	# 计算的结果

# 1 把[7,7,5,8]变成7758

# 方法1
	# 拼接字符串
lst = [7,7,5,8]
strvar = ''
for i in lst:
	strvar += str(i)
res = int(strvar)
print(res)  # 7758
print('------------------------1')	

# 方法2  列表转换成迭代器 (普通方法)
# 规律
# 7   * 10 + 7 = 77
# 77  * 10 + 5 = 775
# 775 * 10 + 8 = 7758

# 1.先变成迭代器
lst = [7,7,5,8]
it = iter(lst)

# 2.取出前面的2个值
num1 = next(it)  #7
num2 = next(it)  #7
print(num1,num2)  #7 7

#  做计算(前2个值)
total = num1 * 10 + num2
print(total) #77

#3.把前2个值的计算结果和剩下的数据做计算
for num in it:  #迭代器已经取出了前面的2个数据,还有后面的2个数据
	total = total * 10 + num  #775  7758   关键点
	
#4.返回最后的结果
print(total,type(total))  #7758 <class 'int'>
print('------------------------2')	

# 方法3 reduce改写方法2
from functools import reduce
lst = [7,7,5,8]
def func(x,y): #2个形参
	# print(x,y)
	# 7 7
	# 77 5
	# 775 8
	return x * 10 + y
	
res = reduce(func,lst)
print(res)  #7758
print('------------------------3')	

# 方法4 使用lambda 改造reduce
res = reduce(lambda x,y:x*10+y,lst)
print(res)
print('------------------------4')	

# 2   '123'==>123 不使用int的情况下实现该操作

# 方法1  map  reduce
strvar = '123'
def func(x,y):
	return x * 10 + y
	
# 把字符串'123' 处理成数字123
def func2(n):
	dic = {}
	# dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	for i in range(10):
		dic[str(i)] = i
	# print(dic) 
	#{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	# print(dic[n])  #2
	return dic[n]
	
# func2('2')
	
it = map(func2,strvar)
# print(list(it))  #[1, 2, 3]
res = reduce(func,it)
print(res,type(res))  #123 <class 'int'>
print('------------------------2-1')	

# 方法2  map  reduce  lambda
strvar = '123'
	
# 把字符串'123' 处理成数字123
def func2(n):
	dic = {}
	# dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	for i in range(10):
		dic[str(i)] = i
	# print(dic) 
	#{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	# print(dic[n])  #2
	return dic[n]
	
# func2('2')
	
it = map(func2,strvar)
# print(list(it))  #[1, 2, 3]
res = reduce(lambda x,y:x*10 +y ,it)
print(res,type(res))  #123 <class 'int'>
print('------------------------2-2')	

































