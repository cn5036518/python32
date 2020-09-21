# ### 1.集合的相关操作 (交差并补)

#intersection()  交集
set1 = {'易烊千玺','王一博','刘某','王文'}
set2 = {'倪萍','赵忠祥','金龟子','小龙人','王文'}

res = set1.intersection(set2)
print(res)  #{'王文'}

# 简写 &
res = set1 & set2
print(res)  #{'王文'}

# difference()  差集
res = set1.difference(set2)
print(res)  #{'易烊千玺', '王一博', '刘某'}

# 简写  -
res = set1 - set2
print(res)  #{'刘某', '王一博', '易烊千玺'}

# symmetric_difference()  #对称差集 (补集情况涵盖在其中)
res = set1.symmetric_difference(set2)
print(res)  #{'赵忠祥', '金龟子', '易烊千玺', '王一博', '倪萍', '刘某', '小龙人'}

# 简写 ^
res = set1 ^ set2
print(res)  #{'赵忠祥', '小龙人', '刘某', '金龟子', '易烊千玺', '倪萍', '王一博'}

# issubset()  判断是否是子集
set1 = {'刘德华','郭富城','张学友','王文'}
set2 = {'王文'}
res = set2.issubset(set1)
print(res)  #True

# 简写 <
res = set2 < set1
print(res)   #True


# issuperset 判断是否是父集
set1 = {'刘德华','郭富城','张学友','王文'}
set2 = {'王文'}
res = set1.issuperset(set2)
print(res) #True

# 简写
res = set1 > set2
print(res) #True

# isdisjoint()  检测两集合是否不想交  不想交 True 相交False
set1 = {'刘德华','郭富城','张学友','王文'}
set2 = {'王文'}
res = set1.isdisjoint(set2)
print(res)  #False

# ### 2.集合的相关函数 增删
# 增
# add()  向集合中添加数
# 一次加一个
set1 = {'王文'}
set1.add('王伟')
print(set1)  #{'王伟', '王文'}

# update() 迭代着增加
# 一次加多个
set1 = {'王文'}
lst = ['a','b','c']
set1.update(lst)
print(set1)  #{'c', 'a', '王文', 'b'}

set1 = {'王文'}
lst = 'ppp'  #迭代添加,无序,自动去重
set1.update(lst)
print(set1)  #{'王文', 'p'}

# 删
setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
# 1 clear()  清空集合
setvar.clear()
print(setvar)  #set()

# 2 pop() 随机删除集合中的一个数据
setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
res = setvar.pop()
print(res) #刘某PDD
print(setvar)  #{'小龙人', '赵忠祥', '倪萍'}

# 3 discard() 删除集合中指定的值(不存在的不删除,推荐使用)   ***
setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
setvar.discard('刘某PDD111111') #success
print(setvar)  #{'小龙人', '倪萍', '刘某PDD', '赵忠祥'}

setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
setvar.discard('倪萍')
print(setvar)  #{'赵忠祥', '小龙人', '刘某PDD'}

# 4 remove() 删除集合中指定的值(不存在则报错) (了解)
setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
setvar.remove('小龙人')
print(setvar)  #{'刘某PDD', '赵忠祥', '倪萍'}

# setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
# setvar.remove('小龙人11')  #KeyError: '小龙人11'
# print(setvar)  

# ### 3.冰冻集合(额外了解)
# frozenset 单纯的只能做交差并补操作,不能做添加或者删除的操作
lst = ['王文','宋健','何旭彤']
fz1 = frozenset(lst)
print(fz1,type(fz1))
# frozenset({'宋健', '何旭彤', '王文'}) <class 'frozenset'>
# numbers str tuple list dict set 是6个基本的数据类型
# frozenset 是6个基本的数据类型之外的类型

# 不能在冰冻集合中添加或删除元素
# fz1.add(1)  #AttributeError: 'frozenset' object has no attribute 'add'
# fz1.update('abc')
# AttributeError: 'frozenset' object has no attribute 'update'
# fz1.discard('王文')
# AttributeError: 'frozenset' object has no attribute 'discard'

# 冰冻集合只能做交差并补
lst2 = ['王文','王同佩']
fz2 = frozenset(lst2)
print(fz2,type(fz2))  #frozenset({'王同佩', '王文'}) <class 'frozenset'>

# 交集
res = fz1 & fz2
print(res)  #frozenset({'王文'})

# 差集 对称差集 -

#  并集  |

# 补集 symetric_differerce

# 遍历冰冻集合
for i in fz2:
	print(i)
# 王文
# 王同佩



























































