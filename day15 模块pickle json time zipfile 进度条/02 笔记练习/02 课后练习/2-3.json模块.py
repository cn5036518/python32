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






































