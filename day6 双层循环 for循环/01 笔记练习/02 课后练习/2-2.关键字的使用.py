# ### 关键字的使用  pass break continue
# pass 过 (代码块中的占位符)
# """
# if 20 == 20:
	# pass
	
# while True:
	# pass
# "

# break 终止当前循环 (只能用在循环之中)
# 1 ~ 10 遇到5终止循环

for i in range(1,11):
	print(i)
	if i == 5:
		break
print('--------------1 break')

# if 5 == 5:  #break只能用在循环中
	# break #SyntaxError: 'break' outside loop


# continue 跳过当前循环,从下一次循环开始
# 打印 1 ~ 10 跳过5
for i in range(1,11):
	if i == 5:
		continue
	print(i)
print('--------------2 for continue')

i = 1
while i < 11:
	if i == 5:
		i += 1  # 为了避免死循环,必须手动加1 (不推荐while continue搭配使用)
		continue	 
	print(i)
	i += 1
print('--------------2-2 while continue')

# 1 ~ 100 打印所有不含有4的数字
for i in range(1,101):
	if "4" not in str(i):
		print(i)
print('--------------3-1')

for i in range(1,101):
	if i // 10 == 4 or i % 10 == 4:
		continue
	print(i)
print('--------------3-2')
























