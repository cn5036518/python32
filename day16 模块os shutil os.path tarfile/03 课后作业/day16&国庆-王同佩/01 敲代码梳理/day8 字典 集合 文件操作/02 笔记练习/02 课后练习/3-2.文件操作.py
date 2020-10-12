# ### 文件操作


# 1 文件的写入  write()
fp = open("ceshi1.txt",mode="w",encoding="utf-8")
fp.write('把大象装冰箱')  
fp.close()

# write()和writelines()的区别
# write()的参数是字符串
# writelines()的参数是可迭代数据类型(容器 range() 迭代器),
               # 可迭代数据的元素必须是字符串,加\n可以一次写入多行

# 2 文件的读取
fp = open("ceshi1.txt",mode="r",encoding="utf-8")
res = fp.read() #把大象装冰箱
print(res)
fp.close()

# read()和readline() readlines()的区别
# read()  参数为空,默认读取全部  参数是字符数,r模式 参数是字节数,rb模式
# readline()  参数为空,默认读取一行
			# 参数是字符数<一行字符数,r模式  读取指定字符数
				  # 字符数>一行字符数,r模式  读取一行
			# 参数是字节数<一行字节数,rb模式 读取指定字节数
				  # 字节数>一行字节数,rb模式 读取一行
# readlines()  参数是空  返回list 每一行内容是list的一个元素

# 3.二进制字节流
# b"abc" b开头的字节流要求数据只能是ascii编码中的字符,不能是中文
    # encode() 编码  将字符串转化为字节流(Bytes流)
    # decode() 解码  将Bytes流转化为字符串

# 1 encode() 编码  str==>bytes
data = "中文".encode("utf-8")  #encode() 将字符串变成bytes utf-8下 一个中文占3个字节
print(data,type(data))
#b'\xe4\xb8\xad\xe6\x96\x87' <class 'bytes'>
# 计算字节总大小
print(len(data)) #6  

# 2 decode() 解码  bytes==>str
data = b'\xe4\xb8\xad\xe6\x96\x87'
str1 = data.decode('utf-8')
print(str1,type(str1))  #中文 <class 'str'>

# 4.文件存储(写入)二进制的字节流  文件中只能存储字符串或字节流
# """如果存储的是二进制字节流,指定模式wb,不要指定encoding编码集,否则报错""" 
fp = open("ceshi2.txt",mode="wb")
str1 = "红鲤鱼"
bytes1 = str1.encode('utf-8')
print(bytes1)  #b'\xe7\xba\xa2\xe9\xb2\xa4\xe9\xb1\xbc'
# 这个字节流在notepad++ 自动通过菜单encoding--encode in utf-8反解成了字符串'红鲤鱼'
fp.write(bytes1)
fp.close()


# 5.文件读取二进制的字节流  （中文也可以用二进制来读取成字节流）
fp = open("ceshi2.txt",mode="rb")
bytes1 = fp.read()
print(bytes1)  #b'\xe7\xba\xa2\xe9\xb2\xa4\xe9\xb1\xbc'
fp.close()
print(bytes1.decode('utf-8'))  #红鲤鱼

# 6.复制文件
# """所有的图片,音频,视频都需要通过二进制字节流来进行存储传输."""

# 思路
# 1先把原文件的二进制字节流读取出来
# 2在把二进制字节流写入到另外一个文件中,相当于复制


# 1先把原文件的二进制字节流读取出来
# fp = open(r"C:\Users\Administrator\Desktop\ubuntu_gx\python32\day8 字典 集合 文件操作\02 笔记练习\02 课后练习\集合.png",mode="rb")
#FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Administrator\\Desktop\\ubuntu_gx
# \\python32\\day8 字典 集合 文件操作\\02 笔记练习\\02 课后练习\\集合2.png'  #这个是win下的路径 不能在linix下执行

# fp = open(r"/mnt/hgfs/ubuntu_gx/python32/day8 字典 集合 文件操作/02 笔记练习/02 课后练习/集合2.png",mode="rb")
# 绝对路径

import os
print(os.getcwd())  #当前py文件所在的目录 方法1
#/mnt/hgfs/ubuntu_gx/python32/day8 字典 集合 文件操作/02 笔记练习/02 课后练习
print(__file__)  #当前py文件的完整绝对路径
#/mnt/hgfs/ubuntu_gx/python32/day8 字典 集合 文件操作/02 笔记练习/02 课后练习/3-2.文件操作.py

print(os.path.dirname(__file__)) #当前py文件所在的目录 方法2
#/mnt/hgfs/ubuntu_gx/python32/day8 字典 集合 文件操作/02 笔记练习/02 课后练习
print(os.path.basename(__file__)) #当前py文件的文件名字
# 3-2.文件操作.py

# 相对路径
fp = open(r"集合2.png",mode="rb")
bytes1 = fp.read() #读取字节流
fp.close()

# 2在把二进制字节流写入到另外一个文件中,相当于复制
fp = open("集合2-2.png",mode="wb") #相对路径
fp.write(bytes1) #写入字节流
fp.close()













