# ### 1.set 集合类型  (交差并补)
# """特点: 无序,自动去重 单个元素不可获取 不可修改  可循环迭代"""
# 1.集合无序
setvar = {"巨石强森","史泰龙","施瓦辛格","王文"}
print(setvar,type(setvar))
#{'王文', '施瓦辛格', '史泰龙', '巨石强森'} <class 'set'>

# 01 下标获取集合中的元素 不可以  因为集合无序
# print(setvar[0])
#TypeError: 'set' object does not support indexing

# 02 修改集合中的元素 不可以   因为集合元素无法通过下标获取(无序)
# setvar[1] = 111
#TypeError: 'set' object does not support item assignment

# 2.集合自动去重
setvar = {"巨石强森","史泰龙","施瓦辛格","王文","史泰龙","史泰龙","史泰龙"}
print(setvar)
#{'史泰龙', '王文', '巨石强森', '施瓦辛格'}

# 3.定义一个空集合
setvar = set()

# ### 2.dict 字典类型
# """
# 键值对存储的数据,表面上有序,本质上无序
# dictvar = {键1:值1, 键2:值2 , ... }
# 3.6版本之前,完全无序,
# 3.6版本之后,存储的时候,保留了字典定义的字面顺序,在获取内存中数据时
# 重新按照字面顺序做了排序,所以看起来有序,实际上存储时还是无序.
# """

# 1.定义一个字典
dictvar = {"top":"the shy","middle":"肉鸡"}

# 2.获取字典中的值
res = dictvar['top']
print(res)  #the shy

# 3.修改字典中的值
dictvar['top'] = 'boy'
print(dictvar)
#{'top': 'boy', 'middle': '肉鸡'}

# 4.定义空字典
dictvar = {}


# ### 3.set 和 dict 的注意点
# 字典的键 和 集合的值 有数据类型上的要求:
# (允许的类型范围)不可变的类型: Number(int float complex bool) str tuple
# (不允许的类型)可变的类型    : list set dict

# 哈希算法的提出目的是让数据尽量均匀的在内存当中分配,以减少哈希碰撞,提升存储分配的效率;
# 哈希算法一定是无序的散列,所以集合 和 字典都是无序

# 字典的 键有要求,值没要求
# 字典的值可以任意换掉,但是键不可以.

# 允许的类型范围
dictvar = {1:"abc",4.89:111,False:333,3+90j:666,"王文":"你好帅啊,我好喜欢哦,没毛病",(1,2,3,4,5,6):9999}
print(dictvar[(1,2,3,4,5,6)])  #9999

# dictvar = {[1,2,3]:123} error
#TypeError: unhashable type: 'list'

# 允许的类型范围
setvar = {1,"a",4.56,9+3j,False,(1,2,3)}
setvar = {1,"a",4.56,9+3j,False,(1,2,3),{"a","b"}}  #集合中不能嵌套集合 集合是可变的  {"a","b"}
# TypeError: unhashable type: 'set'

# 总结:
# """
# 无论是变量缓存机制还是小数据池的驻留机制,
# 都是为了节省内存空间,提升代码效率
# """


















