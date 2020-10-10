# ### 反向引用
import re
strvar = r"<div>明天又要休息了</div>"
# obj = re.search(r'<.*?>',strvar)  #<div>
# obj = re.search(r'<.*>',strvar)  #<div>明天又要休息了</div>
obj = re.search(r'<.*?>.*?<.*?>',strvar)
print(obj)
# <.*?>  非贪婪
#.任意一个字符  
#*是0次或多次
#*? 非贪婪  <开头 第一个>结尾 中间是任意个字符   <div>

# <.*>
#.任意一个字符  
#*是0次或多次
# 贪婪  <开头 最后一个>结尾 中间是任意个字符  <div>明天又要休息了</div>


# 获取匹配到的内容  多
res1 = obj.group()
print(res1)  #<div>明天又要休息了</div>
 
# 获取分组里的内容
res2 = obj.groups()  #少
print(res2)  #()   #没有分组,就返回空元组
print('-------------------1')

strvar = r"<div>明天又要休息了</div>"
# obj = re.search(r'<.*?>',strvar)  #<div>
# obj = re.search(r'<.*>',strvar)  #<div>明天又要休息了</div>
obj = re.search(r'(<.*?>)(.*?)(<.*?>)',strvar)
print(obj)
# <.*?>  非贪婪
#.任意一个字符  
#*是0次或多次
#*? 非贪婪  <开头 第一个>结尾 中间是任意个字符   <div>

# <.*>
#.任意一个字符  
#*是0次或多次
# 贪婪  <开头 最后一个>结尾 中间是任意个字符  <div>明天又要休息了</div>


# 获取匹配到的内容  多
res1 = obj.group()
print(res1)  #<div>明天又要休息了</div>
 
# 获取分组里的内容  少
res2 = obj.groups()
print(res2)  #('<div>', '明天又要休息了', '</div>')
print('-------------------2')

# 反向引用的语法 \1把第一个括号里面匹配到的内容再引用一次

strvar = r"<div>明天又要休息了</div>"
obj = re.search(r'(<.*?>)(.*?)(<.*?>)',strvar)
obj = re.search(r"<(.*?)>(.*?)</\1>",strvar)   #('div', '明天又要休息了')
# obj = re.search(r"<(.*?)>(.*?)<(/\1)>",strvar)  #('div', '明天又要休息了', '/div')
print(obj) #<_sre.SRE_Match object; span=(0, 18), match='<div>明天又要休息了</div>'>
print(obj.group())  #<div>明天又要休息了</div>
print(obj.groups()) #('div', '明天又要休息了')
print('-------------------3')

strvar = r" z3d4pzd a1b2cab "
obj = re.search(r'(.*?)\d(.*?)\d(.*?)\1\2',strvar)
print(obj) #<_sre.SRE_Match object; span=(1, 8), match='z3d4pzd'>
print(obj.group())  #z3d4pzdssss
print(obj.groups())  #('z', 'd', 'p')
print('-------------------4')

# ### 命名分组
# 3) (?P<组名>正则表达式) 给这个组起一个名字
# 4) (?P=组名) 引用之前组的名字,把该组名匹配到的内容放到当前位置
# 写法一
strvar = r" z3d4pzd a1b2cab "
obj = re.search(r'(?P<tag1>.*?)\d(?P<tag2>.*?)\d(.*?)\1\2',strvar)
print(obj)  #<_sre.SRE_Match object; span=(1, 8), match='z3d4pzd'>
print(obj.group()) #z3d4pzd
print(obj.groups()) #('z', 'd', 'p')

# 写法一
strvar = r" z3d4pzd a1b2cab "
obj = re.search(r'(?P<tag1>.*?)\d(?P<tag2>.*?)\d(.*?)(?P=tag1)(?P=tag2)',strvar)
print(obj)  #<_sre.SRE_Match object; span=(1, 8), match='z3d4pzd'>
print(obj.group()) #z3d4pzd
print(obj.groups()) #('z', 'd', 'p')
print('-------------------5')

strvar = r" z3d4pzd a1b2cab "
lst = re.findall(r'(?P<tag1>.*?)\d(?P<tag2>.*?)\d(.*?)(?P=tag1)(?P=tag2)',strvar)
print(lst)
#[('z', 'd', 'p'), ('a', 'b', 'c')]

strvar = r" z3d4pzd a1b2cab "
lst = re.findall(r'(?P<tag1>.*?)\d(?P<tag2>.*?)\d(?:.*?)(?P=tag1)(?P=tag2)',strvar)
lst = re.findall(r'(?P<tag1>.*?)\d(?P<tag2>.*?)\d(.*?)(?P=tag1)(?P=tag2)',strvar)
print(lst)  #[('z', 'd', 'p'), ('a', 'b', 'c')]
























