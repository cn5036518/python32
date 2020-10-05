# ### 列表类型 list
# """特征: 可获取,可修改,有序"""
# 1.定义列表
# 01 定义一个空列表
listvar = []

# 02 定义普通列表
listvar = [1,2,3]

# 2.获取列表中的元素  索引获取
# 正向索引   0  1   2     3      4
listvar =   [98,6.9,True,12-90j,"赵万里"]
# 逆向索引  -5  -4  -3     -2      -1

res = listvar[2]
print(res)  #True

res = listvar[-2]
print(res)  #(12-90j)

# 获取list中最后一个元素
#方法1  推荐
print(listvar[-1])  #赵万里

#方法2
print(listvar[len(listvar)-1])  #赵万里


# 3.修改列表中的元素
listvar = [98,6.9,True,12-90j,"赵万里"]
listvar[3] = 'elephant'
print(listvar)  #[98, 6.9, True, 'elephant', '赵万里']
print('----------------------------1 list')



# ### 元组类型 tuple
# """特征: 可获取,不可修改,有序"""
# 1 定义一个元组
#   01 定义空元组
tuplevar = ()

#   02 定义普通元组
tuplevar = ("梦好心","王伟","安晓东","孙坚")

# 2 获取元组中的元素
# 正向索引   0          1       2       3      
tuplevar = ("梦好心","王伟","安晓东","孙坚")
# 逆向索引    -4       -3      -2      -1

print(tuplevar[2])  #安晓东
print(tuplevar[-1]) #孙坚

# 3 修改元组中的元素 : 元组中的值不能修改
# tuplevar[0] = 'jack'
#TypeError: 'tuple' object does not support item assignment

# 4 注意点
# """逗号才是区分是否是元组的标识符,()不是"""
tuplevar = (8.9,)  #元组
print(tuplevar,type(tuplevar))
# (8.9,) <class 'tuple'>

tuplevar = 8.1,  #元组
print(tuplevar,type(tuplevar))
#(8.1,) <class 'tuple'>

tuplevar = 8.1,9.1  #元组
print(tuplevar,type(tuplevar))
#(8.1, 9.1) <class 'tuple'>

tuplevar = (8.9)  #float
print(tuplevar,type(tuplevar))
# 8.9 <class 'float'>

tuplevar = 8.1  #float
print(tuplevar,type(tuplevar))
# 8.1 <class 'float'>
print('----------------------------2 tuple')


# ### 字符串类型
# """特征: 可获取,不可修改,有序"""
# 0 定义字符串
#   01 定义空字符串
strvar = ''

#   03 定义纯空格的字符串
strvar = '   '  #字符串中含有3个空格字符

# 1 获取字符串中的元素
# 正向索引   0 1 2 3 4 5 6 7 8
strvar =    "看你,我就心跳加速"
# 逆向索引  -9-8-7-6-5-4-3-2-1

print(strvar[2]) #,
print(strvar[-2]) #加

# 2 不能修改字符串中的元素
# strvar[3] = '你'  #error 字符串是不可变类型
#TypeError: 'str' object does not support item assignment
# 不可变类型: numbers(int float bool complex)  tuple  str
#               集合的元素和字符的键必须是不可变类型
# 可变类型:list dict set


























