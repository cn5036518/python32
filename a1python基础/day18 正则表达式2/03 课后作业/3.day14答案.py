# 1.结果
# """ 默认参数身上的默认值会提前在内存中驻留 , 方便找到默认值 """
def extendList(val,list=[]):
    list.append(val)
    return list
list1 = extendList(10)   
print(list1)  # [10]  
list2 = extendList(123 , []) 
print(list2)  # [123]
list3 = extendList('a')   
print(list3)  # [10,a]

# 2.res是多少?
def func():
	return [lambda x : i*x    for i in range(4)]
res = [m(2) for m in func()]

# [    lambda x : i*x    for i in range(4)      ]
res = [     lambda x : i*x        for i in range(4)      ]

def func():
	lst = []
	for i in range(4):
		def niming(x): # x=2 i=3
			return i*x
		lst.append(i*x)
	return lst
lst = func()
print(lst)
[

<function func.<locals>.niming at 0x000001D6761EB8C8>,  
<function func.<locals>.niming at 0x000001D6761EB950>, 
<function func.<locals>.niming at 0x000001D6761EB9D8>, 
<function func.<locals>.niming at 0x000001D6761EBA60>

]

res = [m(2) for m in lst] #  0 2 4 6 
res = [i for i in range(34)]
res = [ 1 for i in range(4) ]
# 为什么i是3
# """
# for i in range(4):
	# print(i)

# print(i)
# print(i)
# print(i)
# print(i)
# print(i)
# print(i)
# """

# """
# 1.判断返回值到底是推导式还是匿名函数.
# 2.定义函数时,里面的代码一句都不走
# 3.只有在调用函数时,才会执行其中的代码块,此刻去找寻当时的i , 已经通过循环遍历到3 了.
# 4.由于当时变量i与内函数发生绑定,延长该变量的生命周期,所以内存没有释放,仍然可以找到
# 5.在列表中是4个函数,通过传递参数x = 2 , i = 3 return 6  , 返回 4个 6
# """


# 3.打印结果是多少?
def add(a,b):                     
    return a + b
def test():                       
    for r in range(4): 
        yield r
g=test() 
for n in [2,10]:
	g=(add(n,i) for i in g)
print(n)
print(list(g))
	
for n in [2,10]:
	print(n)
	
	
print(n)
print(n)
print(n)
print(n)
	
# 4.如何判断输入的数是质数( 1.通用方法完成 2.使用for .. else 完成 )
# """大于1的自然数,除了1和他本身,没有任何因数"""
# """如果循环被意外终止,else这个分支不执行"""
n = 13
if n > 1:
	for i in range(2,n):
		if n % i == 0:
			print("不是质数")
			break			
	else:
		print("是质数")		
else:
	print("不是质数")


n = 13
sign = False
if n > 1:
	for i in range(2,n):
		if n % i == 0 :
			sign = True
			break			
	if sign:
		print("不是质数")
	else:
		print("是质数")
		
else:
	print("不是质数")




# 5.计算文件夹大小
import os
print(os.getcwd())
# os.path.getsize




















