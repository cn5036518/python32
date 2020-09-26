''''''
'''

# 1文件相关的函数有哪些?
flush()  刷新缓冲区

readable() 判断是否可读
writable()  判断是否可写 

seek()   单位是字节     seek(0) 文件开头  seek(0,2) 文件结尾

read()      读取全部  单位：字符
write()     写入  参数是str  文件中存储的都是字符串

readline()  每次读取一行  #迭代器 生成器
readlines() 按行读取，每一行作为列表的一个元素
writelines()  一次写入多行，参数：可迭代数据，数据的元素必须是字符串，而不能是int 注意点
truncate()    截取  单位是字节（utf-8下 一个中文字符占3个字节


01刷新缓冲区的4种方法
1 手动刷新
2 缓冲区满了，自动刷新
3 文件关闭的时候，自动刷新  fp.close()
4 程序运行结束的时候，自动刷新

02readline()  每次读取一行  #迭代器 生成器
    默认无参数：每次读取一行
    有参数：r模式下，单位是字符数
                字符数>当前行字符数  读取一行
                字符数<当前行字符数  读取指定的字符数内容
            rb模式下，单位是字节数

03将文件中的内容按照换行读取到列表当中,要求返回标准列表
    --readlines

04 writelines()  一次写入多行，参数：可迭代数据，数据的元素必须是字符串，而不能是int 注意点


# 2如何按照行读取文件所有内容
# strvar = """
# 床前明月光
# 疑是地上霜
# 举头望明月
# 低头想家乡
# """
# 实现效果:写入文件,并且插入一句话:王文真帅呀 , 插在低头想家乡的前面

# 3什么是函数
	功能：实现一个功能，包裹一部分代码，达成一个目的

# 4什么是驼峰命名法
	大驼峰  MyCar
	小驼峰  myCar

# 5参数的种类及顺序
	实参
		普通参数（位置参数） 关键字参数
	形参
		普通参数
		默认参数
		普通收集参数   *
		命令关键字参数  *，之后的参数    *args 和 **kwargs之间的参数
		关键字收集参数 **
		
	顺序：
		形参从前到后依次是：
			普通参数，默认参数，普通收集参数，命名关键字参数，关键字收集参数
		实参从前到后依次是：
			普通实参，关键字实参
			
	星号  *   **
	一个*   
		实参处
			将元组解包
		
		形参处
			打包成元组 （将多余的普通参数打包成元组）
			
	两个*   **
		实参处
			将字典解包成关键字参数 a=1 b=2
		
		形参处
			打包成字典 （将多余的关键字参数打包成字典）
	
	

# 6任意个数值得累加和
# 7拼接任意个数值变成字符串
# #写答案
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# 
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# # 以上两个函数 打印结果

# def f1(a, b, c=0, *args, **kw):  形参处 *args 打包成元组    **kw 打包成字典
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# #(一)
# f1(1, 2) #  a=1 b=2 c=0 args=() kw={}
# f1(1, 2, c=3) #  a=1 b=2 c=3 args=() kw={}
# f1(1, 2, 3, 'a', 'b') #a=1 b=2 c=3 args=('a','b') kw={}
# f1(1, 2, 3, 'a', 'b', x=99) # a=1 b=2 c=3 args=('a','b') kw={x:99}

# def f2(a, b, c=0, *, d, **kw):  #d是命名关键字参数 对应的实参必须指定关键字，否则报错
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# f2(1, 2, d=99, ext=None)# a=1 b=2 c=0 d=99 kw={ext:None}
# 
# #(二)
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}

# # f1(1,2,3,4,d=99,x=#) 实参解包后的
# f1(*args, **kw) # 实参  #a=1 b=2 c=3 args=(4,) kw={d:99,x:#}
# 
# 
# #(三)
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# myargs = (1, 2, 3)
# mykw = {'d': 88, 'x': '#'}
# # f2(1,2,3,d=88,x=#)
# f2(*myargs, **mykw) # a=1 b=2 c=3 d=88 kw={x:#}  #d=88已经被使用了，所以kw不会收集了
# 
# #(四)
# def f1(a, b, c=0, *args,d,**kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#     print(d)
# 
# f1(1,2,3, 'a', 'b',d=67, x=99,y=77) # a=1 b=2 c=3 args=('a','b'),kw={x:99,y:77})
# 									# 67

# 5.等待用户输入内容，是否包含敏感字符？
# 如果存在敏感字符提示“存在敏感字符请重新输入”，敏感字符：“粉嫩”、“铁锤”

'''

