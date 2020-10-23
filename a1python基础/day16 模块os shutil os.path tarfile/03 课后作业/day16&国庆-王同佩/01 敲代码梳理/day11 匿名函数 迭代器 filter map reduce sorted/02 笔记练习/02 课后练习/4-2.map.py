#  ### 高阶函数 (map filter reduce sorter min max)
# 能够把函数当成参数传递的就是高阶参数
# map

# (1) 把列表中的元素都变成整型
lst = ["1","2","3","4"]
# 普通写法
lst_new = []
for i in lst:
	lst_new.append(int(i))
print(lst_new)  #[1, 2, 3, 4]

# map写法1
lst = ["1","2","3","4"]
def func(n):
	return int(n)

it = map(func,lst)  #自定义函数
print(list(it))  #[1, 2, 3, 4]

# map写法2
it = map(int,lst)  #int是内置函数
print(list(it)) #[1, 2, 3, 4]

# (2) [1,2,3,4] => [2,8,24,64]
# 1	1*2^1   2   左移1位
# 2	2*2^2 	8	左移2位
# 3	3*2^3	24	左移3位
# 4	4*2^4	64	左移4位

# 方法1 普通写法
lst = [1,2,3,4]
lst_new = []
for i in lst:
	lst_new.append(i<<i)
print(lst_new)  #[2, 8, 24, 64]

# 方法2 map
lst = [1,2,3,4]
def func(n):  #注意点:形参和返回值必须写;
	return n<<n
	
it = map(func,lst)
print(list(it))  #[2, 8, 24, 64]

# (3) 给你一个列表["a","b","c"] => [97,98,99]
# 字典的键值翻转操作
dic = {97:"a",98:"b",99:"c"}

#方法1 普通写法
dic_new = {}
for k,v in dic.items():
	dic_new[v] = k
print(dic_new)  #{'a': 97, 'b': 98, 'c': 99} #根据键获取值

lst = ["a","b","c"]
lst_new = []
for i in lst:
	lst_new.append(dic_new[i])
print(lst_new)  #[97, 98, 99]

#方法2 map
lst = ["a","b","c"]
def func(n):
	# print(n)  a b c
	dic = {97:"a",98:"b",99:"c"}
	dic_new = {}  #写成[] 拼写错误
	for k,v in dic.items():
		dic_new[v] = k
	# print(dic_new)
	return dic_new[n]  #传入的是键 返回的是值

it = map(func,lst)
print(list(it))  #[97, 98, 99]





































