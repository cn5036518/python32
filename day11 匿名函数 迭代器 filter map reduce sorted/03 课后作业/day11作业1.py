# 1.用map来处理字符串列表,把列表中所有人都变成 leader ,比方alex_leader
name = ['oldboy', 'alex', 'wusir']

# 方法1 map
def func(strvar):
	return strvar+'_leader'

it = map(func,name)
print(list(it))  #['oldboy_leader', 'alex_leader', 'wusir_leader']
print('-------------------------1-1')

# 方法2 map  lambda
it = map(lambda strvar:strvar + '_leader',name)
print(list(it))
print('-------------------------1-2')

# 2.用map来处理下述 listvar ,要求得到新列表,每个元素名字加后面加_leader
listvar = [{'name':'alex'},{'name':'wusir'}]

# 普通方法
li = []
for i in listvar:
	dic = {}
	dic['name'] = i['name'] + '_leader'
	li.append(dic)
print(li)  #[{'name': 'alex_leader'}, {'name': 'wusir_leader'}]
print('-------------------------2-1')

# map改写
listvar = [{'name':'alex'},{'name':'wusir'}]
def func(dic):  #这里需要一个形参
	dic['name']  += '_leader'
	return dic  #形参的dic和return的dic同样都是dic. 但是内容已经变了

it = map(func,listvar)
print(list(it))
print('-------------------------2-2')


# 3.用filter来处理,得到股票价格大于20的股票名字
shares={
   	'IBM':36.6,
   	'Lenovo':23.2,
  	'oldboy':21.2,
        'ocean':10.2,
	}
	
# 普通方法
li = []
for k,v in shares.items():
	if v > 20:
		li.append((k,v))
print(li)  #[('IBM', 36.6), ('Lenovo', 23.2), ('oldboy', 21.2)]
print('---------------------------------3-1')

# filter
def func(k):
	if shares[k]>20:
		return True
	else:
		return False
	
it = filter(func,shares)
print(list(it))
print('---------------------------------3-2')

# filter lambda
it = filter(lambda k: True if shares[k] > 20 else False,shares)
print(list(it))  #['IBM', 'Lenovo', 'oldboy']
print('---------------------------------3-3')


# 4.有下面字典:
portfolio=[
	{'name':'IBM','shares':100,'price':91.1},
	{'name':'AAPL','shares':20,'price':54.0},
	{'name':'FB','shares':200,'price':21.09},
	{'name':'HPQ','shares':35,'price':31.75},
	{'name':'YHOO','shares':45,'price':16.35},
	{'name':'ACME','shares':75,'price':115.65}
]
# a.获取购买每只股票的总价格(乘积),迭代器中[9110.0, 1080.0 ,......]
# b.用filter过滤出price大于100的股票。

# a  普通方法
li = []
for i in portfolio:
	total = i['price'] * i['shares'] 
	li.append(total)
print(li)  #[9110.0, 1080.0, 4218.0, 1111.25, 735.7500000000001, 8673.75]
print('---------------------------------4-1-1')


# a  map方法
def func(dic):
	return dic['price'] * dic['shares']
	
it = map(func,portfolio)
print(list(it))
print('---------------------------------4-1-2')

# a  map方法 lambda
it = map(lambda dic:dic['price'] * dic['shares'],portfolio)
print(list(it))
print('---------------------------------4-1-3')


# b  普通方法
li = []
for i in portfolio:
	if i['price'] > 100:
		# print(i['name'])
		li.append(i['name'])
print(li)  #['ACME']
print('---------------------------------4-2-1')

# b  filter 方法
def func(dic):
	if dic['price'] > 100:
		return True
	else:
		return False
	
it = filter(func,portfolio)
print(list(it))  #[{'name': 'ACME', 'shares': 75, 'price': 115.65}]
print('---------------------------------4-2-2')

# b  filter lambda

it = filter(lambda dic:True if dic['price']>100 else False,portfolio)
print(list(it))  #[{'name': 'ACME', 'shares': 75, 'price': 115.65}]
print('---------------------------------4-2-3')


# 5.将listvar 按照列表中的每个字典的values大小进行排序,形成一个新的列表。
listvar = [
	{'sales_volumn': 0},
	{'sales_volumn': 108},
	{'sales_volumn': 337},
	{'sales_volumn': 475},
	{'sales_volumn': 396},
	{'sales_volumn': 172},
	{'sales_volumn': 9},
	{'sales_volumn': 58},
	{'sales_volumn': 272},
	{'sales_volumn': 456},
	{'sales_volumn': 440},
	{'sales_volumn': 239}
]

#1 普通方法

#2  sorted
def func(dic):
	return dic['sales_volumn']
	
lst = sorted(listvar,key=func)
print(lst)
#[{'sales_volumn': 0}, {'sales_volumn': 9}, {'sales_volumn': 58},
 # {'sales_volumn': 108}, {'sales_volumn': 172}, {'sales_volumn': 239},
 # {'sales_volumn': 272}, {'sales_volumn': 337}, {'sales_volumn': 396},
 # {'sales_volumn': 440}, {'sales_volumn': 456}, {'sales_volumn': 475}]

#3 sorted lambda
lst = sorted(listvar,key=lambda dic:dic['sales_volumn'])
print(lst)
































