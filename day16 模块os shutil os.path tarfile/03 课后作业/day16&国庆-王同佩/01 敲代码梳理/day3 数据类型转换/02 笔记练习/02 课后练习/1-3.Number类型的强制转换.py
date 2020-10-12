# ### Number 类型的强制转换 (int float complex bool)

# 01 int 强制把数据变成整型
# """float bool 纯数字字符串"""
var2 = 5.67
var3  = True
var4 = "123456"
var5 = "123abc"
var6 = 3+5j

print(int(var2))  #5  截取整数部分
print(int(var3))  #1
print(int(var4))  #123456
# print(int(var5))  #ValueError: invalid literal for int() with base 10: '123abc'
# print(int(var6))  #TypeError: can't convert complex to int
print('------------------------1 int')

# 02 float 强制把数据变成小数
# """int bool 纯数字字符串"""
var1 = 13
var2 = 5.67
var3  = True
var4 = "123456"
var5 = "123abc"
var6 = 3+5j

print(float(var1))  #13.0
print(float(var3))  #1.0
print(float(var4))  #123456.0
# print(float(var5))  #ValueError: could not convert string to float: '123abc'
# print(float(var6))  #TypeError: can't convert complex to float
print('------------------------2 float')

# 03 complex 强制把数据变成复数
# """int float bool 纯数字字符串"""
var1 = 13
var2 = 5.67
var3  = True
var4 = "123456"
var5 = "123abc"
var6 = 3+5j

print(complex(var1))   #(13+0j)  添加0j 表达复数
print(complex(var2))   #(5.67+0j)
print(complex(var3))   #(1+0j)
print(complex(var4))   #(123456+0j)
# print(complex(var5))   #ValueError: complex() arg is a malformed string
print('------------------------3 complex')


# 04 bool 强制把数据变成布尔型 (布尔型为假的十种情况)  ***
# """布尔型可以强转一切数据类型"""
# 0 0.0 False 0j  '' () [] {} set() None


# 05 None 初始化变量时,不清楚用什么值,无脑写上None
# """None 代表空的,代表什么也没有,一般用于初始化变量"""

# 06 参数为空 默认转换成当前数据类型的一个值
# int() float() complex() bool()
print(int())  #0
print(float()) #0.0
print(complex()) #0j
print(bool())  #False


# 小结:
# bool为假的10个情况:
# 0
# 0.0
# False
# 0j

# ''
# ()
# []
# {}
# set()

# None

# int()  #参数 float bool 纯数字字符串 
# float()  # 参数 int bool 纯数字字符串 
# complex() # 参数  int bool float 纯数字字符串
# bool()  #参数 所有数据类型






























