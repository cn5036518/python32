# ### Number 自动类型转换 (int float complex bool)
'''
低精度默认向高精度进行转换
bool --> int --> float --> complex
'''
# bool + int
res = True + 100
print(res,type(res))  #101 <class 'int'>

# bool + float
res = True + 344.565 
print(res,type(res))  #345.565 <class 'float'>  # 1.0 + 344.565 => 345.565

# bool + complex
res = True + 7 - 90j
print(res,type(res))  #(8-90j) <class 'complex'> # 1 + 0j + 7 -90j => 8-90j

# int + float
res = 5 + 7.88 # 5.0 + 7.88 +> 12.88  
print(res,type(res))   #12.879999999999999 <class 'float'>

# int + complex
res = 5 + 6 + 8j  #5 + 0j + 6 +8j =>11 + 8j
print(res,type(res))  #(11+8j) <class 'complex'>

# float + complex
res = 5.66 + 9.1 - 90j  #5.66 + 0j + 9.1 -90j ==> 14.76 - 90j
print(res,type(res))  #(14.76-90j) <class 'complex'>

'''
# 小数的精度损耗(小数后面一般有时截取15~18位,但是不完全,存在精度损耗)
不要用小数作比较,咬不准
print(0.1 + 0.2 == 0.3)  #False
print(5.1 + 5.9 == 11.0) #True
0.0999999999999999999999
'''



