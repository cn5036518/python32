# ### for循环
# 遍历 循环 迭代 , 把容器中的元素一个一个获取出来

# # while循环在遍历数据时的局限性
# while循环不能遍历集合,因为集合的无序,但是for可以遍历集合

# for循环的基本语法
# """
# Iterable 可迭代性数据：1.容器类型数据str tuple list dict set
# 2.range对象 3.迭代器
# for 变量 in Iterable:
	# code1.


# 1.遍历不等长多级容器
container = [1,2,3,4,("嗄","234",{"马春配","李虎凌","刘子涛"})]

for i in container:
	if isinstance(i,(tuple,)):
		for j in i:
			if isinstance(j,(set,)):
				for i in j:
					print(i)
			else:
				print(j)
	else:
		print(i)
# 1
# 2
# 3
# 4
# 嗄
# 234
# 李虎凌
# 马春配
# 刘子涛
print('---------------------1')

# 2.遍历不等长多级容器
container = [("刘玉波","历史源","张光旭"), ("上朝气","于朝志"),("韩瑞晓",)]
for i in container:
	for j in i:
		print(j)
print('---------------------2')
# 刘玉波
# 历史源
# 张光旭
# 上朝气
# 于朝志
# 韩瑞晓

# 变量的解包
a,b,c = 'poi'
print(a,b,c)

a,b = (1,3)
print(a,b)

a,b = 1,2
print(a,b)

a,b,c = [10,11,12]
print(a,b,c)

a,b = {"lmh":"林明辉","jsx":"家率先"}
print(a,b)  #lmh jsx   #字典解包取的是键

a,b = {"林明辉","家率先"}
print(a,b)

# 3.遍历等长的容器
container = [("马云","小马哥","马春配") , ["王健林","王思聪","王志国"],{"王宝强","马蓉","宋小宝"}]
for i in container:
	for j in i:
		print(j)

for a,b,c in container:
	print(a,b,c)
# 马云 小马哥 马春配
# 王健林 王思聪 王志国
# 马蓉 宋小宝 王宝强


# ### range对象
# """
# range([开始值,]结束值[,步长])
# 取头舍尾,结束值本身获取不到,获取到它之前的那一个数据
# """

# range(一个值)
for i in range(2):
	print(i)

# range(二个值)
for i in range(0,2):
	print(i)

# range(三个值 正向)
for i in range(0,5,2):
	print(i)
	
# range(三个值 逆向)
for i in range(10,0,-2):
	print(i)

# 总结:
# """
# while 一般用于处理复杂的逻辑关系
        # 不能遍历集合
		# 不推荐和continue一起使用
# for   一般用于迭代数据
		# 不支持死循环
# 部分情况下两个循环可以互相转换;
# """




































