

# ### json 序列化/反序列化模块
import json

# 1 dumps  其他类型==>字符串
dic = {"name":"梁新宇","sex":"野味","age":22}
res = json.dumps(dic)
print(res,type(res))
# {"name": "\u6881\u65b0\u5b87", "sex": "\u91ce\u5473", "age": 22} <class 'str'>

res = json.dumps(dic,ensure_ascii= False)
print(res,type(res))
# {"name": "梁新宇", "sex": "野味", "age": 22} <class 'str'>

# res = json.dumps(dic,ensure_ascii= False,sort_keys= True)
# print(res,type(res))
#{"age": 22, "name": "梁新宇", "sex": "野味"} <class 'str'>

# 2 loads  字符串==>其他类型
dic = json.loads(res)
print(dic,type(dic))
# {'age': 22, 'name': '梁新宇', 'sex': '野味'} <class 'dict'>
print('--------------------------2')

# 3 dump  把其他类型数据变成字符串后,写入到文件
dic = {"name":"梁新宇","sex":"野味","age":22}
with open('lianxi31.json',mode='w',encoding='utf-8') as fp:
	json.dump(dic,fp,ensure_ascii=False)

# 4 load 把文件中的字符串读取出来或是,变成原来的数据类型
with open('lianxi31.json',mode='r',encoding='utf-8') as fp:
	dic = json.load(fp)
print(dic,type(dic))
# {'name': '梁新宇', 'sex': '野味', 'age': 22} <class 'dict'>


#1 json如何连续load数据?
dic1 = {"a":1,"b":2}
dic2 = {"c":3,"d":4}
with open("lianxi41.json",mode="w",encoding="utf-8") as fp:
	json.dump(dic1,fp)
	fp.write('\n')
	json.dump(dic2,fp)

# with open("lianxi41.json",mode="r",encoding="utf-8") as fp:
	# dic = json.load(fp)
	# 不能连续load,是一次性获取所有数据 , error
# json.decoder.JSONDecodeError: Extra data: line 1 column 17 (char 16)

# 解决办法 loads(分开读取)
with open("lianxi41.json",mode="r",encoding="utf-8") as fp:
	for i in fp:
		# print(i,type(i))
		dic = json.loads(i)  #把字符串转成字典
		print(dic,type(dic))
# {'a': 1, 'b': 2} <class 'dict'>
# {'c': 3, 'd': 4} <class 'dict'>

#2 pickle如何一次load所有数据?
import pickle
dic1 = {"a":1,"b":2}
dic2 = {"c":3,"d":4}
with open("lianxi51.pkl",mode="wb") as fp:
	pickle.dump(dic1,fp)
	pickle.dump(dic2,fp)
	pickle.dump(dic1,fp)
	pickle.dump(dic2,fp)

#方法1
with open("lianxi5.pkl",mode="rb") as fp:
	dic1 = pickle.load(fp)
	dic2 = pickle.load(fp)
	print(dic1)
	print(dic2)
# {'a': 1, 'b': 2}
# {'c': 3, 'd': 4}
print('-----------------------------2-1')

#方法2 
# 一次性拿出所有load出来的文件数据
try:
	with open("lianxi5.pkl",mode="rb") as fp:
		while True:
			dic = pickle.load(fp)
			print(dic)
			# EOFError: Ran out of input
except:
	pass



# 小结:
# 1 dumps  其他类型==>字符串
dic = {"name":"梁新宇","sex":"野味","age":22}
res = json.dumps(dic,ensure_ascii= False,sort_keys= True)
print(res,type(res))
{"age": 22, "name": "梁新宇", "sex": "野味"} <class 'str'>

# 2 loads  字符串==>其他类型
dic = json.loads(res)
print(dic,type(dic))
# {'age': 22, 'name': '梁新宇', 'sex': '野味'} <class 'dict'>
print('--------------------------2')

# 3 dump  把其他类型数据变成字符串后,写入到文件
dic = {"name":"梁新宇","sex":"野味","age":22}
with open('lianxi31.json',mode='w',encoding='utf-8') as fp:
	json.dump(dic,fp,ensure_ascii=False)

# 4 load 把文件中的字符串读取出来或是,变成原来的数据类型
with open('lianxi31.json',mode='r',encoding='utf-8') as fp:
	dic = json.load(fp)
print(dic,type(dic))
# {'name': '梁新宇', 'sex': '野味', 'age': 22} <class 'dict'>








































