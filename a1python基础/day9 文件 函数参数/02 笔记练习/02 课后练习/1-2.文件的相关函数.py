fp = open('ceshi1.txt',mode='w',encoding='utf-8')
fp.write('abc')

# fp.flush()

# while True:
# 	pass

fp.close()

# 0  readbale()  writable()
fp = open('ceshi1.txt',mode='r',encoding='utf-8')
print(fp.readable())  #True  可读
print(fp.writable())  #False 可写
# 遍历fp文件对象
for i in fp:
	print(i)  #abc


# 1 readline()  #读取一行文件内容 返回str
# 参数为空，读取一行。参数也可以是字符数（字节数）
with open('ceshi1.txt',mode='r',encoding='utf-8') as fp:
	res = fp.readline()
	print(res)  #abc
	res = fp.readline()
	print(res,type(res))  #  <class 'str'>  空行
	res = fp.readline()
	print(res,type(res))  #  <class 'str'>  空行
print('---------------1-1')
 
# 01 一次把所有内容都读取出来  （只用readline()实现）
fp = open('ceshi1.txt',mode='w',encoding='utf-8')
# fp.write('\n')
fp.write('abc\n')
fp.write('bc')

with open('ceshi1.txt',mode='r',encoding='utf-8') as fp:
    #1 先读取一行
	res = fp.readline().strip()  #如果第一行是空行，就不循环了
	# 2 判断是不是空 不是空再循环
	while res:
		print(res)
		# 再读取一行，放在34行while循环中判断
		res = fp.readline()
print('---------------1-2')

# 02 readline(读取的字符数)  #r模式是字符数  rb模式是字节数
with open('ceshi1.txt',mode='r',encoding='utf-8') as fp:
	# res = fp.readline(300)  #abc
	res = fp.readline(1)  #a
	print(res)  
print('---------------1-3')

# 2 readlines()  功能：将文件中的内容按照换行读取到列表中  返回list 参数为空
lst_new = []
with open('ceshi1.txt',mode='r+',encoding='utf-8') as fp:
	lst = fp.readlines()
	print(lst)  #['abc\n', 'bc']
	for i in lst:
		lst_new.append(i.strip())
print(lst_new)  #['abc', 'bc']  标准的数据（去掉\n换行符）

# 3 writelines()  功能：将元素是字符串的可迭代性数据写入文件中
# 参数：元素是字符串类型的可迭代数据
# 返回：None
lst = ['床前明月光', '疑是地上霜', '举头望明月', '低头想家乡']
with open("ceshi2.txt",mode="w+",encoding="utf-8") as fp:  #w+每次都清空
	fp.writelines(lst)  #床前明月光疑是地上霜举头望明月低头想家乡
	# 一次写入到文件,文件没有换行
	# res = fp.writelines(lst)
	# print(res)  #None
 
# 3.1 实现效果:
#加入换行效果,并且插入一句话:王文真帅呀 , 插在低头想家乡的前面
#思路： 
#1先在列表插入
#2加上换行
#3写入文件
lst.insert(-1,'王文真帅呀')
print(lst)  
#['床前明月光', '疑是地上霜', '举头望明月', '王文真帅呀', '低头想家乡']

lst_new = []
for i in lst:
	lst_new.append(i+'\n')
print(lst_new)
#['床前明月光\n', '疑是地上霜\n', '举头望明月\n', '王文真帅呀\n', '低头想家乡\n']

with open("ceshi2.txt",mode="w+",encoding="utf-8") as fp:
	fp.writelines(lst_new)  #一次写入多行(包含换行符\n)
print('---------------3-1')

# map
lst = ['床前明月光', '疑是地上霜', '举头望明月', '低头想家乡']
def func(n):
	return n+'\n'
it = map(func,lst)

with open("ceshi2-1.txt",mode="w+",encoding="utf-8") as fp:
	fp.writelines(list(it))  #一次写入多行(包含换行符\n)
print('---------------3-2')

# map lambda
lst = ['床前明月光', '疑是地上霜', '举头望明月', '低头想家乡']
# def func(n):
	# return n+'\n'
it = map(lambda n: n+'\n',lst)

with open("ceshi2-2.txt",mode="w+",encoding="utf-8") as fp:
	fp.writelines(list(it)) #一次写入多行(包含换行符\n)
print('---------------3-3')

# 注意点，可迭代数据的元素必须是字符串，不能是整型等其他类型
# lst = [1,2,3]
# with open("ceshi2.txt",mode="w+",encoding="utf-8") as fp:
	# fp.writelines(lst)
# TypeError: write() argument must be str, not int

# 4.truncate()  #功能:把要截取的字符串提取出来,然后清空内容将提取的字符串
# 重新写入文件中(单位:字节)  参数:字节数int   返回:None

with open("ceshi3.txt",mode="w+",encoding="utf-8") as fp:
	fp.write('abc\n')
	fp.write('bc')
	fp.truncate(3)   #utf-8下,一个中文字符是3个字节

# with open("ceshi4.txt",mode="r+",encoding="utf-8") as fp:  #报错 r+模式
	# fp.write('abc\n')
	# fp.write('bc')
	# fp.truncate(3)
# FileNotFoundError: [Errno 2] No such file or directory: 'ceshi4.txt'

#小结
# seek(字节数)
# truncate(字节数)
# read(字符/字节)  r模式 字符  rb模式 字节
# readline(字符/字节)

# readline()  一次读取一行
# readlines() 读取多行到列表,每一行+\n是列表的一个元素
# writeline() 可以一次写入多行(包含\n 换行符)
	# 参数:元素为字符串类型的可迭代数据
	# lst = ['床前明月光', '疑是地上霜', '举头望明月', '低头想家乡']
	# lst =[1,2,3]  会报错, 1是int 不是字符串
# truncate()  截取

# readable()  判断可读
# writable() 判断可写










































