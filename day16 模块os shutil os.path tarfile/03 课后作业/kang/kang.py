import json
import time
import copy

user_money = int(input("充值吧,大哥>>>"))
print("恭喜您,成功充值{:d}元人民币".format(user_money))
print("加载商品中...")


def myprocess(percent):
	if percent > 1:
		percent = 1
	strvar = int(percent * 50) * '#'
	print("\r[%-50s] %d%%" % (strvar, percent * 100), end="")


recv_size = 0
total_size = 1000
while recv_size < total_size:
	time.sleep(0)
	recv_size += 10
	percent = recv_size / total_size
	myprocess(percent)
print("""\n[===========有如下商品供您选择：===========]
序号     名称       价格
1 		 电脑		1999
2 		 鼠标		10
3 		 游艇		20
4 		 美女		998
5       风油精		30""")
li_product = []
with open("shopping_data.json", mode="r", encoding="utf-8") as fp1:
	for line in fp1:
		dic = json.loads(line)
		li_product.append(dic)
my_product_list = []
li_product = []
with open("shopping_data.json", mode="r", encoding="utf-8") as fp1:
	for line in fp1:
		dic = json.loads(line)
		li_product.append(dic)
my_product_list = []


def add_product():
	dic = {}
	li = []
	while True:
		cho_product = input("请输入您要购买的商品编号:")
		if cho_product == "q" or cho_product == "Q":
			print("程序已退出!感谢您的使用!")
			break
		elif int(cho_product) > 5 or int(cho_product) < 1:
			print("商品不存在")
		else:
			res = li_product[int(cho_product) - 1]
			dic['name'] = res['name']
			dic['price'] = res['price']
			dic['amount'] = 1
			dic['total'] = res['price'] * dic['amount']
			li.append(copy.deepcopy(dic))
		amount = li.count(dic)
		print("""****************************
	您选择的商品具体信息:
	*- 商品名称:{}
	*- 商品单价:{}
	*- 商品数量:{}
	已成功添加到购物车,请您继续购物
	****************************""".format(dic['name'], dic['price'], amount))


add_product()
