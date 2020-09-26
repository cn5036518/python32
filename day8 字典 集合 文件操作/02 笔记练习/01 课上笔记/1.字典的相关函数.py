# ### 字典的相关函数
dic = {}
# 增
# 1.普通方法  (推荐)
dic["top"] = "369"
dic["middle"] = "左手"
dic["bottom"] = "杰克爱"
print(dic)  #{'top': '369', 'middle': '左手', 'bottom': '杰克爱'}

# 1.直接定义
dic = {'name':'jack','age':18}

# 2.fromkeys 使用一组键和默认值创建字典
tup = ("a","b","c")
# fromkeys(盛放键的容器,默认值)
dic = {}.fromkeys(tup,None)
print(dic)  #{'a': None, 'b': None, 'c': None}

# 注意点 (字典中的三个键默认指向的是同一个列表)
dic= {}.fromkeys(tup,[])
print(dic)  #{'a': [], 'b': [], 'c': []}
dic["a"].append(1)
print(dic)  #{'a': [1], 'b': [1], 'c': [1]}

# 改造
dic = {}
dic["top"] = []  #id1
dic["middle"] = []  #id2
dic["bottom"] = []  #id3
dic["top"].append("the boy")
print(dic) #{'top': ['the boy'], 'middle': [], 'bottom': []}
print('--------------------1 新增')

# 删
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
#pop()       通过键去删除键值对 (若没有该键可设置默认值,预防报错)
res = dic.pop("middle")
print(res) #左手
print(dic) #{'top': '369', 'bottom': '杰克爱'}
# 可以给pop设置第二个参数值,以防止键不存在时报错
res = dic.pop("middle1234","该键不存在")
print(res) #该键不存在
print('--------------------2-1 删除 pop')

#popitem()   删除最后一个键值对,并且返回被删除的值
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
res = dic.popitem()
print(res)  #('bottom', '杰克爱')
print(dic)  #{'top': '369', 'middle': '左手'}
print('--------------------------------------2-2 删除 popitem')

#clear()  清空字典
dic.clear()
print(dic)  #{}
print('--------------------------------------2-3 删除 clear')

# 改
#update() 批量更新(有该键就更新,没该键就添加)

# 推荐使用
# 没该键就添加
dic_new = {"jungle":"karsa","support":"宝蓝"}
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
dic.update(dic_new)
print(dic)  #{'top': '369', 'middle': '左手', 'bottom': '杰克爱', 'jungle': 'karsa', 'support': '宝蓝'}
print('--------------------------------------3-1 修改 update')

# 有该键就更新
dic_new = {"top":"the bug","support":"xboyww","xiaozhang":"王思聪"}
dic.update(dic_new)
print(dic) #{'top': 'the bug', 'middle': '左手', 'bottom': '杰克爱', 'jungle': 'karsa', 'support': 'xboyww', 'xiaozhang': '王思聪'}
print('--------------------------------------3-2 修改 update')

# (了解)
dic.update(ww="王文",zl="张磊")
print(dic)
print('--------------------------------------3-3 修改 update')

# 查
# get()    通过键获取值(若没有该键可设置默认值,预防报错)
dic = {"top":"the bug","support":"xboyww","xiaozhang":"王思聪"}
# res = dic["top123"]
# get 在获取字典键时,如果不存在,不会发生任何报错,返回的是None
res = dic.get("top123")

# 可以在获取不到该键时,给与默认值提示.
res = dic.get("top123","抱歉,该键不存在")
print(res) #抱歉,该键不存在
print('--------------------------------------4-1 查询 get')

# 其他操作
#keys()   将字典的键组成新的可迭代对象
dic = {"top":"the bug","support":"xboyww","xiaozhang":"王思聪"}
res = dic.keys()
print(res , type(res))

#values() 将字典中的值组成新的可迭代对象 ***
res = dic.values()
print(res , type(res))

#items()  将字典的键值对凑成一个个元组,组成新的可迭代对象 ***
res = dic.items()
print(res , type(res))
print('--------------------------------------5 keys values items')


# for i in res:
	# print(i)
for k,v in res:
	print(k,v)











