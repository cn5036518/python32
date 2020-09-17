# ### for循环
# 遍历 循环 迭代 ,把容器中的元素一个一个获取出来

# while循环在遍历数据时的局限性
# while循环不支持遍历--集合(因为集合无序,获取不到索引号)

lst = [1,2,3,4,5]   #ok
i = 0
while i < len(lst):
	print(lst[i])
	i += 1
print('-----------1')
	
# setvar = {'a','b','c'}	 #not ok
# i = 0
# while i < len(setvar):  #集合不能获取索引号
	# print(setvar[i])  #TypeError: 'set' object is not subscriptable
	# i += 1

#for 循环的基本语法
'''
iterable 可迭代的数据:1.容器类型数据  2.range对象  3 迭代器
for 变量 in iterable:
	code1.
'''
# 字符串
container = '北京和深圳温差大概20多度'
# 列表
container = [1,2,3,4,4,5]
# 元组
container = ('孙开玺','孙健','孙悟空')
# 集合
container = {'陈璐','曹静怡'}
# 字典
container = {'cl':'风流倜傥','cjy':'拳击选手'}

# 遍历数据
for i in container:
	print(i)
print('-----------2')

#1.遍历不等长多级容器
container = [1,2,3,4,('噶','234',{'马春配','李虎林','刘子涛'})]

for i in container:
	# 判断当前元素是否是容器,如果是,进行二次遍历,如果不是,直接打印
	if isinstance(i,tuple):
		# ('噶','234',{'马春配','李虎林','刘子涛'})
		for j in i:
			#判断当前元素是否是集合,如果是,进行三次遍历,如果不是,直接打印
			if isinstance(j,set):
			# {'马春配','李虎林','刘子涛'}
				for k in j:
					print(k)
			else:
				print(j)
	#打印数据
	else:
		print(i)
print('-----------1')
# 1
# 2
# 3
# 4
# 噶
# 234
# 马春配
# 李虎林
# 刘子涛

#2.遍历不等长多级容器
container = [('刘玉波','李世元','张光绪'),('尚照奇','于朝志')]
for i in container:
	for j in i:
		print(j)

# 刘玉波
# 李世元
# 张光绪
# 尚照奇
# 于朝志
print('-----------2')

#3. 遍历等长的容器
container = [('马云','小马哥','马春配'),('王健林','王思聪','王志国')]
for a,b,c in container:
	print(a,b,c)
	
# 马云 小马哥 马春配
# 王健林 王思聪 王志国

# 变量的解包
a,b,c = 'poi'
a,b = (1,2)
a,b = 1,2
a,b,c = [10,11,12]
a,b = {'林明辉','贾帅贤'}
a,b = {'lmh':'林明辉','jsx':'贾帅贤'}
# a,b,c = ('马云','小马哥','马春配')
print('-----------3')

# ### range 对象
'''
range([开始值,]结束值[,步长])
去头舍尾,结束值本身获取不到,获取到它之前的那一个数据
'''

# range(一个值)
for i in range(5): # 0~4
	print(i)
print('-----------4-1')
	
# range(二个值)
for i in range(3,8):
	print(i)
print('-----------4-2')

# range(三个值) #正向的从左到右 步长是正数
for i in range(1,11,3):  #1 4 7 10
	print(i)
print('-----------4-3')

# range(三个值) 逆向的从右到左 步长是负数
for i in range(10,0,-1):  # 10 9 8 7 ... 1
	print(i)
print('-----------4-4')

# 总结:
'''
while 一般用于处理复杂的逻辑关系
	     while不支持遍历集合
		while的continue,上行必须是i +=1 否则,会出现死循环

for 	一般用于迭代数据,更简洁
		for不支持死循环
部分情况下,两个循环可以相互转换;
'''

# 乘法表
# 方法1  while
i = 1
while i <= 9:
	j = 1
	while j <= i:
		print('%d*%d=%2d ' % (i,j,i*j),end='')
		j += 1
	print()
	i += 1
print('-----------5-1')

# 方法2  for
for i in range(1,10):
	for j in range (1,i+1):  #这里是i+1 ,不是i
		print('%d*%d=%2d ' % (i,j,i*j),end='')
	print()
print('-----------5-2')

#打印 1 ~ 10 跳过5
# 方法1  while
i = 1
while i <= 10:
	if i == 5:
		i += 1  #手动自增1
		continue   #后面的代码不执行
	print(i)  #这个的位置
	i +=1	
print('-----------6-1')

# 方法2  for
for i in range(1,11):
	if i == 5:
		continue
	print(i)
print('-----------6-2')













































	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	