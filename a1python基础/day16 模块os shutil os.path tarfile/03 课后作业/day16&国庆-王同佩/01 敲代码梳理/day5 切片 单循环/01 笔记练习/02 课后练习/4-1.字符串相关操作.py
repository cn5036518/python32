# ### 字符串相关操作
#  (1) 字符串的拼接 +
str1 = '赵沈阳,'
str2 = 'so strong'
# res = '赵沈阳' + 'so strong'
res = str1 + str2
print(res)  #赵沈阳,so strong

# res = res + '旁边的同学很喜欢他~'
res += ',旁边的同学很喜欢他~'
print(res)  #赵沈阳,so strong,旁边的同学很喜欢他~

#  (2) 字符串的重复  *
strvar = '重要的事情说三遍~'
res = strvar * 3
print(res)  #重要的事情说三遍~重要的事情说三遍~重要的事情说三遍~

#  (3) 字符串的跨行拼接 \
str1 = 'aafjjfadj'\
'12244'
print(str1)  #aafjjfadj12244

#  (4) 字符串的索引
#		  0 1 2 3 4 5 
strvar = '赵世超真帅啊'
# 		  -6-5-4-3-2-1
print(strvar[1])  #世

#  (5) 字符串的切片 (截取)
'''
语法 ==> 字符串[::]  完整格式: [开始索引;结束索引;间隔值]
	  (1) [开始索引:] 从开始索引截取到字符串的最后
	  (2) [:结束索引] 从开始截取到结束索引之前(结束索引-1)
	  (3) [开始索引:结束索引]  从开始索引截取到结束索引之前(结束索引-1)
	  (4) [开始索引:结束索引:间隔值]  从开始索引截取到结束索引之前(结束索引-1)
										按照指定的间隔截取字符
	  [5] [:]或[::]  截取所有字符串
'''

strvar = '王文是这个宇宙当中,最完美,无暇,善良,漂亮,英俊,帅气,潇洒,风流倜傥的神秘男孩'
# (1) [开始索引:] 从开始索引截取到字符串的最后
res = strvar[3:]
print(res)  #这个宇宙当中,最完美,无暇,善良,漂亮,英俊,帅气,潇洒,风流倜傥的神秘男孩

# (2) [:结束索引] 从开始截取到结束索引之前(结束索引-1)
# 4这个最大值本身获取不到,要获取到4之前的那一个数据:取头舍尾
res = strvar[:5]
print(res)  #王文是这个

#(3) [开始索引:结束索引]  从开始索引截取到结束索引之前(结束索引-1)
res = strvar[10:16]
print(res)  #最完美,无暇

#	  (4) [开始索引:结束索引:间隔值]  从开始索引截取到结束索引之前(结束索引-1)
										# 按照指定的间隔截取字符

# 从左向右截取(步长是正数)
res = strvar[::3]
#0 3 6 9 12 15 ...
print(res)  #王这宙,美暇良亮俊气洒流的男

# 从右向左截取(步长是负数)
res = strvar[::-1]  #字符串反转
# -1 -2 -3 -4 -5 -6 ....
print(res)
#孩男秘神的傥倜流风,洒潇,气帅,俊英,亮漂,良善,暇无,美完最,中当宙宇个这是文王

res = strvar[-3:-10:-2]
# -3 -5 -7 -9 
print(res)  #秘的倜风

print('==============')
'''
从左到右截,间隔值为正值,
从右到左,间隔值为负数,才能保证截取到数据
res = strvar[-3:-10:10] #错误的逻辑
print(res)
res = strvar[1:10]
print(res)
'''




































