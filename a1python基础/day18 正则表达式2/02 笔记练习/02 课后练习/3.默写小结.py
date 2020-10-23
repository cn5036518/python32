import re
# 反向引用
# 命名分组
# 正则函数
# 修饰符


# 一 反向引用    \1\2  位置  配合()分组使用
strvar = "<div>明天又要休息了</div>"
pattern = re.compile(r'<.*?>.*?<.*?>')
lst = pattern.findall(strvar)
print(lst)
#['<div>明天又要休息了</div>']
print('--------------1 反向引用1')

pattern = re.compile(r'<(.*?)>(.*?)<\1>')
lst = pattern.findall(strvar)
print(lst) #[]\1前面少了一个/

pattern = re.compile(r'<(.*?)>(.*?)</\1>')   #这里的\1和第一个()内的内容一致
lst = pattern.findall(strvar)
print(lst) #[('div', '明天又要休息了')]
print('--------------2 反向引用')

pattern = re.compile(r'<(.*?)>(.*?)<(/\1)>')  #这里的\1和第一个()内的内容一致  \2和第二个()的内容一致
lst = pattern.findall(strvar)
print(lst) #[('div', '明天又要休息了', '/div')]   #只显示分组内的内容 
print('--------------3 反向引用')

# pattern = re.compile(r'<(.*?)>(?:.*?)<(/\1)>')  #报错
pattern = re.compile(r'<(?:.*?)>(?:.*?)<(?:.*?)>')  #
lst = pattern.findall(strvar)
print(lst) #['<div>明天又要休息了</div>']
print('--------------4 反向引用')


# 二 命名分组   ?P<tag1> 标签  ?P=tag1
strvar = "<div>明天又要休息了</div>"
# pattern = re.compile(r'<(.*?)>(.*?)<(/\1)>')  #这里的\1和第一个()内的内容一致  \2和第二个()的内容一致
# 写法1
pattern = re.compile(r'<(?P<tag1>.*?)>(.*?)<(/\1)>')  #
lst = pattern.findall(strvar)
print(lst)  #[('div', '明天又要休息了', '/div')]
print('--------------2-1 命名分组')

# 写法2
strvar = "<div>明天又要休息了</div>"
pattern = re.compile(r'<(?P<tag1>.*?)>(.*?)<(/?P=tag1)>')  #
lst = pattern.findall(strvar)
print(lst)  #[]
print('--------------2-2 命名分组')

strvar = "<div>明天又要休息了<div>"
pattern = re.compile(r'<(?P<tag1>.*?)>(.*?)<(?P=tag1)>')  # 去掉?p前面的/
lst = pattern.findall(strvar)
print(lst)  #[('div', '明天又要休息了')]
print('--------------2-3 命名分组')


# 三 正则函数
# findall  ***
strvar = r'fjaafj s34jjf a123'
lst = re.findall(r'\d+',strvar)
print(lst)  #['34', '123']

strvar = r'fjaafj s34jjf a123'
lst = re.findall(r'(\d+)',strvar)
print(lst)  #['34', '123']  #显示分组的内容

strvar = r'fjaafj s34jjf a123'
lst = re.findall(r'(?:\d+)',strvar)
print(lst)  #['34', '123']  显示匹配的内容
print('------------------------1 findall')

# search   ***  返回对象,匹配第一个满足条件的就返回,不再匹配第二个了
strvar = r"3+4 6*4"
obj = re.search(r'(\d+[+*]\d+)',strvar)
print(obj)  #<_sre.SRE_Match object; span=(0, 3), match='3+4'>
print(obj.group())  #3+4
print(obj.groups())  #('3+4',)
print('------------------------2 search')

# match   从字符串整体的开头开始匹配  和search(r'^')一样  
strvar = r'a13501145281'
obj = re.match(r'\d+',strvar)
print(obj)
print('------------------------3-1 match') #None

strvar = r'13501145281'
obj = re.match(r'\d+',strvar)
print(obj.group())  #13501145281

strvar = r'13501145281'
obj = re.search(r'^\d+',strvar)
print(obj.group())   #13501145281
print('------------------------3-2 match')

