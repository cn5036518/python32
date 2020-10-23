# ### 文件操作
'''
语法:
fp = open(文件,模式,编码集)
fp => 文件的io对象(文件句柄)
i => input 输入
o => output 输出

fp.read() 读取文件内容
fp.write() 写入文件的内容
'''
# 1.文件的写入操作
# (1) 打开文件
fp = open('ceshi.txt',mode='w',encoding='utf-8') #打开冰箱门
# encoding 不写默认是utf-8

# (2) 写入内容
fp.write('把大象怼进去') #把大象怼进去
# (3) 关闭文件
fp.close()  # 把冰箱门关上

# 2.文件的读取操作
# (1) 打开文件
fp = open('ceshi.txt',mode='r',encoding='utf-8')

# (2) 读取内容
res = fp.read()

# (3) 关闭文件
fp.close()
print(res)  #把大象怼进去

# 3.文件存储二进制字节流

# 二进制字节流:用于传输数据或存储数据的一种数据格式
# b'abc'  b开头的字节流要求数据只能是ascii编码中的字符,不能是中文

# 将字符串和字节流(Bytes流)类型进行转换(参数写成转换的字符编码格式)
# encode() 编码 将字符串(中英文)转换成字节码(Bytes流)
# decode() 解码 将Bytes流转化成字符串(中英文)

data = b'abc'
print(data,type(data))  #b'abc' <class 'bytes'>

# data = '中文'.encode('utf-8')
data = '中文'.encode('utf8')  #utf8和utf-8 一样.参数不写默认是utf-8
print(data)  #一个汉字3个字节 在utf-8
# b'\xe4\xb8\xad\xe6\x96\x87'

res = data.decode('utf-8')
# res = data.decode()
print(res,type(res))  #中文 <class 'str'>

# utf-8下 一个中文占用3个字节
data = '中文'.encode('utf-8')
# 计算字节总大小
print(len(data))  #6

# 把'中'字这个字节流进行反解 恢复成原来的字符'中'
res = b'\xe4\xb8\xad'.decode()
print(res)  #中


# 4.文件存储二进制的字节流
# 如果存储的是二进制字节流,指定模式wb,不要指定encoding编码集,否则报错
fp = open('ceshi2.txt',mode='wb')
bytesvar = '红鲤鱼'.encode('utf-8')
print(bytesvar)  #b'\xe7\xba\xa2\xe9\xb2\xa4\xe9\xb1\xbc'
fp.write(bytesvar) #把字节码写入notepad++后,notepad+的encode是utf-8 会自动将字节码反解成字符串,显示
# 文件的内容是字符串'红鲤鱼',而不是字节码
fp.close()

# 5.文件读取二进制的字节流
fp = open('ceshi2.txt',mode='rb')
res = fp.read()  #用rb模式,读取的就是字节码
fp.close()
print(res)  #b'\xe7\xba\xa2\xe9\xb2\xa4\xe9\xb1\xbc'
print(res.decode())  #红鲤鱼

# 6.复制文件
# 所有的图片,音频,视频都需要通过二进制字节流来进行存储传输
# 先把原文件的二进制字节流读取出来
fp = open('集合2.png',mode='rb')
res = fp.read()
fp.close()

# 计算文件中的字节个数==>文件大小
print(len(res))  #45453   个字节

# 在把二进制字节流写入到另外一个文件中,相当于复制
fp = open('集合3.png',mode='wb')
fp.write(res)
fp.close()


































































