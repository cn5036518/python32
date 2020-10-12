# ### 收集参数
# 普通收集形参定义:
# 专门用来收集那些多余的没人要的普通实参,
# 收集之后,会把多余实参打包成一个元组
# 普通收集形参-头上1个星星

def func(a,b,c,*args):
	print(a,b,c) #1 2 3
	print(args) #(4, 5, 6)
	# 这里的args前面没有*

func(1,2,3,4,5,6)

# 1 任意个形参的值的累加和
def mysum(*args):
	total = 0
	for i in args:
		total += i
	print(total)  #15
	return total

mysum(1,2,3,4,5)


# 2 关键字收集形参:
	# 专门用来收集那些多余的没人要的关键字实参
	# 收集之后,会把多余的关键字实参打包成一个字典
	# 关键字收集形参的写法:有2个星星

def func(a,b,c,**kwargs):
	print(a,b,c)
	print(kwargs)
func(c=1,a=3,b=10,f=100,e=200,z=12)


# 拼接任意个数值变成字符串 (修改字典的键)
# """
# 班长: 赵万里
# 班花: 马春陪
# 划水群众: 赵沈阳,李虎凌,刘子涛
# """

# 已知  实参
# monitor="赵万里",classflower="马春陪",water1="赵沈阳",
#water2="李虎凌",water3="刘子涛"

# dic = {"monitor":"班长","classflower":"班花"}

# 思路
# 将字典中的monitor替换成班长 classflower替换成班花 然后格式化输出
# {'monitor': '赵万里', 'classflower': '马春陪', 'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}
	
	# k       v
	# monitor 赵万里
	# classflower 马春陪
	# water1 赵沈阳
	# water2 李虎凌
	# water3 刘子涛

def func(**kwargs):
	strvar1 = ''
	strvar2 = ''
	# 定义职位信息
	dic = {'monitor':'班长','classflower':'班花'}
	print(kwargs)
	# {'monitor': '赵万里', 'classflower': '马春陪', 'water1': '赵沈阳', 'water2': '李虎凌'}
	# 一共4次循环
	for k,v in kwargs.items():
		print(k,v)
		# monitor 赵万里
# classflower 马春陪
# water1 赵沈阳
# water2 李虎凌
		if k in dic:
			strvar1 += dic[k] +':'+ v +'\n'  #拼接1  替换字典的键
		else:
			strvar2 += v + ','  #拼接2
	print(strvar1.strip())
	print('划水群众:{}'.format(strvar2.strip(',')))
	# 班长:赵万里
# 班花:马春陪
# 划水群众:赵沈阳,李虎凌

func(monitor='赵万里',classflower="马春陪",water1="赵沈阳",water2="李虎凌")































