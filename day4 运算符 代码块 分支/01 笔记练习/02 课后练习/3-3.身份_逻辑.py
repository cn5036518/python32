# (5)身份运算符 is 和 is not (检测两个数据在内存当中是否是同一个值)   py3.6.12 小数据池

# 整型 -5~正无穷 
var1 = 100
var2 = 100
print(var1 is var2)  #True

var1 = -6
var2 = -6
print(var1 is var2)  #False

# 浮点型 非负数
var1 = -9.1
var2 = -9.1
print(var1 is var2) #False

var1 = 0.0
var2 = 0.0
print(var1 is var2)  #True

# bool 相同即可
var1 = True
var2 = True
print(var1 is var2)

# complex 在实数+虚数不相同 (只有正虚数的情况下例外)
var1 = 6-8j
var2 = 6-8j
print(var1 is var2)  #False

var1 = -10j
var2 = -10j
print(var1 is var2)  #False

var1 = 10j
var2 = 10j
print(var1 is var2)  #True

# 容器: 相同字符串 , 空元组相同即可  剩下的所有容器都不相同
container1 = ()
container2 = ()
print(container1 is not container2) #False

container1 = "你"
container2 = "你"
print(container1 is not container2)  #False

container1 = [1,23,3]
container2 = [1,23,3]
print(container1 is not container2)  #True
print('---------------------------1 身份运算符')

# (6)逻辑运算符:  and or not
# 01 and 逻辑与   
# """全真则真,一假则假"""
res = True and True
print(res) #True

res = True and False
print(res) #False

res = False and False
print(res) # False

res = False and True
print(res) # False
print('---------------------------and 逻辑与')

# 02 or  逻辑或  
# """一真则真,全假则假"""
res = True or True
print(res) #True

res = True or False
print(res) #True

res = False or False
print(res) # False

res = False or True
print(res) # True
print('---------------------------or 逻辑或')

# 03 not 逻辑非 
res = not True
res = not False
print(res)

# 04 逻辑短路
# 定义:无论后面的表达式是True 还是False 都已经无法改变最后的结果,
# 那么直接短路,后面的代码不执行

# 计算规律:
	# 先脑补计算当前表达式的布尔值是True还是False
	# 如果出现了 True or 表达式  或者 False and 表达式的情况,直接返回前者,后面代码不执行
	# 如果没有出现短路效果,直接返回后者

# 逻辑短路的情况
# True or    False and  返回前者
# 非逻辑短路,  返回后者

res = 5 and 6
print(res)  #6

res = 5 or 6 
print(res) #5

res = 0 and 999
print(res) #0

res = 0 or 'abc'
print(res)  #abc
print('--------------------------- 逻辑短路 True or   False and')

# 05 逻辑运算符的优先级
# 优先级从高到低    () > not > and > or
res = 5 or 6 and 7
res = 5 or 7
res = 5
print(res)  #5

res = (5 or 6) and 7
res = 5 and 7
res =  7
print(res)  #7

res = not (5 or 6) and 7
res = not 5 and 7
res = False and 7
res = False
print(res) #False

res = 1<2 or 3>4 and 5<100 or 100<200 and not (700>800 or 1<-1)
res = True or False and True or True and not (False or False)
res = True or False and True or True and not False
res = True or False and True or True and True
res = True or False  or  True
res = True   or  True
res = True 
print(res) #True
print('--------------------------- 逻辑运算优先级  () not and or )
















































