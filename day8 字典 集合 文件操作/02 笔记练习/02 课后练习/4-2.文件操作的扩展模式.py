# 1.r+ 先读后写
fp = open("ceshi3.txt",mode="r+",encoding="utf-8")
# 先读
res = fp.read() #r+模式 打开文件后，光标默认在文件开头
print(res)  #红鲤鱼cdcd

 # 在写
fp.write('heheh')
 # 在读
fp.seek(0)
print(fp.read())  #红鲤鱼cdcdheheh
fp.close()

# 2.r+ 先写后读
fp = open("ceshi31.txt",mode="r+",encoding="utf-8")
#r+模式 打开文件后，光标默认在文件开头
# # 移动光标到文件最后,否则r+模式下,原字符会被覆盖
fp.seek(0,2)
# # 先写
fp.write('航啊')
# # 把光标移动到文件的开头
fp.seek(0)
# # 在读
res = fp.read()
print(res) #红鲤鱼航啊
fp.close()

# 3.w+ 可读可写,清空重写(默认可以创建新的文件)
fp = open("ceshi41.txt",mode="w+",encoding="utf-8")
fp.write('abc') #写完后,光标在文件最后
fp.seek(0)
print(fp.read())  #abc
fp.close()

# 4.a+ 可读可写,追加写入 (默认可以创建新的文件)
fp = open("ceshi51.txt",mode="a+",encoding="utf-8")
fp.write('def')
fp.seek(0)
print(fp.read()) #def
fp.close()

# 5.r+和a+区别
# """
# r+模式基于当前光标所在位置进行写入覆盖，r+模式下，光标默认在文件开头
# a+模式会强制把光标放到文件末尾进行追加写入
# """

fp = open("ceshi51.txt",mode="a+",encoding="utf-8")
fp.seek(0) # 第一次回到文件开头 失效
fp.write('航啊龙')  ## 模式会强制把光标放到文件末尾进行追加写入  忽略前面的seek(0)
fp.seek(0) # 第2次回到文件开头 有效
print(fp.read())
fp.close()

# 8.with语法 自动实现文件关闭操作
# 方法一.读取二进制字节流
with open('集合2-1.png',mode='rb') as fp:
	res = fp.read()

with open('集合3-1.png',mode='wb') as fp:
	fp.write(res)

# 方法二.继续简化
with open('集合3-1.png',mode='rb') as fp1,open('集合4-1.png',mode='wb') as fp2:
	res = fp1.read()
	fp2.write(res)






















