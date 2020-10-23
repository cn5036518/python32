# ### 1.set 集合类型 (交差并补-运算)
''' 特点:无序,自动去重'''
# 1.集合无序
setvar = {'巨石强森','史泰龙','施瓦辛格','王文'}
print(setvar,type(setvar))  #{'王文', '施瓦辛格', '史泰龙', '巨石强森'} <class 'set'>

# 获取集合中的元素  不可以(因为无序)
# setvar[0]  #TypeError: 'set' object is not subscriptable

# 修改集合中的元素 不可以   注意点
# setvar[2] = 111   #TypeError: 'set' object does not support item assignment

# 2.集合自动去重
setvar = {'巨石强森','史泰龙','施瓦辛格','王文','王文','王文'}
print(setvar)  #{'施瓦辛格', '巨石强森', '史泰龙', '王文'}

# 3.定义一个空集合
setvar = set()  #注意点: {}是空字典,而不是空集合
print(setvar, type(setvar))  #set() <class 'set'>

# ### 2.dict 字典类型
"""
键值对存储的数据,表面上有序,本质上是无序的
dictvar = {键1:值1,键2:值2,...}
3.6版本之前,完全无序  (每次print,顺序都不同)
3.6版本之后,存储的时候,保留了字典定义的字面顺序,在获取内存中数据时
重新按照字面顺序做了排序,所以看起来有序,实际上存储时还是无序
"""

# 1.定义一个字典
dictvar = {'top':'the shy','middle':'肉鸡'}
print(dictvar,type(dictvar))  #{'top': 'the shy', 'middle': '肉鸡'} <class 'dict'>

# 2.获取字典中的值
res = dictvar['middle']  #列表取的是索引下标,字典取的是键
print(res)  #肉鸡

# 3.修改字典中的值
dictvar['top'] = 'the xboy'  
print(dictvar)  #{'top': 'the xboy', 'middle': '肉鸡'}

# 4.定义空字典
dictvar = {}
print(dictvar,type(dictvar))  #{} <class 'dict'>


# ### 3.set和dict的注意点
"""
字典的键和集合的值,有数据类型上的要求:
(允许的类型范围)不可变的类型:
	Number(int,float,complex,bool)   str  tuple
(不允许的类型范文):可变的类型:
	list dict set
	
哈希算法的提出目的是让数据尽量均匀的在内存当中分配.以减少哈希碰撞,提升存储分配的效率;
哈希算法一定是无序的散列,所以集合和字典都是无序的

字典的键有要求,值没要求
字典的值可以修改,但是键不能修改
"""
# dict允许的类型范围
dictvar = {1:'abc',4.89:111,False:333,3+9j:66,'王文':'好帅',(1,2):9999}
print(dictvar)  #{1: 'abc', 4.89: 111, False: 333, (3+9j): 66, '王文': '好帅', (1, 2): 9999}
print(dictvar[(1,2)])  #9999

# set允许的类型范围
# set是没有值的dict
# dict的键需要是不可变类型(Number-int float bool complex,tuple,str),set的元素也需要是不可变类型
setvar = {1,'a',4.56,9+3j,False,(1,2,3)}
print(setvar)  # {False, 1, 4.56, (1, 2, 3), (9+3j), 'a'}

# setvar = {1,'a',4.56,9+3j,False,(1,2,3),{'a','b'}}  #因为集合的元素必须是不可变的,而元素{'a','b'}是集合,是可变的,
# print(setvar)  #TypeError: unhashable type: 'set'   

#总结
'''
无论是变量缓存机制还是小数据池的驻留机制,
都是为了节省内存空间,提升代码效率


'''































