# ### 字符串类型 str
# """
# 用引号引起来的就是字符串,单引号,双引号,三引号

# 转义字符 \ + 字符
	# (1) 可以将无意义的字符变得有意义
	# (2) 可以将有意义的字符变得无意义
	
# \n   : 换行
# \r\n : 换行
# \t   : 缩进(水平制表符)	
# \r   : 将\r后面的字符串拉到了当前行的行首,覆盖行首 (应用:进度条)
# """

# 1.单引号的字符串
strvar = '生活不止眼前'
print(strvar,type(strvar))
#生活不止眼前 <class 'str'>

# 2.双引号的字符串
strvar = "还有诗和远方"
print(strvar,type(strvar))
#还有诗和远方 <class 'str'>

strvar = "还有诗和\n远方的田野"
print(strvar)
# 还有诗和
# 远方的田野
print('-----------------------------n')

strvar = "还有诗和\r\n远方的田野"
print(strvar)
# 还有诗和
# 远方的田野
print('-----------------------------rn')

strvar = "还有诗和\t远方的田野"
print(strvar)
#还有诗和	远方的田野
print('-----------------------------t')

strvar = "还有诗和\r远方的田野" 
#将\r后面的字符串拉到了当前行的行首,覆盖行首
print(strvar,type(strvar))
# 远方的田野 <class 'str'>

# 3.三引号的字符串 (可以支持跨行效果)
# strvar = '''
# 生活就像"醉"酒
# 表面上说'不'要
# 身体却很诚实
# '''
print(strvar)

# 4.元字符串 r"字符串" 原型化输出字符串  repr(字符串)
strvar = r'd:\nython32\tay02'
print(strvar)
# d:\nython32\tay02

strvar = 'd:\nython32\tay02'
res = repr(strvar)
print(res)
#'d:\nython32\tay02'

# 5.字符串的格式化
# """
# %d 整型占位符
# %f 浮点型占位符
# %s 字符串占位符
# 语法形式:
	# "字符串" % (值1,值2)
	
# 一 %d
# 01 %d 整型占位符 占一位
strvar = '%d 个风油精' % (2)
print(strvar)  #2 个风油精

# 02 %2d 整型占位符 占2位  原字符串右对齐
strvar = '%2d 个风油精' % (2)
print(strvar) # 2 个风油精

# 03 %-2d 整型占位符 占2位 原字符串左对齐
strvar = '%-2d 个风油精' % (2)
print(strvar) #2  个风油精
print('------------------------- %d')

# 二 %f
# 01 %f 浮点型占位符 默认保留六位小数
strvar = '工资 %f' % (9.9)
print(strvar)  #工资 9.900000

# 02 %.2f 保留小数点后面两位小数 (存在四舍五入的情况,默认保留六位小数)
strvar = '工资 %.2f' % (9.916)
print(strvar)  #工资 9.92
print('------------------------- %f')

# 三 %s  字符串占位符
strvar = '%s 喜欢看电影' % ('jack')
print(strvar)
#jack 喜欢看电影
print('------------------------- %s')
	
# 四 综合案例	
strvar = '%s在水里跳舞,罚款%.2f元,俯卧撑%d个' % ('jack',500.178,100)
print(strvar)
#jack在水里跳舞,罚款500.18元,俯卧撑100个
	 
# 五 如果搞不清楚用什么占位符,可以无脑使用%s	推荐
strvar = '%s在水里跳舞,罚款%s元,俯卧撑%s个' % ('jack',500.128,100)
print(strvar)
#jack在水里跳舞,罚款500.128元,俯卧撑100个
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	




















