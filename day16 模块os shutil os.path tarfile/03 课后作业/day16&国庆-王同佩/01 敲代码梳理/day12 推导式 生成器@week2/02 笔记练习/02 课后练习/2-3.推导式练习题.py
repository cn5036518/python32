# ### 推导式练习题
# (1).{'x': 'A', 'y': 'B', 'z': 'C' } 把字典写成x=A,y=B,z=C的列表推导式
dic = {'x': 'A', 'y': 'B', 'z': 'C' }
lst = [k +'='+ v for k,v in dic.items()]
print(lst)  #['x=A', 'y=B', 'z=C']

# (2).把列表中所有字符变成小写  ["ADDD","dddDD","DDaa","sss"]
lst = ["ADDD","dddDD","DDaa","sss"]
lst_new = [i.lower() for i in lst]
print(lst_new)  #['addd', 'ddddd', 'ddaa', 'sss']

# (3).x是0-5之间的偶数,y是0-5之间的奇数 把x,y组成一起变成元组,放到列表当中
lst = [(x,y) for x in range(6) for y in range(6) if x % 2 == 0 and y % 2 ==1]
print(lst)
#[(0, 1), (0, 3), (0, 5), (2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)]

# (4).使用列表推导式 制作所有99乘法表中的运算
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
# """双层循环,外层循环动的慢,内层循环动的快,正好符号M N 矩阵的下标"""  规律 关键点
lst = []
for i in range(3):
	for j in range(3):
		lst.append(M[i][j] * N[i][j])
print(lst) 
#[2, 4, 6, 12, 15, 18, 28, 32, 36]

lst_new = [M[i][j] * N[i][j] for i in range(3) for j in range(3)]
print(lst_new)
#[2, 4, 6, 12, 15, 18, 28, 32, 36]

# =>实现效果2   [  [2, 4, 6], [12, 15, 18], [28, 32, 36]   ]
# [[][][]]
lst = []
for i in range(3):
	lst1 = []
	for j in range(3):
		lst1.append(M[i][j] * N[i][j])
	lst.append(lst1)
print(lst)
#[[2, 4, 6], [12, 15, 18], [28, 32, 36]]

lst_new = [[M[i][j] * N[i][j] for j in range(3)] for i in range(3)]
print(lst_new)
#[[2, 4, 6], [12, 15, 18], [28, 32, 36]]














