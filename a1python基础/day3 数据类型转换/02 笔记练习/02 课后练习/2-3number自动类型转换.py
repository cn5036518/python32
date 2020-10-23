# ### Number 自动类型转换 (int float complex bool)
# 低精度默认向高精度进行转换
# bool ==> int ==> float ==> complex

# 1 bool + int
res = True + 100
print(res)  #101

# 2 bool + float
res = True + 344.5
print(res) # 345.5

# 3 bool + complex
res = True + 1 + 2j
print(2 + 2j)

# 4 int + float
res = 5 + 3.5
print(res) #8.5

# 5 int + complex
res = 6 + 1 + 2j
print(res) #7 + 2j

# 6 float + complex 
res = 4.5 + 2 + 4j
print(6.5+4j)

# 101
# 345.5
# (2+2j)
# 8.5
# (7+2j)
# (6.5+4j)

# 小数的精度损耗 (小数后面一般有时截取15~18位,但是不完全,存在精度损耗)
# """不要用小数作比较,咬不准"""

res = 0.1 + 0.2 == 0.3
print(res)  #False  咬不准

res = 5.1 + 5.9 == 11.0
print(res)  #True











































