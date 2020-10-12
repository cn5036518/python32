# ### 关键字的使用  pass break continue
#pass 过(代码块中的占位符)
'''
if 20 == 20:
	pass
	
while True:
	pass
'''

# break 终止当前循环 (只能用在循环之中,只能终止一层循环)
# 1 ~ 10 遇到5终止循环
i = 1
while i <= 10:
	print(i)
	if i == 5:
		break
	i += 1
print('-----------------1')

i = 1
while i <=3:
	j = 1
	while j <= 3:
		if j == 2:
			break
		print(i,j)	
		j += 1
	i += 1
# 1 1
# 2 1
# 3 1
print('-----------------2')

# if 5 == 5: # break 只能用在循环中
	# break  #SyntaxError: 'break' outside loop

# continue 跳过当前循环,从下一次循环开始
# 打印1 ~ 10 跳过5
i = 1
while i <= 10:
	if i == 5:
	# 在跳过之前,因为会终止后面的代码,从下一次循环开始
	# 为了避免死循环,手动加1
		i +=1  # 关键点
		continue
	print(i)
	i += 1
print('-----------------3')

# 小结:
# continue建议用在for循环中,
# 不建议用在while循环中

# 1 ~ 100 打印所有不含有4的数字
# 方法一
# 思路,先将int转换成str,然后用4 in str判断
i = 1
while i <= 100:
	strvar = str(i)
	if '4' in strvar:
		i += 1  #while循环中continue上面必须加上 i += 1
		continue  #
	print(i)  #不能少了
	i += 1
print('-----------------4-1')

# 方法二
# 思路: int地板除后不是4(十位不是4) int取余后也不是4(个位不是4)
i = 1
while i <= 100:
	if i // 10 == 4 or i % 10 ==4:
		i += 1
		continue
	print(i)
	i += 1
print('-----------------4-2')








































