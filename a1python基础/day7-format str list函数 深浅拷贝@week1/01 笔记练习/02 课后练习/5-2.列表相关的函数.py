# ### 列表相关的函数  增删改查
# 一 新增  append insert extend
# 01 append 向列表的末尾添加新的元素
lst = ["赵沈阳"]
lst.append('jack')
print(lst)  #['赵沈阳', 'jack']

# 02 insert 在指定索引之前插入元素
lst = ['赵沈阳', '沈思雨']
lst.insert(1,'王伟')
print(lst) #['赵沈阳', '王伟', '沈思雨']

# 03 extend 迭代追加所有元素
# """迭代追加的数据是可迭代性数据
#(容器类型数据str tuple list dict set,range对象,迭代器)"""
lst = ['赵沈阳', '沈思雨']
tup = (1,2,3)
lst.extend(tup)
print(lst)  #['赵沈阳', '沈思雨', 1, 2, 3]

lst = ['赵沈阳', '沈思雨']
strvar = "abc"
lst.extend(strvar)
print(lst)  #['赵沈阳', '沈思雨', 'a', 'b', 'c']

lst = ['赵沈阳', '沈思雨']
lst.extend(range(2))
print(lst)
#['赵沈阳', '沈思雨', 0, 1]
print('----------------1 append insert extend')

# 删除   pop remove clear
# 1.pop 通过指定索引删除并获取元素,若没有索引移除最后那个 (推荐)
lst = ["曹静怡","王志国","邓鹏","合理"]
# 01 不指定下标,默认删除最后一个
res = lst.pop()
print(res)  #合理
print(lst)  #['曹静怡', '王志国', '邓鹏']

# 02 指定下标,删除并获取具体某个元素
lst = ["曹静怡","王志国","邓鹏","合理"]
res = lst.pop(1)
print(res)  #王志国
print(lst) #['曹静怡', '邓鹏', '合理']


# 2.remove 通过给予的值来删除,如果多个相同元素,默认删除左边第一个
lst = ["曹静怡","王志国","合理","邓鹏","合理"]
res = lst.remove('合理')
print(res)  #None
print(lst) #['曹静怡', '王志国', '邓鹏', '合理']

# 3.clear 清空列表
lst = ["曹静怡","王志国","合理","邓鹏","合理"]
lst.clear()
print(lst) #[]
print('----------------2 pop remove clear')

# 改查 参考4.py

# 三 列表的其他相关函数 index count sort reverse
# 01 index 获取某个值在列表中的索引
lst = ["曹静怡","王志国","合理","邓鹏","合理","邓鹏辉","邓鹏蓝","合理","邓鹏绿"]
res = lst.index('合理')
print(res)  #2

res = lst.index('合理',3)
print(res)  #4

res = lst.index('合理',3,6) # 3 4 5
print(res)  #4

# res = lst.index('合力达')
# ValueError: '合力达' is not in list
print(res)
print('----------------3-1 index')

# 02 count 计算某个元素出现的次数
lst = ["曹静怡","王志国","合理","邓鹏","合理","邓鹏辉","邓鹏蓝","合理","邓鹏绿"]
res = lst.count('合理')   # 没有范围的概念 整个列表
print(res)   # 3

# 03 sort 对列表排序
lst = [-90,-100,-1,90,78]
# 从小到大进行排序
lst.sort()
print(lst)  #[-100, -90, -1, 78, 90]

lst = [-90,-100,-1,90,78]
# 从大到小进行排序
lst.sort(reverse= True)
print(lst)  #[90, 78, -1, -90, -100]

# 对字符串进行排序(按照ascii编码)
lst = ["kobi","james","jordon","yaoming","yi"]
lst.sort()
print(lst) #['james', 'jordon', 'kobi', 'yaoming', 'yi']

# 是否可以对中文排序(了解 无规律可循)
lst = ["王文","蔡徐坤"]
lst.sort()
print(lst)  #['王文', '蔡徐坤']

# 04 reverse 列表反转操作
lst = [1,2,"a","蔡徐坤","易烊千玺"]
lst.reverse()
print(lst)
#['易烊千玺', '蔡徐坤', 'a', 2, 1]
print('----------------3 index count sort reverse')
































