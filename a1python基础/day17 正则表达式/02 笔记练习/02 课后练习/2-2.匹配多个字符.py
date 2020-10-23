# ### 正则表达式 - 匹配多个字符
import re

# (1) 量词  ? + * {m,n} {m}  {m,}
# 量词修饰它前面的字符
# ?  0或1个
# +   >=1个
# *   >=0个
# {m,n}  
# {m}    m个
# {m,}   >=m个

# '''1) ? 匹配0个或者1个a '''
print(re.findall('a?b','abbzab abb aab'))   ##  ab b  ab ab b ab

# '''2) + 匹配1个或者多个a '''
print(re.findall(r'a+b',r'b ab aaaaaab abb'))
# # ab aaaaaab ab

# '''3) * 匹配0个或者多个a '''
print(re.findall('a*b','b ab aaaaaab abbbbbbb'))
#b ab aaaaaab ab b b b b b b 

# '''4) {m,n} 匹配m个至n个a '''
# 1 <= a <= 3 
print(re.findall('a{1,3}b','aaab ab aab abbb aaz aabb'))
#aaab ab aab ab aab

# {2}  代表必须匹配2个a
print(re.findall('a{2}b','aaab ab aab abbb aaz aabb'))
## aab aab aab

# {2,} 代表至少匹配2个a
print(re.findall('a{2,}b','aaab ab aab abbb aaz aabb'))
# aaab aab aab


# (2) 贪婪匹配 和 非贪婪匹配
# 贪婪匹配  : 默认向更多次匹配  (回溯算法)
# 非贪婪匹配: 默认向更少次匹配  (配合?号使用)    

# 回溯算法 : 从左向右进行匹配,直到找到最后一个,再也没有了,回头,返回上一个找到的内容

# . 除了\n,匹配所有字符

# 非贪婪写法: 量词 + ? 

# 量词  ? + * {m,n} {m}  {m,}
# ?  0或1个
# +   >=1个
# *   >=0个
# {m,n}  
# {m}    m个
# {m,}   >=m个

#如何区分贪婪还是非贪婪?
#如果有量词,没有出现量词 + ? ,且量词前面是.(任意字符) 默认就是贪婪匹配
# .+量词  贪婪匹配
# .+量词+? 非贪婪匹配

# 贪婪匹配(模式)
strvar = "刘能和刘老根和刘罗锅111子222子"
lst = re.findall("刘.",strvar)
print(lst)
#['刘能', '刘老', '刘罗']

strvar = "刘能和刘老根和刘罗锅111子222子"
lst = re.findall("刘.?",strvar)
#?表示0或1个,没有出现量词+?(非贪婪),就是贪婪匹配 ?取多的,就是1个
print(lst)
#['刘能', '刘老', '刘罗']

lst = re.findall("刘.+",strvar)
print(lst)  #['刘能和刘老根和刘罗锅111子222子']
#+表示1或多个,没有出现量词+?(非贪婪),就是贪婪匹配 +取多的,就是多个
print('--------------------贪婪  3')

strvar = "刘能和刘老根和刘罗锅111子222子"
lst = re.findall("刘.*",strvar)
print(lst)  #['刘能和刘老根和刘罗锅111子222子']
#*表示0或多个,没有出现量词+?(非贪婪),就是贪婪匹配 *取多的,就是多个

strvar = "刘能和刘老根和刘罗锅111子222子"
lst = re.findall("刘.{1,20}",strvar)
print(lst)  #['刘能和刘老根和刘罗锅111子222子']
#{1,20}表示1-20个,没有出现量词+?(非贪婪),就是贪婪匹配 {1,20}取多的,就是20个
#即刘开头的字符串,字符串长度最大是20

