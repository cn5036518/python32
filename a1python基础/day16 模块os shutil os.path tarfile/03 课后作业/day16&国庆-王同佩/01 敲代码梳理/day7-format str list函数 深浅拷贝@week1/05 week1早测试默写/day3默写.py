#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/20 15:46

''''''
'''

# 1.什么是原码 反码 补码?
# 2.进制转换
# 	234 --> 2 8 16
# 3.进制转换
# 	ob10101101
# 	0o137
# 	0xabc  --> 十进制
# 4.进制转换
# 	0xabc --> 八进制
# 5.计算 9 + (-3) 以及 -9 + 3
# 6.什么是注释
# 7.注释种类
# 8.如何用注释排错
# 9.如何定义变量?
# 10.变量命名
# 11.如何交换变量?
# 12.python 6大标准数据类型
# 13.浮点数和复数的两种表达方法
# 14.写出三个转义字符,含义
# 15.简述如何使用字符串的格式化占位符?
# 16.简述容器类型各个特征
# 17.以下各是什么类型?
# 	()  (1)  ('abc')  (False)
# 18.字典的键和集合的值有什么要求?
# 19.用几种方式获取列表中的最后一个元素
# 20.  3.6 版本中,变量的缓存机制有哪些?
'''

'''
# 1.什么是原码 反码 补码?
原码:用于表示  正数:符号位是0 三码一致  负数:符号位是1 三码不一致
反码:取反码的时候,符号位不变
补码:用于存储和运算      补码=原码取反,末尾加1   原码= 补码取反,末尾加1

# 2.进制转换
# 	234 --> 2 8 16
234      0b 11101010
117  0
 58  1
 29  0
 14  1
  7  0
  3  1
  1  1
  
234    0o 352
 29  2
  3  5
  
234     0xea
 14  10

# 3.进制转换
# 	ob10101101
# 	0o137
# 	0xabc  --> 十进制

# 	ob10101101   1+4+8+32+128 = 173
# 	0o137        64+24+7 = 95
# 	0xabc  -->   160+11*16+12= 172+176=348

# 4.进制转换
# 	0xabc --> 八进制  #先转二进制  

1010 1011 1100   4位一切

101 010 111 100  3位一切
5    2   7   4  0o5274

# 5.计算 9 + (-3) 以及 -9 + 3
9     正数:符号位是0 三码一致
原码  0 000 ... 1001
反码  0 000 ... 1001
补码  0 000 ... 1001

-3    负数:符号位是1 三码不一致
原码  1 000 ... 0011
反码  1 111 ... 1100
补码  1 111 ... 1101

补码1  0 000 ... 1001
补码2  1 111 ... 1101  #补码运算 符号位参与计算
补码3  0 000 ... 0110   #6  正数
-----------------------------------------------------

-9   负数:符号位是1 三码不一致
原码  1 000 ... 1001
反码  1 111 ... 0110
补码  1 111 ... 0111

3     正数:符号位是0 三码一致
原码  0 000 ... 0011
反码  0 000 ... 0011
补码  0 000 ... 0011

补码1  1 111 ... 0111
补码2  0 000 ... 0011
补码3  1 111 ... 1010  负数

反码   1 000 ... 0101
原码   1 000 ... 0110  #-6  负数

# 6.什么是注释
方便阅读,不编译运行

# 7.注释种类
单行注释
多行注释

# 8.如何用注释排错
一行一行注释,逐步缩小范围

# 9.如何定义变量?
变量就是可以改变的量，实际是内存的一块空间
a = 1

# 10.变量命名
字母数字下划线,数字不能开头
严格区分大小写,不能使用关键字
变量命名有意义,不能使用中文

# 11.如何交换变量?
a = 1
b = 2
# 方法1
a,b = b,a

# 方法2
tmp = a
a = b
b = tmp

# 12.python 6大标准数据类型
number
	int
	float
	bool
	complex
容器类型
	str 
	tuple
	list
	dict
	set

# 13.浮点数和复数的两种表达方法
浮点数
1.23
1.23e5

负数
1 + 3j
complex(1,3)

# 14.写出三个转义字符,含义
\n 换行
\t tab 制表符
\r 拿\r后面的内容覆盖行首

# 15.简述如何使用字符串的格式化占位符?
print('%s在水里%s,罚款%.2f,俯卧撑%d' % ('jack','dance',12.345,100))
print('{:s}在水里{:s},罚款{:.2f},俯卧撑{:d}'.format('jack','dance',12.345,100))

# 16.简述容器类型各个特征
str     可获取  不可修改 有序
tuple   可获取  不可修改 有序
list    可获取  可修改 有序
dict    可获取  值可修改 无序
set     不可获取  不可修改 无序 自动去重

# 17.以下各是什么类型?
# 	()  (1)  ('abc')  (False)
元组
int
字符串
bool

# 18.字典的键和集合的值有什么要求?
必须是不可变的类型(number-int float bool complex, tuple, str)
可变类型(list set dict)

# 19.用几种方式获取列表中的最后一个元素
listvar = ['a','b','c']

print(listvar[-1])
print(listvar[len(listvar)-1])

# 20.  3.6 版本中,变量的缓存机制有哪些?
number
	int  -5~正无穷  值相同,id相同
	float   非负浮点数  值相同,id相同
	bool    值相同,id相同
	complex	值相同,id不同(正虚数5j例外)
容器类型
	str	    值相同,id相同
	tuple   空元组 值相同,id相同,非空元组  值相同,id不同
	list    值相同,id不同
	dict    值相同,id不同
	set     值相同,id不同

python 3.7版本值相同,id相同(实际测试,列表例外)

'''


print('%s在水里%s,罚款%.2f,俯卧撑%d' % ('jack','dance',12.345,100))
print('{:s}在水里{:s},罚款{:.2f},俯卧撑{:d}'.format('jack','dance',12.345,100))





































