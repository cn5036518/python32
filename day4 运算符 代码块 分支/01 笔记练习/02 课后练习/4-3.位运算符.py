# ### (7)位运算符:    & | ^ << >> ~
var1 = 19
var2 = 15

# 01 & 按位与
res = var1 & var2
print(res)  #3
# 000 ... 10011   19
# 000 ... 01111   15  每一位上 都是1 结果是1,否则,结果是0
# 000 ... 00011 => 3     逻辑与 都有True 结果是True,否则,结果是False

# 02 | 按位或
var1 = 19
var2 = 15
res = var1 | var2
print(res)   #31
# 000 ... 10011   19
# 000 ... 01111   15  每一位上 只要有一个是1 结果是1,否则,结果是0
# 000 ... 11111	  31    逻辑或 只要有一个是True 结果是True,否则,结果是False

# 03 ^ 按位异或
3# """每一位上 两个值不相同=>1 反之返回 0"""
var1 = 19
var2 = 15
res = var1 ^ var2
print(res) #28
# 000 ... 10011
# 000 ... 01111
# 000 ... 11100

# 04 << 左移 (相当于乘法)
# """5乘以2的n次幂"""
res = 5 << 1  # 5*2=10
res = 5 << 2  # 5*2**2=20
res = 5 << 3  # 5*2**3=40
print(res) #40

# 000 ... 101  => 5
# 000 .. 1010  => 10  #左移一位,右边补0
# 000 ..10100  => 20  #左移2位,右边补00
# 000 .101000  => 40  #左移3位,右边补000


# 05 >> 右移 (相当于除法)
# """5地板除2的n次幂"""
res = 5 >> 1 #2
res = 5 >> 2 #1
res = 5 >> 3 #0
print(res) #0
# 000 ... 101    5
# 000 ... 010 => 2   #右移一位,左边补0
# 000 ... 001 => 1	 #右移2位,左边补00
# 000 ... 000 => 0   #右移3位,左边补000


# 06 ~ 按位非 (针对于补码进行操作,按位取反,包含每一位)
# """ -(n+1) """
res = ~19
print(res) #-20

# 原码:000 ... 10011   #正数符号位是0 三码一致
# 反码:000 ... 10011
# 补码:000 ... 10011

# 补码:   000 ... 10011  #按位非的时候,符号位也取反
# 按位非: 111 ... 01100

# 给你补码->原码   补码取反,末尾加1
# 补码:111 ... 01100
# 反码:100 ... 10011  #补码取反的时候.符号位不变
# 原码:100 ... 10100 => -20

res = ~-19
print(res)  #18
# 原码:100 ... 10011   #负数符号位是1 三码不一致
# 反码:111 ... 01100   #原码和反码 符号位不变
# 补码:111 ... 01101

# 补码:   111 ... 01101
# 按位非: 000 ... 10010

# 给你补码->原码 (因为是正数 ,原反补-三码相同)
# 000 ... 10010 => 18

# 总结:
	# 个别运算符:
		# 运算符优先级最高的: ** 幂
		# 运算符优先级最低的: = 赋值
		# 可以提升优先级    ()
		
	# 一元运算符 > 二元运算符 (优先级)
		# 一元运算符 : 同一时间,操作一个值 ~ - 
		# 二元运算符 : 同一时间,操作2个值 + - * / ....
		
	# 同一种类运算符:
		# 算数运算符 : 乘除 > 加减
		# 逻辑运算符 :  () > not > and >or
		# 位运算符   : (<< >>) > &(逻辑与) > ^(逻辑异或) > |(逻辑或)
	
	# 整体排序:
		# 1 算数
		# 2 位
		# 3 比较
		# 4 身份
		# 5 成员
		# 6 逻辑
		# 7 赋值

res = 5+5 << 6 // 3 is 40 and False
res = 10 << 2 is 40 and False
res = 40 is 40 and False
res = True and False
res = False
print(res)











































