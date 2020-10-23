# ### 正则函数
import re
# search   通过正则匹配出第一个对象返回，通过group取出对象中的值   ***
#groups取出分组()中的值
strvar = r"3+4 6*4"
obj = re.search(r'\d+[+*]\d+',strvar)
obj = re.search(r'(\d+[+*]\d+)',strvar)
print(obj) #<_sre.SRE_Match object; span=(0, 3), match='3+4'>

# 获取匹配到的内容
print(obj.group())  #3+4

# 获取分组当中的内容 (返回元组)
print(obj.groups())  #('3+4',)
print('-------------------1 search')


# match    验证用户输入内容 (了解)
# """search在正则表达式的前面加上^ 等价于 match ,其他用法上一模一样"""
strvar = r"a17366668888"
# strvar = r"17366668888"
obj = re.search(r'^\d+',strvar)
print(obj)  #None
obj = re.match(r'd+',strvar)
print(obj) #None
print('-------------------2 match')

# split    切割  返回list  先用正则将分隔符匹配出来  ****
# 字符串有split os.path.split
strvar = r"alex|wusir_xboyww@risky"  
# 01 按特殊符号将上述字符串分割
lst = re.split(r'[|_@]',strvar)
print(lst)
#['alex', 'wusir', 'xboyww', 'risky']

strvar = r"alex2341273894wusir234234xboyww11111risky"
# 02 按数字将上述字符串分割
lst = re.split(r'\d+',strvar)
print(lst)
#['alex', 'wusir', 'xboyww', 'risky']
print('-------------------3 split')


# sub      替换      ****
# 字符串有replace 
strvar = r"alex|wusir_xboyww@risky"
# 01 把特殊字符统一替换成&
strvar = strvar.replace('|','&')
strvar = strvar.replace('_','&')
strvar = strvar.replace('@','&')
print(strvar)
# alex&wusir&xboyww&risky

# sub(正则,替换的字符,原字符串[,替换的次数])
res = re.sub(r'[|_@]','&',strvar)
print(res)  #全部替换
#alex&wusir&xboyww&risky

strvar = r"alex|wusir_xboyww@risky"
res = re.sub(r'[|_@]','&',strvar,1)
print(res)  #替换左边第一个特殊字符
#alex&wusir_xboyww@risky
print('-------------------4 sub')

# subn     替换  (用法上与sub相同,只是返回值不同)
# 返回的是元组(第一个元素是替换后的字符串  第二个元素是实际替换的次数)
strvar = r"alex|wusir_xboyww@risky"
res = re.subn(r'[|_@]','&',strvar)
print(res) #('alex&wusir&xboyww&risky', 3)
 
strvar = r"alex|wusir_xboyww@risky"
res = re.subn(r'[|_@]','&',strvar,2)
print(res)
#('alex&wusir&xboyww@risky', 2)
print('-------------------5 subn')

# finditer 匹配字符串中相应内容,返回迭代器
# """返回的是迭代器,迭代器中包含了对象 对象.group来获取匹配到的值"""
from collections import Iterator,Iterable
strvar = r"sdf23647fdgdfg()*()*23423423"
it = re.finditer(r'\d+',strvar)
print(isinstance(it,Iterator))  #True

for i in it:
	print(i.group())
	#23647
# 23423423

#findall 返回的是list
#finditer 返回的是迭代器
print('-------------------6 finditer')


# compile  指定一个统一的匹配规则
# """
# 正常情况下,正则表达式编译一次,执行一次
# 为了避免反复编译,节省时间空间,可以使用compile统一规则
# 编译一次,终身受益
# """
strvar = r"asdfs234sdf234"
pattern = re.compile('\d+')

obj = pattern.search(strvar)
print(obj.group())  #234
print(obj.groups())  #()  没有分组,返回空元组
print('-------------------7 compile')


# 修饰符 
# re.I 使匹配对大小写不敏感
strvar = r"<h1>大标题</H1>"
pattern = re.compile(r'<h1>(.*?)</h1>',flags=re.I)

obj = pattern.search(strvar)
print(obj.group())
#<h1>大标题</H1>
print('-------------------1 修饰符 re.I')

# re.M 使每一行都能够单独匹配(多行匹配)，影响 ^ 和 $
# """单行独立匹配,而不是整体匹配"""
# strvar = """
# <p>111</p>
# <a>222</a>
# <strong>333</strong>
# """

# pattern = re.compile(r'<.*?>(.*?)<.*?>',flags=re.M)
pattern = re.compile(r'<.*?>(.*?)<.*?>')
lst = pattern.findall(strvar)
print(lst)  #['111', '222', '333']

pattern = re.compile(r'^<.*?>(.*?)<.*?>$')
lst = pattern.findall(strvar)
print(lst)  #() #因为.不能匹配换行符号

pattern = re.compile(r'^<.*?>(.*?)<.*?>$',flags=re.M)
lst = pattern.findall(strvar)
print(lst)
#['111', '222', '333']

pattern = re.compile(r'^<.*?>(?:.*?)<.*?>$',flags=re.M)
lst = pattern.findall(strvar)
print(lst)
#['<p>111</p>', '<a>222</a>', '<strong>333</strong>']

print('-------------------2 修饰符 re.M')


# re.S 使 . 匹配包括换行在内的所有字符
strvar = """
give
sdfsdfmefive
"""
pattern = re.compile(r'.*?mefive')
obj = pattern.search(strvar)
print(obj.group())
#sdfsdfmefive
print('-------------------3-1 修饰符 re.S')

strvar = """
give
sdfsdfmefive
"""
pattern = re.compile(r'.*?mefive',flags=re.S)
obj = pattern.search(strvar)
print(obj.group())

# give
# sdfsdfmefive
print('-------------------3-2 修饰符 re.S')

# 多个修饰符一起使用通过|拼接
strvar = """
give
sdfsdfmefive
"""
pattern = re.compile(".*?mefivE" , flags = re.S|re.I|re.M )
obj = pattern.search(strvar)
print(obj.group())

# give
# sdfsdfmefive
print('-------------------4 多个修饰符')


























