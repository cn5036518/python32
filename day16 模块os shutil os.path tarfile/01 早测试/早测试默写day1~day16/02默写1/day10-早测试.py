# 1 文件相关的函数有哪些?
# open()
# read()
# write()
# readable()
# writable()
# seek()
# tell()

# readline() #读取一行
# readlines() #返回列表
# writelines()  #可迭代数据(元素是字符串)
# truncate()


# 2 如何按照行读取文件所有内容
strvar = """床前明月光
疑是地上霜
举头望明月
低头想家乡
"""
# 实现效果:写入文件,并且插入一句话:王文真帅呀 , 插在低头想家乡的前面

with open('poem.txt',mode='w+',encoding='utf-8') as fp:
	fp.write(strvar)
	fp.seek(0)
	lst = fp.readlines()
	print(lst)
	lst.insert(-1,'王文真帅呀\n')
	print(lst)
	fp.seek(0) #清空文件 必须加这个
	fp.truncate(0)
	fp.writelines(lst)

# 3什么是函数
# 实现一个功能,打包一组代码,实现一个动作

# 4什么是驼峰命名法
# 大驼峰 MyCat
# 小驼峰 myCat

# 5参数的种类及顺序
# 实参:普通实参,关键字实参
# 形参:普通形参(位置形参),默认形参,普通收集形参,命名关键字形参,关键字收集形参  (顺序也是)

# 6任意个数值得累加和
def func(*args):  #*在形参处,打包成元组
	# print(args)
	total = 0
	for i in args:
		total += i
	print(total)  #11

func(1,2,3,5)
print('------------------------------6')

# 7拼接任意个数值变成字符串
# 替换字典的键
def func(**kwargs): # **在形参处,将关键字参数打包成字典
	print(kwargs)
	#{'monitor': '赵万里', 'classflower': '马春培', 'water1': '刘子涛', 'water2': '李虎凌'}
	dic = {'monitor':'班长','classflower':'班花'}
	dic_new = {} #新字典,存放替换键后的数据  (班长替换monitor 班花替换classflower)
	for k,v in kwargs.items():
		# print(k,v)
		if k in dic:
			dic_new[dic[k]] = v
		else:
			dic_new[k] = v
	print(dic_new)  #完成替换键
	#{'班长': '赵万里', '班花': '马春培', 'water1': '刘子涛', 'water2': '李虎凌'}
	
	strvar1 = ''   #定义2个字符串,分别接受班长班花(已经替换键),划水群众(未替换键)
	strvar2 = ''		
	for k,v in dic_new.items():  #完成字符串拼接后打印
		if k.startswith('water'):
			strvar2 += v+','
		else:	
			strvar1 += (k +':'+ v + '\n')   #赋值运算符的优先级< 算数运算符
			
	print(strvar1.strip())
	print('划水群众:',strvar2.strip(','))
	
# 班长:赵万里
# 班花:马春培
# 划水群众: 刘子涛,李虎凌

func(monitor='赵万里',classflower='马春培',water1='刘子涛',water2='李虎凌')
print('------------------------------7')

#8写答案
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw): #d是命名关键字参数  实参必须指定关键字 比如 d=99 否则报错
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# 以上两个函数 打印结果
#(一)
f1(1, 2) # a =1 b=2 c=0 args=() kw={}
f1(1, 2, c=3) # a=1,b=2,c=3,args=() kw={}
f1(1, 2, 3, 'a', 'b') #a=1 b=2 c=3 args=(a,b) kw={}
f1(1, 2, 3, 'a', 'b', x=99) # a=1 b=2 c=3 args=(a,b) kw={x:99}
f2(1, 2, d=99, ext=None)#a=1 b=2 c=0 d=99 kw={ext:None}

#(二)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
# f1(1,2,3,4,d=99,x=#)
f1(*args, **kw) # a=1 b=2 c=3 args=(4,) kw={d:99,x:#}
# * ** 在实参处,将元组 列表 字典解包
# * ** 在形参处,将多余普通参数打包成元组,多余关键字参数打包成字典


#(三)
myargs = (1, 2, 3)
mykw = {'d': 88, 'x': '#'}
# f2(1,2,3,d=88,x=#)
f2(*myargs, **mykw) # a=1,b=2,c=3 d=88 kw={x:#}

#(四)
def f1(a, b, c=0, *args,d,**kw): #d是命名关键字参数
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
    print(d)

f1(1,2,3, 'a', 'b',d=67, x=99,y=77) # a=1 b=2 c=3 args=(a,b)  kw={x:99,y:77}
									# d=67

