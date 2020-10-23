# 预定义字符集
# 字符组
# 量词
# 贪婪和非贪婪
# 边界符
# ^ $

# ### 匹配分组 ()表达整体
import re
# (1)分组
print(re.findall('.*?_good','wusir_good alex_good secret男_good'))
#.*? 是非贪婪 取少的,即_good结尾,任意字符开头
# 匹配到一个满足条件的,就作为列表的元素返回,直到没有满足条件的为止
#['wusir_good', ' alex_good', ' secret男_good']

#优先显示分组里面的内容 findall
print(re.findall('(.*?)_good','wusir_good alex_good secret男_good'))
#['wusir', ' alex', ' secret男']

# (?:) 代表不优先显示分组里面的内容,只是显示正常匹配到的内容
print(re.findall('(?:.*?)_good','wusir_good alex_good secret男_good'))
#['wusir_good', ' alex_good', ' secret男_good']


# (2) | 代表或 , a|b 匹配字符a 或者 匹配字符b . 
strvar = "abceab"
lst = re.findall("a|b",strvar)
print(lst)  #['a', 'b', 'a', 'b']

# 注意点:把不容易匹配到的内容放到前面,把容易匹配到的内容放到后面
strvar = "abcdeabc234f"
lst = re.findall("abcd|abc",strvar)
print(lst)  #['abcd', 'abc']

# (3) 练习
# .  可以匹配任意的字符,除了\n
# \. 对.进行转义,表达.这个字符本身.

# 匹配小数 
strvar = r"3....  ....4  .3 ...3   1.3  9.89  10"
lst = re.findall(r"\d+\.\d+",strvar)
print(lst)
#['1.3', '9.89']

# 匹配小数和整数 
strvar = r"3....  ....4  .3 ...3   1.3  9.89  10"
lst = re.findall(r"\d+\.\d+|\d+",strvar)
print(lst)
#['3', '4', '3', '3', '1.3', '9.89', '10']


# 使用分组改造
# '''findall优先显示括号里的内容,需要加上?:取消括号优先显示,按照匹配到的内容显示'''
strvar = r"3....  ....4  .3 ...3   1.3  9.89  10"
lst = re.findall(r"\d+(?:\.\d+)?",strvar)
print(lst)
r"\d+(?:\.\d+)?"
# \d+ 表示整数
# (?:\.\d+) 表示小数
# ? 表示0个或者1个

# 3
# 3.14

# 匹配135或171的手机号 
strvar = "13566668888 17366669999 17135178392"
# lst = re.findall(r"(135|171)\d{8}",strvar)  #['135', '171']
lst = re.findall(r"(?:135|171)\d{8}",strvar)
#['13566668888', '17135178392']
# lst = re.findall(r"135\d{8}|171\d{8}",strvar)
print(lst)

# 优化,只能匹配出一个手机号
strvar = "13566668888"
lst = re.findall(r"^(?:135|171)\d{8}$",strvar)
print(lst)  #['13566668888']

# strvar = "13566668888 17366669999 17135178392"
# lst = re.findall(r"^(?:135|171)\d{8}$",strvar)
# print(lst)  #[]

strvar = "13566668888"
obj = re.search(r"^(135|171)\d{8}$",strvar)
print(obj) #<_sre.SRE_Match object; span=(0, 11), match='13566668888'>
print(obj.group())  #13566668888
print(obj.groups())  #('135',)   显示小括号分组的


# 匹配www.baidu.com 或者 www.oldboy.com

# findall : 从左到右,匹配出所有的内容,返回到列表
		  # 问题是,匹配到的字符串和分组的内容不能同时显示;

# search  : 从左到右,匹配到一组内容就直接返回(而不是所有),返回的是对象
		  # 优点是,可以让匹配到的内容和分组里的内容同时显示;
		  # 匹配不到内容时,返回的是None
		  
# obj.group() : 获取匹配到的内容
# obj.groups(): 获取分组里面的内容

# findall   方法1
strvar = r"www.baidu.com  www.oldboy.com  www.wangwen.com"
lst = re.findall(r"(?:www)\.(?:baidu|oldboy)\.(?:com)",strvar)
print(lst)
#['www.baidu.com', 'www.oldboy.com']

strvar = r"www.baidu.com  www.oldboy.com  www.wangwen.com"
lst = re.findall(r"(www)\.(baidu|oldboy)\.(com)",strvar)
print(lst)
#[('www', 'baidu', 'com'), ('www', 'oldboy', 'com')]


# search  方法2
strvar = r"www.baidu.com  www.oldboy.com  www.wangwen.com"
obj = re.search(r"(www)\.(baidu|oldboy)\.(com)",strvar)
print(obj)
#<_sre.SRE_Match object; span=(0, 13), match='www.baidu.com'>

