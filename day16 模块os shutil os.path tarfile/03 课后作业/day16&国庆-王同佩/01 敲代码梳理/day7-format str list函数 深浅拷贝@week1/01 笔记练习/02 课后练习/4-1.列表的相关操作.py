# ### 列表的相关操作  #增删改查
lst1 = ['孟凡伟','康玉忠']
lst2 = ['康玉忠','张宇']
# (1)列表的拼接  (同元组)  +
res = lst1 + lst2
print(res)  #['孟凡伟', '康玉忠', '康玉忠', '张宇']

# (2)列表的重复  (同元组)  *
res = lst1 * 3
print(res)  #['孟凡伟', '康玉忠', '孟凡伟', '康玉忠', '孟凡伟', '康玉忠']

# (3)列表的切片  (同元组)
'''
语法 => 列表[::]  完整格式：[开始索引:结束索引:间隔值]
	(1)[开始索引:]  从开始索引截取到列表的最后
	(2)[:结束索引]  从开头截取到结束索引之前(结束索引-1)
	(3)[开始索引:结束索引]  从开始索引截取到结束索引之前(结束索引-1)
	(4)[开始索引:结束索引:间隔值]  从开始索引截取到结束索引之前
	按照指定的间隔截取列表元素值
	(5)[:]或[::]  截取所有列表
'''
lst = ['孟凡伟','康玉忠','张宇','赵沈阳','需保障','梁新宇','沈思雨']
# (1)[开始索引:]  从开始索引截取到列表的最后
res = lst[2:]
print(res)  #['张宇', '赵沈阳', '需保障', '梁新宇', '沈思雨']

# (2)[:结束索引]  从开头截取到结束索引之前(结束索引-1)
lst = ['孟凡伟','康玉忠','张宇','赵沈阳','需保障','梁新宇','沈思雨']
res = lst[:3]
print(res)  #['孟凡伟', '康玉忠', '张宇']

# (3)[开始索引:结束索引]  从开始索引截取到结束索引之前(结束索引-1)
res = lst[3:5]
print(res)  #['赵沈阳', '需保障']

#(4)[开始索引:结束索引:间隔值]  从开始索引截取到结束索引之前
	# 按照指定的间隔截取列表元素值
#正向截取
lst = ['孟凡伟','康玉忠','张宇','赵沈阳','需保障','梁新宇','沈思雨']
res = lst[::5]  #0 5 10
print(res)  #['孟凡伟', '梁新宇']
# 逆向截取
res = lst[::-3]  # -1 -4 -7
print(res)  #['沈思雨', '赵沈阳', '孟凡伟']

#(5) [:]或[::]  截取所有列表
res = lst[:]
res = lst[::]
print(res) 
 #['孟凡伟', '康玉忠', '张宇', '赵沈阳', '需保障', '梁新宇', '沈思雨']

# (4)列表的获取  (同元组)
#       0  1  2
lst = [10,20,30]
# 		-3 -2 -1
print(lst[-1])

# (5)列表的修改  (可切片)
lst = ['孟凡伟','康玉忠','张宇','赵沈阳','需保障','梁新宇','沈思雨']
# 1 修改单个值
lst[1] = '陈璐'
print(lst)  #['孟凡伟', '陈璐', '张宇', '赵沈阳', '需保障', '梁新宇', '沈思雨']

# 2.修改多个值
# (如果使用切片进行修改,要求数据必须是iterable可迭代的)
lst = ['孟凡伟','康玉忠','张宇','赵沈阳','需保障','梁新宇','沈思雨']
lst[1:4] = ['孙悟空','猪八戒','白骨精']
print(lst)  #['孟凡伟', '孙悟空', '猪八戒', '白骨精', '需保障', '梁新宇', '沈思雨']

lst[1:4] = '你好'
print(lst)  #['孟凡伟', '你', '好', '需保障', '梁新宇', '沈思雨']

# 3.修改多个值(带有步长)
# 带有步长的切片修改,切出几个元素就修改几个元素,数量要一致
lst = ['孟凡伟','康玉忠','张宇','赵沈阳','需保障','梁新宇','沈思雨']
lst[::3] = 'abc' # 0 3 6
print(lst)  #['a', '康玉忠', '张宇', 'b', '需保障', '梁新宇', 'c']

# lst[::3] = 'ab'  #报错
#ValueError: attempt to assign sequence of size 2 to extended slice of size 3

# (6)列表的删除  (可切片)
lst = ['孟凡伟','康玉忠','张宇','赵沈阳','需保障','梁新宇','沈思雨']
# 1.一次删除一个
# del lst[2]
print(lst)  #['孟凡伟', '康玉忠', '赵沈阳', '需保障', '梁新宇', '沈思雨']

# 2.一次删多个
del lst[1:-1]
print(lst)  #['孟凡伟', '沈思雨']

# 3.注意点
res = lst[1:-1]
del res # 删除的是res这个变量 和列表无关
print(lst)  #['孟凡伟', '沈思雨']

# 额外的注意点
# 元组的一级元素不能修改,二级元素可以修改
tup = (1,2,3,4,[10,11,12])
print(tup[-1])
tup[-1][-1] = 13
print(tup)  #(1, 2, 3, 4, [10, 11, 13])


































