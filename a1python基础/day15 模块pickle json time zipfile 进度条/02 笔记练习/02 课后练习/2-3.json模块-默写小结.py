# ### json 序列化/反序列化模块
import json
# """
# json格式的数据,所有的编程语言都能识别,本身是字符串
# 类型有要求: int float bool str list tuple dict None  没有set和complex

# json   主要应用于传输数据 , 序列化成字符串
# pickle 主要应用于存储数据 , 序列化成二进制字节流
# """

# json 基本用法
# json =>  dumps 和 loads

# 1 dumps   
#其他数据类型==>str
# """ensure_ascii=False 显示中文 sort_keys=True 按键排序"""
dic = {"name":"梁新宇","sex":"野味","age":22}
res = json.dumps(dic)
print(res,type(res))
#{"name": "\u6881\u65b0\u5b87", "sex": "\u91ce\u5473", "age": 22} <class 'str'>

dic = {"name":"梁新宇","sex":"野味","age":22}
res = json.dumps(dic,ensure_ascii=False) #ensure_ascii=False 显示中文 
print(res,type(res))
#{"name": "梁新宇", "sex": "野味", "age": 22} <class 'str'>

dic = {"name":"梁新宇","sex":"野味","age":22}
res = json.dumps(dic,ensure_ascii=False,sort_keys=True)  #sort_keys=True 按键排序
print(res,type(res))
#{"age": 22, "name": "梁新宇", "sex": "野味"} <class 'str'>

# 2 loads 
#str==>其他数据类型 还原
dic = json.loads(res)
print(dic,type(dic))
#{'age': 22, 'name': '梁新宇', 'sex': '野味'} <class 'dict'>
print('--------------------------1 dumps loads')


# json => dump 和 load
# 3 dump
# 其他数据类型==>str 写入到文件对象
with open('lianxi32.txt','w',encoding='utf-8') as fp:
	json.dump(dic,fp)  #文件中的中文乱码

with open('lianxi33.txt','w',encoding='utf-8') as fp:
	json.dump(dic,fp,ensure_ascii=False)  #文件中的中文正常显示  #注意:3个参数
	
# 4 load
# 从文件对读取str==>其他数据类型
with open('lianxi33.txt','r',encoding='utf-8') as fp:
	dic = json.load(fp)
print(dic,type(dic))
#{'age': 22, 'name': '梁新宇', 'sex': '野味'} <class 'dict'>
print('--------------------------2 dump load')

# ### json 和 pickle 之间的区别
# 1.json
# json 连续dump数据 , 但是不能连续load数据  , 是一次性获取所有内容进行反序列化.
dic1 = {"a":1,"b":2}
dic2 = {"c":3,"d":4}
with open('lianxi42.json',mode='w',encoding='utf-8') as fp:
	json.dump(dic1,fp)
	fp.write('\n')
	json.dump(dic2,fp)
	fp.write('\n')

# 不能连续load,是一次性获取所有数据 , error
# with open('lianxi42.json',mode='r',encoding='utf-8') as fp:
	# json.load(fp) #error
	#json.decoder.JSONDecodeError: Extra data: line 2 column 1 (char 17)

# 解决办法 loads(分开读取)
with open('lianxi42.json',mode='r',encoding='utf-8') as fp:
	# json.loads(fp) #error
 #TypeError: the JSON object must be str, bytes or bytearray, not 'TextIOWrapper'
	for i in fp:
		# print(i,type(i))
		# {"a": 1, "b": 2}
 # <class 'str'>
# {"c": 3, "d": 4}
 # <class 'str'>
		dic = json.loads(i)
		print(dic,type(dic))
# {'a': 1, 'b': 2} <class 'dict'>
# {'c': 3, 'd': 4} <class 'dict'>


# 2.pickle
import pickle
# pickle => dump 和 load   字节流bytes
# pickle 连续dump数据,也可以连续load数据
dic1 = {"a":1,"b":2}
dic2 = {"c":3,"d":4}
# 写入bytes到文件 dump
with open('lianxi53.txt','wb') as fp:
	pickle.dump(dic1,fp)
	pickle.dump(dic2,fp)
	pickle.dump(dic1,fp)
	pickle.dump(dic2,fp)

# 方法1  dump4次,就load4次
# 从文件读取bytes后,还原成原数据
with open('lianxi53.txt','rb') as fp:
	dic1 = pickle.load(fp)
	dic2 = pickle.load(fp)
print(dic1,type(dic1))
print(dic2)
# {'a': 1, 'b': 2}
# {'c': 3, 'd': 4}
print('---------------------1 单个load')

# 方法2  dump4次,load4次--for
# 从文件读取bytes后,还原成原数据
lst = []
with open('lianxi53.txt','rb') as fp:
	for i in range(4):
		dic = pickle.load(fp)
		lst.append(dic)
print(lst)
#[{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4}]

print('---------------------2 for load')

with open('lianxi53.txt','rb') as fp:
	for i in range(4):
		dic = pickle.load(fp)
		print(dic)

print('---------------------2-2 for load')

# 方法3 (扩展)
# """try .. except .. 把又可能报错的代码放到try代码块中,
# 如果出现异常执行except分支,来抑制报错"""
# 一次性拿出所有load出来的文件数据
try:
	with open('lianxi53.txt','rb') as fp:
		while True:  #死循环
			dic = pickle.load(fp)
			print(dic)
			# EOFError: Ran out of input   #如果不加try			
except:
	pass
print('---------------------3 while load')


# 小结默写
# dumps
	# 其他数据类型==>str   6大标准数据类型(除了set complex)  类型有要求: int float bool str list tuple dict None
import json
dic = {'name':'jack','age':19}
strvar = json.dumps(dic)
print(strvar,type(strvar))
#{"name": "jack", "age": 19} <class 'str'>

dic = {'name':'小强','age':19}
strvar = json.dumps(dic,ensure_ascii=False)
print(strvar,type(strvar))
# {"name": "小强", "age": 19} <class 'str'>

dic = {'name':'小强','age':19}
strvar = json.dumps(dic,ensure_ascii=False,sort_keys=True)
print(strvar,type(strvar))
#{"age": 19, "name": "小强"} <class 'str'>
print('---------------------1 json.dumps')

# loads
	# str==>其他数据类型
dic = json.loads(strvar)
print(dic,type(dic))
#{'age': 19, 'name': '小强'} <class 'dict'>
print('---------------------2 json.loads')

# dump
	# 其他数据类型==>str==>写入文件
dic = {'name':'小强','age':12}
with open('moxie23.txt',mode='w',encoding='utf-8') as fp:
	strvar = json.dump(dic,fp)
	print(strvar)  #None
	# {"name": "\u5c0f\u5f3a", "age": 12}  文件的内容
	
dic = {'name':'小强','age':12}
with open('moxie24.txt',mode='w',encoding='utf-8') as fp:
	strvar = json.dump(dic,fp,ensure_ascii=False)
	print(strvar)  #None
	# {"name": "小强", "age": 12}  文件的内容
	
dic = {'name':'小强','age':12}
with open('moxie25.txt',mode='w',encoding='utf-8') as fp:
	strvar = json.dump(dic,fp,ensure_ascii=False,sort_keys=True)
	print(strvar)  #None
	# {"age": 12, "name": "小强"}  文件的内容
print('---------------------3 json.dump')

# load
	# 文件读取str==>其他数据类型
with open('moxie25.txt',mode='r',encoding='utf-8') as fp:
	dic = json.load(fp)
	print(dic,type(dic))
#{'age': 12, 'name': '小强'} <class 'dict'>














































