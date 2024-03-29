# ### 在同一个文件中,变量的缓存机制(仅仅针对python3.6版本负责)
# 1.对于整型而言,-5~正无穷大范围内的相同值 id一致   python3.6版本
# 1.对于整型而言,		整数范围内的相同值 id一致   python3.7及其以上版本
var1 = 5
var2 = 5
print(id(var1),id(var2))  
#140719892357904 140719892357904

var1 = -100
var2 = -100
print(id(var1),id(var2))
#2492291405744 2492291405744   py3.7

# 2.对于浮点数而言,非负数范围内的相同值,id一致   python3.6版本
# 2.对于浮点数而言,浮点数范围内的相同值,id一致	 python3.7及其以上版本
var1 = 4.67
var2 = 4.67
print(id(var1),id(var2))
#2661264700040 2661264700040

var1 = -4.67
var2 = -4.67
print(id(var1),id(var2))
#1689986446104 1689986446104   python3.7

# 3.布尔值而言,值相同情况下,id一致   python3.6和python3.7相同
var1 = True
var2 = True
print(id(var1),id(var2))
#140719637625168 140719637625168

# 4.复数在 实数+虚数 这样的结构中永不相同(只有正虚数的情况例外)  python3.6版本
# 4.复数在 实数+虚数 如果值相同,那么id就一致					 python3.7及其以上版本
var1 = 4 + 5j
var2 = 4 + 5j
print(id(var1),id(var2))  
#3106654491504 3106654491504   #python3.7

var1 = 5j
var2 = 5j
print(id(var1),id(var2))
#2878805611440 2878805611440   #python3.7
print('-----------------------------')

# -->容器类型部分
# 5.字符串和空元组,相同的情况下,id相同   #python3.6和python3.7相同
var1 = '你'
var2 = '你'
print(id(var1),id(var2))
#2843840769920 2843840769920  

var1 = ()
var2 = ()
print(id(var1),id(var2))
#2824104312904 2824104312904

# 6.列表,元组,字典,集合 无论什么情况,id标识都不同(空元组除外)   python3.6版本
# 6.列表,元组,字典,集合 值相同,id就一致(空元组除外)   			python3.7及其以上版本
#   特别注意点:列表的值相同,id不一致  python3.7版本
var1 = (1,2)
var2 = (1,2)
print(id(var1),id(var2))
# 2645761156232 2645761156232   python3.7

var1 = [1,2]
var2 = [1,2]
print(id(var1),id(var2))
# 2266589717128 2266589717192   python3.7























