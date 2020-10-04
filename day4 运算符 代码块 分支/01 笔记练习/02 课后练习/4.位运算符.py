# ### (7)位运算符:    & |  ^ << >> ~

var1 = 19
var2 = 15

# & 按位与
res = var1 & var2
# """
# 000 ... 10011
# 000 ... 01111
# 000 ... 00011 => 3
# """
print(res)

# | 按位或
res = var1 | var2
# """
# 000 ... 10011
# 000 ... 01111
# 000 ... 11111
# """
print(res)

# ^ 按位异或
# """两个值不相同=>1 反之返回0"""
res = var1 ^ var2
# """
# 000 ... 10011
# 000 ... 01111
# 000 ... 11100
# """
print(res)

# << 左移 (相当于乘法)
# """5乘以2的n次幂"""
res = 5 << 1 # 10
res = 5 << 2 # 20
res = 5 << 3 # 40
print(res)

# """
# 000 ... 101  => 5
# 000 .. 1010  => 10
# 000 ..10100  => 20
# 000 .101000  => 40
# """

# >> 右移 (相当于除法)
# """5地板除2的n次幂"""
res = 5 >> 1 # 2
res = 5 >> 2 # 1
res = 5 >> 3 # 0
# """
# 000 ... 101
# 000 ... 010 => 2
# 000 ... 001 => 1
# 000 ... 000 => 0
# """
print(res)


# ~ 按位非 (针对于补码进行操作,按位取反,包含每一位)
# """ -(n+1) """
# res = ~22
res = ~19
print(res)
# """
# 原码:000 ... 10011
# 反码:000 ... 10011
# 补码:000 ... 10011

# 补码:   000 ... 10011
# 按位非: 111 ... 01100

# 给你补码->原码
# 补码:111 ... 01100
# 反码:100 ... 10011
# 原码:100 ... 10100 => -20
# """

res = ~-19
print(res)
# """
# 原码:100 ... 10011
# 反码:111 ... 01100
# 补码:111 ... 01101

# 补码:   111 ... 01101
# 按位非: 000 ... 10010

# 给你补码->原码 (因为是正数 ,原反补相同)
# 000 ... 10010 => 18
# """


# """
# 总结:
	# 个别运算符:
		# 运算符优先级最高的: **
		# 运算符优先级最低的: =
		# ()可以提升优先级
		
	# 一元运算符 > 二元运算符 (优先级)
		# 一元运算符 : 同一时间,操作一个值 ~ - 
		# 二元运算符 : 同一时间,操作2个值 + - * / ....
		
	# 同一种类运算符:
		# 算数运算符 : 乘除 > 加减
		# 逻辑运算符 : () > not > and > or 
		# 位运算符   : ( << >> ) > & > ^ > |
	
	# 整体排序:
		# 算数运算符 > 位运算符 > 比较运算符 > 身份运算符 > 成员运算符 > 逻辑运算符>赋值运算符
		# 赋值运算符用来做收尾
# """

# 运算符优先级  算数 比较 赋值 成员 身份 逻辑 位运费符
# 1算数 2位 3比较 4身份 5 成员  6逻辑  7赋值
#   +    <<  ==     is    in      and    =

res = 5+5 << 6 // 3 is 40 and False
# """
# res = 10 << 2 is 40 and False
# res = 40 is 40 and False
# res = True and False
# res = False
# """
print(res)

# 用括号提升下优先级
res = (5+5) << (6//3) is 40 and False

























