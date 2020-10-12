# ### 列表的深浅拷贝
# 0. 赋值拷贝= 

a = 100
b = a
a = 200  # 新开辟了一个空间 int str是值类型
print(b) #100

lst1 = [1,2,3]
lst2 = lst1
lst1.append(4) #list dict是引用类型  一改都改
print(lst2) #[1, 2, 3, 4]
print('---------------1 赋值拷贝=')

# 1.浅拷贝
import copy
# """模块.方法() 同名模块下的同名方法"""
# 方法一 (推荐)
lst1 = [1,2,3]
lst2 = copy.copy(lst1)
lst1.append(10)
print(lst2) #[1,2,3]  #浅拷贝  第一层独立
print(lst1)  #[1, 2, 3, 10]

# 方法二
lst1 = [1,2,3]
lst2 = lst1.copy()
lst1.append(11)
print(lst1)  #[1, 2, 3, 11]
print(lst2)  #[1,2,3]
print('---------------2 浅拷贝  copy.copy()')

# 2.深拷贝
# """把所有层级的容器元素都单独拷贝一份,放到独立的空间中"""
lst1 = [1,2,3,[4,5,6]]
lst2 = copy.copy(lst1)  #浅拷贝  修改第二层,一改都改
lst1[-1].append(77)
# lst1.append(8888)    #浅拷贝  第一层独立
print(lst2)  #[1, 2, 3, [4, 5, 6, 77]]
print(lst1)  #[1, 2, 3, [4, 5, 6, 77]]

import copy
lst1 = [1,2,3,[4,5,6]]
lst2 = copy.deepcopy(lst1)  ##深拷贝  每一层都完全独立
lst1[-1].append(999)
print(lst2)  #[1,2,3,[4,5,6]]
print(lst1)  #[1, 2, 3, [4, 5, 6, 999]]
print('---------------3 深拷贝  copy.deepcopy()')

# 其他容器的深拷贝
lst1 = (1,2,3,{"a":1,"b":[10,20]})
lst2 = copy.deepcopy(lst1)
lst1[-1]['b'].append(30)
print(lst1)  #(1, 2, 3, {'a': 1, 'b': [10, 20, 30]})
print(lst2)  #(1,2,3,{"a":1,"b":[10,20]})
print('---------------3-2 深拷贝  copy.deepcopy()')

# """
# 总结:
# 浅拷贝:
	# 只拷贝一级容器中的所有元素独立出一个单独的空间.
# 深拷贝:
	# 把所有层级的容器中所有元素都单独拷贝一份,形成独立的空间
# """

# """
# tuple 只有count  index 两个方法 使用同列表
# """





























