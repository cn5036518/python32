# ### 字符串的相关函数   产出新字符串,原字符串不变
#  一 大小写  capitalize  title  upper lower swapcase

# 01 capitalize  首字符串字母大写
strvar = "how are you"
res = strvar.capitalize()
print(res)  #How are you

# 02 title  每个单词的首字母大写 
strvar = "how old are you"
res = strvar.title()
print(res)  #How Old Are You

# 03 upper 将所有字母变成大写
strvar = "How Old Are You"
res = strvar.upper()
print(res)  #HOW OLD ARE YOU

# 04 lower  将所有字母变成小写 
strvar = "How Old Are You"
res = strvar.lower()
print(res)  #how old are you

# 05 swapcase 大小写互换 
strvar = "How old Are You"
res = strvar.swapcase()
print(res)  #hOW OLD aRE yOU
print('-----------------1  大小写  capitalize  title  upper lower swapcase')

# 二 len  count find  index startswith endswith
# 01  len 计算字符串的长度 字符数
strvar = "python32真热"
res = len(strvar)
print(res)  #10

# 02  count 统计字符串中某个元素的数量 
# """count(字符,[开始值,结束值])"""
strvar = "真热真热呀"
res = strvar.count('真')
print(res)  #2

res = strvar.count('真',2)
print(res)  #1

res = strvar.count('热',2,3)  #左闭右开
print(res)  #0
print('-----------------02  count')


# 03  find 查找某个字符串第一次出现的索引位置  (推荐)
# """find(字符,[开始值,结束值])"""   如果find 返回的是 -1 代表没找到
strvar = "To be or not to be that is a question"
res = strvar.find('to')
print(res) #13

res = strvar.find('be',4)
print(res) #16

res = strvar.find('be',4,10)  #左闭右开
print(res) #-1
print('-----------------03 find')

# 04 index 不推荐
# index 与 find 功能相同 find找不到返回-1,index找不到数据直接报错
strvar = "To be or not to be that is a question"
# res = strvar.index('be',4,10)
# print(res)
#ValueError: substring not found

# 05 startswith 判断是否以某个字符或字符串为开头 
# startswith(字符,[开始值,结束值])  #左闭右开
strvar = "To be or not to be that is a question"
res = strvar.startswith('To')
print(res)  #True

res = strvar.startswith('To',10)
print(res)  #False
print('-----------------05 startswith')

# 06  endswith 判断是否以某个字符或字符串结尾 
# endswith(字符,[开始值,结束值])  #左闭右开
res = strvar.endswith('question')
print(res)  #True

res = strvar.endswith('is',-14,-11)
print(res)  #True
print('-----------------2  len count find index startswith endswith')

# ### 三 is系列  isupper islower isdecimal
# 01 isupper 判断字符串是否都是大写字母 
strvar = "HOW  A  YOU"
res = strvar.isupper()
print(res)  #True
print('-----------------01 isupper')

# 02 islower 判断字符串是否都是小写字母 
strvar = "asdf - as"  #可以包含特殊字符
res = strvar.islower()
print(res)  #True
print('-----------------02 islower')

# 03  isdecimal 检测字符串是否以数字组成  必须是纯数字
strvar = "abcdefg"
res = strvar.isdecimal()
print(res) #False

strvar = "2134234.123"  #有小数点
res = strvar.isdecimal()
print(res)  #False

strvar = "2134234"
res = strvar.isdecimal()
print(res)  #True
print('-----------------03 isdecimal')
print('-----------------3  isupper islower isdecimal')

# ### 四 重点  split join replace strip center
# 01 split 按某分割字符将字符串分割成列表(默认字符是空格)  ***
strvar = "you can you up no can no bb"
lst = strvar.split()  #默认是空格作为分隔符
print(lst)
# ['you', 'can', 'you', 'up', 'no', 'can', 'no', 'bb']

strvar = "you#can#you#up#no#can#no#bb"
lst = strvar.split('#')
print(lst)
#['you', 'can', 'you', 'up', 'no', 'can', 'no', 'bb']
print('-----------------01 split')


# 02 join  按某字符(连接符)将列表等容器类型(list tuple dict set str)
#拼接成字符串(容器类型都可)    ***
lst = ['you', 'can', 'you', 'up', 'no', 'can', 'no', 'bb']
strvar = ' '.join(lst)
print(strvar) #you can you up no can no bb

strvar1 = '#'.join(lst)
print(strvar1)  #you#can#you#up#no#can#no#bb

tuplevar = ('you', 'can')
strvar2 = ' '.join(tuplevar)
print(strvar2)  #you can

setvar = {'you', 'can'} #不推荐
strvar3 = '*'.join(setvar)
print(strvar3)  #can*you

dic = {'name':'jack','age':18}  #连接的是键
strvar4 = '*'.join(dic)
print(strvar4)  #name*age

str1 = 'jack'
strvar5 = '*'.join(str1)
print(strvar5)  #j*a*c*k
print('-----------------02 join')

# 03 replace 把字符串的旧字符换成新字符  ***  会产生新的字符串
# """字符串.replace('旧字符','新字符'[, 限制替换的次数])"""
strvar = "范冰冰爱不爱我"
res = strvar.replace('不爱我','爱我')
print(res)  #范冰冰爱爱我

res = strvar.replace('爱','喜欢',1)
print(res)  #范冰冰喜欢不爱我
print('-----------------03 replace')

# 04 strip  默认去掉首尾两边的空白符  ***
# """空白符 空格 \n \t \r ... """
strvar = "     周润发  "
res = strvar.strip()
print(res)  #周润发

strvar = "哈哈,"
res = strvar.strip(',')  #去掉两端的逗号
print(res)  #哈哈
print('-----------------04 strip')


# 05 center 填充字符串,原字符居中 (默认填充空格)
# """center(字符长度,填充符号)"""
strvar = "赵世超"
res = strvar.center(10)
print(res)  #   赵世超  

res = strvar.center(10,'*')
print(res)  #***赵世超****




