# 获取匹配到的内容
print(obj.group())  #www.baidu.com
# 获取分组里面的内容 (推荐)
print(obj.groups())  #('www', 'baidu', 'com')

# 方法二,可以直接通过下标1来获取分组里面的第一个内容;
print(obj.group(1))
print(obj.group(2))
print(obj.group(3))

print(obj.groups()[0])
print(obj.groups()[1])
print(obj.groups()[2])
print('--------------------------1 网址')


# search 练习 : 计算"5*6-7/3"结果  匹配 5*6 或者 7/3
strvar =  r"5*6-7/3"
obj = re.search(r"\d+[*/]\d+",strvar)#匹配到一个就返回了
res1 = obj.group()
print(res1 , type(res1)) # 5*6 <class 'str'>

# 计算结果
a,b = res1.split('*')
res = int(a) * int(b)
print(res)  #30

# 把30替换回原来的字符串中
strvar = strvar.replace(res1,str(res))
print(strvar)
#30-7/3

#二 计算7/3
#匹配出来
obj = re.search(r"\d+[*/]\d+",strvar)
res1 = obj.group()
print(res1)  #7/3

# 计算结果7/3
a,b = res1.split('/')
res = int(a) / int(b)
print(res)  #2.3333333333333335

# 把2.3替换回原来的字符串中
strvar = strvar.replace(res1,str(res))
print(strvar)
#30-2.3333333333333335

#三 计算30-2.3333333333333335
a,b = strvar.split('-')
res = int(a) - float(b)
print(res)  #27.666666666666668

print('------------------------------------计算1')

#优化提取思路
# 一匹配
  # 1 小括号
  # 2 匹配乘除
  # 3 匹配加减

# 二 运算
# 乘除
# 加减

# 替换
# 主函数

strvar = "5*6-7/3"
# 一匹配
  # 1 小括号
def pipei_kuohao():
	lst = re.findall(r'\([^()]+\)',strvar)  #最外层的小括号() 必须\转义    ^只能用在[]字符组,如果不在字符组[],就是卡开头
	print(lst)
print('--------------1')

# pipei_kuohao()
  
  # 2 匹配乘除
def pipei_cheng():
	# obj = re.search(r"\d+[*]\d+",strvar)#匹配到一个就返回了
	# res1 = obj.group()
	lst = re.findall(r"\d+[*]\d+",strvar)#匹配到一个就返回了
	
	return lst
# res1 = pipei_cheng()
# print(res1)  #['5*6', '7/3']

def pipei_chu():
	# obj = re.search(r"\d+[/]\d+",strvar)#匹配到一个就返回了
	# res1 = obj.group()
	lst = re.findall(r"\d+[/]\d+",strvar)#匹配到一个就返回了
	
	return lst
# res2 = pipei_chu()
# print(res2)

def pipei_add():
	# obj = re.search(r"\d+[+]\d+",strvar)#匹配到一个就返回了
	# res1 = obj.group()
	lst = re.findall(r"\d+[+]\d+",strvar)#匹配到一个就返回了
	
	return lst
	
def pipei_jian():
	# obj = re.search(r"\d+[-]\d+",strvar)#匹配到一个就返回了
	# res1 = obj.group()
	lst = re.findall(r"\d+[-]\d+",strvar)#匹配到一个就返回了
	
	return lst
	
  # 3 匹配加减

# 二 运算
# 乘除
def cheng():
	a,b = res1[0].split('*')
	res = int(a) * int(b)
	# print(res) 
	return res
# res_cheng = cheng()
# print(res_cheng) #30

def chu():
	a,b = res3[0].split('/')
	res = int(a) / int(b)
	# print(res) 
	return res

# def chu():
	# for i in res1:
		# if '/' in i:
			# pass
		# elif '*' in i:
			# pass
# res_chu = chu()
# print(res_chu) #

# 加减
def add(strvar):
	a,b = strvar.split('+')
	res = float(a) + float(b)
	print(res) 

def jian(strvar):
	a,b = strvar.split('-')
	res = int(a) - float(b)
	print(res)  

# 替换
def tihuan(lst,result):
	global strvar
	strvar = strvar.replace(lst[0],str(result))
	# print(strvar)
	return strvar
	
	
# 主函数
res1 = pipei_cheng()
print(res1)  #['5*6']

res2 = cheng()
print(res2)  #30

res3 = pipei_chu()
print(res3)  #['7/3']

res4 = chu()
print(res4)  #2.3333333333333335

res5 = tihuan(res1,res2)
print(res5)
print('--------1')

res6 = tihuan(res3,res4)
print(res6)

res7 = jian(res6)































