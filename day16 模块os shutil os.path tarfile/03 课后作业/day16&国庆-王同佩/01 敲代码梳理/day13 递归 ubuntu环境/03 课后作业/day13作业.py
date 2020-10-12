# (选做)
# 1.可滑动的序列 自定义一个函数 根据参数n的值 , 变成对应个元素的容器 （zip）
"""
listvar = [1,2,3,4,5,6,7,8,9]
n = 2
listvar = [[1,2],[3,4],[5,6],[7,8]]
n = 3
listvar = [[1,2,3],[4,5,6],[7,8,9]]
n = 4
listvar = [[1,2,3,4],[5,6,7,8]]
"""

# 找规律
# n=2
# l21 = [1,3,5,7,9]  切片得到l21  然后zip
# l22 = [2,4,6,8]
#
# n = 3
# l31 = [1,4,7]
# l32 = [2,5,8]
# l33 = [3,6,9]
#
# n = 4
# l41 = [1,5]
# l42 = [2,6]
# l43 = [3,7]
# l44 = [4,8]

'''
思路:
第一步:先得到--通过切片 步长是3
# n = 3
# l31 = [1,4,7]
# l32 = [2,5,8]
# l33 = [3,6,9]

第二步:  zip(*列表)
[(1,2,3),(4,5,6),(7,8,9)]

第三步:  
[[1,2,3],[4,5,6],[7,8,9]]

步骤:
1 先写死 n=3
2 再写活 n
'''

# 写死
listvar = [1,2,3,4,5,6,7,8,9]
li1 = []
li2 = []
def func(n):
	if n == 3:
		# print(listvar[0::3])
		# print(listvar[1::3])
		# print(listvar[2::3])
		li1.append(listvar[0::3])
		li1.append(listvar[1::3])
		li1.append(listvar[2::3])
		print(li1)  #[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

	it = zip(listvar[0::3],listvar[1::3],listvar[2::3])
	# print(list(it))  #[(1, 2, 3), (4, 5, 6), (7, 8, 9)]

	for i in list(it):
		li2.append(list(i))
	print(li2)  #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# func(3)

# 写活1
listvar = [1,2,3,4,5,6,7,8,9]
li1 = []
li2 = []
def func(n):
	li1.append(listvar[0::n])
	li1.append(listvar[1::n])
	li1.append(listvar[2::n])
	print(li1)  #[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

	it = zip(listvar[0::n],listvar[1::n],listvar[2::n])
	# print(list(it))  #[(1, 2, 3), (4, 5, 6), (7, 8, 9)]

	for i in list(it):
		li2.append(list(i))
	print(li2)  #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# func(3)

# 写活2
listvar = [1,2,3,4,5,6,7,8,9]
li1 = []
li2 = []
def func(n):
	# 第一步: 先得到 - -通过切片	步长是n
	for i in range(n):
		li1.append(listvar[i::n])  #这里n是步长
	print(li1)  #[[1, 4, 7], [2, 5, 8], [3, 6, 9]]


    # 第二步: zip(*列表)
	it = zip(*li1)
	# print(list(it))  #[(1, 2, 3), (4, 5, 6), (7, 8, 9)]

	# 第三步:	[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	for i in list(it):
		li2.append(list(i))
	print(li2)  #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

func(2)




#方法1  不用zip  切片+步长
listvar = [1,2,3,4,5,6,7,8,9]

li = []
li2 = []
def func(n):
	# if n == 3:
		# li21 = listvar[0::n]
		# print(li21)  # [1, 3, 5, 7, 9]
		# li22 = listvar[1::n]
		# print(li22)  # [2, 4, 6, 8]
		# li23 = listvar[2::n]
		# print(li23)

	li1 = []
	for i in range(n):
		li1.append(listvar[i::n])  #n是步长  关键点1
	print(li1)  #[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

	it = zip(*li1)  #实参将列表解包成3个小列表  关键点2
	# print(list(it))  #[(1, 2, 3), (4, 5, 6), (7, 8, 9)]

	li2 = []
	for i in list(it):
		li2.append(list(i))
	print(li2)  #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# func(2)
# func(3)
# func(4)



listvar = [1,2,3,4,5,6,7,8,9]

def lj_list(n):
   lst = []
   for i in range(n):
      lst.append(listvar[i::n])
      print(listvar[i::n])
   res = [list(i)for i in zip(*lst)]
   return res

# s = lj_list(4)
# s = lj_list(3)
# s = lj_list(2)
# print(s)

# listvar = [1,2,3,4,5,6,7,8,9]

# li = []
# for i in listvar:
# 	li.append()

# 2.青蛙跳台阶  (递归实现)
'''
一只青蛙要跳上n层高的台阶
一次能跳一级,也可以跳两级
请问这只青蛙有多少种跳上这个n层高台阶的方法?

层数   方法   规律:类似斐波那契数列 有不同
1       1
2       2
3       3
4       5

4    1111
4    112
4    121
4    211
4    22
'''
def func(n):  #参数n是台阶数
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return  func(n-1) + func(n-2)
res = func(5)  #5级台阶
print(res)
'''
思路:  
去的过程
先想最后一步--倒着想
如果是4级台阶,fog的最后一步只有2个选择
选择1:跳1步  从3级到4期  
选择2:跳2步  从2级到4期  
即fog到达4级的办法是:fog到达3级的办法+fog到达2级的办法
func(4)= func(3) + func(2)
---------------------------------------------------------1
fog到达3级的办法= func(2) + func(1)
fog到达2级的办法= 2
fog到达1级的办法= 1
至此,去的过程结束

归的过程
func(1) =1
func(2) =2
func(3) =func(2) + func(1)  = 3
func(4) =func(3) + func(2)  = 3 + 2 =5
....................


'''


# 3.递归反转字符串 "将14235 反转成53241" (递归实现)
def reverse(s):
	# if s == '':  #递归终止条件
	if len(s) == 1: #递归终止条件
		return s
	else:
	    return reverse(s[1:])+ s[0]  #规律:每次把首位放在最后
res = reverse('123')
print(res)

# 去的过程
# s = '123'   return reverse(s[1:])+ s[0]  reverse('23') + '1'  '321'
# s = '23'	return reverse(s[1:])+ s[0]  reverse('3') + '2'   '32'
# s = '3'	    return  '3'
# 至此,去的过程结束

# 回的过程
# s＝'23'  返回 '32'
# s＝'123'  返回 '321'


# 4.斐波那契数列用尾递归实现














