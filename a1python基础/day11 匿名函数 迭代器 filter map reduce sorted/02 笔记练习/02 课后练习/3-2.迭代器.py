# ### 迭代器

# 一.可迭代对象
setvar = {"王同培","马春配","赵万里","赵沈阳"}
# 获取当前对象的内置成员
print(dir(setvar))
# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
# '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__',
 # '__ixor__'

# 判断是否是可迭代对象(容器,range对象,迭代器)
res = '__iter__' in dir(setvar)
print(res)  #True

# 二.迭代器
# 1创建一个迭代器
setvar = {"王同培","马春配","赵万里","赵沈阳"}
it = iter(setvar)
print(it)  #<set_iterator object at 0x7f0a91c1f360>

# 2 如何判断一个迭代器
res = '__iter__' in dir(it) and '__next__' in dir(it)
print(res)  #True

from collections import Iterator,Iterable
print(isinstance(it,Iterator))  #True

# 3 调用迭代器
# 1 next
print(next(it))  
print(it.__next__())

# 2 next for  用多少,取多少
for i in range(2):
	print(next(it))
print('--------------------3-2')

# 3 for
it = iter(setvar)
for i in it:
	print(i)
print('--------------------3-3')

# 4 list
it = iter(setvar)
print(list(it))
# ['马春配', '王同培', '赵万里', '赵沈阳']

# 4 range是可迭代对象,不是迭代器,如何转成迭代器
print(isinstance(range(3),Iterable)) #True
print(isinstance(range(3),Iterator)) #False

it = iter(range(3))
it = range(3).__iter__()
print(isinstance(it,Iterator)) #True





































