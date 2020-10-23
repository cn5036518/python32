# (5) 斐波那契数列
# """使用生成器分段获取所有内容,而不是一股脑的把所有数据全部打印"""
# """1 1 2 3 5 8 13 21 34 .... """
def fab(maxval):
	a,b = 0,1
	for i in range(0,maxval):
		yield b
		a,b = b,a+b  #规律:b = a+b
gen = fab(5)
print(list(gen))  #[1, 1, 2, 3, 5]
































