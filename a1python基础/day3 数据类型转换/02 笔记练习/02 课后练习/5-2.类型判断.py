# ### 判断类型 isinstance
'''
# 使用方法一
isinstance(数据,类型)
如果该数据是这个类型,返回True 反之,返回False
类型: int float complex bool str list tuple set dict

# 使用方法二
isinstance(数据,(类型1,类型2,类型3...))
如果该数据在所对应的类型元祖中,返回True,反之,返回False
'''


# 使用方法一
n = 123
res = isinstance(n,int)
print(res)

# 使用方法二
n = '1233'
res = isinstance(n,(list,tuple,set,str))
print(res)

n = {'a':1}
res = isinstance(n,(list,tuple,set,str))  #参数2只能是元组
# res = isinstance(n,[list,tuple,set,str])  #TypeError: isinstance() arg 2 must be a type or tuple of types
print(res)
