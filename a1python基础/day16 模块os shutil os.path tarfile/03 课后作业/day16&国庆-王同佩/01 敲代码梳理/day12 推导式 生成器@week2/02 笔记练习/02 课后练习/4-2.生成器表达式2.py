# ### 生成器

# 1 生成器表达式(元组推导式)
gen = (i for i in range(6))
print(gen,type(gen))
# <generator object <genexpr> at 0x7f44016f8048> <class 'generator'>

from collections import Iterator
res = isinstance(gen,Iterator)
print(res)  #True

# 1 next
print(next(gen))  #0
print(next(gen))  #1

# 2 for + next   常用
for i in range(2):
	print(next(gen))

# 3 for  
for i in gen:  # 打印所有
	print(i)

# 4 list
gen = (i for i in range(6))
print(list(gen))  #[0, 1, 2, 3, 4, 5]

# print(gen.__next__())  #StopIteration





































