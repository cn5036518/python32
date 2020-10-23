# ### 集合推导式
# """
# 案例:
	# 满足年龄在18到21,存款大于等于5000 小于等于5500的人,
	# 开卡格式为:尊贵VIP卡老x(姓氏),否则开卡格式为:抠脚大汉卡老x(姓氏)	
	# 把开卡的种类统计出来
# """
lst = [
    {"name":"赵沈阳","age":18,"money":3000},
    {"name":"赵万里","age":19,"money":5200},
    {"name":"赵蜂拥","age":20,"money":100000},
    {"name":"赵世超","age":21,"money":1000},
    {"name":"王志国","age":18,"money":5500},
    {"name":"王永飞","age":99,"money":5500}
]

setvar = set()  #无序,去重
for i in lst:
	if i['age'] >=18 and i['age'] <=21 and i['money'] >= 5000 and i['money'] <=5500:
		res = '尊贵VIP卡老{}(姓氏)'.format(i['name'][0])
	else:
		res = '抠脚大汉卡老{}(姓氏)'.format(i['name'][0])
	setvar.add(res)
print(setvar)
#{'尊贵VIP卡老赵(姓氏)', '抠脚大汉卡老赵(姓氏)', '尊贵VIP卡老王(姓氏)', '抠脚大汉卡老王(姓氏)'}

# { 三元运算符 + 推导式 }
setvar = {'尊贵VIP卡老{}(姓氏)'.format(i['name'][0]) if i['age'] >=18 and i['age'] <=21 and i['money'] >= 5000 and i['money'] <=5500 else '抠脚大汉卡老{}(姓氏)'.format(i['name'][0]) for i in lst}
print(setvar)
# {'尊贵VIP卡老赵(姓氏)', '抠脚大汉卡老王(姓氏)', '抠脚大汉卡老赵(姓氏)', '尊贵VIP卡老王(姓氏)'}
print('----------------------0 集合推导式')

# ### 字典推导式
### 一.enumerate
# enumerate(iterable,[start=0])
# 参数:iterable
# 返回值:迭代器

lst =["王文","吕洞宾","何仙姑","铁拐李","张国老","曹国舅","蓝采和","韩湘子"]
it = enumerate(lst,start=100)
print(list(it))
#[(100, '王文'), (101, '吕洞宾'), (102, '何仙姑'), (103, '铁拐李'), (104, '张国老'), (105, '曹国舅'), (106, '蓝采和'), (107, '韩湘子')]

#方法1  --推荐 简洁
it = enumerate(lst,start=100)
print(dict(it))
#{100: '王文', 101: '吕洞宾', 102: '何仙姑', 103: '铁拐李', 104: '张国老', 105: '曹国舅', 106: '蓝采和', 107: '韩湘子'}

#方法2
dic = {k:v for k,v in enumerate(lst,start=100)}
print(dic)
#{100: '王文', 101: '吕洞宾', 102: '何仙姑', 103: '铁拐李', 104: '张国老', 105: '曹国舅', 106: '蓝采和', 107: '韩湘子'}
print('----------------------1 enumerate')

### 二.zip
# zip(iterable, ... ...)
# 参数:  iterable: 可迭代性数据 (常用:容器类型数据,range对象,迭代器) 
# 返回值:迭代器

lst1 = ["孙开启","王永飞","于朝志"]
lst2 = ["薛宇健","韩瑞晓","上朝气"]
lst3 = ["刘文博","历史园","张光旭"]

it = zip(lst1,lst2,lst3)
print(list(it))
#[('孙开启', '薛宇健', '刘文博'), ('王永飞', '韩瑞晓', '历史园'), ('于朝志', '上朝气', '张光旭')]

# (1) 字典推导式 配合 zip 来实现
lst_key = ["ww","axd","yyt"]
lst_val = ["王维","安晓东","杨元涛"]

it = zip(lst_key,lst_val)
print(list(it))  #[('ww', '王维'), ('axd', '安晓东'), ('yyt', '杨元涛')]

# 方法1 推荐 简洁
it = zip(lst_key,lst_val)
print(dict(it))
#{'ww': '王维', 'axd': '安晓东', 'yyt': '杨元涛'}

# 方法2 
# 字典推导式
dic = {k:v for k,v in zip(lst_key,lst_val)}
print(dic)
#{'ww': '王维', 'axd': '安晓东', 'yyt': '杨元涛'}

print('----------------------2 zip')


























