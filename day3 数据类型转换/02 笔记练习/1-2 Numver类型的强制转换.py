
# ### Number 类型的强制转换 (int float bool complex)

# int 强制把数据变成整型
''' int 可以强制转换的类型有:  float bool 纯数字字符串(不能有空格)'''
var1 = 13
var2 = 5.67
var3 = True
var4 = '123456'
var5 = '123abc'
var6 = 3+5j

res = int(var2)
print(res)  #5  #截断小数部分

res = int(var3)
print(res)  #True => 1

res = int(False)
print(res) # False => 0

res = int(var4)
print(res,type(res))  #123456 <class 'int'>

# res = int(var5)
# print(res)  #ValueError: invalid literal for int() with base 10: '123abc'

# res = int(var6)
# print(res)  #TypeError: can't convert complex to int

# float 强制把数据变成小数
''' float 可以强制转换的类型有: int bool 纯数字字符串(不能有空格)  '''
var1 = 13
var2 = 5.67
var3 = True
var4 = '123456'
var5 = '123abc'
var6 = 3+5j

res = float(var1)
print(res)  #13.0

res = float(var3)
print(res)  #True => 1.0

res = float(False)
print(res)  #False => 0.0

res = float(var4) 
print(res,type(res))  #123456.0 <class 'float'>

# complex 强制把数据变成小数
'''complex 可以强制转换的类型有: int float bool 纯数字字符串(不能有空格)'''
var1 = 13
var2 = 5.67
var3 = True
var4 = '123456'
var5 = '123abc'
var6 = 3+5j

res = complex(var1)
print(res,type(res))  #(13+0j) <class 'complex'> #添加0j 表达复数

res = complex(var2)
print(res,type(res))  #(5.67+0j) <class 'complex'>

res = complex(var3)
print(res,type(res))  #True =>(1+0j) <class 'complex'>

res = complex(False)
print(res,type(res))  #False => 0j <class 'complex'>

res = complex(var4)
print(res,type(res))  #(123456+0j) <class 'complex'>

# bool 強制把数据变成布尔型(布尔型为假-False的10种情况)
'''
布尔型可以强转一切数据类型
Number
	int     0
	float   0.0
	bool    False
	complex 0j
str			''
tuple		()
list		[]
dict		{}
set			set()
			None
'''
res = bool(None)
print(res,type(res))  #False <class 'bool'>

# 初始化变量时,不清楚用什么值,无脑写上None
'''None 代表空的,代表什么也没有,一般用于初始化变量'''
a = None
b = None
 
 
'''
默认转换成当前数据类型的一个值
int() float() complex() bool()
'''
res = bool()
print(res,type(res))  #False <class 'bool'>

res = int()
print(res)  #0

res = float()
print(res)  #0.0
















































