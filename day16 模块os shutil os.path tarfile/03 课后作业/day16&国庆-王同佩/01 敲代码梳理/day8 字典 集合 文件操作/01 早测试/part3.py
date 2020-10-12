#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/21 11:56

''''''
'''
# part3
# 1.break 和 continue有什么区别
break   跳出整个循环,终止循环
continue  跳出当次循环,进入到下一次循环

# 2.[1,2,3,(4,5,6,{'a','b'})] 如何遍历
# 3.([1,2],{3,4})如何遍历
# 4密码111,输错三次循环终止,每次打印剩余输入机会.
# 5求结果
	# 87 % 7
	# -87 % 7
	# 87 % 7
	# 81 // 7
	# 81.0 // 7
	# ~18
	# ~-18
	# 40 >> 2 ** 2
	# 1 > 2 and 3<=4 or not 0
'''

# 2.[1,2,3,(4,5,6,{'a','b'})] 如何遍历
listvar = [1,2,3,(4,5,6,{'a','b'})]
for i in listvar:
	if isinstance(i,(tuple)):
		for j in i:
			if isinstance(j,(set)):
				for k in j:
					print(k)
			else:
				print(j)
	else:
		print(i)
print('------------------------------2')

# 3.([1,2],{3,4})如何遍历
tuplevar = ([1,2],{3,4})
for a,b in tuplevar:
	print(a)
	print(b)
print('------------------------------3')

# 4密码111,输错三次循环终止,每次打印剩余输入机会.
for i in range(3):
	content = input('请输入密码:')
	if content.isdecimal():
		content = int(content)
		if content == '111':
			print('登录成功')
			break
		else:
			print('登录失败')
			print('你还有{:d}次登录机会'.format(2-i))



















































