# ### 容器类型的强制转换 (str tuple list dict set)

var1 = '我爱你,文哥哥'
var2 = [1,2,3]
var3 = (4,4,5)
var4 = {'陈璐','上朝气','刘子涛','合理'}
var5 = {'cl':'文质彬彬,斯文败类','szq':'学霸','lzt':"篮球少年",'hl':'武大高手'}
var6 = 90
var7 = True


# str  强制转换成字符串
'''所有的数据类型都可以转换,在当前的数据类型两边套上引号   '''
res = str(var2)
res = str(var3)
res = str(var4)
res = str(var5)
res = str(var6)
res = str(var7)
print(res,type(res))
# repr 不转义字符原型化输出字符串  #True <class 'str'>
print(repr(res))  #'True'

# list 强制转换成列表
'''
如果是字符串:把字符串中的每个元素单独拿出来,作为列表的新元素
如果是字典:只保留字典中的键
如果是其他容器数据:就是单纯的在原数据类型的两边换上[]括号
'''
res = list(var1)
print(res,type(res))  #['我', '爱', '你', ',', '文', '哥', '哥'] <class 'list'>

res = list(var3)
print(res,type(res))  #[4, 4, 5] <class 'list'>

res = list(var4)
print(res,type(res))   #['刘子涛', '合理', '上朝气', '陈璐'] <class 'list'>

# 字典:只获取字典的键,忽略掉值
res = list(var5)
print(res,type(res))  #['cl', 'szq', 'lzt', 'hl'] <class 'list'>

# res = list(var6)  #只能是容器间的互转   90是int(number类型),不是容器类型(str tuple list dict set)
print(res,type(res))  #TypeError: 'int' object is not iterable

# tuple 强制转成元组
'''
如果是字符串:把字符串中的每个元素单独拿出来,作为元组中的新元素
如果是字典:	  只保留字典中的键
如果是其他容器数据:就是单纯的在原数据类型的两边换上()括号
'''
var1 = '我爱你,文哥哥'
var2 = [1,2,3]
var3 = (4,4,5)
var4 = {'陈璐','上朝气','刘子涛','合理'}
var5 = {'cl':'文质彬彬,斯文败类','szq':'学霸','lzt':"篮球少年",'hl':'武大高手'}
var6 = 90
var7 = True

res = tuple(var1)
print(res,type(res))
#('我', '爱', '你', ',', '文', '哥', '哥') <class 'tuple'>

res = tuple(var2)
print(res,type(res)) #(1, 2, 3) <class 'tuple'>

res = tuple(var4)
print(res,type(res))  #('上朝气', '陈璐', '合理', '刘子涛') <class 'tuple'>

res = tuple(var5)
print(res,type(res)) #('cl', 'szq', 'lzt', 'hl') <class 'tuple'>

# set 强制转换成集合
'''
如果是字符串:把字符串中的每个元素单独拿出来,作为集合中的新元素,集合无序
如果是字典:  只保留字典中的键
如果是其他容器数据:就是单纯的在原数据类型的两边换上{}括号
'''
var1 = '我爱你,文哥哥'
var2 = [1,2,3]
var3 = (4,4,5)
var4 = {'陈璐','上朝气','刘子涛','合理'}
var5 = {'cl':'文质彬彬,斯文败类','szq':'学霸','lzt':"篮球少年",'hl':'武大高手'}
var6 = 90
var7 = True

res = set(var1)
print(res,type(res))  #{'爱', ',', '文', '你', '哥', '我'} <class 'set'>

res = set(var2)
print(res,type(res))  #{1, 2, 3} <class 'set'>

res = set(var5)
print(res,type(res))  #{'lzt', 'szq', 'hl', 'cl'} <class 'set'>

#小练习  过滤掉列表中所有重复元素;
# 先转换成集合(集合自动去重),然后再转换成列表

lst = [1,222,3,3,3,44,88,999,777,88,1]
res = set(lst)
print(res)  #{1, 3, 999, 777, 44, 88, 222}
# 再把当前的集合转换成原来的列表
res2 = list(res)
print(res2) #[1, 3, 999, 777, 44, 88, 222]

'''
默认不加任何值,转换成该数据类型的空值
sre() lisr() tuple() set() dict()
'''
res = dict()
print(res,type(res))  #{} <class 'dict'>

res = str()
print(res,type(res))  #空字符串

res = list()
print(res,type(res)) #[] <class 'list'>

res = tuple()
print(res,type(res)) #() <class 'tuple'>

res = set()
print(res,type(res))  #set() <class 'set'>






















































