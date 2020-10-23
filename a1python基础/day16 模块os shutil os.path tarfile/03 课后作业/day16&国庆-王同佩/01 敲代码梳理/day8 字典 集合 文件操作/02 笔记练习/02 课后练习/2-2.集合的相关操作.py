# ### 集合的相关操作 (交差并补)

# 1 intersection() 交集  &
set1 = {"易烊千玺","王一博","刘某PDD","王文"}
set2 = {"倪萍","赵忠祥","金龟子大风车","小龙人","王文"}

res = set1.intersection(set2)
print(res) #{'王文'}

res = set1 & set2
print(res) #{'王文'}
print('-------------------------------1 交集')

# 2 difference()  差集  -
set1 = {"易烊千玺","王一博","刘某PDD","王文"}
set2 = {"倪萍","赵忠祥","金龟子大风车","小龙人","王文"}

res = set1.difference(set2)
print(res)  #{'王一博', '易烊千玺', '刘某PDD'}

res = set1 - set2
print(res)  #{'王一博', '易烊千玺', '刘某PDD'}
print('-------------------------------2 差集')

# 3 union() 并集 |
set1 = {"易烊千玺","王一博","刘某PDD","王文"}
set2 = {"倪萍","赵忠祥","金龟子大风车","小龙人","王文"}

res = set1.union(set2)
print(res) #{'王一博', '赵忠祥', '刘某PDD', '金龟子大风车', '易烊千玺', '王文', '小龙人', '倪萍'}

res = set1 | set2
print(res)
#{'王一博', '赵忠祥', '刘某PDD', '金龟子大风车', '易烊千玺', '王文', '小龙人', '倪萍'}
print('-------------------------------3 并集')

# 4 symmetric_difference() 对称差集(补集在其中) ^
set1 = {"易烊千玺","王一博","刘某PDD","王文"}
set2 = {"倪萍","赵忠祥","金龟子大风车","小龙人","王文"}

res = set1.symmetric_difference(set2)
print(res) #{'刘某PDD', '倪萍', '易烊千玺', '金龟子大风车', '王一博', '赵忠祥', '小龙人'}

res = set1 ^ set2
print(res)
#{'刘某PDD', '倪萍', '易烊千玺', '金龟子大风车', '王一博', '赵忠祥', '小龙人'}
print('-------------------------------4 补集')

# 5 issubset() 子集  <
set1 = {"刘德华","郭富城","张学友","王文"}
set2 = {"王文"}

res = set2.issubset(set1)
print(res)  #True

res = set2 < set1
print(res) #True
print('-------------------------------5 子集')

# 6 issuperset() 父集  >
set1 = {"刘德华","郭富城","张学友","王文"}
set2 = {"王文"}

res = set1.issuperset(set2)
print(res)  #True

res = set1 > set2
print(res)  #True
print('-------------------------------6 父集')

# 7 isdisjoint() 不相交
set1 = {"刘德华","郭富城","张学友","王文"}
set2 = {"王文"}
res = set1.isdisjoint(set2)
print(res)  #False
print('-------------------------------7 不相交')

# ###集合的相关函数   只能增删,不能修改,不能获取(查) 无序去重
# 一 增加
# 01 单个添加(一次添加一个)
#add()    向集合中添加数据
set1 = {"王文"}
set1.add('王伟')
set1.add('王伟') #
print(set1)  #{'王伟', '王文'}
print('-------------------------------1 增加add')

# 02 多个添加(一次添加多个)
#update() 迭代着增加
set1 = {"王文"}
lst = ["a","b","c"]
res = set1.update(lst)  ##参数是可迭代数据（容器类型 range对象 迭代器）
print(res) # None
print(set1)  #{'王文', 'c', 'a', 'b'}

set1 = {"王文"}
str1 = 'ppp'
set1.update(str1)
print(set1) #{'王文', 'p'}   # 迭代这添加,无序,会自动去重
print('-------------------------------2 增加update')


# 二 删除  pop(不推荐) discard remove(不推荐) clear
# 01 方法1 pop()  随机删除集合中的一个数据  不推荐
setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
res = setvar.pop()
print(res) #刘某PDD
print(setvar)  #{'小龙人', '赵忠祥', '倪萍'}
print('-------------------------------删除 pop 1')

# 02 方法2 discard
#discard() 删除集合中指定的值(不存在的不删除 推荐使用) ***
setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
res = setvar.discard('小龙人')
print(res) #None
print(setvar)  #{'赵忠祥', '倪萍', '刘某PDD'}
print('-------------------------------删除 discard 2-1')

setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
res = setvar.discard('小龙人1123') #不存在的不删除,不会报错
print(setvar)  #{'小龙人', '刘某PDD', '倪萍', '赵忠祥'}
print('-------------------------------删除 discard 2-2')

# 03 方法3 remove  不推荐
#remove()  删除集合中指定的值(不存在则报错) (了解)
setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
setvar.remove('小龙人')  
print(setvar) #{'赵忠祥', '倪萍', '刘某PDD'}
print('-------------------------------删除 remove 3-1')

setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
# setvar.remove('小龙人123')
# print(setvar) ##KeyError: '小龙人123'
print('-------------------------------删除 remove 3-2')


# 04 方法4 clear()  清空集合
setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
setvar.clear()
print(setvar)  #set()
print('-------------------------------删除 clear 4')

# ### 3.冰冻集合 (额外了解)
# """frozenset 单纯的只能做交差并补操作,不能做添加或者删除的操作  只读"""
lst = ["王文","宋健","何旭彤"]
fz1 = frozenset(lst)
print(fz1)
#frozenset({'宋健', '王文', '何旭彤'})

# 不能在冰冻集合中添加或者删除元素
# fz1.add(1) #AttributeError: 'frozenset' object has no attribute 'add'
# fz1.update("abc") #AttributeError: 'frozenset' object has no attribute 'update'
# fz1.discard("王文") #AttributeError: 'frozenset' object has no attribute 'discard'

# 冰冻集合只能做交差并补
lst2 = ["王文","王同培","刘一缝"]
fz2 = frozenset(lst2)
print(fz2,type(fz2))  #frozenset({'王文', '王同培', '刘一缝'}) <class 'frozenset'>

# 交集
res = fz1 & fz2
print(res)  #frozenset({'王文'})

# 遍历冰冻集合
for i in fz2:
	print(i)
# 刘一缝
# 王文
# 王同培

# set和frozenset(只读) 类比 list和tuple(只读)
# set 交差并补 增加 删除 遍历  不能修改 不能获取(单个查)
# frozenset 交差并补 遍历 不能增加 不能删除 不能修改 不能获取(单个查)




























