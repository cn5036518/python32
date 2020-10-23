# ### 推导式练习题
# (1).{'x': 'A', 'y': 'B', 'z': 'C' } 把字典写成x=A,y=B,z=C的列表推导式
# 普通写法
dic = {'x': 'A', 'y': 'B', 'z': 'C' }
lst = []
for k,v in dic.items():
	lst.append(k+'='+v)
print(lst)  #['x=A', 'y=B', 'z=C']

# 推导式
lst = [k+'='+v for k,v in dic.items()]
print(lst) #['x=A', 'y=B', 'z=C']


# (2).把列表中所有字符变成小写  ["ADDD","dddDD","DDaa","sss"]
# 推导式
lst = ["ADDD","dddDD","DDaa","sss"]
lst_new = [i.lower() for i in lst]
print(lst_new)  #['addd', 'ddddd', 'ddaa', 'sss']

# (3).x是0-5之间的偶数,y是0-5之间的奇数 把x,y组成一起变成元组,放到列表当中
lst = [(i,j) for i in range(6) for j in range(6) if i % 2 == 0 and j % 2 == 1]
print(lst)
# [(0, 1), (0, 3), (0, 5), (2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)]

# (4).使用列表推导式 制作所有99乘法表中的运算
# 普通写法
for i in range(1,10):
	for j in range(1,i+1):
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')  #默认靠右
		# print('{:d}*{:d}={:<2d} '.format(i,j,i*j),end='') # <左对齐  ^居中  >右对齐
	print()

lst = ['{:d}*{:d}={:2d} '.format(i,j,i*j) for i in range(1,10) for j in range(1,i+1)]
print(lst)

# (5)求M,N中矩阵和元素的乘积
# M = [ [1,2,3], 
#       [4,5,6], 
#       [7,8,9]  ] 

# N = [ [2,2,2], 
#       [3,3,3], 
#       [4,4,4]  ] 

M = [ [1,2,3] ,[4,5,6] , [7,8,9] ]
N = [ [2,2,2] ,[3,3,3] , [4,4,4] ]


# =>实现效果1   [2, 4, 6, 12, 15, 18, 28, 32, 36]
# 规律   关键点
# M[0][0]  *  N[0][0] = 2 
# M[0][1]  *  N[0][1] = 4 
# M[0][2]  *  N[0][2] = 6

# M[1][0]  *  N[1][0] = 12
# M[1][1]  *  N[1][1] = 15
# M[1][2]  *  N[1][2] = 18

# M[2][0]  *  N[2][0] = 28
# M[2][1]  *  N[2][1] = 32
# M[2][2]  *  N[2][2] = 36

# 普通方法
lst = []
for i in range(3):
	for j in range(3):  # 外循环动的慢 内循环动的快
		lst.append(M[i][j] * N[i][j])
print(lst)

# 推导式
lst = [M[i][j] * N[i][j] for i in range(3) for j in range(3)]
print(lst)  #[2, 4, 6, 12, 15, 18, 28, 32, 36]
print('-------------------------------1')

# =>实现效果2   [  [2, 4, 6], [12, 15, 18], [28, 32, 36]   ]
# 普通方法
# [[],[],[]]

lst  = []
for i in range(3):
	lst2 = []
	for j in range(3):
		lst2.append(M[i][j] * N[i][j])
	lst.append(lst2)
print(lst) #[[2, 4, 6], [12, 15, 18], [28, 32, 36]]

# 推导式
lst = [[M[i][j] * N[i][j] for j in range(3)] for i in range(3)]  
# 注意内中括号的位置
print(lst)  #[[2, 4, 6], [12, 15, 18], [28, 32, 36]]
















































