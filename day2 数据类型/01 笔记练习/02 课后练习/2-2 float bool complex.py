# ### Number 数字类型 (int float bool complex)

# float 浮点型(小数)
# 表达方式1
floatvar = 3.6
print(floatvar,type(floatvar))

# 表达方式2
floatvar = 5.7e5  #小数点右移5
folatvar = 5.7e-2  #小数点左移动2
print(floatvar, type(floatvar))


# bool  布尔型 (True 真的, FALSE 假的)
boolvar = True
boolvat = False
print(boolvar, type(boolvar))


#complex 复数类型
"""
3 + 4j
实数+虚数
实数:3
虚数:4j
虚数的概念:
	j:如果有一个数他的平方等于-1.那么这个数就是j
	   科学家认为.表达高精度的类型
"""
# 表达方式1
complexvar = 3 + 4j
complexvar = -3j
print(complexvar, type(complexvar))

# 表达方式2
"""
complex(实数,虚数) ==>复数
"""
res  = complex(3,4)
print(res,type(res))




























