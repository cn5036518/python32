# ### 随机模块
import random

#第一组    random randrange  randint  uniform
#01 random() 获取随机0-1之间的小数(左闭右开) 0<=x<1   参数:无
print(random.random())  #0.5826224187371736
print('--------------------1 random')

#02 randrange() 随机获取指定范围内的整数(包含开始值,不包含结束值,间隔值) 
#***
print(random.randrange(1,10,2))  #1  3 5 7 9 随机取一个
# print(random.randrange(1,5.5,2))  #error
#ValueError: non-integer stop for randrange()
print(random.randrange(-5,0,2))  #-5,-3 -1 随机取一个
print('--------------------2 randrange')

#03 randint()   随机产生指定范围内的随机整数 (了解)  参数1:整数  参数2:整数 
# 特殊 (左闭右闭)
print(random.randint(1,2))  # 1 2 随机取一个
# print(random.randint(1,2.1))  # error
# ValueError: non-integer stop for randrange()
print(random.randint(-1,0))  # -1 0 随机取一个
print('--------------------3 randint')

#04 uniform() 获取指定范围内的随机小数(左闭右开)  ***  参数1:整数或小数  参数2:整数或小数
print(random.uniform(0,2))  #0.12483487854395459
print(random.uniform(0,1.5))  #1.4483276013556767
print(random.uniform(-2,0)) #-1.0941846304671883
print('--------------------4 uniform')
print('--------------------第一组  random randrange randint uniform')

#第二组
#01 choice()  随机获取序列中的值(多选一) 单项选择 **
# 参数:可迭代数据(容器 range 迭代器)(序列) 返回值:容器的一个元素
lst = [1,3,5]
res = random.choice(lst)
print(res)

res = random.choice(range(2))
print(res)
print('--------------------1 choice')

#02 sample()  随机获取序列中的值(多选多) [返回列表] **
# 参数 :参数1:可迭代数据(序列)  参数2:正整数 范围是0~序列的长度
# 返回值:可迭代数据
lst = ['a','b','c']
res = random.sample(lst,2)
print(res)  #['b', 'a']

# res = random.sample(lst,4) #error
# res = random.sample(lst,-2) #error
print('--------------------2 sample')

#03 shuffle() 随机打乱序列中的值(直接打乱原序列) **
# 参数    可迭代数据(序列)
# 返回值  None  (原可迭代数据的元素顺序打乱了)
lst = ['a','b','c']
res = random.shuffle(lst)
print(res) #None
print(lst)  #['c', 'b', 'a']

# it = range(3)
# random.shuffle(it)
# for i in it:
	# print(i)
# TypeError: 'range' object does not support item assignment
print('--------------------3 shuffle')


# import random
# 第一组小结
# random   #参数:无 												 返回值:[0,1)  0~1之间的小数  左闭右开
# randrange #参数:1个 2个或者3个整数(正整数 0 负整数) 不能是小数   返回值:指定范围内的随机整数  左闭右开   ***
	      # (开始值,结束值,步长)
# randint  #参数:2个整数 不能是小数                                返回值:指定范围内的随机整数  左闭右闭  (了解)
# uniform  # 参数:2个,整数或者小数都可  							 返回值:指定范围内的随机小数  左闭右开   ***


# 第二组小结默写
# choice  单选  **
	# 参数:可迭代数据(序列)
	# 返回值:可迭代数据的一个元素

# sample  多选  **
	# 参数:   
		# 参数1:可迭代数据   
		# 参数2:正整数  范围在0~可迭代数据的长度  超出会报错
	# 返回值: 
		# 可迭代数据

# shuffle  打乱容器的元素顺序  **
	# 参数:容器数据
	# 返回值:None  原容器数据的元素打乱了































