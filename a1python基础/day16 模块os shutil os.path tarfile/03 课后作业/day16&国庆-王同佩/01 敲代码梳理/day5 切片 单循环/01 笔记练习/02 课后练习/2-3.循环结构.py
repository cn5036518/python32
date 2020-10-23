# ### 循环结构
# """特点:减少冗余代码,提升执行效率"""
# """
# 语法:
# while 条件表达式:
	# code1

# (1) 初始化一个变量
# (2) 写上循环的条件
# (3) 自增自减的值


# ### 打印1 ~ 100
i = 1
while i < 101:
	# print(i)
	i += 1

# ### 1 ~ 100的累加和
i = 1
total = 0
while i < 101:
	total += i
	i += 1
print(total)  #5050

total = 0
for i in range(1,101):
	total += i
print(total)  #5050

# ### 用死循环的方法实现 1 ~ 100累加和
i = 1
sign = True  #标志位
total = 0
while sign:
	total += i
	i += 1
	if i == 101:
		sign = False  
print(total)  #5050



















































