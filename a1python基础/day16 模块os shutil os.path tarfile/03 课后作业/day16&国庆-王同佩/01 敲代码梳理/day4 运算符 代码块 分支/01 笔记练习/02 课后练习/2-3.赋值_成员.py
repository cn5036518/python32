# ### (3)赋值运算符:   = += -= *= /= //= %= **=
# = 赋值运算符 将=右侧的值赋值给左侧变量
a = 5<= 3
print(a)  #False

# 运算符优先级  算数 比较 赋值 成员 身份 逻辑 位运费符
# 1算数 2位 3比较 4身份 5 成员  6逻辑  7赋值
#   +    <<  ==     is    in      and    =

var1 = 10
var2 = 5
# +=
var1 += var2
print(var1)  #15

# -=
var1 = 10
var2 = 5
var1 -= var2
print(var1) #5

# %=
var1 = 10
var2 = 5
var1 %= var2
print(var1)  #0

# (4)成员运算符:  in 和 not in (针对于容器型数据)
# """字符串判断时,必须是连续的片段"""
strvar = "今天天气要下雨,赶紧回家收衣服"

res = '今天' in strvar
print(res) #True

res = '赶回' in strvar
print(res) #False

# 针对于列表,元组,集合
container = ["赵沈阳","赵万里","赵世超"]
container = ("赵沈阳","赵万里","赵世超")
container = {"赵沈阳","赵万里","赵世超"}
res = '赵世超12' not in container
print(res)  #True

# 针对于字典 (判断的是字典的键,不是值)
container = {"zsy":"赵沈阳","zwl":"赵万里","zsc":"赵世超"}
res = '赵沈阳' in container
print(res) #False

res = 'zsy' in container
print(res) #True





























