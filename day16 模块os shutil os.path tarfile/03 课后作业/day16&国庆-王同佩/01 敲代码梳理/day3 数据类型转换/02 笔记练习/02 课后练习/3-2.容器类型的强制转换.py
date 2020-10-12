# ### 容器类型的强制转换(str list tuple set dict)

var1 = '我爱你,文哥哥'
var2 = [1,2,3]
var3 = (4,4,5)
var4 = {'陈璐','上朝气','刘子涛','合理'}
var5 = {'cl':'文质彬彬,斯文败类','szq':'学霸','lzt':'篮球少年','hl':'武林高手'}
var6 = 90
var7 = True

# str 强制转换成字符串
'''所有的数据类型都可以转换,在当前的数据类型两边套上引号   '''
res = str(var2)
res = str(var3)
res = str(var4)
res = str(var5)
res = str(var6)
res = str(var7)
print(res,type(res))  #True <class 'str'>
# repr 不转义,字符原型化输出字符串
print(repr(res))  #'True'

# list 强制转换陈列表
'''
如果是字符串:把字符串中的每个元素单独拿出来,作为列表中的新元素
如果是字典: 只保留字典中的键
如果是其他容器数据:就是单纯的在原数据类型的两边换上[]括号
'''
var1 = '我爱你,文哥哥'
var2 = [1,2,3]
var3 = (4,4,5)
var4 = {'陈璐','上朝气','刘子涛','合理'}
var5 = {'cl':'文质彬彬,斯文败类','szq':'学霸','lzt':'篮球少年','hl':'武林高手'}
var6 = 90
var7 = True

res = list(var1)
res = list(var3)
res = list(var4)
# 字典:只获取字典的键,忽略掉值
res = list(var5)
print(res)  #['cl', 'szq', 'lzt', 'hl']
# res = list(var6) #error 只能是容器间的互转  #TypeError: 'int' object is not iterable
print(res)

# tuple 强制转换成元组
'''
如果是字符串:把字符串中的每个元素单独拿出来,作为元祖中的新元素
如果是字典:只保留字典中的键
如果是其他容器数据:就是单纯的在原数据类型的两边换上()括号
'''
res = tuple(var1)
res = tuple(var2)
res = tuple(var4)
res = tuple(var5)
print(res,type(res))  #('cl', 'szq', 'lzt', 'hl') <class 'tuple'>

# set 强制转换成集合
'''
set 无序 去重  元素是不可变类型
如果是字符串:把字符串中的每个元素单独拿出来,作为集合中的新元素
如果是字典:只保留字典中的键
如果是其他容器数据:就是单纯的在原数据类型的两边换上{}括号
'''
res = set(var1)
res = set(var2)
res = set(var5)
print(res,type(res)) #{'cl', 'hl', 'lzt', 'szq'} <class 'set'>

#过滤掉列表中所有重复元素;
lst = [1,222,3,3,3,44,88,999,77,88,1]
res = set(lst)
print(res)  #{1, 3, 999, 44, 77, 88, 222}
# 再把当前的集合转换成原来的列表
res2 = list(res)
print(res2)  #[1, 3, 999, 44, 77, 88, 222]

'''
默认不加任何值,转换成该数据类型的空值
str() list() tuple() set() dict()
'''
res = dict()
print(res,type(res))  #{} <class 'dict'>





























