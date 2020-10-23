# ###数学模块
import math

# 1 ceil()  #向上取整  ***
res = math.ceil(3.01)
print(res) #4
res = math.ceil(-3.45)
print(res) #-3

# 2 floor()  向下取整   ***
res = math.floor(3.99)
print(res)  #3
res = math.floor(-3.99)
print(res) #-4

# 3 pow()
res = math.pow(2,3)
print(res)  #8.0

# 4 sqrt()
res = math.sqrt(9)
print(res) #3.0

# 5 fabs()
res = math.fabs(-2)
print(res) #2.0

# 6 modf()
res = math.modf(3.12)
print(res)  #(0.1200000000000001, 3.0)

# 7 copysign()
res = math.copysign(-12,-9.1)
print(res)  #-12.0

# 8 fsum()
lst = [1,3]
res = math.fsum(lst)
print(res)  #4.0

# 9 圆周率常数  pi  ***
print(math.pi)  #3.141592653589793























