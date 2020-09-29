# ### 数学模块
import math

# ceil() 向上取整操作(对比内置round)  ***
res = math.ceil(3.01)  #4
res = math.ceil(-3.45)  #-3
print(res)  

# floor() 向下取整操作 (对比内置rounf)  ***
res = math.floor(3.99) #3
res = math.floor(-3.99) #-4
print(res)  

# pow() 计算一个数值的N次方(结果为浮点数) (对比内置pow)
# 结果为浮点数,必须是两个参数.三个参数,就报错
res = math.pow(2,3)  #8.0
# res = math.pow(2,3,3)  #TypeError: pow expected 2 arguments, got 3
print(res)

# sqrt()  开平方运算 (结果是浮点数)
res = math.sqrt(9)
print(res)  # 3.0

# fabs()  计算一个数值的绝对值(结果是浮点数) (对比内置abs)
res = math.fabs(-1)
print(res)  #1.0

#modf() 将一个数值拆分成整数和小数两个部分组成元组
res = math.modf(3.89)
print(res)  #(0.8900000000000001, 3.0)

# copysign()  将参数第二反而数值的正负号拷贝给第一个(返回一个小数)
res = math.copysign(-12,-9.1)
print(res)  #-12.0

# fsum()  将一个容器数据中的数据进行求和运算(结果浮点数) (对比内置sum)
lst = [1,3,5]
res = math.fsum(lst)
print(res) #9.0

# 圆周率常数  pi  ***
print(math.pi)  #3.141592653589793

















































