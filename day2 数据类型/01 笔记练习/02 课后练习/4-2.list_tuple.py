# ### 列表类型 list
"""特征: 可获取,可修改,有序"""
# 1.定义一个空列表
listvar = []
print(listvar,type(listvar))  #[] <class 'list'>

# 定义普通列表
listvar = [98,6.9,True,12-90j,'赵万里']
print(listvar)

# 2.获取列表中的元素
# 正向索引 0	1  2    3		4
listvar = [98,6.9,True,12-90j,'赵万里']
# 逆向索引-5   -4  -3   -2    	-1

res = listvar[2]
res = listvar[-2]
print(res)  #12 - 90j

# 通用写法
# len 获取容器类型数据中元素个数
length = len(listvar)
res = listvar[length-1]
print(res)  #赵万里

# 简写
res = listvar[len(listvar)-1]
print(res)  #赵万里

# python逆向索引的特点,瞬间得到列表中最后一个元素
print(listvar[-1])  #赵万里

# 3.修改列表中的元素
listvar = [98,6.9,True,12-90j,'赵万里']
listvar[3] = '大象'
print(listvar)  #[98, 6.9, True, '大象', '赵万里']

# ### 元组类型 tuple
"""特征:可获取,不可修改,有序"""
#定义一个元组
tuplevar = ('梦好心','王伟','安晓东','孙坚')
print(tuplevar,type(tuplevar))  #('梦好心', '王伟', '安晓东', '孙坚') <class 'tuple'>

# 获取元组中的元素
# 正向索引	0		1 			2 		3
tuplevar = ('梦好心','王伟','安晓东','孙坚')
# 逆向索引	-4		-3 		  -2		-1

print(tuplevar[2])  #安晓东
print(tuplevar[-1])  #孙坚

#修改元组中的元素:元组中的值不能修改
# tuplevar[0]  = '梦不好心'     #TypeError: 'tuple' object does not support item assignment

#注意点
"""都好才是区分是否是元组的标识符"""
tuplevar = (8.9,)
tuplevar = 8.1,   #元组可以不用小括号 小括号不是必须的
print(tuplevar)
print(type(tuplevar))

# 定义空元组
tuplevar = ()
print(tuplevar,type(tuplevar))  #() <class 'tuple'>


# ### 字符串类型
"""
	特征:可获取,元素不可修改,有序
"""
# 正向索引   0 1 2 3 4
strvar = 	'看你,我就'
# 逆向索引	 -5-4-3-2-1

# 获取字符串中的元素
print(strvar[3])  #我
print(strvar[-2]) #我

# 不能修改字符串中的元素
#strvar[3] = '你'  #TypeError: 'str' object does not support item assignment

print('<============================>')
strvar = ''  #单纯定义一个字符串类型
print(strvar)
print(type(strvar))  #<class 'str'>

strvar = '   '  # 字符串中含有3个空格字符
print(strvar[0])
print(type(strvar))  #<class 'str'>
























































