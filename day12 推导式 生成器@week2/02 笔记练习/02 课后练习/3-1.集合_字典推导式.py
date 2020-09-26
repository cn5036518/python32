# ### 集合推导式  去重无序
# 案例:
	# 满足年龄在18到21,存款大于等于5000 小于等于5500的人,
	# 开卡格式为:尊贵VIP卡老x(姓氏),否则开卡格式为:抠脚大汉卡老x(姓氏)	
	# 把开卡的种类统计出来
lst = [
    {"name":"赵沈阳","age":18,"money":3000},
    {"name":"赵万里","age":19,"money":5200},
    {"name":"赵蜂拥","age":20,"money":100000},
    {"name":"赵世超","age":21,"money":1000},
    {"name":"王志国","age":18,"money":5500},
    {"name":"王永飞","age":99,"money":5500}
]
setvar = set()
for i in lst:
	print(i) # # {'name': '赵沈阳', 'age': 18, 'money': 3000}
	if 18 <= i['age'] <=21 and 5000 <= i['money'] <= 5500:
		res = '尊贵VIP卡老{}'.format(i['name'][0])
	else:
		res = '抠脚大汉卡老{}'.format(i['name'][0])
	#添加到集合中
	setvar.add(res)
print(setvar)  
#{'尊贵VIP卡老赵', '抠脚大汉卡老赵', '抠脚大汉卡老王', '尊贵VIP卡老王'}

# {三元运算符 + 推导式}
setvar = {'尊贵VIP卡老{}'.format(i['name'][0]) 
if 18 <= i['age'] <=21 and 5000 <= i['money'] <= 5500
else '抠脚大汉卡老{}'.format(i['name'][0]) for i in lst}
print(setvar)  #{'尊贵VIP卡老赵', '抠脚大汉卡老王', '尊贵VIP卡老王', '抠脚大汉卡老赵'}

# ### 字典推导式
### 一.enumerate
# enumerate(iterable,[start=0])
# 功能:
# 参数:
	# iterable:
	# start:
# 返回值:迭代器

# 基本语法
# from collections import Iterator,Iterable  #py3.6
from collections.abc import Iterator  #py3.7及其以上
lst =["王文","吕洞宾","何仙姑","铁拐李","张国老","曹国舅","蓝采和","韩湘子"]
it = enumerate(lst)
# it = enumerate(lst,start = 100)  #(100, '王文')
# it = enumerate(lst,200)  #(200, '王文')
print(isinstance(it,Iterator))  #True

# next
print(next(it))  #(0, '王文')

# for  next (推荐,数据较大时使用)
for i in range(3):
	print(next(it))
# (1, '吕洞宾')
# (2, '何仙姑')
# (3, '铁拐李')

# for
for i in it:
	print(i)

# list 强转迭代器
it = enumerate(lst)
print(list(it))
# [(0, '王文'), (1, '吕洞宾'), (2, '何仙姑'), (3, '铁拐李'),
 # (4, '张国老'), (5, '曹国舅'), (6, '蓝采和'), (7, '韩湘子')]

# 1 字典推导式  配合 enumerate来实现
lst =["王文","吕洞宾","何仙姑","铁拐李","张国老","曹国舅","蓝采和","韩湘子"]
dic = {k:v for k,v in enumerate(lst,start= 100)}
print(dic)
# {100: '王文', 101: '吕洞宾', 102: '何仙姑', 103: '铁拐李', 
# 104: '张国老', 105: '曹国舅', 106: '蓝采和', 107: '韩湘子'}

# 2 使用dict强转迭代器(enumerate),瞬间得到字典
dic = dict(enumerate(lst,start=100))
print(dic) #{100: '王文', 101: '吕洞宾', 102: '何仙姑', 103: '铁拐李', 104: '张国老', 
# 105: '曹国舅', 106: '蓝采和', 107: '韩湘子'}

### 二.zip
# 特点:按照索引配对
# zip(iterable,...)
# 返回:迭代器

# 基本语法
lst1 = ["孙开启","王永飞","于朝志"]
lst2 = ["薛宇健","韩瑞晓","上朝气"]
lst3 = ["刘文博","历史园","张光旭"]

it = zip(lst1,lst2,lst3)
print(list(it))
#[('孙开启', '薛宇健', '刘文博'),
 # ('王永飞', '韩瑞晓', '历史园'), ('于朝志', '上朝气', '张光旭')]

# 在索引下标同时存在时,才会进行配对,否则舍弃
lst1 = ["孙开启","王永飞","于朝志"]
lst2 = ["薛宇健","韩瑞晓"]
lst3 = ["刘文博"]
it = zip(lst1,lst2,lst3)
print(list(it))  #[('孙开启', '薛宇健', '刘文博')]

# 1 字典推导式 配合 zip 来实现
lst_key = ["ww","axd","yyt"]
lst_val = ["王维","安晓东","杨元涛"]

it = zip(lst_key,lst_val)
print(list(it))  #[('ww', '王维'), ('axd', '安晓东'), ('yyt', '杨元涛')]

dic = {k:v for k,v in zip(lst_key,lst_val)}
print(dic)  #{'ww': '王维', 'axd': '安晓东', 'yyt': '杨元涛'}

# 2 使用dict强转迭代器,瞬间得到字典  推荐
dic = dict(zip(lst_key,lst_val))
print(dic)  #{'ww': '王维', 'axd': '安晓东', 'yyt': '杨元涛'}

























