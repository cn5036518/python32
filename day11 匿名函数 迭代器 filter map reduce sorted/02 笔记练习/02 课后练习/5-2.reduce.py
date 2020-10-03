# ### reduce
# (1) [7,7,5,8] => 7758
# 方法1 普通写法
lst = [7,7,5,8]
strvar = ''
for i in lst:
	strvar += str(i)
print(int(strvar))  #7758

# 方法2  reduce
# 规律
# 7 * 10 + 7 =77
# 77 * 10 + 5 = 775
# 775 * 10 + 8 = 7758
from functools import reduce

lst = [7,7,5,8]
def func(x,y):
	res = x*10 + y
	return res

res2 = reduce(func,lst)
print(res2)  #7758

res2 = reduce(lambda x,y:x*10+y,lst)
print(res2)
print('-----------------1')

# 方法3 迭代器
# 规律
# 7 * 10 + 7 =77
# 77 * 10 + 5 = 775
# 775 * 10 + 8 = 7758
lst = [7,7,5,8]

it = iter(lst)
# 获取前2个数字
num1 = next(it)  #7
num2 = next(it)  #7
# 前2个数字做计算
total = num1*10 + num2
print(total)
# 获取余下的所有数字
for i in it:
	total = total * 10 +i
print(total)  #7758

# (2) "123" => 123 不使用int的情况下实现该操作;
#思路  
# '123'  ==>[1,2,3]  map
# [1,2,3] ==> 123 reduce

# 方法1 
strvar = '123'
# dic = {'1':1,'2':2,'3':3}

# dic2 = {}
# for i in range(10):
	# dic2[str(i)] = i
# print(dic2)
# {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def func(n):
	dic2 = {}
	for i in range(10):
		dic2[str(i)] = i
	# print(dic2)
	return dic2[n]
it = map(func,strvar)
# print(list(it))  #[1, 2, 3]

def func(x,y):
	return x*10 + y

res = reduce(func,list(it))
print(res)  #123






































