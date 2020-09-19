# ### 列表的深浅拷贝
a = 100
b = a
a = 200  #str 新开辟了一个空间 两个变量对应2个空间
print(b) #100

lst1 = [1,2,3]
lst2 = lst1  # 列表赋值,没有新开辟空间,还是同一个空间  (两个列表变量指向同一个空间)
lst1.append(4)
print(lst2)  #[1, 2, 3, 4]  列表等号赋值,一改都改


# 1.浅拷贝
import copy
# 模块.方法() 同名模块下的同名方法
# 方法一 (推荐)
lst1 = [1,2,3]
lst2 = copy.copy(lst1)  #lst1和lst2 对应不同的空间,第一层拷贝(独立)
lst1.append(10)
print(lst2) #[1,2,3]
print(lst1) #[1,2,3,10]

# 方法二
lst1 = [1,2,3]
lst2 = lst1.copy()   #lst1和lst2 对应不同的空间,第一层拷贝(独立)
lst1.append(11)
print(lst1)  #[1,2,3,11]
print(lst2)  #[1,2,3]

# 2.深拷贝
# 把所有层级的容器元素都单独拷贝一份,放到独立的空间中
# 现象
lst1 = [1,2,3,[4,5,6]]
lst2 = copy.copy(lst1)
lst1[-1].append(77)  #浅拷贝只拷贝第一层,第二层及其以上都是同一份
lst1.append(8888)
print(lst2)  #[1, 2, 3, [4, 5, 6, 77]]
print(lst1)  #[1, 2, 3, [4, 5, 6, 77], 8888]


import copy
lst1 = [1,2,3,[4,5,6]]
lst2 = copy.deepcopy(lst1)
lst1[-1].append(999)
print(lst2)  #[1,2,3,[4,5,6]]
print(lst1)  #[1,2,3,[4,5,6,999]]

# 其他容器的深拷贝
lst1 = (1,2,3,{'a':1,'b':[10,20]})
lst2 = copy.deepcopy(lst1)
lst1[-1]['b'].append(30)
print(lst1)  # (1,2,3,{'a':1,'b':[10,20]})
print(lst2)  # (1,2,3,{'a':1,'b':[10,20,30]})


'''
总结:
浅拷贝:
	只拷贝一级容器中的所有元素,独立出来一个单独的空间.
深拷贝:
	把所有层级的容器中所有元素都单独拷贝一个呢,形成完全独立的空间

tuple 只有count index 两个方法,使用同列表


'''













































