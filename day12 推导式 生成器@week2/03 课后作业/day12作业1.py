''''''
'''

# # 1.用推导式写如下程序
# (1)构建如下列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# (2)lst = ['alex', 'WuSir', '老男孩', '神秘男孩'] 将lst构建如下列表:['alex0', 'WuSir1', '老男孩2', '神秘男孩3']
# (3)构建如下列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# (4)求出50以内能被3整除的数的平方，并放入到一个列表中。
# (5)M = [[1,2,3],[4,5,6],[7,8,9]], 把M中3,6,9组成新列表
# (6)构建如下列表：['python1期', 'python2期', 'python3期', 'python4期', 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
# (7)过滤掉长度小于3的字符串列表 , 并转换成大写字母
# (8)除了大小王,里面有52项,每一项是一个元组,请返回如下扑克牌列表[('红心'，'2'),('草花'，'J'), …('黑桃'，'A')]
#
# # 2.用推导式写如下程序
# lst1 = {
# 		'name':'alex',
# 		'Values':[
# 			{'timestamp': 1517991992.94,'values':100,},
# 			{'timestamp': 1517992000.94,'values': 200,},
# 			{'timestamp': 1517992014.94,'values': 300,},
# 			{'timestamp': 1517992744.94,'values': 350},
# 			{'timestamp': 1517992800.94,'values': 280}
# 		]
# 	}
# 将lst1 转化成如下lst2:
# lst2 = [
# 	[1517991992.94, 100],
# 	[1517992000.94, 200],
# 	[1517992014.94, 300],
# 	[1517992744.94, 350],
# 	[1517992800.94, 280]
# ]
#
# # 3.读取一个文件所有内容,通过生成器调用一次获取一行数据.
# # 4.将普通求和函数改写成yield写法
# def add(a,b):
#    return a + b

'''

# # 1.用推导式写如下程序
# (1)构建如下列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
lst = [i for i in range(19) if i % 2 == 0]
print(lst)  #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# (2)lst = ['alex', 'WuSir', '老男孩', '神秘男孩'] 将lst构建如下列表:['alex0', 'WuSir1', '老男孩2', '神秘男孩3']
# 普通方法
lst = ['alex', 'WuSir', '老男孩', '神秘男孩']
lst_new = []
for i in range(len(lst)):
	lst_new.append(lst[i] + str(i))
print(lst_new)  #['alex0', 'WuSir1', '老男孩2', '神秘男孩3']

# 推导式
lst = ['alex', 'WuSir', '老男孩', '神秘男孩']
lst_new = [(lst[i] + str(i)) for i in range(len(lst))]
print(lst_new)  #['alex0', 'WuSir1', '老男孩2', '神秘男孩3']
print('-----------------------2')

# (3)构建如下列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# 普通方法
lst_new = []
for i in range(6):
	lst_new.append((i,i+1))
print(lst_new)  #[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]

# 推导式
lst_new = [(i,i+1) for i in range(6)]
print(lst_new)
print('-----------------------3')

# (4)求出50以内能被3整除的数的平方，并放入到一个列表中。
# 普通方法
lst_new = []
for i in range(50):
	if i % 3 == 0:
		lst_new.append(i**2)
print(lst_new)  #[0, 9, 36, 81, 144, 225, 324, 441, 576, 729, 900, 1089, 1296, 1521, 1764, 2025, 2304]

# 推导式
lst = [i**2 for i in range(50) if i%3==0]
print(lst)
print('-----------------------4')

# (5)M = [[1,2,3],[4,5,6],[7,8,9]], 把M中3,6,9组成新列表
# 普通方法
lst_new = []
M = [[1,2,3],[4,5,6],[7,8,9]]
for i in M:
	lst_new.append(i[-1])
print(lst_new)  #[3, 6, 9]

# 推导式
lst = [i[-1] for i in M]
print(lst)
print('-----------------------5')

# (6)构建如下列表：['python1期', 'python2期', 'python3期', 'python4期', 'python6期',
# 'python7期', 'python8期', 'python9期', 'python10期']
# 普通方法
lst_new = []
for i in range(1,11):
	lst_new.append('python{}期'.format(i))
print(lst_new)

# 推导式
lst = ['python{}期'.format(i) for i in range(1,11)]
print(lst)
print('-----------------------6')

# (7)过滤掉长度小于3的字符串列表 , 并转换成大写字母
# (8)除了大小王,里面有52项,每一项是一个元组,请返回如下扑克牌列表[('红心'，'2'),('草花'，'J'), …('黑桃'，'A')]
# 普通方法
lst_new = []

li1 = ['红心','黑桃','方块','梅花']
li2 = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

for i in li1:
	for j in li2:
		lst_new.append((i,j))
print(lst_new)

# 推导式
li1 = ['红心','黑桃','方块','梅花']
li2 = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

lst = [(i,j) for i in li1 for j in li2]
print(lst)
print('-----------------------8')





















