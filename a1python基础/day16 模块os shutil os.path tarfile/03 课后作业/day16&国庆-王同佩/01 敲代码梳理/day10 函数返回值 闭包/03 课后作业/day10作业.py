# ### 定义函数
# 1.定义函数:接收任意个参数,打印其中的最小值
# 2.定义函数:传入一个参数n，返回n的阶乘(5! = 5*4*3*2*1)
# 3.写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等)
# 将容器中的每个元素依次添加到新的列表中返回
	#例:传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
# 4.写函数，用户传入要修改的文件名，与要修改的内容，执行函数，修改操作
# 5.写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# 6.写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，返回处理后的结果.
	#例:参数为:dic = {"k1": "v1v1", "k2": [11,22,33,44]}

# 7传入多个容器类型数据,计算所有元素的个数

# ### 闭包
#下面代码成立么?如果不成立为什么报错?怎么解决?
#1
# a = 2
# def wrapper():
#	print(a)
# wrapper()


#2
# a = 2
# def wrapper():
#     a += 1
#     print(a)
# wrapper()

#3
# a = 2
# def wrapper():
#     global a
#     a += 1
#     print(a)
# wrapper()

#4
# def wrapper():
#      a = 1
#      def inner():
#          print(a)
#      inner()
# wrapper()

#5
# def wrapper():
#      a = 1
#      def inner():
#          a += 1
#          print(a)
#      inner()
# wrapper()

#6
# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a
#         a += 1
#         print(a)
#     inner()
# wrapper()




