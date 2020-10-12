# ### 收集形参
# 普通形参:
	# 专门用来收集多余的没人要的普通实参,收集之后,会把多余实参打包成一个元组
	
def func(*args):
	pass
	
def func(a,b,c,*args):
	print(a,b,c)  #1 2 3
	print(args)  #(4, 5, 6)  #这里没有*
	
func(1,2,3,4,5,6)
	
# 任意个数的实参值的累加和
def mysum(*args):
	print(args)  # 元组
	total = 0
	for i in args:
		total += i
	print(total)  #18
	
mysum(1,2,3,4,8)
print('-------------------1')

# 2 关键字收集形参:
	# 专门用来收集那些多余的没人要的关键字实参收集之后,
	# 会把多余关键字实参打包成一个字典
	# 参数前面you2个星星
# def func(**kwargs):
	# pass
# kwargs ==> keyword arguments

def func(a,b,c,**kwargs):  #**lwargs 形参把关键字实参打包成字典
	print(a,b,c) #3 10 1
	print(kwargs)  #{'f': 100, 'e': 200, 'z': 12}
func(c=1,a=3,b=10,f=100,e=200,z=12)
print('-------------------2')

# 拼接任意个数值变成字符串
# 替换字典的键,把monitor变成班长,classflower变成班花,把water变成划水群众
# 输出结果如下

# 班长: 赵万里
# 班花: 马春陪
# 划水群众: 赵沈阳,李虎凌

def func(**kwargs):  #**kwargs 形参把关键字实参打包成字典
	strvar1 = ''
	strvar2 = ''

	print(kwargs)   #**kwargs 形参把关键字实参打包成字典
	#{'monitor': '赵万里', 'classflower': '马春培', 
	# 'water1': '赵沈阳', 'water2': '李虎凌'}
	
	# 定义职位信息
	dic = {'monitor':'班长','classflower':'班花'}
	
	for k,v in kwargs.items():
		if k in dic:
			# 将2次循环的结果通过+=拼接在一起
			strvar1 += dic[k] + ":" + v +'\n'
		else:
			# 将3次循环的结果通过+=拼接在一起
			strvar2 += v + ','
	print(strvar1.strip())
	print('划水群众:',strvar2.strip(','))


func(monitor='赵万里',classflower='马春培',water1='赵沈阳',water2='李虎凌')
print('-------------------3-1')

# 拼接任意个数值变成字符串
# 替换字典的键,把monitor变成班长,classflower变成班花,把water变成划水群众
# 输出结果如下

# 班长: 赵万里
# 班花: 马春陪
# 划水群众: 赵沈阳,李虎凌

def func(**kwargs):  #**kwargs 形参把关键字实参打包成字典
	strvar1 = ''
	strvar2 = ''

	print(kwargs)  #{'monitor': '赵万里', 'classflower': '马春培', 'water1': '赵沈阳', 'water2': '李虎凌'}
	dic = {'monitor':'班长','classflower':'班花'}
	for k,v in kwargs.items():
		if k in dic:
			strvar1 += dic[k] + ':' + v +'\n'
		else:
			strvar2 += v + ','
	print(strvar1.strip())
	print('划水群众',strvar2.strip(','))

func(monitor='赵万里',classflower='马春培',water1='赵沈阳',water2='李虎凌')
print('-------------------3-2')


# 拼接任意个数值变成字符串
# 替换字典的键,把monitor变成班长,classflower变成班花,把water变成划水群众
# 输出结果如下

# 班长: 赵万里
# 班花: 马春陪
# 划水群众: 赵沈阳,李虎凌

# 步骤: 1先打印  2拼接字符串

# 1打印
def func(**kwargs):  #**kwargs 形参把关键字实参打包成字典
	print(kwargs)  #{'monitor': '赵万里', 'classflower': '马春培', 'water1': '赵沈阳', 'water2': '李虎凌'}
	dic = {'monitor':'班长','classflower':'班花'}
	for k,v in kwargs.items():
		# print(k,v)
		if k in dic:
			print(dic[k] + ':' + v)  #替换键
		else:
			print(v)

func(monitor='赵万里',classflower='马春培',water1='赵沈阳',water2='李虎凌')
print('-------------------3-3')


# 2 拼接字符串
def func(**kwargs):  #**kwargs 形参把关键字实参打包成字典
	strvar1 = ''
	strvar2 = ''

	print(kwargs)  #{'monitor': '赵万里', 'classflower': '马春培', 'water1': '赵沈阳', 'water2': '李虎凌'}
	dic = {'monitor':'班长','classflower':'班花'}
	for k,v in kwargs.items():
		# print(k,v)
		if k in dic:
			# print(dic[k] + ':' + v)  #替换键
			strvar1  += (dic[k] + ':' + v + '\n')
		else:
			# print(v)
			strvar2 += v + ','   #优先级 , +(算数运算符)  >  +=(赋值运算符)
	print(strvar1.strip())
	print('划水群众:',strvar2.strip(','))

func(monitor='赵万里',classflower='马春培',water1='赵沈阳',water2='李虎凌')
print('-------------------3-4')














	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	