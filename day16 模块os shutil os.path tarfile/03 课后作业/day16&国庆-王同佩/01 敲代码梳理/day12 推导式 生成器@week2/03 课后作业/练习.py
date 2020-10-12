#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/25 9:57


# 2
li = ['Ad','DDaa']

lst_new = []
for i in li:
	i = i.upper()
	lst_new.append(i)
print(lst_new)   #['AD', 'DDAA']

res = [i.upper() for i in li]
print(res)  #['AD', 'DDAA']
print('-----------------------------2')

# 3
lst_new = []
for i in range(6):
	for j in range(6):
		if i % 2 == 0 and j %2 == 1:
			lst_new.append((i,j))
print(lst_new)
# [(0, 1), (0, 3), (0, 5), (2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)]
print('-----------------------------3-1')

lst_new = [(i,j) for i in range(6) for j in range(6) if i % 2 == 0 and j % 2 == 1]
print(lst_new)
print('-----------------------------3-2')

# 4
for i in range(1,10):
	for j in range(1,i+1):
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	print()
print('-----------------------------4-1')


res = [print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='') for i in range(1,10) for j in range(1,i+1)]
print(res)  #一行
print('-----------------------------4-2')

# 1
dic = {'x':'A','y':'B'}

lst_new = []
for k,v in dic.items():
	# print(k,v)
	lst_new.append((k + '=' + v))
print(lst_new)
print('-----------------------------1-1')

res = [(k + '=' + v)for k,v in dic.items()]
print(res)
print('-----------------------------1-2')


# 5
m = [[1,2,3],[4,5,6],[7,8,9]]
n = [[2,2,2],[3,3,3],[4,4,4]]

li1 = []
for i in m:
	for j in i:
		# print(j,end='')
		li1.append(j)
print(li1)  #[1, 2, 3, 4, 5, 6, 7, 8, 9]

li2 = []
for i in n:
	for j in i:
		# print(j,end='')
		li2.append(j)
print(li2)  #[2, 2, 2, 3, 3, 3, 4, 4, 4]

li3 = []
for i in li1:
	for j in li2:
		if li1.index(i) == li2.index(j):
			li3.append(i * j)
print(li3)


m = [[1,2,3],[4,5,6],[7,8,9]]
n = [[2,2,2],[3,3,3],[4,4,4]]

for a,b,c in m:
	print(a,b,c)
