strvar = "刘能和刘老根和刘罗锅111子222子"
lst = re.findall("刘.*子",strvar)
print(lst)  #['刘能和刘老根和刘罗锅111子222子']
#*表示0或多个,没有出现量词+?(非贪婪),就是贪婪匹配 *取多的,就是多个
#刘开头,子结尾.贪婪匹配,取第二个子
print('--------------------贪婪  6')

# 非贪婪匹配(模式)  非贪婪写法: 量词 + ? 
# 量词  ? + * {m,n} {m}  {m,}
# ?  0或1个
# +   >=1个
# *   >=0个
# {m,n}  
# {m}    m个
# {m,}   >=m个

strvar = "刘能和刘老根和刘罗锅111子222子"
lst = re.findall("刘.??",strvar)
print(lst)
#第一个?表示0或1个,第二个?表示非贪婪, 第一个?取少的,即0个
##即刘开头,一共是1个字符,即取到第一个'刘'后,就把'刘'作为列表的
#一个元素返回,接着取第二个'刘'...依次类推
#['刘', '刘', '刘']

strvar = "刘能和刘老根和刘罗锅111子222子"
lst = re.findall("刘.+?",strvar)
print(lst)# 刘能 刘老 刘罗
#+表示1或多个,+?符合量词+?,是非贪婪,+取少的,即1次
#即刘开头,一共是2个字符,即取到第一个'刘x'后,就把'刘x'作为列表的
#一个元素返回,接着取第二个'刘x'...依次类推 x是任意字符

strvar = "刘能和刘老根和刘罗锅111子222子"
lst = re.findall("刘.*?",strvar)
print(lst)
#*表示0或多个,*?符合量词+?,是非贪婪,+取少的,即0次
#即刘开头,一共是1个字符 #['刘', '刘', '刘']
print('--------------------非贪婪  3')

strvar = "刘能和刘老根和刘罗锅111子222子"
lst = re.findall("刘.{1,20}?",strvar)
print(lst)  #['刘能', '刘老', '刘罗']
#{1,20}表示1-20个,{1,20}?符合量词+?,是非贪婪,{1,20}取少的,即1次
#即刘开头,一共是2个字符

strvar = "刘能和刘老根和刘罗锅111子222子"
lst = re.findall("刘.*?子",strvar)
print(lst)  #['刘能和刘老根和刘罗锅111子']
#*表示0或多个,*?符合量词+?,是非贪婪,*取少的
#即刘开头,子结尾取少的




# (3) 边界符  \b  \b
# \b 本身是转义字符 退格,退到光标上一位 back键
# \b 在正则中还有边界符的意思 比如:字符串中的空格

# "word"
# 卡住左边界:\bw  \b在左边
# 卡住右边界:d\b   \b在右边

#如何区分贪婪还是非贪婪?
#如果有量词,没有出现量词 + ? ,且量词前面是.(任意字符) 默认就是贪婪匹配
# .+量词  贪婪匹配
# .+量词+? 非贪婪匹配

strvar = r"word old duck"
# 右边界
lst = re.findall(r"d\b",strvar)
print(lst)  #['d', 'd']

lst = re.findall(r".*d\b",strvar)
print(lst) 
#*表示0或多个,没有出现量词+?(非贪婪),就是贪婪匹配 *取多的,就是多个
#即取从头取到第二个d作为边界符  #['word old']

strvar = r"word old duck"
lst = re.findall(r".*?d\b",strvar)
print(lst)  #['word', ' old']
#*表示0或多个,*?符合量词+?,是非贪婪,取少的
#即遇到第一个d作为边界符,就返回,再去取第二个d作为边界符,接着返回,直到没有符合d作为边界符为止
print('--------------------边界符3')

# 左边界
strvar = r"word old duck"
lst = re.findall(r"\bw",strvar)
print(lst)   #['w']

strvar = r"word old duck"
lst = re.findall(r"\bw.*",strvar)
print(lst)  #['word old duck']
#*表示0或多个,没有出现量词+?(非贪婪),就是贪婪匹配 *取多的,就是多个
#即w开头,字符串的长度尽可能的长,即整个字符串

