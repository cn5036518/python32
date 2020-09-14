# ### 二级容器 (list tuple set dicr)

# 二级列表
lst = [1,2,3,[4,5,6]]
# 二级元组
tup = (1,2,(10,11))
# 二级集合
setvar = {1,3,('a','b')}  #字典的元素必须以不可变类型
# 二级字典,
dic = {'a':1,'b':{'c':10}}
print(dic['b']['c'])  #10

# 四级容器
container = [1,2,3,(4,5,6,{'a':1,'b':[11,'bingbo']})]
# (4,5,6,{'a':1,'b':[11,'bingo']})
res1 = container[-1]
print(res1)  #(4, 5, 6, {'a': 1, 'b': [11, 'bingbo']})

# {'a':1,'b':[11,'bingo']}
res2 = res1[-1]
print(res2)  #{'a': 1, 'b': [11, 'bingbo']}

# [11,'bingo']
res3 = res2['b']
print(res3)  #[11, 'bingbo']

# bingo
res4 = res3[-1]
print(res4)  #bingbo

# 一步简写
res = container[-1][-1]['b'][-1]
print(res)  #bingbo

# 等长的二级容器
'''概念: 外面是容器,里面的元素也是容器,且元素个数相同  '''
lst = [(1,2,3),[4,5,6],{7,8,9}]

# ### dict 字典类型的强制转换
'''
要求:必须是等长的二级容器,并且里面的元素个数是2个;
外层是列表,元组,里层是列表或者元组的等长二级容器 => 字典
外层是集合,里层是元组(不能是列表)的等长二级容器 => 字典
'''

# 1.外层是列表,里层是列表或者元组
lst = [['a',1],('b',2)]
dic = dict(lst)
print(dic,type(dic))  #{'a': 1, 'b': 2} <class 'dict'>

# 2.外层是元组,里层是列表或者元组
tup = (['a',1],('b',2))
dic = dict(tup)
print(dic,type(dic))  #{'a': 1, 'b': 2} <class 'dict'>

# 3.外层是集合,里层是元组  (集合的元素不能是列表)
setvar = {('a',1),("b",2)}
dic = dict(setvar)
print(dic,type(dic))  #{'b': 2, 'a': 1} <class 'dict'>

# 例外1:外层是列表/元组,里层放集合
'''可以实现,不推荐使用,因为达不到想要的目的,集合无序,不推荐使用'''
lst  = [['a',1],{'b','250'}]
dic = dict(lst)
print(dic)  #{'a': 1, '250': 'b'}  #这里250和b的位置经常对换

# 例外2:外层是列表/元组,里层放字符串
'''字符串长度只能是2位,有极大的局限性(字符串长度只能是2),不推荐使用  '''
lst = ['a1','b2'] #字符串长度只能是2
dic = dict(lst)
print(dic)  #{'a': '1', 'b': '2'}

# lst = ['a11','b22']  #字符串长度只能是2
# dic = dict(lst)
# print(dic)  #ValueError: dictionary update sequence element #0 has length 3; 2 is required


































