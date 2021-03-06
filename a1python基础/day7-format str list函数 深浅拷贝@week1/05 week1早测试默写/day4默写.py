#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/20 11:50

# 1.布尔值为假的10种情况
# 2.True和False 在强制转换为 int float complex 时的值
# 3.Number的自动类型转换原则
# 4.容器类型转换的特点
# 5.写一个等长的二级容器
# 6.什么样的类型可以转化成字典
# 7.[1,2,3,4,[5,6,7,[8,9,10,(11,{'a':{'bb':98},'pp':{'d':'bingo'}})]]]
# 8.判断类型的方法有几个

# 1.布尔值为假的10种情况
# number	int    0
		# float  0.0
		# bool   False
		# complex  0j
# 容器类型
		# str  	''
		# tuple   ()
		# list	[]
		# dict	{}
		# set 	set()
# None

# 2.True和False 在强制转换为 int float complex 时的值
	# True  
		# int 1
		# float 1.0
		# complex 1+0j
	# False
		# int	0
		# float  0.0
		# complex  0+0j	

# 3.Number的自动类型转换原则
    # 精度从低到高
	# bool  int float  complex
	# 低精度默认向高精度进行转换

# 4.容器类型转换的特点
	# str  
		# 所有的数据类型都可以转换，在当前的数据类型两边套上引号
	# tuple
		# 如果是字符串：把字符串的每个元素单独拿出来，作为元组的新元素
		# 如果是字典：  只保留字典中的键
		# 如果是其他容器数据（list set）：
			# 就是单纯的在原数据类型的两边换上()小括号		
	# list
		# 如果是字符串：把字符串的每个元素单独拿出来，作为列表的新元素
		# 如果是字典：  只保留字典中的键
		# 如果是其他容器数据（tuple set）：
			# 就是单纯的在原数据类型的两边换上[]中括号
	
	# dict
		# 要求：必须是等长的二级容器，并且里面的元素个数是2个
		# 外层是列表或元组，里层是列表或元组的等长的二级容器
		# 外层是集合，里层只能是元组（不能是列表，因为集合的元素是不可变类型）
	
	# set
		# 如果是字符串：把字符串的每个元素单独拿出来，作为集合的新元素
		# 如果是字典：  只保留字典中的键
		# 如果是其他容器数据（tuple list）：
			# 就是单纯的在原数据类型的两边换上{}大括号


# 5.写一个等长的二级容器
[(1,3),[2,4]]

# 6.什么样的类型可以转化成字典
# dict
		# 要求：必须是等长的二级容器，并且里面的元素个数是2个
		# 外层是列表或元组，里层是列表或元组的等长的二级容器
			# 里层不推荐放集合（无序）或者字符串（字符串长度只能是2位，局限性大）
		# 外层是集合，里层只能是元组（不能是列表，因为集合的元素是不可变类型）

# 7.[1,2,3,4,[5,6,7,[8,9,10,(11,{'a':{'bb':98},'pp':{'d':'bingo'}})]]] 获取bingo
strvar = [1,2,3,4,[5,6,7,[8,9,10,(11,{'a':{'bb':98},'pp':{'d':'bingo'}})]]]
print(strvar[-1][-1][-1][-1]['pp']['d'])

# 8.判断类型的方法有几个
# 方法1
res = isinstance(n,int)

# 方法2
res = isinstance(n,(int,float,bool,complex))  #参数2的类型是元组
res = isinstance(n,(str,tuple,list,dict,set))


















































