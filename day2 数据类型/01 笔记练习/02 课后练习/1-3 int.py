# ### Number 数字类型 (int float bool complex)
# int 整型(正整型 0 负整型)

intvar = 100
print(intvar)  #100

# type 获取值的类型
res = type(intvar)
print(res)  #<class 'int'>

# id 获取值的内存地址
res = id(intvar)
print(res)  #140717188804336

# 二进制整型
intvar = 0b110
print(intvar)  #6
print(type(intvar))
print(id(intvar))

# 八进制整型
intvar = 0o127
print(intvar)  #87
print(type(intvar))
print(id(intvar))

# 十六进制整型
intvar = 0xff
intvar = 0XFF
print(intvar) #255
print(type(intvar))
print(id(intvar))

"""
二进制 1+1 = 10
八进制 7+1 = 10
十六进制 f+1 = 10

"""

























