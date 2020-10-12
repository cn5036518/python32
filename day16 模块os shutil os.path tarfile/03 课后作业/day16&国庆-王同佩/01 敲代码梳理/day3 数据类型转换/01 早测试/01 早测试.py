#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/14 10:08

''''''
'''
早练习
1.什么是原码 反码 补码?
	正数的原码 反码 补码相同  符号位是0
	负数的原码 反码 补码不相同  符号位是1
			原码 = 补码取反,末位加1
			补码 = 原码取反,末位加1
	原码:表现形式
	补码:存储和运算	

2.进制转换:234 -> 2 8 16     (已完成验算)
	234 ->16  商14,余数10  0xea
	234 ->8    商29,余数2
				商3,余数5  0o352
	234 ->2    商117,余数0
			   商58,余数1
			   商29,余数0
			   商14,余数1
			   商7,余数0
			   商3,余数1
			   商1,余数1  0b11101010
	

3.进制转换:0b101001101 0o137 0xabc -> 十进制  (已完成验算)
	0b101001101   1+4+8+64+256= 13+320 = 333
	0o137		  7+3*8+64 = 7+24+64 =95
	0xabc         12+11*16+10*16^2 = 12+176+2560 = 2560+188 = 2748

4.进制转换:0xabc 转换成八进制   #先转换成二进制  (已完成验算)
	0xabc    0b   00 1010 1011 1100
	0xabc    0b   00 101 010 111 100
	0o               5    2   7   4   0o5274

5.计算 9+(-3) 以及 -9 + (3)
   9+(-3)
	9    正数 符号位是0 三码一致
		原码  0 000 ... 01001
		反码  0 000 ... 01001
		补码  0 000 ... 01001
		
		原码变反码 符号位不变
		补码运算  符号位参与运算
	
	-3  负数 符号位是1 三码不一致
		原码  1 000 ... 00011
		反码  1 111 ... 11100
		补码  1 111 ... 11101
		
		补码1  0 000 ... 01001
		补码2  1 111 ... 11101
		补码3  0 000 ... 00110    #正数 三码一致
		反码3  0 000 ... 00110 
		原码3  0 000 ... 00110   #6
		
	-9 + (3)
	-9    负数 符号位是1 三码不一致
		原码  1 000 ... 01001
		反码  1 111 ... 10110
		补码  1 111 ... 10111
		
		原码变反码 符号位不变
		补码运算  符号位参与运算
	
	3  正数 符号位是0 三码一致
		原码  0 000 ... 00011
		反码  0 000 ... 00011
		补码  0 000 ... 00011
		
		补码1  1 111 ... 10111
		补码2  0 000 ... 00011
		补码3  1 111 ... 11010  #负数 三码不一致
		反码3  1 000 ... 00101
		原码3  1 000 ... 00110  #-6


6.什么是注释
	用于方便阅读代码,注释的内容不会执行	

7.注释种类
	单行注释
	多行注释

8.如何用注释排错?
	一行一行注释,逐步缩小范围

9.如何定义变量?
	a = 16
	a,b = 1,2
	a = b =3

10.变量命名
	字母数字下划线,不能数字开头
	严格区分大小写,不能使用关键字
	变量命名有意义,不能使用中文	

11.如何交换变量
    a=1
	b=2
	a,b = b,a  #python特有
	
	#第三方变量  通用方法
	tmp = a
	a = b
	b = tmp

12.python的6大标准数据类型
	Number(int float bool complex)
	str
	tuple
	list
	dict
	set

13.浮点型和复数的两种数据类型
    浮点数
		1.23
		1.23e5  #科学计数法
	
	复数
		1+2j
		complex(1,2)

14.写出三个转义字符,含义
	\n 换行
	\t 制表符tab
	\r 覆盖当前行的行首

15.简述如何使用字符串的格式化占位符?
	print( '%s在水里%s,被发现了,罚款%.2f,俯卧撑%d个' % ('jack','dance',500.126,501))
	print( '%s在水里%s,被发现了,罚款%s,俯卧撑%s个' % ('jack','dance',500.126,501))  #万能写法
	%s 字符串占位符
	%f 浮点数占位符
	%d 整型占位符

16.简述容器类型各个特征
	str 	可获取,元素不可修改,有序
	tuple   可获取,元素不可修改,有序
	list	可获取,元素可修改,有序
	dict	可获取,值可修改,无序
	set		不可获取,值不可修改,无序

17.以下各是什么类型:
	()    #tuple
	(1)   #int
	('abc')  #str
	(False,)  #tuple
	
18.字典的键和集合的值有什么要求?
	字典的键
		1.无序
		2.不可重复
		3.必须是不可改变类型:tuple str Number(int float bool complex)
	
	集合的值
		1.无序
		2.不可重复
		3.必须是不可改变类型:tuple str Number(int float bool complex)
		
	附:
		可改变类型;list dict set

19.用几种方式获取列表中的最后一个元素
	方式1:listvar[-1]
	方式2:listvar[len(listvar)-1]

20.3.6版本中,变量的缓存机制有哪些?
    python3.6
		Number
			(int    -5~255范围内,值相同,id就相同
					上述范围外,值相同,id不相同
			float   正浮点数,值相同,id就相同
					负浮点数,值相同,id不相同				
			bool 	值相同,id就相同
			complex) 值相同,id不相同 (正虚数除外)
		str		str和空元祖 值相同,id就相同
		tuple   值相同,id不相同(空元组除外)
		list	值相同,id不相同
		dict	值相同,id不相同
		set		值相同,id不相同
	
	python3.7及其以上版本 
				只要值相同,id就相同
			   (list除外,list是值相同,id也不同)



'''



















