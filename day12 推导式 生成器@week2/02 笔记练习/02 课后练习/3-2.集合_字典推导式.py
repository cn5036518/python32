# ### 集合推导式  #无序去重

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

# 普通写法
setvar = set()
for dic in lst:
	# print(dic)
	# {'name': '赵沈阳', 'age': 18, 'money': 3000}
	if dic['age'] >= 18 and dic['age'] <= 21 and dic['money'] >= 5000 and dic['money'] <= 5500:
		# print('尊贵VIP卡老{:s}(姓氏)'.format(dic['name'][0]))
		res = '尊贵VIP卡老{:s}(姓氏)'.format(dic['name'][0])
	else:
		# print('抠脚大汉卡老{:s}(姓氏)'.format(dic['name'][0]))
		res = '抠脚大汉卡老{:s}(姓氏)'.format(dic['name'][0])
	setvar.add(res)
print(setvar)

# 集合推导式
# {三元运算符+ 推导式}

# 了解
listvar = ['尊贵VIP卡老{:s}(姓氏)'.format(dic['name'][0])
if dic['age'] >= 18 and dic['age'] <= 21 and dic['money'] >= 5000 and dic['money'] <= 5500 
else '抠脚大汉卡老{:s}(姓氏)'.format(dic['name'][0])
  for dic in lst]
print(listvar)
#['抠脚大汉卡老赵(姓氏)', '尊贵VIP卡老赵(姓氏)', '抠脚大汉卡老赵(姓氏)', '抠脚大汉卡老赵(姓氏)', '尊贵VIP卡老王(姓氏)', '抠脚大汉卡老王(姓氏)']

# 集合推导式
setvar = {'尊贵VIP卡老{:s}(姓氏)'.format(dic['name'][0])
if dic['age'] >= 18 and dic['age'] <= 21 and dic['money'] >= 5000 and dic['money'] <= 5500
else '抠脚大汉卡老{:s}(姓氏)'.format(dic['name'][0])
  for dic in lst}
print(setvar)
#{'抠脚大汉卡老王(姓氏)', '抠脚大汉卡老赵(姓氏)', '尊贵VIP卡老赵(姓氏)', '尊贵VIP卡老王(姓氏)'}

# ### 字典推导式
# 一 enumerate

from collections import Iterator

lst =["王文","吕洞宾","何仙姑","铁拐李","张国老","曹国舅","蓝采和","韩湘子"]
# it = enumerate(lst)
it = enumerate(lst,100)
res = isinstance(it,Iterator)
print(res)  #True

# print(list(it))
#[(0, '王文'), (1, '吕洞宾'), (2, '何仙姑'), (3, '铁拐李'),
 # (4, '张国老'), (5, '曹国舅'), (6, '蓝采和'), (7, '韩湘子')]
 
print(dict(it))  #{100: '王文', 101: '吕洞宾', 102: '何仙姑', 103: '铁拐李', 
# 104: '张国老', 105: '曹国舅', 106: '蓝采和', 107: '韩湘子'}

# 字典推导式 配合 enumerate 来实现
it = enumerate(lst,100)
dic = {k:v for k,v in it}
print(dic)
# {100: '王文', 101: '吕洞宾', 102: '何仙姑',
 # 103: '铁拐李', 104: '张国老', 105: '曹国舅', 106: '蓝采和', 107: '韩湘子'}

### 二 zip
# 基本语法
lst1 = ["孙开启","王永飞","于朝志"]
lst2 = ["薛宇健","韩瑞晓","上朝气"]
# lst3 = ["刘文博","历史园","张光旭"]

# it = zip(lst1,lst2,lst3)
it = zip(lst1,lst2)
# print(list(it)) 
# [('孙开启', '薛宇健', '刘文博'), ('王永飞', '韩瑞晓', '历史园'), ('于朝志', '上朝气', '张光旭')]

print(dict(it))
# {'孙开启': '薛宇健', '王永飞': '韩瑞晓', '于朝志': '上朝气'}

# 字典推导式 配合  zip来实现
lst_key = ["ww","axd","yyt"]
lst_val = ["王维","安晓东","杨元涛"]
it = zip(lst_key,lst_val)

dic = {k:v for k,v in it }
print(dic)  
# {'ww': '王维', 'axd': '安晓东', 'yyt': '杨元涛'}


















