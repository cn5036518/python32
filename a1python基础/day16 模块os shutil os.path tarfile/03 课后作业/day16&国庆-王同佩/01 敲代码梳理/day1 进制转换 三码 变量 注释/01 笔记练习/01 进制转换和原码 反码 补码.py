#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/12 19:24

# ''''''
# '''
# 1.1 计算机硬件基本认知
# cpu:中央处理器.相当于人的大脑.运算中心.控制中心.
# 内存:临时存储数据.
      # 优点:读取速度快
      # 缺点:容量小,造价高,断电即消失.
# 硬盘:长期存储数据.
      # 优点:容量大,造价相对低,断电不消失.
      # 缺点:读取速度慢.
# 操作系统:统一管理计算机硬件资源的程序.

# 1.2 计算机文件大小单位
# b = bit 位(比特)
# B = Byte字节

# 1Byte = 8 bit  #一个字节等于8位 可以简写成 1B = 8b
# 1KB = 1024B
# 1MB = 1024KB
# 1GB = 1024MB
# 1TB = 1024GB
# 1PB = 1024TB
# 1EB = 1024PB

# 1.3 进制转换
# 二进制:由2个数字组成.有0和1   binary
        # 例子:0b101   #5
# 八进制:由8个数字组成.有0,1,2,3,4,5,6,7  octal
        # 例子:0o127  64+16+7=87
# 十进制:由10个数字组成,有0,1,2,3,4,5,6,7,8,9  decimal
        # 例子:250     
# 十六进制:由16个数字组成,有0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f
         # (字母大小写都可以,分别代表10,11,12,13,14,15)        
         # 例子:0xff  0Xff  0XFF
         
# 1.3.1 二进制 转化成  十进制
# 例: 0b10100101
# 运算:1*2^0 + 0*2^1 + 1*2^2 + 0*2^3 + 0*2^4 + 1*2^5 + 0*2^6 + 1*2^7 = 
       # 1+0+4+0+0+32+0+128  = 165
       
# 1.3.2 八进制 转换成 十进制
# 例: 0o127
# 运算:7*8^0 + 2*8^1 + 1*8^2
    # = 7+16+64 = 87
    
# 1.3.3 十六进制 转化成 十进制
# 例:0xff
# 运算:15*16^0 + 15*16^1=15 + 240 = 255

# *小练习:转换成对应进制
# 723 => 2
# 654 => 2
# 723 => 8
# 654 => 8
# 723 => 16
# 654 => 16

# 1.3.4 十进制 转化成 二进制
# 426 => 0b110101010
# 运算过程:用426除以2,得出的结果再去不停地除以2,
         # 直到除完最后的结果小于2停止,
         # 再把每个阶段求得的余数从下到上依次拼接完毕即可.
         
# 1.3.5 十进制 转化成 八进制
# 426 => 0o652
# 运算过程:用426除以8,得出的结果再去不停的除以8
         # 直到除完最后的结果小于8停止,
         # 再把每个阶段求得的余数从下到上依次拼接完毕即可

# 1.3.6 十进制 转化成 八进制
# 426 => 0o652
# 运算过程:用426除以16,得出的结果再去不停地除以16,
          # 直到除完最后的结果小于16停止,
          # 在把每个阶段求得的余数从下到上依次拼接完毕即可
          
# *小练习:转化成 十六进制
# 723 => 2
# 654 => 2
# 723 => 8
# 654 => 8
# 723 => 16
# 654 => 16

# 1.3.7 二进制 与 十六进制
# 二进制与八进制对应关系:
# 八进制 二进制
# 0       000
# 1       001
# 2       010
# 3       011
# 4       100
# 5       101
# 6       110
# 7       111

# 例:1010100101
# 八进制:从右向左 3位一隔开 不够三位用0补位 变成:
# 001 010 100 101
# 0o 1  2   4  5

# 1.3.8 二进制与十六进制转换
# 十六进制  二进制
# 0           0000
# 1           0001
# 2           0010
# 3           0011
# 4           0100
# 5           0101
# 6           0110
# 7           0111
# 8           1000
# 9           1001
# a           1010
# b           1011
# c           1100
# d           1101
# e           1110
# f           1111
         
# 例:1010100101
# 十六进制:从右向左 4位一隔开 不够四位用0补位 变成:
# 0010 1010 0101
# 0x 2a5

# 1.3.9 八进制 与 十六进制的转换
# 先转换成二进制 再去对应转换
# 比如:0x2a5 转换成 1010100101 再转8进制 0o1245

# *小练习:转化成对应进制
# 0x1DD => 8
# 0x29a => 8
# 0o573 => 16
# 0o336 => 16

# 1.4 原码,反码,补码(了解)
# 1.原码 或 补码 都是 二进制数据
# 原码:二进制的表现形式
# 反码:二进制码0变1,1变0叫做反码,[原码][补码]之间的转换形式.(首位符号位不取反)
# 补码:二进制的存储形式

# 数据用[补码]形式存储
# 数据用[原码]形式显示
# [原码]和[补码]可以通过[反码]互相转化,互为取反加1

# 2.提出补码的原因
# 补码的提出用于表达一个数的正负(可实现计算机的减法操作)
# 计算机默认只会做加法,实现减法用负号:5+(-3) =>5-3
# 乘法除法:是通过左移和右移 << >>来实现.

# 3. [原码]形式的正负关系:
# 原码特点:第一位是1
    # 0000 0000  1   表达数字正1
    # 1000 0000  1   表达数字负1    

# 4. [补码]形式的正负关系:
# 补码特点:高位都是1
    # 0000 0000 1 表达数字正1
    # 1111 1111 1 表达数字负1
    
# 5.运算顺序:
    # 补码->原码->最后人们看到的数
    # ***
    # 进制转换的时候,需要先把内存存储的补码拿出来变成原码在进行转换输出
    # ***

    # 转换规律:
        # 如果是一个正数:原码= 反码 = 补码
        # 如果是一个负数:原码与补码之间,互为取反加1
            # 原码 = 补码取反加1 给补码求原码
            # 补码 = 原码取反加1 给原码求补码
            
# *小练习:原码 与 反码的转换

# 给原码求补码
    # -6的补码是多少?
     # 6的补码是多少?
     # 9的补码是多少?
    # -9的补码是多少?
# 给补码求原码
    # 1111...0011 (高位都是1)
    # 0000...1010 (高位都是0)
# 9 + (-5) 用二进制相加运算一下












# '''



















