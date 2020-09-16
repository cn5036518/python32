#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/16 10:03


# # heigh = 1.26
# heigh = input('请输入你的身高:')
# # if type(heigh) == float or type(heigh) == int:
#
# heigh = float(heigh)  #字符串转换成小数  如何判断不是数字 不能用int()转换
# if heigh >= 1 and heigh <= 1.5:
#     print('小强,你在哪里?')
# elif heigh > 1.5 and heigh <= 1.7:
#     print('没有安全感')
# elif heigh > 1.7 and heigh <= 1.8:
#     print('帅哥,留个电话')
# elif heigh > 1.8 and heigh <= 2:
#     print('帅哥,你建议多个女朋友么')
# else:
#     print('身高不标准哈')



i = 0
strvar = ''
while i <5 :
    strvar += '★☆'
    i += 1
print(strvar)  #★☆★☆★☆★☆★☆


i = 0
strvar = ''
while i <5 :
    strvar += '★'
    strvar += '☆'
    i += 1
print(strvar)  #★☆★☆★☆★☆★☆
print('-----------------------')

#
i = 0
strvar = ''
while i <10 :
    if i % 2 == 0:
        strvar += '★'
    else:
        strvar += '☆'
    i += 1
print(strvar)
print('-----------------------')

i = 0
# strvar = ''
while i < 10 :
    if i % 2 == 0:
        print('★',end='')
    else:
        print('☆',end='')
    i += 1
# print(strvar)
print('-----------------------')

i = 0
while i < 100 :
    print('★', end='')
    if i % 10 == 9:  #取余
    # if i % 10 == 0:  #取余是0 就会少1个星
        print('')  #换行
    i += 1
print('-----------------------')

i = 1
while i < 101 :
    print('★', end='')
    if i % 10 == 0:  #取余
    # if i % 10 == 0:  #取余是0 就会少1个星
        print('')  #换行
    i += 1
print('-----------------------1')


i = 1
while i < 101 :
    if i % 2 == 0:
        print('★', end='')
        if i % 10 == 0:  #取余
            print('')  #换行
    else:
        print('☆', end='')
    i += 1
print('-----------------------2')

i = 1  #改进1
while i < 101 :
    if i % 2 == 1: #打印黑白相间
        print('★', end='')
    else:
        print('☆', end='')
    if i % 10 == 0:  # 取余
        print()  # 换行
    i += 1
print('-----------------------3')
""""""
i = 1  #改进2
strvar = ''
while i < 101 :
    if i % 2 == 1: #打印黑白相间
        strvar += '★'
    else:
        strvar += '☆'
    if i % 10 == 0:  # 取余
        strvar += '\n'
        # print('')  # 换行
    i += 1
print(strvar,end="")  #如果没有参数2,就会多一个换行
print('-----------------------4')

i = 1  #改进3
strvar = ''
while i < 101 :
    if i % 2 == 1: #打印黑白相间
        strvar += '★'
    else:
        strvar += '☆'
    if i % 10 == 0:  # 取余
        # strvar += '\n'
        print(strvar, end='')
        print()   #换行
        strvar = ''
    i += 1
print('-----------------------5')

#隔行换色
i = 0  #
strvar = ''
while i < 100 :
    if i // 10 == 0: #打印黑白相间  地板除
        strvar += '★'
    elif i // 10 == 2: #打印黑白相间
        strvar += '★'
    elif i // 10 == 4: #打印黑白相间
        strvar += '★'
    elif i // 10 == 6: #打印黑白相间
        strvar += '★'
    elif i // 10 == 8: #打印黑白相间
        strvar += '★'
    else:
        strvar += '☆'
    if i % 10 == 9:  # 取余
        strvar += '\n'
        # print('')  # 换行
    i += 1
print(strvar,end="")  #如果没有参数2,就会多一个换行
print('-----------------------6')

i = 0  #改进1
strvar = ''
while i < 100 :
    if i // 10 % 2 == 0: #打印黑白相间  地板除  关键
        strvar += '★'
    else:
        strvar += '☆'
    if i % 10 == 9:  # 取余
        strvar += '\n'
        # print('')  # 换行
    i += 1
print(strvar,end="")  #如果没有参数2,就会多一个换行
print('-----------------------7')















