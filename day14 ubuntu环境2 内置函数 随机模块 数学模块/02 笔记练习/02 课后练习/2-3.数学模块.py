# 小结默写
# ### 数学模块
import math

# 第一组  向上向下取整  ceil floor
#1 ceil()  向上取整操作 (对比内置round) ***
print(math.ceil(5.1))  #6  ceil 天花板
print(math.ceil(-5.9)) #-5

#2 floor() 向下取整操作 (对比内置round) ***
print(math.floor(5.9))  #5   floor 地板
print(math.floor(-5.1)) #-6
print('---------------------------1 ceil floor')


# 第二组  幂 开方  绝对值 求和   pow sqrt fabs  fsum
#1 pow()  计算一个数值的N次方(结果为浮点数) (对比内置pow)
# """结果为浮点数,必须是两个参数"""
print(math.pow(2,3))  #8.0

#2 sqrt() 开平方运算(结果浮点数)
print(math.sqrt(4)) # 2.0

#3 fabs() 计算一个数值的绝对值 (结果浮点数) (对比内置abs)
print(math.fabs(-10))  #10.0

#4 fsum() 将一个容器数据中的数据进行求和运算 (结果浮点数)
#(对比内置sum)
lst = [1,3,5]
print(math.fsum(lst)) #9.0
print('---------------------------2 pow sqrt fabs fsum')

#第三组  拆  拷贝符号 圆周率  pi  modf copysign
#1 modf() 将一个数值拆分为整数和小数两部分组成元组  小数在前
print(math.modf(3.15))  #(0.1499999999999999, 3.0)

#2 copysign()  将参数第二个数值的正负号拷贝给第一个 (返回一个小数)
print(math.copysign(-10,-15))  #-10.0

#3 圆周率常数 pi ***
print(math.pi)  #注意:pi后面没有小括号
#3.141592653589793
print('---------------------------3 pi modf copysign')


#小结
# import math
# math的函数一共是3组,都是返回浮点数
# 第1组
# math.ceil() 向上取整   ***    #6.1==>7.0
# floor()     向下取整   ***     #6.9 ==> 6.0

# 第2组
# pow  只有2个参数 幂运算   #2,3 ==>8.0
# sqrt  开方        #4==>2.0   没有-2.0
# fabs  绝对值    #  -5==> 5.0
# fsum  求和      #[1,2,3]==>6.0

# 第3组
# pi   pi后面没有()  #3.1415912653589793
# modf  拆成小数和整数 小数在前  # 3.15  (0.1499999,3.0)
# copysign  把参数2的符号拷贝给参数1  #-10,15==>  10.0





















































