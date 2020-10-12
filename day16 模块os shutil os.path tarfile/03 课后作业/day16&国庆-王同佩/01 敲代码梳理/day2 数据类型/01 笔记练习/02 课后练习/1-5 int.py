# ### Number数字类型 (int float bool complex)
# int 整型 (正整型 0 负整型)

intvar = 100
print(intvar)

# type 获取值得类型
res = type(intvar)
print(res)  #<class 'int'>

# id   获取值得地址
res = id(intvar)
print(res)  #11097472

# 二进制整型
intvar = 0b110
print(intvar,type(intvar),id(intvar))
#6 <class 'int'> 11094464

# 八进制整型
intvar = 0o127
print(intvar,type(intvar),id(intvar))
#87 <class 'int'> 11097056

# 十六进制
intvar = 0xff
intvar = 0xFF
print(intvar,type(intvar),id(intvar))
#255 <class 'int'> 11102432

# 二进制 1 + 1 = 10
# 八进制 7 + 1  = 10
# 十六进制 f + 1 = 10






















































