# ### 迭代器

# 一.可迭代对象
# 获取当前对象的内置成员
setvar = {"王同培","马春配","赵万里","赵沈阳"}
lst = dir(setvar)
print(lst)
# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
 # '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__',
 # '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__',
 # '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', 
 # '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__',
 # 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
 # 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
 # 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# 判断是否是可迭代对象
# 如果对象的dir方法中包含__iter__,说明该对象是可迭代对象
setvar = {"王同培","马春配","赵万里","赵沈阳"}
lst = dir(setvar)
res = '__iter__' in lst
print(res)  #True  #返回真,就是可迭代对象

#集合不能使用while循环(因为无序),只能使用for循环


# 二.迭代器
# 1 创建迭代器
setvar = {"王同培","马春配","赵万里","赵沈阳"}
it = iter(setvar)  #把可迭代对象转换成迭代器
print(it)  #<set_iterator object at 0x000001FEEDAEB990>

# 2 判断是否是迭代器
# 如果对象的dir方法中包含__iter__和__next__,说明该对象是迭代器
print(dir(it))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
 # '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__',
 # '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

res = '__iter__' in dir(it) and '__next__' in dir(it)
print(res)  #True
print('--------------------2')

# 3 如何调用一个迭代器
setvar = {"王同培","马春配","赵万里","赵沈阳"}
it = iter(setvar)

res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)
# res = next(it)
# print(res)   #StopIteration
print('--------------------3')

# 4 重置迭代器
setvar = {"王同培","马春配","赵万里","赵沈阳"}
it = iter(setvar)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
# print(it.__next__())  #StopIteration
print('--------------------4')

# 5 调用迭代器的其他方法
# 1 for
setvar = {"王同培","马春配","赵万里","赵沈阳"}
it = iter(setvar)
for i in it:
	print(i)
print('--------------------5-1')

# 2 for + next
setvar = {"王同培","马春配","赵万里","赵沈阳"}
it = iter(setvar)
for i in range(2):
	print(next(it))
print('--------------------5-2')

print(next(it))
print(next(it))
# print(next(it))  #StopIteration  error 超出了寻址范围

# 6 判断迭代器/可迭代对象的其他方法
# 从...模块		 引入	... 内容
from collections import Iterator,Iterable
# Iterator  迭代器    迭代器一定是可迭代的对象,反之,不一定
# Iterable	可迭代的对象

res = isinstance(it,Iterator)
print(res) #True
res = isinstance(it,Iterable)
print(res)  #True
print('--------------------6')

# 7 range是迭代器么?   -range不是迭代器,是可迭代的对象
print(isinstance(range(5),Iterator))  #False
print(isinstance(range(5),Iterable))  #True
print(type(range(5)))  #<class 'range'>
print('--------------------7-1')

# 变成迭代器  (把可迭代对象转换成迭代器)
it = range(5).__iter__()
it = iter(range(5))
print(isinstance(it,Iterator))  #True
print(isinstance(it,Iterable)) #True
print('--------------------7-2')

# 调用it-迭代器
# 方法1:next
it = iter(range(5))
res = next(it)
print(res)  #0
print('--------------------7-11')

# 方法2:for + next
for i in range(3):
	print(next(it))
print('--------------------7-12')

# 1
# 2
# 3

# 方法3:for
for i in it:
	print(i)
# 4
print('--------------------7-13')


# 方法4:list()
it = iter(range(5))
res = list(it)
print(res)  #[0, 1, 2, 3, 4]















