strvar = r"word old duck"
lst = re.findall(r"\bw.*?",strvar)
print(lst)  #['w']
#*表示0或多个,*?符合量词+? 是非贪婪,*取少的,就是0个
#即w开头,字符串的长度是1
print('--------------------边界符6')

strvar = r"word old duck"
lst = re.findall(r"\bw.*? ",strvar)
print(lst)  #['word ']
#*表示0或多个,*?符合量词+? 是非贪婪,*取少的,第一个空格结尾
#即w开头,第一个空格结尾

strvar = r"word old duck"
lst = re.findall(r"\bw\S*",strvar)
print(lst)  #['word']
#*表示0或多个,没有出现量词+?(非贪婪),就是贪婪匹配 *取多的(最后一个非空白符)
#即w开头,最后一个非空白符结尾(这里,一旦遇到空白符,就返回了)   所以不是整个字符串

# (4) ^ $的使用
# ^ 写在在字符串的开头,表达必须以某个字符开头
# $ 写在在字符串的结尾,表达必须以某个字符结尾
# 当使用了^ $ 代表要把该字符串看成一个整体

strvar = "大哥大嫂大爷"
print(re.findall('大.',strvar))
#['大哥', '大嫂', '大爷']

strvar = "大哥大嫂大爷"
print(re.findall('^大.',strvar))
#['大哥']

strvar = "大哥大嫂大爷"
print(re.findall('大.$',strvar)) #['大爷']
#大开头,固定爷结尾,字符串长度是2

strvar = "大哥大嫂大爷"
print(re.findall('^大.$',strvar))  #[]
#固定大开头,固定爷结尾,字符串长度是2
print('--------------------^ $的使用4')

strvar = "大哥大嫂大爷"
print(re.findall('^大.*?$',strvar)) #['大哥大嫂大爷']
#固定大开头,固定爷结尾,字符串长度不限
print(re.findall('^大.*$',strvar)) #['大哥大嫂大爷']
#固定大开头,固定爷结尾,字符串长度不限

strvar = "大哥大嫂大爷"
print(re.findall('^大.*?大$',strvar))  #[]
#固定大开头,固定大结尾,字符串长度不限  没有符合条件的,返回空列表

strvar = "大哥大嫂大爷"
print(re.findall('^大.*?爷$',strvar)) #['大哥大嫂大爷']
#固定大开头,固定爷结尾,字符串长度不限
print('--------------------^ $的使用7')


print(re.findall('^g.*? ' , 'giveme 1gfive gay'))  #['giveme ']
#固定g开头,空格结尾,*?非贪婪,取少的,即第一个空格结尾
#固定g开头,第一个空格结尾

print(re.findall('five$' , 'aassfive'))
#固定five结尾,字符串长度是4  #['five']

print(re.findall('^giveme$' , 'giveme'))  #['giveme']
#固定giveme开头,固定giveme结尾
print('--------------------^ $的使用3-2')

print(re.findall('^giveme$' , 'giveme giveme')) #[]
#固定giveme开头,固定giveme结尾 字符串长度是6   没有符合条件的,返回空列表[]

print(re.findall('giveme' , 'giveme giveme')) #['giveme', 'giveme']

print(re.findall("^g.*e",'giveme 1gfive gay'))
#固定g开头 e结尾  贪婪匹配(.+量词),第二个e结尾
#固定g开头,第二个e结尾  #['giveme 1gfive']


# 小结:
#如何区分贪婪还是非贪婪?
# .+量词  贪婪匹配
# .+量词+? 非贪婪匹配

# 非贪婪匹配(模式)  非贪婪写法: 量词 + ? 
# 量词  ? + * {m,n} {m}  {m,}
# ?  0或1个
# +   >=1个
# *   >=0个
# {m,n}  
# {m}    m个
# {m,}   >=m个

























