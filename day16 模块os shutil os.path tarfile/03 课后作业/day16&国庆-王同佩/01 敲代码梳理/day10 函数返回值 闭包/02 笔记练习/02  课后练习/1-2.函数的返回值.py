# return

def func():
	for i in range(5):
		if i == 3:
			return 4
		print(i)
res = func()
print(res)
# 0
# 1
# 2
# 4

# 模拟+-*/计算器
# 功能:   完成计算
# 参数:   2个数字和运算符
# 返回值: 计算后的结果

def calc(num1,num2,sign):
	if sign == '+':
		return num1 + num2
	elif sign == '-':
		return num1 - num2
	elif sign == '*':
		return num1 * num2
	elif sign == '/':
		return  num1 / num2
	else:
		print('输入格式不对')
		
res = calc(3,4,'*')
print(res)  #12


















































