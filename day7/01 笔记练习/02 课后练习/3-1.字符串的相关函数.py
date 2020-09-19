# ### 字符串的相关函数
# * capitalize 字符串首字母大写
strvar = 'how are you'
res = strvar.capitalize()
print(res)  #How are you

# * title 每个单词的首字母大写
strvar = 'how old are you'
res = strvar.title()
print(res)  #How Old Are You

# * upper 将所有字母变成大写
strvar = 'How Old Are You'
res = strvar.upper()
print(res)  #HOW OLD ARE YOU

# * lower 将所有字母变成小写
strvar = 'How Old Are You'
res = strvar.lower()
print(res)  #how old are you

# *swapcase 大小写互换
strvar = 'How old Are You'
res = strvar.swapcase()
print(res)  #hOW OLD aRE yOU

# *len 计算字符串的长度
strvar = 'python32真热'
res = len(strvar)
print(res)  #10

# *count 统计字符串中某个元素的数量
# count(字符,[开始值,结束值])
strvar = '真热真热啊'
res = strvar.count('真')
print(res)  #2

res = strvar.count('热',2)
print(res)  #1

res = strvar.count('热',2,3)  #只有真这个字符 没有热
print(res)  #0

# *find 查找某个字符串第一次出现的索引位置(推荐)
# find(字符,[开始值,结束值])
strvar = 'To be or not to be that is a question'
res = strvar.find('to')
print(res)  #13

res = strvar.find('be',4)
print(res)  #16

# 如果find 返回的是-1 代表没找到
res = strvar.find('be',4,10) # 4~9
print(res)  #-1

# *index 与 find 功能相同 find找不到返回-1,
# index找不到数据直接报错
# res = strvar.index('be',4,10)
# print(res)  #ValueError: substring not found

# *starswith 判断是否以某个字符或字符串为开头
#  startswith(字符,[开始值,结束值])
# endswith(字符,[开始值,结束值])

strvar = 'To be or not to be that is a question'
res = strvar.startswith('To')
print(res)  #True

res = strvar.startswith('To',10)
print(res)  #False

# *endswith 判断是否以某个字符或字符串结尾
res = strvar.endswith('question')
print(res)  #True

res = strvar.endswith('is',-14,-11) #is
print(res)  #True


# ### is系列
# *isupper 判断字符串是否都是大写字母
strvar = 'HOW A YOU'
res = strvar.isupper()
print(res)  #True

# *islower 判断字符串是否都是小写字母
strvar = 'asdf - as' #这里包含-等特殊字符,也可以判断
res = strvar.islower()
print(res)  #True

# * isdecimal 检测字符串是否以数字组成 必须是纯数字
# 应用:在猜数游戏,判断用户输入的是否是数字
strvar = 'abcdefg'
res = strvar.isdecimal()
print(res)  #False

strvar = '1.2'
res = strvar.isdecimal()
print(res)   #False

strvar = '12'
res = strvar.isdecimal()
print(res)   #True


# * split 按某字符将字符串分割成列表(默认分割字符是空格)   ***
strvar = 'you can you up no can no bb'
lst = strvar.split()
print(lst)  #['you', 'can', 'you', 'up', 'no', 'can', 'no', 'bb']

strvar = 'you#can#you#up#no#can#no#bb'
lst = strvar.split('#') #这里#是分隔符
print(lst)  #['you', 'can', 'you', 'up', 'no', 'can', 'no', 'bb']

# *join 按某字符(拼接符)将列表(容器类型都可)拼接成字符串   ***
lst = ['you', 'can', 'you', 'up', 'no', 'can', 'no', 'bb']
strvar = ' '.join(lst)
print(strvar)  #you can you up no can no bb

lst = ['you', 'can', 'you', 'up', 'no', 'can', 'no', 'bb']
strvar = '#'.join(lst)
print(strvar)  #you#can#you#up#no#can#no#bb

# * replace 把字符串的旧字符换成新字符   ***
# 字符串.replace('旧字符','新字符'[,限制替换的次数])
strvar = '范冰冰爱不爱我'
res = strvar.replace('爱','喜欢',1)  #选择替换的次数
print(res)  #范冰冰喜欢不爱我

strvar = '范冰冰爱不爱我'
res = strvar.replace('爱','喜欢')
print(res)  #范冰冰喜欢不喜欢我

# *strip 默认去掉首尾两边的空白符 ***
# 空白符包括:  空格 \n \t \r ... 
strvar = '   周润发   '
res = strvar.strip()
print(strvar)  #   周润发   
print(res)  #周润发

# * center 填充字符串,原字符居中(默认填充空格)
# center(字符长度,填充符号)  #这里的字符长度包括填充符号+原字符串的长度和
strvar = '赵世超'
res = strvar.center(10)
print(res) #   赵世超  

strvar = '赵世超'
res = strvar.center(10,'*')
print(res) #   ***赵世超****















































