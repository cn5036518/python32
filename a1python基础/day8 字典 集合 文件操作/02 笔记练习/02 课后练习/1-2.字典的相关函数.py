# ### 字典的相关函数  增删改查
dic = {}
# 新增
# 方法1 键值对添加
dic['top'] = '369'
dic['middle'] = '左手'
dic['bottom'] = '杰克爱'
print(dic)  #{'top': '369', 'middle': '左手', 'bottom': '杰克爱'}

# 方法2 直接定义
dic = {'name':'jack','age':18}

# 方法3 fromkeys 一组键和默认值创建字典
tup = ("a","b","c")
dic = {}.fromkeys(tup,None)
print(dic)  #{'a': None, 'b': None, 'c': None}

# 注意点 (字典中的三个键默认指向的是同一个列表)
dic = {}.fromkeys(tup,[])
print(dic)  #{'a': [], 'b': [], 'c': []}
dic['a'].append(1)
print(dic)  #{'a': [1], 'b': [1], 'c': [1]}
# 字典\列表是引用类型,一改都改

# 改造
dic = {}
dic['top'] = []  #id1
dic['middle'] = [] #id2
dic['bottom'] = [] #id3
print(dic)  #{'top': [], 'middle': [], 'bottom': []}
dic['top'].append('the boy')
print(dic)  #{'top': ['the boy'], 'middle': [], 'bottom': []}
print('--------------------1 新增')


# 二 删除  pop  popitem clear
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
#01 pop()       通过键去删除键值对,并且获取被删除的键对应的值
# (若没有该键可设置默认值,预防报错)
res = dic.pop('middle')
print(res) #左手
print(dic)  #{'top': '369', 'bottom': '杰克爱'}

## 可以给pop设置第二个参数值,以防止键不存在时报错
res = dic.pop('middle1237782','该键不存在')
print(res) #该键不存在
print('--------------------2-1 删除 pop')

#02 popitem()   删除最后一个键值对,并且返回被删除的键和值组成的元组
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
res = dic.popitem()
print(res) #('bottom', '杰克爱')
print(dic)  #{'top': '369', 'middle': '左手'}
print('--------------------------------------2-2 删除 popitem')

#03 clear()  清空字典
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
dic.clear()
print(dic)  #{}
print('--------------------------------------2-3 删除 clear')

# 三 修改  update
#01 update() 批量更新(有该键就更新,没该键就添加)

# 推荐使用
# 没该键就添加
dic_new = {"jungle":"karsa","support":"宝蓝"}
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
dic.update(dic_new)
print(dic)
# {'top': '369', 'middle': '左手', 'bottom': '杰克爱', 
# 'jungle': 'karsa', 'support': '宝蓝'}
print('--------------------------------------3-1 修改 update')

# 有该键就更新
dic_new = {"top":"the bug"}
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
dic.update(dic_new)
print(dic)  #{'top': 'the bug', 'middle': '左手', 'bottom': '杰克爱'}
print('--------------------------------------3-2 修改 update')

# (了解)
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
dic.update(ww='王文') #关键字参数
print(dic)
# {'top': '369', 'middle': '左手', 'bottom': '杰克爱', 'ww': '王文'}
print('--------------------------------------3-3 修改 update')

# 四 查询-获取  get
#方法1 
dic = {"top":"the bug","support":"xboyww","xiaozhang":"王思聪"}
res = dic['top']
print(res) #the bug

# res = dic['top123'] 报错
# print(res) #KeyError: 'top123'

#方法2 get()  通过键获取值(若没有该键可设置默认值,预防报错)
# 可以在获取不到该键时,给与默认值提示.
res = dic.get('top123')
print(res)  #None

res = dic.get('top123','该键不存在')
print(res)  #该键不存在
print('--------------------------------------4 查询 get')

#  五 其他操作
#keys()   将字典的键组成新的可迭代对象
dic = {"top":"the bug","support":"xboyww","xiaozhang":"王思聪"}
res = dic.keys()
print(res)  # dict_keys(['top', 'support', 'xiaozhang'])

#values() 将字典中的值组成新的可迭代对象 ***
dic = {"top":"the bug","support":"xboyww","xiaozhang":"王思聪"}
res = dic.values()
print(res) #dict_values(['the bug', 'xboyww', '王思聪'])

#items()  将字典的键值对凑成一个个元组,组成新的可迭代对象 ***
dic = {"top":"the bug","support":"xboyww","xiaozhang":"王思聪"}
res = dic.items()
print(res) 
#dict_items([('top', 'the bug'), ('support', 'xboyww'), ('xiaozhang', '王思聪')])

print('--------------------------------------5 keys values items')

for k,v in dic.items():
	print(k,v)
# top the bug
# support xboyww
# xiaozhang 王思聪






























