# split    ****
strvar = r"alex|wusir_xboyww@risky"
lst = re.split(r'[|_@]',strvar)
print(lst)
#['alex', 'wusir', 'xboyww', 'risky']

strvar = r"alex|wusir_xboyww@risky"
lst = re.split(r'[|_@]',strvar,1)
print(lst)
#['alex', 'wusir_xboyww@risky']
print('------------------------4 split')

# sub 	 ****
strvar = r"alex|wusir_xboyww@risky"
res = re.sub(r'[|_@]','&',strvar)
print(res)  #alex&wusir&xboyww&risky

strvar = r"alex|wusir_xboyww@risky"
strvar_new = re.sub(r'[|_@]','&',strvar,1)
print(strvar_new) #alex&wusir_xboyww@risky
print('------------------------5 sub')

# subn   返回元组  元素1是替换后的字符串 元素2是实际替换次数
strvar = r"alex|wusir_xboyww@risky"
strvar = re.subn(r'[|_@]','&',strvar)
print(strvar)
#('alex&wusir&xboyww&risky', 3)

strvar = r"alex|wusir_xboyww@risky"
strvar = re.subn(r'[|_@]','&',strvar,1)
print(strvar)
#('alex&wusir_xboyww@risky', 1)
print('------------------------6 subn')

# finditer  返回迭代器,迭代器里面是对象
from collections import Iterator,Iterable
strvar = r"alex|wusir_xboyww@risky"
it = re.finditer(r'[\W]',strvar) 
for i in it:
	print(i.group())  
	# |
# @
print(isinstance(it,Iterator)) #True
print('------------------------7 finditer')

# compile
strvar = r"alex|wusir_xboyww@risky"
pattern = re.compile(r'[\W_]')

strvar = pattern.sub('&',strvar)
print(strvar)
#alex&wusir&xboyww&risky
print('------------------------8 strvar')

# 四 修饰符
# re.I  不区分大小写匹配
strvar = "<h1>大标题</H1>"
pattern = re.compile(r'<.*?>.*?<.*?>')
lst = pattern.findall(strvar)
print(lst)  #['<h1>大标题</H1>']

strvar = "<h1>大标题</H1>"
pattern = re.compile(r'<.*?>.*?</h1>')
lst = pattern.findall(strvar)
print(lst)  #[]

strvar = "<h1>大标题</H1>"
pattern = re.compile(r'<.*?>.*?</h1>',flags=re.I)
lst = pattern.findall(strvar)
print(lst)  #['<h1>大标题</H1>']
print('------------------------1 re.I')

# re.M  ^$有影响   多行字符串  单行独立匹配
strvar = """
<p>111</p>
<a>222</a>
<strong>333</strong>
"""
pattern = re.compile(r'^<.*?>.*?<.*?>$')
obj = pattern.search(strvar)
print(obj)  #None  #因为.不能匹配换行符\n

pattern = re.compile(r'<.*?>.*?<.*?>')
obj = pattern.search(strvar)
print(obj)  
print(obj.group())   #<p>111</p>

pattern = re.compile(r'^<.*?>.*?<.*?>$',flags = re.M)
obj = pattern.search(strvar)
print(obj) 
print(obj.group())   #<p>111</p>
print('------------------------2 re.M')

# re.S  使.可以匹配换行/n
strvar = """
give
sdfsdfmefive
"""
pattern = re.compile(r'.*?mefive')
lst = pattern.findall(strvar)
print(lst)  #['sdfsdfmefive']

pattern = re.compile(r'.*?mefive',flags = re.S)
lst = pattern.findall(strvar)
print(lst)  #['\ngive\nsdfsdfmefive']
print('------------------------3 re.S')

# 多个修饰符组合使用
strvar = """
give
sdfsdfmefive
"""
pattern = re.compile(r'(.*?)mefivE',flags = re.S|re.M|re.I)
obj = pattern.search(strvar)
print(obj)
print(obj.group())

# give
# sdfsdfmefive
print(obj.groups())  #('\ngive\nsdfsdf',)
print('------------------------4 多个修饰符')








































