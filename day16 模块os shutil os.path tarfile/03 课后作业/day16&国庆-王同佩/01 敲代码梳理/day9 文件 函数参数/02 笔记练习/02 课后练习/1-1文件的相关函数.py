# ### 刷新缓冲区
'''
刷新缓冲区 flush
	1 当文件关闭的时候自动刷新缓冲区
	2 当整个程序运行结束的时候自动刷新缓冲区
	3 当缓冲区写满了,会自动刷新缓冲区
	4 手动刷新缓冲区
'''
# fp = open("ceshi1.txt",mode="a",encoding="utf-8")
# fp.write('abc')

# 手动刷新缓冲区,直接把内容从缓冲区写入到文件
# fp.flush()

# while True:
	# pass
	
# fp.close()


# ### 文件相关的函数
# fp这个对象本身是迭代器,可以把文件中的内容按照换行一行一行遍历出来
fp = open("ceshi1.txt",mode="r",encoding="utf-8")
# readable() # 判断文件对象是否可读
print(fp.readable())  #True
print(fp.writable())  #False

# writable()  # 判断文件对象是否可写
# 遍历fp文件对象
for i in fp:
	print(i)  #abc
	
# 1.readline() # 读取一行文件内容
with open("ceshi1.txt",mode="r",encoding="utf-8") as fp:
	res = fp.readline()  #一次只读取一行
	print(res)  #abc
print('-------------------------1')

# (1) 一次把所有内容都读取出来
with open("ceshi1.txt",mode="r",encoding="utf-8") as fp:
	# 先读取一行
	res = fp.readline().strip()
     #去掉两端空白
	# 判断是不是空,不是空再循环
	while res:
		print(res)
		# 再读取一行,放到循环中判断
		res = fp.readline().strip()
print('-------------------------2')

# (2) 注意点: readline(读取的字符数)
	# 读取的字符数量 > 实际当前行字符数量的时候 => 按照当前行读取
	# 读取的字符数量 < 实际当前行字符数量的时候 => 按照实际数量来读
with open("ceshi1.txt",mode="r",encoding="utf-8") as fp:
	res = fp.readline(300)
	print(res)
print('-------------------------3')

# 2.readlines()  将文件中的内容按照换行读取到列表中

lst_new = []
with open("ceshi1.txt",mode="r+",encoding="utf-8") as fp:
	lst = fp.readlines()  #这里是readlines 而不是readline
	for i in lst:
		lst_new.append(i.strip())
print(lst_new)  #['abc', '开开', '按键']
print('-------------------------2-1')

# 3.writelines()
  # 将内容是字符串的可迭代数据写入文件中
  # 参数:内容为字符串类型的可迭代数据

lst = ['床前明月光', '疑是地上霜', '举头望明月', '低头想家乡']
with open("ceshi2.txt",mode="w+",encoding="utf-8") as fp:
	fp.writelines(lst)
print('-------------------------3-1')

# ### 实现效果:加入换行效果 并且插入一句话:王文真帅呀 , 插在低头想家乡的前面
lst_new = []
# 先把内容插入到原列表中
lst.insert(-1,'王文真帅啊')

#循环原列表,把每个元素拼接\n ,放到新的列表
for i in lst:
	lst_new.append(i + '\n')
print(lst_new)

#把新的列表的每行内容插入到文件中
with open("ceshi2.txt",mode="w+",encoding="utf-8") as fp:
	fp.writelines(lst_new)
print('-------------------------3-2')

# writelines的参数类型是可迭代类型,且可迭代类型的数据的元素必须
# 是字符串,不能是整型
# lst = [1,2,3]
# with open("ceshi2.txt",mode="w+",encoding="utf-8") as fp:
	# fp.writelines(lst)
#  TypeError: write() argument must be str, not int

# 4.truncate()  
# 功能:把要截取的字符串提取出来,
# 然后清空内容将提取的字符串重新写入文件中(字节)

with open("ceshi2.txt",mode="r+",encoding="utf-8") as fp:
	fp.truncate(3)  #3个字节是一个汉字 文件只有一个汉字
print('-------------------------4')

# seek(字节)
# tell(字节)
# truncate(字节)
# read(字符/字节 b)
# readline(字符/字节 b)





































