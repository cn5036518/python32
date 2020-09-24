# 1.用map来处理字符串列表,把列表中所有人都变成 leader ,比方alex_leader
name = ['oldboy', 'alex', 'wusir']

# 2.用map来处理下述 listvar ,要求得到新列表,每个元素名字加后面加_leader
listvar = [{'name':'alex'},{'name':'wusir'}]

# 3.用filter来处理,得到股票价格大于20的股票名字
shares={
   	'IBM':36.6,
   	'Lenovo':23.2,
  	'oldboy':21.2,
        'ocean':10.2,
	}

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