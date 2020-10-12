# ### 容器类型的强制转换(str list tuple set dict)

# 01 str 强制转换成字符串
# """所有的数据类型都可以转换, 在当前的数据类型两边套上引号"""
var1 = "我爱你,文哥哥"
var2 = [1,2,3]
var3 = (4,4,5)
var4 = {"陈璐","上朝气","刘子涛","合理"}
var5 = {"cl":"文质彬彬,斯文败类","szq":"学霸","lzt":"篮球少年","hl":"武大高手"}
var6 = 90
var7 = True

res = str(var2)
print(res,type(res))  #[1, 2, 3] <class 'str'>
## repr 不转移字符原型化输出字符串
print(repr(res))  #'[1, 2, 3]'
print('-------------------1 str')


# 02 list 强制转换成列表
# """
# 如果是字符串:把字符串中的每个元素单独拿出来,作为列表中的新元素
# 如果是字典:  只保留字典中的键
# 如果是其他容器数据:就是单纯的在原数据类型德两边换上[]括号
# 只能是容器间互转
# """
var1 = "我爱你,文哥哥"
var2 = [1,2,3]
var3 = (4,4,5)
var4 = {"陈璐","上朝气","刘子涛","合理"}
var5 = {"cl":"文质彬彬,斯文败类","szq":"学霸","lzt":"篮球少年","hl":"武大高手"}
var6 = 90
var7 = True

res = list(var1)
print(res) #['我', '爱', '你', ',', '文', '哥', '哥']

res = list(var5)
# 字典: 只获取字典得键,忽略掉值
print(res) #['cl', 'szq', 'lzt', 'hl']

# res = list(var6)  #error 只能是容器间的互转
# print(res)  #TypeError: 'int' object is not iterable
print('-------------------2 list')

# 03 tuple 强制转换成元组
# """
# 如果是字符串:把字符串中的每个元素单独拿出来,作为元组中的新元素
# 如果是字典:  只保留字典中的键
# 如果是其他容器数据:就是单纯的在原数据类型得两边换上()括号
# """
var1 = "我爱你,文哥哥"
var2 = [1,2,3]
var3 = (4,4,5)
var4 = {"陈璐","上朝气","刘子涛","合理"}
var5 = {"cl":"文质彬彬,斯文败类","szq":"学霸","lzt":"篮球少年","hl":"武大高手"}
var6 = 90
var7 = True

res = tuple(var1)
print(res) #('我', '爱', '你', ',', '文', '哥', '哥')

# 字典: 只获取字典得键,忽略掉值
res = tuple(var5)
print(res) #('cl', 'szq', 'lzt', 'hl')

res = tuple(var2)
print(res) #(1, 2, 3)
print('------------------ 3 tuple')


# 04 set 强制转换成集合  无序 去重
# """
# 如果是字符串:把字符串中的每个元素单独拿出来,作为集合中的新元素
# 如果是字典:  只保留字典中的键
# 如果是其他容器数据:就是单纯的在原数据类型得两边换上{}括号
# """
var1 = "我爱你,文哥哥"
var2 = [1,2,3]
var3 = (4,4,5)
var4 = {"陈璐","上朝气","刘子涛","合理"}
var5 = {"cl":"文质彬彬,斯文败类","szq":"学霸","lzt":"篮球少年","hl":"武大高手"}
var6 = 90
var7 = True

res = set(var1)
print(res)
#{'我', ',', '你', '文', '哥', '爱'}

res = set(var5)
print(res)
#{'cl', 'szq', 'hl', 'lzt'}
print('------------------ 4 set')

# 05 多滤掉列表中所有重复元素;
lst = [1,222,3,3,3,44,88,999,77,88,1]
# 方法1
setvar = set(lst)
print(setvar)  #{1, 3, 999, 44, 77, 88, 222}
lst_new = list(setvar)
print(lst_new) #[1, 3, 999, 44, 77, 88, 222]  #没有考虑列表元素顺序的问题
print('------------------ 5-1')

lst_new = []
for i in lst:
	if lst.count(i) == 1:
		lst_new.append(i)
print(lst_new)
#[222, 44, 999, 77]  #只添加了出现一只的元素
print('------------------ 5-2')

# 方法2  推荐
lst_new = []
for i in lst:
	if i not in lst_new:
		lst_new.append(i)
print(lst_new)
# [1, 222, 3, 44, 88, 999, 77]
print('------------------ 5-3')

# 06 默认不加任何值,转换成该数据类型的空值
# str() list()  tuple()  set()  dict()

print(str())  #空字符串显示空白
print(repr(str())) #''
print(tuple())
print(list())
print(dict())
print(set())

# ()
# []
# {}
# set()














































