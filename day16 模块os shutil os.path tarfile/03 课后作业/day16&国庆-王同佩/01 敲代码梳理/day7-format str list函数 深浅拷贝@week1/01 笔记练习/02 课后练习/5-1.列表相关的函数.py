# ###  列表相关的函数
# 增 append insert entend
# append 向列表的末尾添加新的元素
lst = ['赵沈阳']
lst.append('沈思雨')
print(lst)  #['赵沈阳', '沈思雨']

# insert 在指定索引之前插入元素
lst = ['赵沈阳', '沈思雨']
lst.insert(1,'王伟')
print(lst)  #['赵沈阳', '王伟', '沈思雨']

# extend 迭代追加所有元素
# 迭代追加的数据是可迭代性的数据(容器类型数据,range对象,迭代器)
lst = ['赵沈阳','沈思雨']
tup = (1,2,3)
lst.extend(tup)
print(lst)  #['赵沈阳', '沈思雨', 1, 2, 3]

strvar = 'abc'
lst.extend(strvar)
print(lst) #['赵沈阳', '沈思雨', 1, 2, 3, 'a', 'b', 'c']

lst = ['赵沈阳','沈思雨']
lst.extend(range(3))
print(lst)  #['赵沈阳', '沈思雨', 0, 1, 2]

# 删  pop remove clear
# 1.pop 通过指定索引删除元素,若没有索引移除最后那个(推荐)
lst = ['曹静怡','王志国','邓鹏','合理']
# 不指定下标,默认删除最后一个
res = lst.pop()
print(res)  # 合理
print(lst)  #['曹静怡', '王志国', '邓鹏']

# 指定下标,删除具体某个元素
lst = ['曹静怡','王志国','邓鹏','合理']
res = lst.pop(1)
print(res) # 王志国
print(lst)  #['曹静怡', '邓鹏', '合理']

# 2.remove 通过给予的值来删除,如果多个相同元素,默认删除第一个
lst = ['曹静怡','王志国','邓鹏','合理']
res = lst.remove('合理')
print(res)  #None
print(lst)  #['曹静怡', '王志国', '邓鹏']

# 3.clear 清空列表
lst = ['曹静怡','王志国','邓鹏','合理']
lst.clear()
print(lst)  #[]

# 改查  参考4.py

# 列表的其他相关函数    index count sort reverse
# 1 index  获取某个值在列表中的索引
lst = ['曹静怡','王志国','合理',"邓鹏","合理","邓鹏辉","邓鹏蓝","合理","邓鹏绿"]
res = lst.index('合理')
print(res)  #2

res = lst.index('合理',3)
print(res)  #4

res = lst.index('合理',3,6)  # 3 4 5
print(res)  #4

# res = lst.index('合理大')  #报错  list中没有find方法(str有find方法  没有返回-1)
#ValueError: '合理大' is not in list

# 2 count 计算某个元素出现的次数
lst = ['曹静怡','王志国','合理',"邓鹏","合理","邓鹏辉","邓鹏蓝","合理","邓鹏绿"]
res = lst.count('合理')  #没有start end
print(res)  #3

# 3 sort 对列表排序
lst = [-90,-100,-1,90,78]
# 默认从小到大排序 列表本身修改了
lst.sort()
print(lst)  #[-100, -90, -1, 78, 90]

lst = [-90,-100,-1,90,78]
# 从大到小排序
lst.sort(reverse= True)
print(lst)  #[90, 78, -1, -90, -100]

# 对字符串进行排序(按照ascii编码)
lst = ['kobi','james','jordan','yaoming','yi']
lst.sort()
print(lst)  # ['james', 'jordan', 'kobi', 'yaoming', 'yi']

# 是否可以对中文排序(了解 无规律可循)
lst = ['王文','蔡徐坤']
lst.sort()
print(lst)  #['王文', '蔡徐坤']

# 4 reverse 列表反转操作
lst = [1,2,'a','蔡徐坤','易烊千玺']
lst.reverse()  # 列表本身修改了
print(lst)  #['易烊千玺', '蔡徐坤', 'a', 2, 1]






