# 5.等待用户输入内容，是否包含敏感字符？
# 如果存在敏感字符提示“存在敏感字符请重新输入”，敏感字符：“粉嫩”、“铁锤”


# 第一题
# 03将文件中的内容按照换行读取到列表当中,要求返回标准列表（去掉空白字符等）
#     --readlines
lst_new = []
def func():
	with open('a.txt',mode='r',encoding= 'utf-8') as fp:
		lst = fp.readlines()
		for i in lst:
			lst_new.append(i.strip())
	print(lst_new)
	return lst_new
func()  #['jack', 'tom', 'bob']
print('---------------1')

# 2如何按照行读取文件所有内容
strvar = """床前明月光
疑是地上霜
举头望明月
低头想家乡
"""
# 实现效果:写入文件,并且插入一句话:王文真帅呀 , 插在低头想家乡的前面
with open('2.txt',mode='w+',encoding= 'utf-8') as fp:
	fp.write(strvar)
	fp.seek(0)
	lst = fp.readlines()
	print(lst)  #['床前明月光\n', '疑是地上霜\n', '举头望明月\n', '低头想家乡\n']
	
	lst.insert(-1,'王文真帅呀\n')
	print(lst)
	
	fp.seek(0)
	# lst = [1,2,3]  #TypeError: write() argument must be str, not int
	# 报错原因是：可迭代数据的元素是int 而不是str
	fp.writelines(lst)  #这里的参数lst必须是可迭代数据，且可迭代数据的元素必须是字符串

# 6任意个数值得累加和（计算多个普通参数的和）
def func(*args):
	# print(args)  #(1, 3, 5, 7, 9)
	total = 0
	for i in args:
		total += i
	print(total)  #25
	return total
	
res = func(1,3,5,7,9)
print(res)  #25

# 7拼接任意个数值变成字符串（修改字典的键）
"""
班长: 赵万里
班花: 马春陪
划水群众: 赵沈阳,李虎凌,刘子涛
"""

# 1完成新字典的打印
def func(**kwargs):
	dic = {'monitor':'班长','classflower':'班花'}
	print(kwargs)  #{'monitor': '赵万里', 'classflower': '马春陪', 'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}
	dic_new = {}
	for k,v in kwargs.items():
		if k in dic:
			dic_new[dic[k]]=v  #{'班长': '赵万里', '班花': '马春陪'}  #关键点
		else:
			dic_new[k]=v  #{'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}
	print(dic_new)  #{'班长': '赵万里', '班花': '马春陪', 'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}
	

func(monitor="赵万里",classflower="马春陪",water1="赵沈阳",water2="李虎凌",water3="刘子涛")

# 思路
# 1 实现   --ok
	# dic = {'班长':"赵万里",'班花':"马春陪",water1="赵沈阳",water2="李虎凌",water3="刘子涛"}
# 2 先字典打印  --ok
# 3 后拼接字符串

# 2 后拼接字符串输出
"""
班长: 赵万里
班花: 马春陪
划水群众: 赵沈阳,李虎凌,刘子涛
"""
def func(**kwargs):
	dic = {'monitor': '班长', 'classflower': '班花'}
	print(kwargs)  # {'monitor': '赵万里', 'classflower': '马春陪', 'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}
	dic_new = {}
	strvar1 = ''
	strvar2 = ''

	for k, v in kwargs.items():
		if k in dic:
			strvar1 += (dic_new[dic[k]] + ':' + v)  # {'班长': '赵万里', '班花': '马春陪'}  #关键点
		else:
			dic_new[k] = v  # {'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}
	print(dic_new)  # {'班长': '赵万里', '班花': '马春陪', 'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}
	print(strvar1)

func(monitor="赵万里", classflower="马春陪", water1="赵沈阳", water2="李虎凌", water3="刘子涛")












































