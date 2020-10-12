# ### json 序列化/反序列化模块
import json
# json格式的数据.所有的编程语言都能识别,本身是字符串
# 类型有要求:  8种
# 	int float bool str tuple list dict None
# 不包含 complex set(因为其他语言没有)
#
# json   主要应用于传输数据,序列化成字符串
# pickle 主要应用于存储数据,序列化成二进制字节流


# json 基本用法
# json  ==> dumps 和 loads
# ensure_ascii= Fasle  显示中文   sort_keys= True 按键排序
dic = {"name":"梁新宇","sex":"野味","age":22,"family":["爸爸","妈妈","姐姐"]}
res = json.dumps(dic,ensure_ascii= False,sort_keys= True)
print(res , type(res))
# {"age": 22, "family": ["爸爸", "妈妈", "姐姐"], "name": "梁新宇", "sex": "野味"} <class 'str'>

dic = json.loads(res)
print(dic , type(dic))
# {'age': 22, 'family': ['爸爸', '妈妈', '姐姐'], 'name': '梁新宇', 'sex': '野味'} <class 'dict'>


# json ==> dump 和load
with open("lianxi3.json",mode="w",encoding="utf-8") as fp:
	json.dump(dic,fp,ensure_ascii=False)
with open("lianxi3.json",mode="r",encoding="utf-8") as fp:
	dic = json.load(fp)
print(dic , type(dic))
# {'age': 22, 'family': ['爸爸', '妈妈', '姐姐'], 'name': '梁新宇', 'sex': '野味'} <class 'dict'>

# ### json和pickle之间的区别
#1.json
# json 连续dump数据,但是不能连续load数据,是一次性获取所有内容
# 进行反序列化
dic1 = {"a":1,"b":2}
dic2 = {"c":3,"d":4}
with open("lianxi4.json",mode="w",encoding="utf-8") as fp:
	json.dump(dic1,fp)
	fp.write('\n')
	json.dump(dic2,fp)
	fp.write('\n')
print('-------------------1')

# 不能连续load,是一次性获取所有数据,error
# with open("lianxi4.json",mode="r",encoding="utf-8") as fp:
	# dic = json.load(fp)
	# print(dic)
	# json.decoder.JSONDecodeError: Extra data: line 2 column 1 (char 17)

# 解决办法 loads
with open("lianxi4.json",mode="r",encoding="utf-8") as fp:
	for line in fp:
		dic = json.loads(line)
		print(dic,type(dic))
# {'a': 1, 'b': 2} <class 'dict'>
# {'c': 3, 'd': 4} <class 'dict'>
print('-------------------2')

# 2. pickle
import pickle
# pickle ==> dump 和load
# pickle 连续dump数据.也可以连续load数据
dic1 = {"a":1,"b":2}
dic2 = {"c":3,"d":4}
with open("lianxi5.pkl",mode="wb") as fp:
	pickle.dump(dic1,fp)  #写入字节流
	pickle.dump(dic2,fp)
	pickle.dump(dic1,fp)
	pickle.dump(dic2,fp)

with open("lianxi5.pkl",mode="rb") as fp:
	dic1 = pickle.load(fp)
	dic2 = pickle.load(fp)
	print(dic1)
	print(dic2)

# {'a': 1, 'b': 2}
# {'c': 3, 'd': 4}
print('-------------------3')

# json 和 pickle 两个模块的区别:
# 1 json序列化之后的数据类型是str,所有的编程语言都识别,
  # 但是仅仅限于 int float bool str list tuple dict None
  # json不能连续load,只能一次性拿出所有数据
# 2 pickle序列化之后的数据类型是bytes,用于数据存储,
  # 所有数据类型都可转化,但仅限于python之间的存储传输,
  # pickle可以连续load,多套数据放到同一个文件中








































